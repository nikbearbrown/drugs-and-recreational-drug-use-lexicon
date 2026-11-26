import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=17
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:15888179','A transient state of profound dissociation and immobility during ketamine intoxication.',
  'A short-lived state of intense dissociation during ketamine intoxication, in which the person feels cut off from body and surroundings and is largely unable to move; usually unwanted, occasionally sought.',
  dp=['q:A K-hole is a transient dissociative state experienced during ketamine intoxication.'],
  var=[('K-holing','verbal form',['q:Often referred to as "K-holing"'])],
  rel=[('hypernym','Substance intoxication',[]),('contrast','Bad trip',[],'Distress with psychedelics rather than ketamine dissociation.')])
D('enwiki:38567144','A medicinal mixture of kaolin clay and morphine used for acute diarrhoea.',
  'An oral medicine combining kaolin clay with a small amount of morphine, used to relieve acute diarrhoea.',
  dp=['q:Kaolin and morphine mixture is a drug for the relief of acute diarrhoea.'],
  var=[('kaolin and morphine mixture',None,['q:Kaolin and morphine mixture'])],
  rel=[('hypernym','Antipropulsive',['wd:P279=Q4775138'])],
  flags=['ambiguous: an over-the-counter medicine; relevance to the domain is mainly its opioid content'])
D('enwiki:1625150','The religious and cultural traditions of kava drinking in Oceania.',
  'The ritual, social and cultural traditions surrounding the drinking of kava in the Pacific Islands, which differ between islands and cultures.',
  dp=['q:Kava cultures are the religious and cultural traditions of western Oceania which consume kava.','wd:P31=Q2389669'],
  rel=[('hypernym','Drug culture',['wd:P31=Q2389669']),('hypernym','drink culture',['wd:P279=Q16041721'])],flags=[TOPIC])
D('enwiki:66087885','The medical, recreational and cultural history of ketamine.',
  'The range of medical and recreational uses of ketamine since its discovery in 1962, and its place in culture, law and naming.',
  dp=['q:Ketamine has had a wide variety of medicinal and recreational uses since its discovery in 1962.'],
  rel=[('contrast','K-hole',[],'A specific ketamine experience.')],flags=[TOPIC])
O('enwiki:67639781','an organisation (North Korean pharmaceutical company), not a term')
D('enwiki:47024473','A North Korean product claimed, without evidence, to cure several serious infections.',
  'A medicinal product made in North Korea and promoted as a cure for AIDS, Ebola and other diseases, claims that are unsupported.',
  dp=['q:is an alleged cure for AIDS, Ebola, MERS, Herpes and tuberculosis created in North Korea'],
  rel=[('hypernym','medicinal product',['wd:P31=Q12034612']),('contrast','Royal Blood-Fresh',[],'Another North Korean medicinal product.')],
  flags=['ambiguous: a single named commercial product rather than a general term'])
D('enwiki:80064741','A synthetic cannabinoid-like street drug that spread in Sierra Leone from 2021.',
  'A synthetic street drug resembling synthetic cannabinoids, of variable composition, reported from about 2018 and widespread in Sierra Leone from 2021.',
  dp=['q:Kush is a synthetic cannabinoid-like drug.','wd:P279=Q1200715'],
  rel=[('hypernym','Designer drug',['wd:P279=Q1200715']),('contrast','kush (cannabis)',[],'Kush is also a name for cannabis strains; a different substance.')],
  flags=['ambiguous: "kush" also names cannabis strains; the seed sense is the West African synthetic drug','domain rule: the source notes use "particularly among young people"; demographic framing is not carried into the entry','regional term: Sierra Leone and West Africa'])
O('enwiki:62369025','a biography (social worker), not a term')
D('enwiki:4223023','Adulterating a drug with another substance, for example to bulk it out.',
  'In drug culture, the practice of adding another substance to a drug, whatever the reason, most often to bulk out the product or substitute something cheaper; the result is called laced or cut.',
  dp=['q:to adulterate substances independent of the reason','q:it is most commonly done to bulk up the original product'],
  var=[('cutting','in drug culture; often specifically dilution',['q:Lacing or cutting, in drug culture']),('adulteration of drugs',None,['wda:adulteration of drugs'])],
  rel=[('hypernym','adulteration',['wd:P279=Q4681306']),('uses','Cutting agent',['q:(referred to as the lacing agent or cutting agent)']),('contrast','Adulterant',[],'The substance rather than the practice.')],
  wnr='WordNet "lacing" senses are liquor added to food, a shoelace and a beating; none is drug adulteration.')
D('enwiki:7605695','A recreational drink made with prescription opioid cough syrup.',
  'A recreational polysubstance drink based on prescription cough or cold syrup containing an opioid and an antihistamine, associated with hip-hop culture in the southern United States.',
  dp=['q:is a polysubstance drink used as a recreational drug','wd:P31=Q8386'],
  var=[('purple drank',None,['q:Lean or purple drank']),('sizzurp','slang',['wda:sizzurp']),('drank','slang',['wda:drank']),('syrup','slang; ambiguous',['wda:syrup'])],
  rel=[('hypernym','drug',['wd:P31=Q8386']),('hypernym','Polysubstance',[]),('contrast','Recreational use of dextromethorphan',[],'A different cough-medicine drug.')],
  wnr='WordNet "lean" senses are tilt and leaning verbs; none is the drink.',
  flags=['domain rule: preparation details in the source are omitted'])
L.save(17)
