import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=9
D('enwiki:7966','A genre of dance music and associated nightlife subculture from the late 1960s and 1970s.',
  'A dance-music genre and nightlife subculture that arose in US urban clubs in the late 1960s and peaked in the 1970s; its club scene was associated with recreational drug use.',
  dp=['q:Disco is a genre of dance music and a subculture','wd:P31=Q188451'],
  var=[('disco music','names the genre only',['wda:disco music']),('discotheque','names the venue, a different sense',['wn:lemma=disco'])],
  rel=[('hypernym','music genre',['wd:P31=Q188451']),('contrast','Clubbing (subculture)',[],'The broader activity of going to clubs.')],
  wn='disco.n.01',flags=['ambiguous: a music genre connected to drugs only through its subculture; peripheral to the domain','ambiguous: names both a music genre and a venue (discotheque)'])
D('enwiki:56103154','Discrimination and stigma directed at people who use drugs or have substance use disorders.',
  'Unfair treatment and stigma directed at people who use drugs or have substance use disorders, in society and in healthcare, often rooted in viewing addiction as a moral failing.',
  dp=['q:is a form of discrimination against people who abuse drugs, alcohol, and other substances','wd:P279=Q169207'],
  var=[('discrimination against drug users',None,['wda:discrimination against drug users']),('discrimination against people with substance use disorders','person-first phrasing',['wda:discrimination against people with substance use disorders'])],
  rel=[('hypernym','discrimination',['wd:P279=Q169207']),('contrast','drug-related stigma',[],'Stigma is attitudes; discrimination is treatment; often used together.')],
  flags=['The seed title uses "drug addicts", which current public-health usage avoids; the person-first variant is preferred'])
D('enwiki:243387','A medication for alcohol use disorder that causes an unpleasant reaction when alcohol is consumed.',
  'A medication, sold as Antabuse, that blocks the breakdown of alcohol so that drinking causes an immediate unpleasant, hangover-like reaction; it is used to support abstinence in alcoholism.',
  dp=['q:is a medication used to support the treatment of chronic alcoholism','q:by inhibiting the enzyme aldehyde dehydrogenase'],
  var=[('Antabuse','brand name',['wn:lemma=Antabuse']),('tetraethylthiuram disulfide','chemical name',['wda:tetraethylthiuram disulfide'])],
  rel=[('hypernym','Disulfiram-like drug',['wd:P2868=Q1302366']),('hypernym','medication',['wd:P366=Q12140']),('contrast','Acamprosate',[],'Reduces craving instead of causing an aversive reaction.')],
  wn='disulfiram.n.01')
D('enwiki:74857405','The unpleasant reaction that occurs when alcohol is taken with disulfiram or similar agents.',
  'The adverse reaction, with flushing, nausea and other symptoms, that follows alcohol intake in someone who has taken disulfiram or certain mushrooms; it is the basis of alcohol-aversive therapy.',
  dp=['q:is the effect of the interaction in the human body of alcohol drunk with disulfiram or some types of mushrooms'],
  var=[('DAR','abbreviation',['q:Disulfiram-alcohol reaction (DAR)']),('antabuse effect',None,['wda:antabuse effect']),('disulfiram-like reaction','when caused by other agents',['wda:disulfiram like reaction'])],
  rel=[('hypernym','alcohol intolerance',['wd:P279=Q28135156']),('contrast','Hangover',[],'Similar symptoms but a different cause.')])
D('enwiki:55272732','Any drug that causes a disulfiram-like aversive reaction to alcohol.',
  'A drug that, like disulfiram, provokes an adverse reaction to alcohol, such as nausea and flushing, by causing the toxic metabolite acetaldehyde to build up.',
  dp=['q:is a drug that causes  an adverse reaction to alcohol','q:These effects are caused by accumulation of acetaldehyde'],
  var=[('alcohol deterrent','when used deliberately for treatment; narrower',['wda:alcohol deterrent'])],
  rel=[('hyponym','Disulfiram',[]),('hypernym','central nervous system agent',['wd:P279=Q50429917'])],
  flags=['ambiguous: Wikidata merges this with "alcohol deterrents"; drugs causing the reaction as a side effect are not all deterrents'])
D('enwiki:1796740','Visiting multiple doctors to obtain multiple prescriptions.',
  'The practice of seeing several doctors to collect more prescriptions than one would provide, associated with substance use disorders and diversion of prescription drugs.',
  dp=['q:Doctor shopping is the practice of visiting multiple physicians to obtain multiple prescriptions.'],
  rel=[('hypernym','fraud',['wd:P279=Q28813']),('contrast','Drug fraud',[],'Wider category of fraud involving drugs.'),('contrast','Prescription drug addiction',[],'A possible underlying condition, not the behaviour.')],
  flags=['ambiguous: the phrase is also used for patients seeking second opinions without misuse; the source sense is prescription-seeking'])
O('enwiki:59860864','a creative work (podcast), not a term')
D('enwiki:9311172','Any non-nutrient chemical substance that produces a biological effect when administered to an organism.',
  'A chemical substance, other than a nutrient, that has a biological effect when taken into a living organism. The word covers both medicines and substances used non-medically.',
  dp=['q:A drug is any chemical substance other than a nutrient or an essential dietary ingredient'],
  var=[('drugs',None,['wda:drugs'])],
  rel=[('hypernym','xenobiotic',['wd:P279=Q409205']),('hyponym','Medication',['q:A pharmaceutical drug, also called a medication or medicine']),('hyponym','Psychoactive drug',[]),('contrast','Medication',[],'In everyday usage "drug" often implies an illicit substance, unlike "medication".')],
  wn='drug.n.01',flags=['ambiguous: "drug" is used both broadly (any bioactive substance) and narrowly (illicit or recreational substance); entry uses the broad sense'])
D('enwiki:73227898','Retinal damage caused by chronic drug misuse.',
  'Damage to the retina resulting from chronic drug misuse, including several distinct types, linked with substances such as poppers, opioids, stimulants, tobacco and alcohol.',
  dp=['q:Drug abuse retinopathy is damage to the retina of the eyes caused by chronic drug abuse.'],
  rel=[('hyponym','talc retinopathy',['q:maculopathy, Saturday night retinopathy, and talc retinopathy']),('hypernym','retinopathy',[])])
D('enwiki:76556523','The blocking by one drug of the action or effect of another substance.',
  'The process by which a medicine stops another substance from acting, preventing a biological response; it operates by chemical, pharmacokinetic, receptor or physiological mechanisms.',
  dp=['q:refers to a medicine stopping the action or effect of another substance','wd:P279=Q718753'],
  rel=[('hypernym','drug interaction',['wd:P279=Q718753']),('contrast','drug synergism',[],'Combined effects greater than expected; the opposite interaction.')])
L.save(9)
