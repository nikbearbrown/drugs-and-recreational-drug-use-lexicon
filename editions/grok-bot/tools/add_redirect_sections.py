"""For redirect seeds whose redirect points at a section, append that section's plain text (same pinned revision)."""
import json, urllib.parse, urllib.request, re, time
UA={'User-Agent':'GrokBot-lexicon-replication/1.0 (research)'}
meta=json.load(open('tools/seed_meta.json'))
rows=[json.loads(l) for l in open('bundles.jsonl',encoding='utf8')]
for b in rows:
    m=meta[b['concept_id']]
    if not m['redirect'] or not m['target'].get('fragment'): continue
    t=m['target']['title']; frag=m['target']['fragment']
    q='https://en.wikipedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','format':'json','formatversion':2,'titles':t,'prop':'extracts|revisions','explaintext':1,'rvprop':'ids'})
    p=json.load(urllib.request.urlopen(urllib.request.Request(q,headers=UA)))['query']['pages'][0]
    txt=p['extract']; rid=str(p['revisions'][0]['revid'])
    # find heading line equal to fragment
    mm=re.search(r'\n=+ *'+re.escape(frag.replace('_',' '))+r' *=+\n',txt)
    sec=None
    if mm:
        rest=txt[mm.end():]; nxt=re.search(r'\n==+ ',rest)
        sec=(rest[:nxt.start()] if nxt else rest).strip()[:3000]
    else:
        i=txt.lower().find(frag.lower().replace('_',' '))
        if i>=0: sec=txt[max(0,i-200):i+2500]
    w=b['wikipedia'][1]
    if rid!=w['revision_id']: print('revision moved',t,w['revision_id'],rid); continue
    if sec: w['text']=w['text']+'\n\n[Section: '+frag+']\n'+sec
    print(b['concept_id'],t,frag,bool(sec),len(sec or ''))
    time.sleep(0.3)
with open('bundles.jsonl','w',encoding='utf8') as f:
    for b in rows: f.write(json.dumps(b,ensure_ascii=False)+'\n')
