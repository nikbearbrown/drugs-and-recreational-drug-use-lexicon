import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=10
D('enwiki:57266384','A harm-reduction service that lets people learn the content and purity of drugs they intend to use.',
  'A harm-reduction service that analyses substances people intend to take so they can learn what the substance contains and how pure it is, helping them avoid more dangerous products.',
  dp=['q:is a way to reduce the harm from drug consumption','q:find out the content and purity of substances that they intend to consume'],
  var=[('pill testing','common in Australia and the UK; may imply tablets only',['q:Drug checking or pill testing']),('drug testing','ambiguous: usually means testing people for drug use, not testing substances',['wda:drug testing'])],
  rel=[('hypernym','Harm reduction',['q:is a way to reduce the harm from drug consumption']),('hyponym','Reagent testing',[],'One technique used in drug checking.'),('contrast','drug test',[],'Testing a person\'s body fluids for drug use.')])
D('enwiki:48471223','A group of drugs sharing chemical structure, mechanism, mode of action or therapeutic use.',
  'A grouping of medications and related compounds that share similar chemical structures, a common mechanism of action, similar modes of action, or similar therapeutic uses.',
  dp=['q:is a group of medications and other compounds that share similar chemical structures'],
  var=[('pharmacological class',None,['wda:pharmacological class']),('class of drug',None,['wda:class of drug']),('drug group',None,['wda:drug group'])],
  rel=[('hypernym','group or class of chemical substances',['wd:P279=Q17339814']),('contrast','Anatomical Therapeutic Chemical Classification System',[],'A classification system rather than a single class.')])
D('enwiki:22907964','A coupon that reduces what a consumer pays for a pharmaceutical drug.',
  'A discount coupon for prescription or over-the-counter medicines, usually issued by drug companies and often used as a marketing tool.',
  dp=['q:is a coupon intended to help consumers save money on pharmaceutical drugs'],
  flags=['ambiguous: pharmaceutical marketing term; peripheral to substance use and public-health terminology'])
D('enwiki:35558299','The social practices, values, norms and symbols associated with recreational drug use.',
  'The shared practices, values, norms and symbols that surround recreational drug use, including drug subcultures whose members share views on the meaning and risks of drug use.',
  dp=['q:Drug culture is a set of social practices, values, norms, and symbols associated with recreational drug use.'],
  var=[('drug subculture','a group within drug culture; narrower',['wda:drug subculture'])],
  rel=[('hypernym','culture',['wd:P279=Q11042']),('hyponym','Narcoculture',[],'Culture around drug trafficking, a different subculture.'),('contrast','Recreational drug use',[],'The activity rather than its culture.')])
D('enwiki:16383884','The managed process of withdrawal from a drug on which a person is physically dependent.',
  'Intervention to manage withdrawal from a drug on which someone is physically dependent; the term is also used for the withdrawal experience itself and for treating acute overdose, and its use for dependence treatment is contested.',
  dp=['q:Drug detoxification (informally, detox)','q:the process and experience of a withdrawal syndrome'],
  var=[('detox','informal',['q:(informally, detox)'])],
  rel=[('hypernym','detoxification',['wd:P279=Q1090423']),('contrast','Drug rehabilitation',[],'Longer-term treatment that may follow detoxification.'),('contrast','Drug withdrawal',[],'The syndrome detoxification manages.')],
  flags=['ambiguous: the source gives several senses (managed withdrawal, the withdrawal process, overdose treatment) and calls the first arguably a misnomer'])
D('enwiki:15775369','Fraud in which drugs are diluted or altered so they are worth less than their sale price.',
  'A kind of fraud in which legal or illegal drugs are diluted or altered so that their value falls below the price charged, for example street drugs cut with inert powders or counterfeit medicines.',
  dp=['q:Drug fraud is a type of fraud in which drugs, legal or illegal, are cut or altered'],
  rel=[('hypernym','health care fraud',['wd:P279=Q5690836']),('contrast','Lacing (drugs)',[],'Lacing is the adulteration practice; fraud concerns the deceptive sale.'),('contrast','Doctor shopping',[],'A different, prescription-related fraud.')])
D('enwiki:6447865','Introducing a drug into the body through a hypodermic needle, medically or non-medically.',
  'A route of drug use in which a drug is introduced through a hypodermic needle, usually into a vein but also into muscle or under the skin; it occurs both in medical care and in non-medical drug use.',
  dp=['q:is a method of introducing a drug into the bloodstream via a hollow hypodermic needle','wd:P31=Q621636'],
  var=[('injecting','common in harm-reduction usage',['wda:injecting']),('shooting up','slang, non-medical use',['wda:shooting up'])],
  rel=[('hypernym','route of administration',['wd:P31=Q621636']),('hyponym','Skin popping',[],'Subcutaneous injection in drug culture.'),('contrast','Chasing the dragon',[],'An inhaled route.')],
  wdr="Item Q1369403 ('intravenous injection') lists 'drug injection' as an alias; it is narrower (intravenous only) but the closest candidate.",
  flags=['Wikidata item is intravenous injection, narrower than drug injection generally'])
D('enwiki:13803076','Drug policy that decriminalises, legalises or repeals prohibitions on drugs.',
  'A drug-policy process of decriminalising, legalising or repealing laws that prohibit producing, possessing, selling or using drugs, including legalisation, relegalisation and decriminalisation.',
  dp=['q:is a drug policy process of decriminalizing, legalizing, or repealing laws','wd:P279=Q1260003'],
  var=[('drug legalization','narrower; one variety',['wda:drug legalization']),('decriminalization of drugs','narrower; one variety',['wda:decriminalization of drugs'])],
  rel=[('hypernym','drug policy',['wd:P279=Q1260003']),('contrast','Harm reduction',[],'A public-health approach that can operate under prohibition.')],
  flags=['Wikidata lists legalisation and decriminalisation as aliases; the source treats them as varieties, so they are recorded with conditions'])
D('enwiki:2920372','The state of having no tolerance or habituation to a drug or drug class.',
  'The state of not being habituated or tolerant to a particular drug or group of related drugs, often because the person has never taken it; used in medical and non-medical contexts.',
  dp=['q:is the physiological state of non-habituation or non-tolerance'],
  var=[('drug-naïve','adjective form',['wda:Drug-naïve']),('drug naivety','spelling without diaeresis',[])],
  rel=[('contrast','drug tolerance',[],'The opposite state.'),('contrast','opioid-naive',[],'Narrower, drug-specific use.')])
D('enwiki:313009','Taking a drug in an amount much greater than recommended, with risk of toxicity or death.',
  'Taking in a drug or other substance in a quantity far above what is recommended or usual, to the point of risking harm, poisoning or death.',
  dp=['q:is the ingestion or application of a drug or other substance in quantities much greater than are recommended','wd:P279=Q114953'],
  var=[('overdose',None,['wda:overdose']),('OD','abbreviation',['wda:OD'])],
  rel=[('hypernym','poisoning',['wd:P279=Q114953']),('contrast','Overmedication',[],'Excess prescribing over time rather than an acute toxic dose.'),('contrast','Substance intoxication',[],'Intoxication need not be an overdose.')])
L.save(10)
