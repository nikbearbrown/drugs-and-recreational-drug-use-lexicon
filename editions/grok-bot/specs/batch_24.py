import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=24
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:1704222','Inhaled alkyl nitrite products used recreationally for brief vasodilator effects.',
  'Recreational products containing alkyl nitrites whose vapours are inhaled; they dilate blood vessels and give brief euphoria, warmth and dizziness.',
  dp=['q:Poppers are recreational drugs belonging to the alkyl nitrite family of chemical compounds.','q:they act as potent vasodilators'],
  var=[('popper','singular, also the container',['wda:popper']),('amyl','slang; strictly amyl nitrite, one alkyl nitrite',['wda:amyl'])],
  rel=[('hypernym','Inhalant',[]),('contrast','amyl nitrite',[],'One specific alkyl nitrite; poppers may contain others.')],
  wn='popper.n.02',wnr='popper.n.02 (a container of amyl or butyl nitrite) is the closest sense; WordNet calls it a stimulant, which is imprecise.',
  flags=['Wikidata classes poppers as a hallucinogen (Q194270), which is inaccurate; not used','Wikidata aliases include product-labelling names used to sell poppers; not recorded'])
D('enwiki:58552272','The frequent co-occurrence of post-traumatic stress disorder and substance use disorders.',
  'The relationship between post-traumatic stress disorder and substance use disorders, which commonly occur together in the same people.',
  dp=['q:a co-occurring, or comorbid diagnosis of a SUD is present in 20–35% of that clinical population'],
  rel=[('hypernym','Dual diagnosis',[]),('contrast','Self-medication',[],'One proposed explanation for the link.')],flags=[TOPIC])
D('enwiki:1111272','Medication given before another therapy, such as surgery or chemotherapy, to prepare for it.',
  'The use of medication before another treatment, usually surgery or chemotherapy, to prepare the patient, for example sedatives before an operation or anti-nausea drugs before chemotherapy.',
  dp=['q:Premedication is using medication before some other therapy','wd:P279=Q701216'],
  rel=[('hypernym','pharmacotherapy',['wd:P279=Q701216'])],
  flags=['ambiguous: clinical practice term; peripheral to substance use and public-health terminology'])
D('enwiki:67079155','Chronic repeated use of a prescription drug other than as prescribed.',
  'Repeated, chronic use of a prescription medicine in ways other than prescribed, including taking another person\'s prescription, most often involving opioids, sedatives and stimulants.',
  dp=['q:is the chronic, repeated use of a prescription drug in ways other than prescribed for','wd:P279=Q12029'],
  var=[('prescription drug misuse','broader: includes misuse without addiction',[])],
  rel=[('hypernym','Addiction',['wd:P279=Q12029']),('contrast','Doctor shopping',[],'A behaviour sometimes associated with it.')])
O('enwiki:25281520','an organisation (Illinois prevention non-profit), not a term')
O('enwiki:36245182','an organisation (Philadelphia harm-reduction non-profit), not a term')
O('enwiki:72966366','an organisation (Rhode Island harm-reduction group), not a term')
D('enwiki:67102966','A medicine made or sold under a name protected by trademark or patent.',
  'A medicine produced or marketed under a name protected by trademark or patent; it is usually still called proprietary after the patent ends, when generics may appear.',
  dp=['q:which are formulated or manufactured under a name protected from competition through trademark or patent'],
  var=[('brand-name drug',None,['wn:lemma=brand-name drug'])],
  rel=[('hypernym','Drug',['wn:hypernym=drug.n.01']),('contrast','generic drug',[],'Sold without the proprietary name after patent expiry.')],
  wn='brand-name_drug.n.01',
  flags=['ambiguous: historically "proprietary medicine" also meant patent medicines of unproven value; the source sense is trademarked medicines'])
D('enwiki:11109026','The 4-propynyloxy analogue of mescaline, a phenethylamine of the scaline group.',
  'A mescaline analogue of the scaline group in which the 4-position methoxy group is replaced by a propynyloxy group.',
  dp=['q:is a psychoactive drug of the scaline family related to mescaline','q:has been replaced with a propynyloxy group'],
  var=[('propynylscaline',None,['q:or as propynylscaline']),('4-propynyloxy-3,5-dimethoxyphenethylamine',None,['wda:4-propynyloxy-3,5-dimethoxyphenethylamine'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','Buscaline',[],'Sibling scaline with a butoxy group.')],
  flags=['ambiguous: "propynyl" is also a general chemistry term for a substituent group'])
D('enwiki:69305147','A bacterial-derived vaccine adjuvant being tested as a nasal immunomodulator.',
  'An immunomodulating drug made from bacterial lipopolysaccharide combined with outer-membrane proteins, first developed as a vaccine adjuvant and later trialled as a nasal treatment.',
  dp=['q:Protollin is a drug initially formulated as a vaccine adjuvant.','wd:P279=Q1660194'],
  rel=[('hypernym','immunomodulator',['wd:P279=Q1660194'])],
  flags=['ambiguous: an investigational immunology drug with no substance-use or public-health sense; peripheral to the domain'])
L.save(24)
