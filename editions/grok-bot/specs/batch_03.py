import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=3
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:2772469','Education that conveys information about alcohol\'s effects on health, families and society.',
  'Teaching and public information about how alcohol affects health, the family and society, historically introduced into schools by temperance groups and now part of prevention work.',
  dp=['q:is the practice of disseminating information about the effects of alcohol on health','wd:P279=Q8434'],
  rel=[('hypernym','education',['wd:P279=Q8434']),('hypernym','Substance abuse prevention',[],'Alcohol education is commonly a form of prevention activity.')])
D('enwiki:8844881','The practice of taking alcohol rectally rather than by drinking, a high-risk form of alcohol use.',
  'Introducing alcohol into the body through the rectum instead of drinking it. It is considered dangerous because it can cause rapid intoxication and bypasses vomiting as a protective response.',
  dp=['q:is the act of introducing alcohol into the rectum and colon via the anus','q:This method of alcohol consumption can be dangerous and even deadly'],
  var=[('butt-chugging','colloquial',['wda:butt-chugging']),('boofing','colloquial; also used for rectal use of other drugs',['q:butt-chugging or boofing'])],
  rel=[('hypernym','alcohol abuse',['wd:P279=Q7331102']),('hypernym','enema',['wd:P279=Q194517']),('hypernym','Route of administration',[],'A rectal route applied to alcohol.')])
D('enwiki:14678677','A theory that alcohol narrows perception and attention to salient cues, explaining its social effects.',
  'A cognitive-physiological model holding that alcohol narrows perception and thought so that drinkers attend to the most salient cues and neglect others, which explains many of its social and stress-relieving effects.',
  dp=['q:is a cognitive-physiological theory on alcohol use disorder','q:alcohol produces a myopia effect'],
  rel=[('contrast','disinhibition',[],'The model is offered as an alternative to the disinhibition account.')],
  flags=['Wikidata classes this theory under alcohol-related brain damage (Q18205193), which does not fit a cognitive theory; the link is kept for the item itself only'])
D('enwiki:5689023','A ten-item WHO screening questionnaire for hazardous and harmful alcohol use.',
  'A short WHO-endorsed screening questionnaire of ten items used to identify hazardous and harmful drinking and possible alcohol dependence.',
  dp=['q:is a ten-item questionnaire approved by the World Health Organization','q:to screen patients for hazardous (risky) and harmful alcohol consumption'],
  var=[('AUDIT','abbreviation',['q:The Alcohol Use Disorders Identification Test (AUDIT)']),('AUDIT questionnaire',None,['wda:AUDIT questionnaire'])],
  rel=[('contrast','AUDIT-C',[],'Three-item shortened version.')])
D('enwiki:10306673','Dementia caused by long-term heavy alcohol consumption.',
  'A form of dementia resulting from long-term excessive alcohol use, which damages the nervous system and impairs cognition.',
  dp=['q:is a form of dementia caused by long-term, excessive consumption of alcohol'],
  var=[('ARD','abbreviation',['q:Alcohol-related dementia (ARD)']),('alcohol dementia',None,['wda:Alcohol dementia'])],
  rel=[('contrast','Wernicke–Korsakoff syndrome',[],'A related alcohol-associated brain disorder caused by thiamine deficiency.')])
D('enwiki:2965','Continued alcohol use despite inability to manage the problems it causes; broadly, alcohol use disorder.',
  'Persistent drinking despite being unable to control the problems it causes. Some definitions also require dependence and withdrawal; in current diagnostic terms it broadly corresponds to alcohol use disorder.',
  dp=['q:Alcoholism is the continued drinking of alcohol despite the user being unable to manage the problems it causes.','q:Some definitions require evidence of dependence and withdrawal.'],
  var=[('alcohol use disorder','current clinical term; broadly equivalent',['wda:alcohol use disorder']),('alcohol dependence syndrome','older diagnostic term',['wda:alcohol dependence syndrome']),('alcohol addiction',None,['wn:lemma=alcohol addiction']),('AUD','abbreviation of alcohol use disorder',['wda:AUD'])],
  rel=[('hypernym','substance use disorder',['wd:P279=Q7632070']),('hypernym','drug addiction',['wn:hypernym=drug_addiction.n.01']),('contrast','Alcohol abuse',[],'Former DSM-IV category of harmful use without dependence.'),('contrast','Dipsomania',[],'Historical term for episodic craving; WordNet treats it as a synonym.')],
  wn='alcoholism.n.01',flags=[L.pdup('Alcohol abuse','often conflated in lay usage'),'WordNet lists "drunkenness" and "inebriation" as lemmas, which name intoxication, not the disorder; not used'])
D('enwiki:47699434','Problem alcohol use and alcohol use disorder among adolescents.',
  'Harmful or dependent alcohol use occurring during adolescence, notable for the added risks it poses to the developing brain.',
  dp=['q:presents a unique set of dangers due to the developing brain\'s vulnerability to alcohol\'s effects','wd:P279=Q15326'],
  var=[('underage drinking','broader: includes any drinking below the legal age, not only disorder',['wda:underage drinking'])],
  rel=[('hypernym','Alcoholism',['wd:P279=Q15326'])],flags=[TOPIC])
D('enwiki:2770','The WHO drug classification system grouping active ingredients by organ system and properties.',
  'A WHO-maintained system that classifies the active ingredients of drugs by the organ or system they act on and by their therapeutic, pharmacological and chemical properties, used to monitor drug use.',
  dp=['q:is a drug classification system that classifies the active ingredients of drugs','q:Its purpose is an aid to monitor drug use'],
  var=[('ATC','abbreviation',['q:The Anatomical Therapeutic Chemical (ATC) Classification System']),('Anatomical Therapeutic Chemical Classification',None,['wda:Anatomical Therapeutic Chemical Classification'])],
  rel=[('hypernym','medication classification',['wd:P279=Q2943035']),('contrast','Drug class',[],'A drug class is a group; ATC is a system of such groupings.')])
O('enwiki:73366456','legislation in one jurisdiction (a set of US bills), not a term')
D('enwiki:1918584','The class of medicines used to treat cancer by killing or inhibiting malignant cells.',
  'Medicines used against malignant tumours, acting by various mechanisms to kill cancer cells or stop their growth. They include cytotoxic and non-cytotoxic agents.',
  dp=['q:are medications used to treat malignant tumors','wd:P31=Q2585617'],
  var=[('anticancer drug',None,['wda:anticancer drug']),('antineoplastic agent',None,['wda:antineoplastic agent']),('cancer drug',None,['wn:lemma=cancer drug'])],
  rel=[('hypernym','drug class',['wd:P31=Q2585617']),('hyponym','Targeted therapy',[],'Targeted agents are one kind of antineoplastic therapy.')],
  wn='antineoplastic.n.01',flags=['ambiguous: oncology drug class with no recreational or public-health drug-use sense; peripheral to the domain'])
L.save(3)
