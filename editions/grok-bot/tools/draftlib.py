"""Turns Grok Bot's per-seed drafting decisions (written by hand in specs/batch_NN.py) into gen-v2 draft
objects. It only expands pointer shorthand, fills default link reasons and looks up neighbor ids; every
sense, definition, variant, relation and flag is written by the drafting model in the spec file."""
import json, re, sys
sys.path.insert(0,'/workspace/drugs-lexicon-checkout/replication/scripts')
from verify_drafts import verify, norm, copies_wikipedia
B={}
for l in open('bundles.jsonl',encoding='utf8'):
    r=json.loads(l); B[r['concept_id']]=r
META=json.load(open('tools/seed_meta.json'))
OUT=[]; ERR=[]
BATCH=None
def _main_wd(b):
    m=[w for w in b['wikidata'] if not w.get('ancestor_of')]
    return m[0] if m else None
def _ptr(p,links):
    if p.startswith('q:'): return f"wp:{links['wikipedia']['choice']}#quote={p[2:]}"
    if p.startswith('wda:'): return f"wd:{links['wikidata']['choice']}#alias={p[4:]}"
    if re.match(r'wd:P\d+=',p): return f"wd:{links['wikidata']['choice']}#{p[3:]}"
    if p.startswith('wn:') and '#' not in p: return f"wn:{links['wordnet']['choice']}#{p[3:]}"
    return p
def D(cid,sense,defn,dp=(),var=(),rel=(),flags=(),wp='d',wd='d',wn=None,wpr=None,wdr=None,wnr=None):
    b=B[cid]; m=META[cid]
    if wp=='d': wp=1 if m['redirect'] else 0
    wpc=None if wp is None else b['wikipedia'][wp]['revision_id']
    if wpr is None:
        if wpc is None: raise ValueError(cid+': wikipedia abstention needs a reason')
        wpr=(f"The seed page is a redirect; the pinned revision of its target '{b['wikipedia'][wp]['title']}' is used only as evidence for the term, not as a mapping decision." if m['redirect'] and wp==1
             else "The pinned revision of the seed article describes the concept in the stated sense.")
    mw=_main_wd(b)
    if wd=='d': wd=mw['qid'] if mw else None
    if wd is False: wd=None
    if wdr is None:
        if wd: wdr=f"Wikidata item {wd} ('{next(w['label'] for w in b['wikidata'] if w['qid']==wd)}') matches the stated sense."
        elif not mw: wdr="The bundle has no Wikidata candidate for this page."
        else: raise ValueError(cid+': wikidata abstention needs a reason')
    if wnr is None:
        if wn: wnr=f"WordNet synset {wn} matches the stated sense."
        elif not b['wordnet']: wnr="The bundle has no WordNet synset for this name."
        else: raise ValueError(cid+': wordnet abstention needs a reason')
    links={'wikipedia':{'choice':wpc,'reason':wpr},'wikidata':{'choice':wd,'reason':wdr},'wordnet':{'choice':wn,'reason':wnr}}
    nb={x['name'].lower():x['id'] for x in b['neighbors']}
    def claim(ptrs): 
        ps=[_ptr(p,links) for p in ptrs]; return ('source' if ps else 'model_knowledge'), ps
    bs,ps=claim(dp)
    e={'concept_id':cid,'work_sense':sense,'links':links,'definition':{'text':defn,'basis':bs,'pointers':ps},'variants':[],'relations':[],'flags':list(flags)}
    for v in var:
        t,c,pp=(v+((),))[:3] if len(v)==2 else v
        bs,ps=claim(pp); e['variants'].append({'text':t,'condition':c,'basis':bs,'pointers':ps})
    for r in rel:
        r=tuple(r)+(None,)*(4-len(r)); ty,lab,pp,note=r
        tid=nb.get(lab.lower()); bs,ps=claim(pp or ())
        e['relations'].append({'type':ty,'target_label':lab,'target_id':tid,'proposed_new':tid is None,'basis':bs,'pointers':ps,'note':note})
    _finish(e,b)
def O(cid,reason,flags=()):
    b=B[cid]; mw=_main_wd(b)
    e={'concept_id':cid,'work_sense':'Out of scope','links':{
        'wikipedia':{'choice':None,'reason':'Out of scope: '+reason},
        'wikidata':{'choice':None,'reason':'Out of scope; no terminology sense to link.'},
        'wordnet':{'choice':None,'reason':'Out of scope; no terminology sense to link.'}},
       'definition':{'text':'Out of scope','basis':'model_knowledge','pointers':[]},'variants':[],'relations':[],
       'flags':['out-of-scope: '+reason]+list(flags)}
    _finish(e,b)
def _finish(e,b):
    errs,warns=verify(e,b)
    t=e['definition']['text']
    if len(re.findall(r'\b\d+(\.\d+)?\s*(mg|µg|mcg|g|ml|mL)\b',t)): errs.append('dose-like text in definition')
    if errs: ERR.append((e['concept_id'],errs))
    e['_meta']={'model':'Grok Bot','model_version':'unknown (exact model string not visible to the drafting agent)',
                'run_mode':'batched, same session (protocol deviation approved by Nik Bear Brown, 24 Nov 2026)',
                'attempt':1,'batch':BATCH}
    OUT.append(e)
def save(n):
    if ERR:
        for c,es in ERR: print('ERROR',c,es)
        sys.exit(1)
    with open(f'parts/batch_{n:02d}.jsonl','w',encoding='utf8') as f:
        for e in OUT: f.write(json.dumps(e,ensure_ascii=False)+'\n')
    print('saved',len(OUT),'drafts to batch',n)
_T={v['title']:k for k,v in META.items()}
def cid(title): return _T[title]
def pdup(title,why=''): return f"possible-duplicate: overlaps {title} ({_T[title]})"+(f"; {why}" if why else '')
