import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=12
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
O('enwiki:27914146','a website and business (online drug encyclopedia), not a term')
D('enwiki:12391913','Having a mental illness together with a co-occurring substance use disorder.',
  'The co-occurrence in one person of a mental illness and a substance use disorder; whether one category suits such a varied group is debated.',
  dp=['q:is the condition of having a mental illness and a comorbid substance use disorder'],
  var=[('co-occurring disorders',None,['wda:co-occurring disorders']),('COD','abbreviation',['wda:COD']),('dual pathology','mainly European usage',['q:or dual pathology'])],
  rel=[('hypernym','mental disorder',['wd:P279=Q12135']),('contrast','Polysubstance use',[],'Multiple substances, not mental illness plus substance use.')],
  flags=['ambiguous: "dual diagnosis" is also used in intellectual-disability services for disability plus mental illness'])
O('enwiki:797244','a creative work (book), not a term')
O('enwiki:79240376','a creative work (song), not a term')
D('enwiki:54048325','The policies and practices schools and the education sector use to address substance use.',
  'How the education sector plans, develops and implements policies and practices addressing tobacco, alcohol and other drug use in educational settings.',
  dp=['q:refers to the way in which the education sector strategizes'],
  rel=[('contrast','Substance abuse prevention',[],'Broader prevention field not limited to education.')],flags=[TOPIC])
D('enwiki:21442391','The dependence and adverse effects associated with using benzodiazepines for months or longer.',
  'The consequences of using benzodiazepines over the long term, commonly three months or more, including dependence and possible harm to cognition and physical and mental health.',
  dp=['q:include drug dependence as well as the possibility of adverse effects on cognitive function','q:Long-term use is sometimes described as use for at least three months.'],
  rel=[('hypernym','side effect',['wd:P31=Q3269441']),('contrast','Benzodiazepine use disorder',[],'Misuse rather than long-term prescribed use.')],flags=[TOPIC])
D('enwiki:11996885','A battery-powered device that vaporises a liquid for inhalation, simulating smoking.',
  'A battery-powered device that heats a liquid, usually containing nicotine, into an aerosol that the user inhales, simulating tobacco smoking without combustion.',
  dp=['q:is a device that simulates tobacco smoking','q:Instead of smoke, the user inhales vapor, often called "vaping".'],
  var=[('e-cigarette',None,['wda:e-cigarette']),('vape','informal',['q:or vape']),('electronic nicotine delivery system','regulatory term; narrower, nicotine products only',['wda:Electronic Nicotine Delivery System']),('e-cig','informal',['wda:e-cig'])],
  rel=[('hypernym','electronic device',['wd:P279=Q2858615']),('contrast','Smoking',[],'Combustion of tobacco rather than vaporisation.'),('contrast','Nicotine replacement therapy',[],'Licensed cessation products.')])
D('enwiki:70764591','An isonicotinic acid derivative registered as an antiviral drug in several Eastern European countries.',
  'An antiviral drug derived from isonicotinic acid, registered in Ukraine and several other Eastern European and Central Asian countries.',
  dp=['q:Enisamium iodide is a derivative of isonicotinic acid.','q:is a registered antiviral drug sold in Ukraine'],
  var=[('carbabenzpiride','shortened chemical name',['q:the shortened name carbabenzpiride is sometimes used']),('Amizon','trade name',['q:under the trade names Amizon'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('hypernym','antiviral drug',[])],
  flags=['ambiguous: an antiviral medicine with no recreational or public-health drug-use sense; peripheral to the domain'])
D('enwiki:261899','A psychoactive substance used to induce altered states for spiritual or religious purposes.',
  'A psychoactive substance, typically a hallucinogen, used to bring about altered states of consciousness in religious, spiritual or ritual settings; the same substances are also used recreationally and therapeutically.',
  dp=['q:Entheogens are psychoactive substances used in spiritual, religious, recreational, therapeutic, and experimental contexts','wd:P279=Q3706669'],
  rel=[('hypernym','Psychoactive drug',['wd:P279=Q3706669']),('contrast','hallucinogen',[],'A pharmacological class; entheogen names a use context.')],
  flags=['ambiguous: the term names a context of use rather than a pharmacological class, so membership depends on setting'])
D('enwiki:12678136','Archaeological and historical evidence for ritual use of entheogenic drugs.',
  'The archaeological evidence that cultures have used entheogenic substances in religious, shamanic or spiritual contexts over thousands of years.',
  dp=['q:Entheogenic drugs have been used by various cultural groups for thousands of years'],
  rel=[('contrast','History of entheogenic drugs',[],'Overlapping historical topic.')],flags=[TOPIC,L.pdup('History of entheogenic drugs','overlapping historical topic pages')])
L.save(12)
