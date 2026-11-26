import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=7
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:30855169','The social activity and subculture of going to nightclubs to dance and socialise.',
  'Visiting and gathering at nightclubs and festivals to listen to music, dance and socialise; the related subculture is often called club culture.',
  dp=['q:is the activity of visiting and gathering socially at nightclubs','wd:P279=Q264965'],
  var=[('club culture','names the subculture rather than the activity',['q:(also known as club culture, related to raving)'])],
  rel=[('hypernym','subculture',['wd:P279=Q264965']),('contrast','Rave',[],'Related but distinct event culture.')],
  wnr='WordNet "clubbing" is digital clubbing (a medical sign) and the verb senses are unrelated; none is nightclub-going.',
  flags=['ambiguous: a social activity connected to drugs by association; peripheral to the domain'])
D('enwiki:1364686','The freedom of an individual to control their own mental processes and consciousness.',
  'The principle that a person has the right to control their own cognition and states of consciousness, framed as an extension of freedom of thought and invoked in debates on drug use and neurotechnology.',
  dp=['q:is the freedom of an individual to control their own mental processes, cognition, and consciousness'],
  var=[('right to mental self-determination',None,['wda:right to mental self-determination'])],
  rel=[('hypernym','liberty',['wd:P279=Q2979'])])
D('enwiki:2937493','A separation technique using cold water; in drug culture, separating an opioid from other tablet ingredients.',
  'A technique that separates components of a mixture by differences in their solubility in cold water. In drug culture the term refers to removing other ingredients from combination opioid tablets; the method itself is not described here.',
  dp=['q:is the process whereby a substance is extracted from a mixture via cold water','q:It is a type of fractional crystallization.'],
  var=[('CWE','abbreviation',['q:(also called CWE)'])],
  rel=[('hypernym','fractional crystallization',['q:It is a type of fractional crystallization.'])],
  flags=['domain rule: preparation steps in the source are deliberately omitted; only the term is described'])
D('enwiki:41016474','A toxic mineral-based psychoactive powder used in medieval China.',
  'A poisonous psychoactive preparation based on several minerals that was popular in China from the Six Dynasties to the Tang dynasty.',
  dp=['q:was a poisonous psychoactive drug popular in China'],
  var=[('Five Minerals Powder',None,['wda:Five Minerals Powder']),('hanshisan','pinyin romanisation',[])],
  rel=[('hypernym','traditional Chinese medical formula',['wd:P31=Q6791480']),('hypernym','Psychoactive drug',['wd:P366=Q3706669'])])
D('enwiki:67074309','Drugs that doctors frequently prescribe, often first-line treatments for common diseases.',
  'Medicines frequently prescribed by doctors for common conditions, often as first-line treatments.',
  dp=['q:are drugs that are frequently provided by doctors in a prescription to treat a certain disease'],
  rel=[('hypernym','Medication',['wd:P279=Q12140'])],
  flags=[TOPIC,'ambiguous: a loose descriptive grouping rather than an established term'])
D('enwiki:59612421','A learned automatic response opposite to a drug\'s effect, triggered by cues associated with use.',
  'An automatic, learned bodily response that opposes the effect of alcohol or another drug and is triggered by cues linked to past use. It helps explain why tolerance depends on setting and why overdose risk rises in unfamiliar settings.',
  dp=['q:is an automatic response that is opposite to the effect of alcohol or substance usage'],
  var=[('CR','abbreviation used in the source; ambiguous elsewhere',['q:Conditioned compensatory response (CR)'])],
  rel=[('contrast','drug tolerance',[],'Tolerance is the outcome; the compensatory response is one mechanism.')])
D('enwiki:7751709','A drug-like effect felt by a sober person from being around someone who is intoxicated.',
  'A drug-like experience in a sober person brought on by contact with someone under the influence, attributed to conditioning and setting much like a placebo effect.',
  dp=['q:a drug-like effect just by coming into contact with someone who is under the influence of a psychoactive drug'],
  rel=[('contrast','second-hand smoke exposure',[],'Actual exposure to drug smoke is a different, pharmacological effect.')],
  flags=['ambiguous: the term is also used loosely for genuine passive exposure to cannabis smoke'])
D('enwiki:18556316','Banknotes carrying traces of cocaine or other drugs.',
  'The presence of traces of cocaine or other illicit drugs on circulating banknotes, documented in many countries and relevant to forensic evidence.',
  dp=['q:Most banknotes have traces of cocaine on them'],
  rel=[('hypernym','money',['wd:P279=Q1368'])],flags=[TOPIC])
D('enwiki:80303804','A cactus species endemic to Mexico.',
  'A species of cactus native to Mexico. The source does not describe any drug use of it.',
  dp=['q:is a species of cactus that is endemic to Mexico'],
  rel=[('hypernym','taxon',['wd:P31=Q16521'])],
  flags=['ambiguous: a plant species listed in Category:Drugs without stated drug relevance','The pinned article opens with the name Coryphantha cornifera, a different species; likely an error in the source'])
O('enwiki:63435931','a specific research effort (drug development for one disease), not a term')
L.save(7)
