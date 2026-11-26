import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=2
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:82042226','A 5-methoxy tryptamine with an N-sec-butyl group that appeared online as a designer drug in 2022.',
  'A tryptamine of the 5-methoxytryptamine group carrying a sec-butyl group on the side-chain nitrogen. It surfaced as a novel designer drug through an online drug forum in late 2022.',
  dp=['q:is a psychoactive drug of the tryptamine and 5-methoxytryptamine families','q:It emerged as a novel designer drug online in December 2022.'],
  var=[('5-methoxy-N-sec-butyltryptamine',None,['wda:5-methoxy-N-sec-butyltryptamine'])],
  rel=[('hypernym','Designer drug',['q:It emerged as a novel designer drug online in December 2022.']),('contrast','N-sec-Butyltryptamine',[],'Same side chain without the 5-methoxy group.')])
D('enwiki:81460166','The ring-chlorinated derivative of MDA, an amphetamine-family psychoactive compound.',
  'A methylenedioxy amphetamine with a chlorine atom added to the ring of MDA. It is psychoactive and also a weak monoamine oxidase inhibitor.',
  dp=['q:It is the 6-chloro derivative of MDA.','q:It is a weak monoamine oxidase inhibitor (MAOI).'],
  var=[('6-chloro-3,4-methylenedioxyamphetamine',None,['q:6-chloro-3,4-methylenedioxyamphetamine']),('2-Cl-4,5-MDA',None,['q:(2-Cl-4,5-MDA)'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','2-Bromo-4,5-methylenedioxyamphetamine',[],'Look-alike bromo analogue of MDA.')])
D('enwiki:3560079','A medication used to reduce alcohol craving in the treatment of alcohol use disorder.',
  'A prescription medication, sold as Campral, that is used alongside counselling to reduce craving for alcohol and support abstinence in alcohol use disorder.',
  dp=['q:is a medication which reduces cravings in alcoholism','wd:P366=Q12140'],
  var=[('Campral','brand name',['q:sold under the brand name Campral']),('N-acetylhomotaurine','chemical name',['wda:N-Acetylhomotaurine'])],
  rel=[('hypernym','medication',['wd:P366=Q12140']),('contrast','Disulfiram',[],'Another alcohol use disorder medication with a different mechanism (aversive reaction rather than craving reduction).')])
D('enwiki:27707818','A drug-associated state of agitation and restlessness, reported especially when starting SSRIs.',
  'A state of restlessness, agitation, anxiety and emotional lability observed in association with some psychoactive medications, particularly early in SSRI treatment. A causal role of the drugs has not been established.',
  dp=['q:is a form of stimulation or agitation that has been observed in association with some psychoactive drugs','q:A causative role has not been established.'],
  rel=[('hypernym','anxiety',['wd:P279=Q154430'],'Wikidata classes it under anxiety.')])
D('enwiki:65297106','A clinical-trial design whose parameters may be modified based on interim analysis.',
  'A clinical trial design in which planned changes to the trial, such as dosing arms or sample size, can be made after interim analyses, unlike fixed-protocol trials.',
  dp=['q:may be changed based on an interim analysis'],
  rel=[('contrast','randomized controlled trial',[],'Traditional trials keep the protocol fixed until completion.')],
  flags=['ambiguous: drug-development methodology term; peripheral to substances and recreational use'])
D('enwiki:27158894','A disorder of compulsive drug use or rewarding behaviour that persists despite harm.',
  'A neuropsychological disorder marked by a persistent, intense urge to use a drug or repeat a rewarding behaviour despite substantial harm. Repeated use causes lasting changes in brain reward and control systems.',
  dp=['q:Addiction is a neuropsychological disorder characterized by a persistent and intense urge to use a drug'],
  var=[('dependence','in older or lay usage; technical usage distinguishes physical dependence from addiction',['wda:dependence'])],
  rel=[('hypernym','health problem',['wd:P279=Q2057971']),('contrast','Physical dependence',[],'Physical dependence can exist without addiction.'),('contrast','Substance use disorder',[],'Diagnostic category overlapping with addiction; not identical.')],
  wn='addiction.n.01',wnr='Sense 1 (dependence on a habit-forming substance) is closest; senses 2 and 3 are craving and a Roman-law term.',
  flags=['WordNet sense 1 equates addiction with dependence, which current terminology separates'])
D('enwiki:28734159','The psychiatric subspecialty concerned with substance use and other addictive disorders.',
  'A subspecialty of psychiatry dealing with the evaluation, diagnosis and treatment of people with addiction-related disorders, including substance use disorders and behavioural addictions.',
  dp=['q:Addiction psychiatry is a medical subspecialty within psychiatry','wd:P279=Q7867'],
  rel=[('hypernym','psychiatry',['wd:P279=Q7867']),('contrast','addiction medicine',[],'Related specialty that is not limited to psychiatry.')])
D('enwiki:1616827','A substance covertly added to a product, lowering its purity or safety; in street drugs, lacing.',
  'A substance added, often secretly, to another product in a way that can compromise its safety or effectiveness, typically to cut costs. Adulteration of street drugs is known as lacing.',
  dp=['q:An adulterant is a substance discreetly added to another that may compromise its safety or effectiveness.','q:The adulteration of street drugs is known as lacing.'],
  var=[('adulterator',None,['wn:lemma=adulterator'])],
  rel=[('hypernym','material',['wd:P279=Q214609']),('contrast','Cutting agent',[],'Cutting agents dilute a drug; the terms overlap and are often confused.'),('contrast','Lacing (drugs)',[],'Lacing is the act or practice of adulterating street drugs.')],
  wn='adulterant.n.01')
D('enwiki:65737896','An EU regulatory class of medicines based on gene therapy, cell therapy or tissue engineering.',
  'A European regulatory category of medicines built on gene therapy, somatic cell therapy or tissue engineering, with criteria set out in EU regulation.',
  dp=['q:are advanced therapeutic drugs that are based on cell therapy or gene therapy','q:defined in Article 17 of Regulation (EC) No 1394/2007'],
  var=[('ATMP',None,['wda:ATMP'])],
  rel=[('hypernym','Medication',['wd:P31=Q12140'])],
  flags=['ambiguous: regulatory medicines term; peripheral to recreational drug use'])
D('enwiki:3039288','In drug culture, the lingering positive after-effects following a drug experience.',
  'In recreational drug use, positive mental and physical effects that remain after the main or peak effects of a drug have faded, most often described after psychedelics and entactogens.',
  dp=['q:refers to positive physical and mental effects that linger after the main effects of a drug have subsided'],
  rel=[('contrast','Hangover',[],'Negative after-effects rather than positive ones.')],
  wd=False,wdr='Item Q4690719 is a bare "Afterglow" label with no claims; it cannot be confirmed as this drug-culture sense.',
  wnr='WordNet senses are a sky glow and pleasant remembering; neither is the drug-culture sense.')
D('enwiki:43173137','Ethanol considered as a psychoactive drug, the active ingredient of alcoholic drinks.',
  'Ethanol considered as a drug: the intoxicating ingredient of beer, wine and spirits, acting as a central nervous system depressant that causes intoxication.',
  dp=['q:is the active ingredient in alcoholic drinks such as beer, wine, and distilled spirits','q:Alcohol is a central nervous system (CNS) depressant','wd:P279=Q3706669'],
  var=[('ethanol','chemical name; names the drug when the substance rather than the drink is meant',['q:sometimes referred to by the chemical name ethanol']),('alcohol as a drug',None,['wda:alcohol as a drug'])],
  rel=[('hypernym','Psychoactive drug',['wd:P279=Q3706669']),('contrast','alcoholic beverage',[],'The drink containing the drug, not the drug itself.')],
  wnr='alcohol.n.01 is the beverage and alcohol.n.02 the chemical class; neither is ethanol as a drug.')
D('enwiki:231994','A spectrum of harmful alcohol use; a former DSM-IV diagnosis now merged into alcohol use disorder.',
  'A pattern of harmful alcohol use ranging from mild to severe. It was a DSM-IV diagnosis, merged in DSM-5 with alcohol dependence into alcohol use disorder.',
  dp=['q:Alcohol abuse encompasses a spectrum of alcohol-related substance abuse.','q:it has been merged with alcohol dependence in the DSM-5 into alcohol use disorder'],
  var=[('alcohol misuse',None,['wda:alcohol misuse']),('harmful use of alcohol','ICD-style phrasing',['wda:harmful use of alcohol']),('alcohol use disorder','only as the DSM-5 successor category; broader than DSM-IV alcohol abuse',['wda:alcohol use disorder'])],
  rel=[('hypernym','Substance abuse',['wd:P279=Q3184856']),('contrast','Alcoholism',[],'Alcoholism usually denotes dependence; the terms are often conflated.')],
  wn='alcohol_abuse.n.01',flags=[L.pdup('Alcoholism','often conflated in lay usage')])
D('enwiki:24387271','Alcohol consumption as a causal risk factor for breast cancer.',
  'The established relationship in which drinking alcohol raises the risk of breast cancer; alcohol is among the most common modifiable breast-cancer risk factors.',
  dp=['q:drinking alcoholic beverages, including wine, beer, or liquor, is a risk factor for breast cancer'],
  rel=[('hypernym','alcohol and cancer',['wd:P279=Q4713253'])],flags=[TOPIC])
O('enwiki:15266163','an organisation (Australian non-profit), not a term')
D('enwiki:78149881','The interrelationship between alcohol use and human society across history and cultures.',
  'The long historical relationship between people and alcohol, covering the drug\'s social, cultural and health effects on individuals and societies.',
  dp=['q:Alcohol and society have been closely intertwined for a large portion of human history.'],
  flags=[TOPIC])
L.save(2)
