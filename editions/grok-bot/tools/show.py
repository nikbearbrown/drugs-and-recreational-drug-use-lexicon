"""Compact view of bundles [a,b) for drafting (Grok Bot reads this, then writes a spec)."""
import json, sys
a,b=int(sys.argv[1]),int(sys.argv[2]); n=int(sys.argv[3]) if len(sys.argv)>3 else 900
rows=[json.loads(l) for l in open('bundles.jsonl',encoding='utf8')][a:b]
meta=json.load(open('tools/seed_meta.json'))
for i,r in enumerate(rows,a):
    m=meta[r['concept_id']]
    print(f"### [{i}] {r['concept_id']} | {r['concept']['preferred_name']} | {m['cats']}" + (f" | REDIRECT->{m['target']['title']}#{m['target']['fragment']} seed={m['target']['target_is_seed']}" if m['redirect'] else ''))
    for j,w in enumerate(r['wikipedia']):
        t=w['text'].replace('\n',' ')
        if '[Section:' in t: t=t[:300]+' … '+t[t.index('[Section:'):][:n]
        print(f"WP{j} {w['title']} rev {w['revision_id']}: {t[:n]}")
    for w in r['wikidata']:
        c=' '.join(f"{p}={','.join(v)}" for p,v in w['claims'].items())
        print(f"WD anc {w['qid']} '{w['label']}'" if w.get('ancestor_of') else f"WD {w['qid']} '{w['label']}' al={w['aliases'][:6]} {c}")
    for s in r['wordnet']: print(f"WN {s['synset']} {s['lemmas']}: {s['gloss'][:120]} {s['relations'].get('hypernym','')}")
    if r['neighbors']: print('NB', '; '.join(x['name'] for x in r['neighbors'][:10]))
    print()
