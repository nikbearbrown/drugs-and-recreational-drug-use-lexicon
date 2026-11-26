import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=21
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:46695897','The molecular and epigenetic changes thought to underlie alcohol use disorder.',
  'The molecular and gene-regulatory mechanisms, including epigenetic changes, through which chronic alcohol use is thought to produce dependence and alcohol use disorder.',
  dp=['q:Alcoholism is a chronic disease characterized by trouble controlling the consumption of alcohol'],
  rel=[('contrast','Epigenetics of cocaine addiction',[],'Parallel topic for cocaine.')],flags=[TOPIC])
O('enwiki:76734839','a specific historical experiment (1969 animal studies), not a term')
D('enwiki:31300355','A brief, structured adaptation of motivational interviewing for alcohol and other substance problems.',
  'A time-limited counselling approach, typically four sessions, derived from motivational interviewing, that gives personalised feedback and builds motivation to change alcohol or other drug use.',
  dp=['q:is a time-limited, four-session adaptation used in Project MATCH','q:It is a development of motivational interviewing and motivational therapy.'],
  var=[('MET','abbreviation',['q:Motivational enhancement therapy (MET)'])],
  rel=[('contrast','Motivational therapy',[],'The broader approach MET was developed from.'),('contrast','motivational interviewing',[],'The counselling style MET adapts.')],
  flags=[L.pdup('Motivational therapy','closely related named therapies')])
D('enwiki:4682452','A therapy combining humanistic and cognitive-behavioural methods to motivate change in substance use.',
  'A treatment for substance use disorders combining humanistic counselling with cognitive-behavioural strategies, aimed at building a person\'s own motivation to change.',
  dp=['q:is a combination of humanistic treatment and enhanced cognitive-behavioral strategies','wd:P279=Q179661'],
  var=[('MT','abbreviation; ambiguous',['wda:MT'])],
  rel=[('hypernym','therapy',['wd:P279=Q179661']),('contrast','Motivational enhancement therapy',[],'A brief structured adaptation.')],
  flags=[L.pdup('Motivational enhancement therapy','closely related named therapies')])
O('enwiki:47047521','a specific place (a museum in Mexico), not a term')
D('enwiki:3273731','An infusion of mushrooms in water, either medicinal or psilocybin-containing.',
  'A tea made by steeping mushrooms in water; the term covers both medicinal mushroom teas and infusions of psilocybin mushrooms, whose active compounds are psilocybin and psilocin.',
  dp=['q:Mushroom tea is an infusion of mushrooms in water','q:The active ingredient in psychedelic mushroom teas are psilocin and its prodrug psilocybin.'],
  var=[('beoseot-cha','Korean medicinal mushroom tea; names only that sense',['q:mushroom teas known as beoseot-cha'])],
  rel=[('hypernym','herbal tea',['wd:P279=Q379932']),('contrast','Magic truffle',[],'Another psilocybin product.')],
  flags=['ambiguous: covers both medicinal and psychedelic senses','domain rule: preparation details are omitted'])
D('enwiki:81431780','A tryptamine with an N-sec-butyl group, related to DMT, briefly described by Shulgin.',
  'A tryptamine-family psychoactive compound related to DMT and other psychedelics, carrying a sec-butyl group on the side-chain nitrogen.',
  dp=['q:is a psychoactive drug of the tryptamine family related to psychedelics like dimethyltryptamine (DMT)'],
  var=[('NsBT','abbreviation',['wda:NsBT'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','N-tert-Butyltryptamine',[],'Isomer with a tert-butyl group.'),('contrast','5-MeO-NsBT',[],'5-methoxy analogue.')])
D('enwiki:69037620','A tryptamine with an N-tert-butyl group, related to DMT, briefly described by Shulgin.',
  'A tryptamine-family psychoactive compound related to DMT, carrying a tert-butyl group on the side-chain nitrogen.',
  dp=['q:is a psychoactive drug of the tryptamine family related to psychedelics like dimethyltryptamine (DMT)'],
  var=[('NtBT','abbreviation',['q:N-tert-Butyltryptamine (NtBT)'])],
  rel=[('hypernym','tryptamine alkaloid',['wd:P279=Q66589878']),('contrast','N-sec-Butyltryptamine',[],'Isomer with a sec-butyl group.')])
D('enwiki:39558336','A subculture that has grown around drug cartels, with its own music, dress and beliefs.',
  'A subculture that developed around the strong presence of drug-trafficking cartels, notably in Mexico, with characteristic dress, music, film and religious practices.',
  dp=['q:is a subculture that has developed in response to the strong presence of drug cartels','wd:P279=Q2389669'],
  var=[('narco culture','spelling variant',['wda:narco culture'])],
  rel=[('hypernym','Drug culture',['wd:P279=Q2389669'])])
O('enwiki:38978117','a social-inequality topic about one population, not a drug or public-health term',
  flags=['domain rule: the page centres on one population group; no demographic inference is drawn'])
L.save(21)
