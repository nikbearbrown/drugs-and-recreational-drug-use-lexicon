"""Part 2: Wikidata + WordNet, then write bundles.jsonl (seven fields, seed order)."""
import csv, json, time, urllib.parse, urllib.request, re, sys
from nltk.corpus import wordnet as wn
SEEDS='/workspace/drugs-lexicon-checkout/data/seeds.tsv'
UA={'User-Agent':'GrokBot-lexicon-replication/1.0 (research; contact via github nikbearbrown)'}
WD='https://www.wikidata.org/w/api.php'
def get(params):
    q=WD+'?'+urllib.parse.urlencode(params)
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(q,headers=UA),timeout=60) as r: return json.load(r)
        except Exception as e: time.sleep(2+3*i); err=e
    raise err
PROPS=['P31','P279','P361','P527','P366','P2868','P1889','P460','P3781','P2175','P769','P106']
seeds=list(csv.DictReader(open(SEEDS,encoding='utf8'),delimiter='\t'))
info=json.load(open('tools/wp_info.json'))
def ents(qids):
    out={}
    qids=[q for q in dict.fromkeys(qids) if q]
    for i in range(0,len(qids),50):
        d=get({'action':'wbgetentities','format':'json','ids':'|'.join(qids[i:i+50]),'props':'labels|aliases|claims|info','languages':'en'})
        for q,e in d.get('entities',{}).items():
            if 'missing' in e: continue
            claims={}
            for p in PROPS:
                vals=[c['mainsnak'].get('datavalue',{}).get('value',{}).get('id') for c in e.get('claims',{}).get(p,[])]
                vals=[v for v in vals if v]
                if vals: claims[p]=vals
            out[q]={'qid':q,'label':e.get('labels',{}).get('en',{}).get('value',''),'aliases':[a['value'] for a in e.get('aliases',{}).get('en',[])],'claims':claims,'revision_id':str(e.get('lastrevid'))}
        time.sleep(0.3)
    return out
main_q=[x['qid'] or x.get('qid_from_target') for x in info.values()]
items=ents(main_q)
anc=[v for it in items.values() for p in ('P31','P279') for v in it['claims'].get(p,[])]
ancs=ents(anc)
qid2cid={}
for s in seeds:
    x=info[s['page_id']]; q=x['qid'] or x.get('qid_from_target')
    if q: qid2cid.setdefault(q,s['concept_id'])
title2cid={s['preferred_name']:s['concept_id'] for s in seeds}
def wordnet(name):
    base=re.sub(r'\s*\([^)]*\)$','',name).strip()
    cands=[]
    for form in dict.fromkeys([base, base.lower()]):
        for syn in wn.synsets(form.replace(' ','_')):
            if syn.name() in [c['synset'] for c in cands]: continue
            rel={}
            for k,f in [('hypernym',syn.hypernyms),('hyponym',syn.hyponyms),('part_meronym',syn.part_meronyms),('part_holonym',syn.part_holonyms),('member_meronym',syn.member_meronyms),('member_holonym',syn.member_holonyms)]:
                v=[t.name() for t in f()]
                if v: rel[k]=v
            cands.append({'synset':syn.name(),'lemmas':[l.replace('_',' ') for l in syn.lemma_names()],'gloss':syn.definition(),'relations':rel})
    return cands[:6]
out=open('bundles.jsonl','w',encoding='utf8')
for s in seeds:
    cid=s['concept_id']; x=info[s['page_id']]
    wp=[]
    if x['redirect']:
        t=x['target']
        wp.append({'title':s['preferred_name'],'revision_id':str(x['lastrevid']),'text':x['wikitext_head']})
        wp.append({'title':t['title'],'revision_id':str(x['extract_revid']),'text':x['extract']})
    else:
        wp.append({'title':x['title'],'revision_id':str(x['extract_revid']),'text':x['extract']})
    q=x['qid'] or x.get('qid_from_target')
    wd=[]
    if q and q in items:
        it=items[q]; wd.append(it)
        for p in ('P31','P279'):
            for v in it['claims'].get(p,[]):
                if v in ancs and not any(a['qid']==v for a in wd[1:]): wd.append(dict(ancs[v],ancestor_of=q))
    nb={}
    for t in x['links']:
        if t!=s['preferred_name']: nb[title2cid[t]]=t
    if x['redirect'] and x['target']['title'] in title2cid and x['target']['title']!=s['preferred_name']:
        nb[title2cid[x['target']['title']]]=x['target']['title']
    if q and q in items:
        for vs in items[q]['claims'].values():
            for v in vs:
                if v in qid2cid and qid2cid[v]!=cid:
                    c=qid2cid[v]; nb[c]=next(z['preferred_name'] for z in seeds if z['concept_id']==c)
    b={'concept_id':cid,'concept':{'id':cid,'preferred_name':s['preferred_name'],'kind':'unclassified','broad_class':'unclassified','variants':[],'relations':[]},
       'neighbors':[{'id':k,'name':v} for k,v in nb.items()],'examples':[],'wikipedia':wp,'wikidata':wd,'wordnet':wordnet(s['preferred_name'])}
    out.write(json.dumps(b,ensure_ascii=False)+'\n')
out.close()
# side metadata for drafting/report (not part of bundles)
meta={s['concept_id']:{'title':s['preferred_name'],'cats':s['direct_categories'],'redirect':info[s['page_id']]['redirect'],'target':info[s['page_id']].get('target'),'disambig':info[s['page_id']]['disambig'],'qid':info[s['page_id']]['qid'],'revid':info[s['page_id']]['lastrevid'],'revts':info[s['page_id']]['revts']} for s in seeds}
json.dump(meta,open('tools/seed_meta.json','w'),ensure_ascii=False,indent=0)
print('bundles written',len(seeds))
