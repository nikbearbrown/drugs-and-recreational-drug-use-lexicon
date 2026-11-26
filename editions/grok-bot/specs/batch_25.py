import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=25
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:79209493','A retail shop selling hallucinogenic mushroom products, analogous to a cannabis dispensary.',
  'A shop that sells psilocybin mushroom products, comparable to a cannabis dispensary, which became common in some places in the early 2020s.',
  dp=['q:is a retail outlet that sells hallucinogenic mushroom products','q:They are analogous to cannabis dispensaries.'],
  var=[('magic mushroom dispensary',None,['q:also known as a magic mushroom dispensary'])],
  rel=[('contrast','Smart shop',[],'Dutch shops selling legal psychoactive products.'),('contrast','Head shop',[],'Sells paraphernalia, not the drugs.')],
  wd=False,wdr="Item Q132797970 has no statements; the bundle cannot confirm the sense.")
D('enwiki:33632441','A chemical substance that changes mental functioning by acting on the central nervous system.',
  'A chemical substance that changes perception, mood, consciousness, cognition or behaviour by acting on the central nervous system; the class includes medicines and recreational drugs.',
  dp=['q:is a chemical substance that alters psychological functioning by modulating central nervous system (CNS) activity','wd:P279=Q8386'],
  var=[('psychoactive substance',None,['wn:lemma=psychoactive substance']),('mind-altering drug',None,['wn:lemma=mind-altering drug']),('psychotropic','sometimes narrower: psychiatric medications',['wda:psychotropic']),('psychopharmaceutical','usually therapeutic agents only',['wda:psychopharmaceutical'])],
  rel=[('hypernym','Drug',['wd:P279=Q8386']),('hyponym','Entheogen',[]),('hyponym','Inhalant',[])],
  wn='psychoactive_drug.n.01')
D('enwiki:79627713','The use, misuse and regulation of psychoactive drugs in Nigeria.',
  'The patterns of psychoactive drug use and misuse in Nigeria and how they are regulated, treated as a public-health and social concern.',
  dp=['q:In Nigeria, the use, abuse, and regulation of psychoactive substances have been a major public health and social concern.'],
  rel=[('contrast','Psychoactive drug',[],'The general concept.')],
  wd=False,wdr="Item Q133896513 has no statements; the bundle cannot confirm the sense.",
  flags=[TOPIC,'ambiguous: country-specific topic page'])
D('enwiki:841441','The exploration and description of altered states of consciousness by deliberately entering them.',
  'An approach to studying altered states of consciousness, induced by meditation or psychoactive substances, in which the investigator deliberately enters those states to explore and describe them; a practitioner is a psychonaut.',
  dp=['q:refers both to a methodology for describing and explaining the subjective effects of altered states of consciousness'],
  var=[('psychonaut','names the practitioner',['wda:psychonaut'])],
  rel=[('hypernym','methodology',['wd:P31=Q185698']),('contrast','Recreational drug use',[],'Use for pleasure rather than exploration.')])
O('enwiki:82067151','a website (drug-information wiki), not a term')
O('enwiki:46224274','an organisation (Norwegian psychedelics non-profit), not a term')
D('enwiki:43488','A dance party, often all night, featuring DJs playing electronic dance music.',
  'An event, often lasting through the night in a warehouse or club, where DJs play electronic dance music over a loud sound system with lighting effects; the surrounding scene is called rave culture.',
  dp=['q:is a dance party at a warehouse, club, or other public or private venue','wd:P279=Q200538'],
  var=[('rave party',None,['wda:rave party']),('rave culture','names the subculture',['wda:rave culture'])],
  rel=[('hypernym','party',['wd:P279=Q200538']),('contrast','Clubbing (subculture)',[],'Regular nightclub-going.')],
  wn='rave.n.01',flags=['ambiguous: an event and subculture term connected to drugs by association; peripheral to the domain'])
D('enwiki:8380557','Identifying substances in a drug sample with chemical reagents that change colour.',
  'A chemical spot-test method for identifying which substances are present in a pill or powder, usually illicit drugs, using reagents that produce characteristic colour changes; it is one technique of drug checking.',
  dp=['q:Reagent testing is one of the processes used to identify substances contained within a pill','wd:P279=Q3519101'],
  var=[('drug reagent testing',None,['wda:drug reagent testing']),('pill testing','broader: usually means drug checking with any technique',['q:the terms "drug checking" or "pill testing" may also be used'])],
  rel=[('hypernym','Drug checking',['wd:P279=Q3519101']),('hypernym','chemical test',['wd:P279=Q3944822'])],
  wdr="Item Q1261129 is labelled 'pill testing' but lists 'reagent testing' as an alias and is a subclass of drug checking; it matches the sense.")
D('enwiki:1281835','An urban Greek popular-music genre, historically linked with hashish dens.',
  'A genre of urban Greek popular song that took shape in the 1930s from disparate earlier styles; part of its early repertoire was associated with hashish-smoking venues.',
  dp=['q:is a term used to designate previously disparate kinds of urban Greek music','wd:P31=Q188451'],
  var=[('rembetiko','transliteration variant',['wda:Rembetiko']),('rebetika','plural',['wda:Rebetika'])],
  rel=[('hypernym','music genre',['wd:P31=Q188451'])],
  flags=['ambiguous: a music genre connected to drugs only through part of its history; peripheral to the domain'])
D('enwiki:1251434','Travel to obtain or use recreational drugs that are unavailable, illegal or costly at home.',
  'Travelling to another country or region in order to obtain or use recreational drugs that are unavailable, prohibited or expensive where one lives.',
  dp=['q:is travel for the purpose of obtaining or using drugs for recreational use'],
  var=[('drug tourism',None,['wda:drug tourism'])],
  rel=[('hypernym','tourism',['wd:P279=Q49389'])],
  flags=['domain rule: no destinations or procurement details are given'])
L.save(25)
