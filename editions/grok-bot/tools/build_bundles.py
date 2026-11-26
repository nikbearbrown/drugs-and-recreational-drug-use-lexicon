"""Build one independently sourced evidence bundle per seed (Grok Bot run, 2026-11-24).
Sources: en.wikipedia API (pinned lastrevid, plain-text lead extract), Wikidata wbgetentities
(item revision, en label/aliases, selected item-valued claims, one level of P31/P279 ancestors),
Princeton WordNet 3.0 via NLTK. Neighbors: seed titles linked from the article (or redirect target)
plus seeds whose Wikidata item is referenced by this item's selected claims."""
import csv, json, sys, time, urllib.parse, urllib.request, re
from nltk.corpus import wordnet as wn
SEEDS='/workspace/drugs-lexicon-checkout/data/seeds.tsv'
UA={'User-Agent':'GrokBot-lexicon-replication/1.0 (research; contact via github nikbearbrown)'}
def get(url,params):
    q=url+'?'+urllib.parse.urlencode(params)
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(q,headers=UA),timeout=60) as r: return json.load(r)
        except Exception as e:
            time.sleep(2+3*i); err=e
    raise err
WP='https://en.wikipedia.org/w/api.php'; WD='https://www.wikidata.org/w/api.php'
seeds=list(csv.DictReader(open(SEEDS,encoding='utf8'),delimiter='\t'))
byid={s['page_id']:s for s in seeds}; title2cid={s['preferred_name']:s['concept_id'] for s in seeds}
info={}
ids=[s['page_id'] for s in seeds]
for i in range(0,len(ids),50):
    chunk=ids[i:i+50]
    d=get(WP,{'action':'query','format':'json','formatversion':2,'pageids':'|'.join(chunk),'prop':'info|pageprops|revisions','rvprop':'ids|timestamp|content','rvslots':'main'})
    for p in d['query']['pages']:
        rev=p['revisions'][0]
        info[str(p['pageid'])]={'title':p['title'],'redirect':p.get('redirect',False),'lastrevid':rev['revid'],'revts':rev['timestamp'],
            'wikitext_head':rev['slots']['main']['content'][:400] if p.get('redirect') else None,
            'qid':p.get('pageprops',{}).get('wikibase_item'),'disambig':'disambiguation' in p.get('pageprops',{})}
    time.sleep(0.5)
# redirect targets
for pid,x in info.items():
    if x['redirect']:
        d=get(WP,{'action':'query','format':'json','formatversion':2,'pageids':pid,'redirects':1,'prop':'info|pageprops|revisions','rvprop':'ids|timestamp'})
        p=d['query']['pages'][0]; r=d['query'].get('redirects',[{}])[0]
        x['target']={'title':p['title'],'fragment':r.get('tofragment'),'pageid':p.get('pageid'),'lastrevid':p['revisions'][0]['revid'] if 'revisions' in p else None,'qid':p.get('pageprops',{}).get('wikibase_item'),
                     'target_is_seed':p['title'] in title2cid}
        if not x['qid']: x['qid_from_target']=x['target']['qid']
# extracts (lead, plain text) for article pages and redirect targets
def extract(title):
    d=get(WP,{'action':'query','format':'json','formatversion':2,'titles':title,'prop':'extracts|revisions','explaintext':1,'exintro':1,'rvprop':'ids'})
    p=d['query']['pages'][0]
    return p.get('extract','') , p['revisions'][0]['revid']
def links(title):
    out=set(); cont={}
    while True:
        d=get(WP,dict({'action':'query','format':'json','formatversion':2,'titles':title,'prop':'links','plnamespace':0,'pllimit':'max'},**cont))
        for p in d['query']['pages']:
            for l in p.get('links',[]): out.add(l['title'])
        if 'continue' in d: cont=d['continue']
        else: return out
for n,(pid,x) in enumerate(info.items()):
    t=x['target']['title'] if x['redirect'] else x['title']
    txt,rid=extract(t)
    if len(txt)<600:  # short lead: add the first section(s) too
        d=get(WP,{'action':'query','format':'json','formatversion':2,'titles':t,'prop':'extracts','explaintext':1,'exchars':2500})
        txt=d['query']['pages'][0].get('extract',txt)
    x['extract']=txt[:4000]; x['extract_revid']=rid
    x['links']=sorted(links(t)&set(title2cid))
    if n%25==0: print(n,file=sys.stderr)
json.dump(info,open('tools/wp_info.json','w'),ensure_ascii=False)
print('wp done',file=sys.stderr)
