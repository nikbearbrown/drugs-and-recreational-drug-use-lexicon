import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=4
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:76334245','Non-medical or inappropriate use of antipsychotic medications.',
  'The use of antipsychotic medications outside their intended therapeutic purpose, for example for sedation or other non-medical effects.',
  dp=['q:refers to the non-medical or inappropriate use of antipsychotic medications'],
  var=[('antipsychotics abuse',None,[])],
  rel=[('hypernym','Substance abuse',[],'A drug-specific form of substance misuse.'),('contrast','Self-medication',[],'Self-medication may involve the same drugs but describes a motive, not misuse as such.')])
D('enwiki:1181942','The set of commonly made arguments for and against prohibiting drugs.',
  'A survey of the reasons commonly given for and against drug prohibition, including claims about effectiveness, harms, costs and rights.',
  dp=['q:Commonly-cited arguments for and against the prohibition of drugs include the following:'],
  rel=[('contrast','Drug liberalization',[],'A policy position, not the debate itself.')],flags=[TOPIC])
D('enwiki:2050894','A substance that causes body tissues to shrink or constrict.',
  'A chemical or drug that constricts or tightens body tissues; the related sensory quality is the dry, puckering feel caused by tannins.',
  dp=['q:is a chemical that shrinks or constricts body tissues','wd:P279=Q1809112'],
  var=[('adstringent','rare variant spelling',['q:(sometimes called adstringent)']),('astringent drug',None,['wn:lemma=astringent drug']),('styptic','when used to stop bleeding; narrower',['wn:lemma=styptic'])],
  rel=[('hypernym','dermatologic drug',['wd:P279=Q1809112'])],
  wn='astringent.n.01',flags=['ambiguous: pharmacological class with no recreational or public-health drug-use sense; peripheral to the domain'])
O('enwiki:41650632','an organisation (Australian peer drug-user network), not a term')
D('enwiki:99398','An acute distressing psychological reaction during the effects of a psychedelic drug.',
  'An acute adverse psychological reaction, such as fear or panic, while under the effects of a psychoactive substance, chiefly a psychedelic. There is no agreed clinical definition.',
  dp=['q:is an acute adverse psychological reaction to the effects of psychoactive substances, namely psychedelics','q:There is no clear definition of what constitutes a bad trip.'],
  var=[('psychedelic crisis','clinical or harm-reduction phrasing',['q:psychedelic crisis']),('acute intoxication from hallucinogens','clinical phrasing; broader',['wda:acute intoxication from hallucinogens'])],
  rel=[('hypernym','psychedelic experience',['wd:P279=Q1076521']),('contrast','Hallucinogen persisting perception disorder',[],'A lasting disorder, not an acute episode.'),('contrast','Hallucinogen-induced psychotic disorder',[],'Psychosis outlasting intoxication.')],
  flags=['The source also lists "emergence phenomenon" as a synonym; that term normally names anaesthetic emergence reactions, so it is not recorded as a variant'])
D('enwiki:26983756','Dependence on barbiturates, involving tolerance and withdrawal and potential addiction.',
  'A state that develops with regular barbiturate use, marked by tolerance and potential addiction and physical dependence.',
  dp=['q:Barbiturate dependence develops with regular use of barbiturates.','q:Barbiturate use can lead to both addiction and physical dependence'],
  var=[('barbiturism','historical',['wda:barbiturism']),('barbitalism','historical',['wda:barbitalism'])],
  rel=[('hypernym','Substance dependence',[]),('contrast','Benzodiazepine use disorder',[],'Analogous condition for a different sedative class.')])
D('enwiki:36262014','A street name for a group of synthetic designer stimulants, mainly substituted cathinones.',
  'A group of recreational designer drugs, mostly synthetic cathinones, whose name comes from being sold labelled as bath salts. They are unrelated to genuine bathing products.',
  dp=['q:are a group of recreational designer drugs','q:The name derives from instances in which the drugs were disguised as bath salts.','wd:P279=Q7632116'],
  var=[('psychoactive bath salts',None,['wda:psychoactive bath salts']),('PABS','abbreviation',['wda:PABS']),('monkey dust','regional street name (UK); may name specific cathinones',['wda:monkey dust'])],
  rel=[('hypernym','Designer drug',['wd:P279=Q1200715']),('hypernym','cathinone',['wd:P279=Q7632116'],'Most products are substituted cathinones.'),('contrast','bath salts',[],'The cosmetic product sharing the name.')],
  wnr='The only WordNet synset is the cosmetic bath preparation, a different sense.')
D('enwiki:62385','A member of the mid-20th-century Beat social movement, a media stereotype.',
  'A member of the mid-twentieth-century American Beat movement, which rejected conformity and consumerism and experimented with art, spirituality and drugs.',
  dp=['q:Beatniks were members of a social movement in the mid-20th century'],
  var=[('beat',None,['wn:lemma=beat'])],
  rel=[('hypernym','stereotype',['wd:P31=Q167172'])],wn='beatnik.n.01',
  flags=['ambiguous: a cultural movement term connected to drugs only incidentally; peripheral to the domain'])
D('enwiki:65540554','A 2020 social media challenge involving deliberate overdose of diphenhydramine.',
  'An internet challenge from 2020 in which participants took excessive amounts of the antihistamine diphenhydramine to provoke deliriant effects, leading to poisonings.',
  dp=['q:is an internet challenge that emerged in 2020','wd:P31=Q3184856'],
  rel=[('hypernym','internet meme',['wd:P31=Q2927074']),('hypernym','Substance abuse',['wd:P31=Q3184856']),('contrast','Recreational use of dextromethorphan',[],'Different over-the-counter drug.')],
  flags=['ambiguous: a specific named internet phenomenon rather than a general term'])
D('enwiki:22951352','Use of benzodiazepines without prescription or recreationally, with risk of dependence.',
  'Non-prescribed or recreational use of benzodiazepines, which carries risks of dependence, withdrawal and long-term harms.',
  dp=['q:is the use of benzodiazepines without a prescription or for recreational purposes'],
  var=[('benzodiazepine misuse',None,['wda:benzodiazepine misuse']),('benzodiazepine abuse',None,['wda:benzodiazepine abuse'])],
  rel=[('hypernym','abuse of medicaments',['wd:P279=Q2258219']),('contrast','Effects of long-term benzodiazepine use',[],'Effects of prescribed long-term use, not misuse.')])
L.save(4)
