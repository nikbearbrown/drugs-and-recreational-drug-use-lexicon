import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=29
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
def RNS(t): return f'ambiguous: redirect to non-seed page "{t}"; mapping left to the maintainer'
O('enwiki:47357571','a specific company and mobile app, not a term')
O('enwiki:80942607','a specific organisation (a former London advocacy group), not a term')
D('enwiki:4813452','Lighting cannabis in a pipe by focusing sunlight with a magnifying lens.',
  'Slang for smoking cannabis by igniting it with sunlight concentrated through a magnifying lens rather than with a flame.',
  rel=[('hypernym','Smoking',[]),('contrast','Drug paraphernalia',[],'The lens is treated as paraphernalia in the redirect target.')],
  wp=None,wpr='The redirect target section "Magnifying lens" was not found at the pinned revision; the general Drug paraphernalia article is a broader concept.',
  wd=False,wdr="Item Q7556869 has no statements; the bundle cannot confirm it.",
  flags=[RNS('Drug paraphernalia#Magnifying lens'),'definition is model knowledge: the target section was absent from the pinned revision'])
O('enwiki:63544717','a specific clinical trial (WHO COVID-19 treatments trial), not a term')
D('enwiki:698717','A mixture of a stimulant with a depressant, classically cocaine with heroin.',
  'A combination of a stimulant and a depressant drug taken together, most commonly cocaine with heroin; the combination carries a high risk of fatal overdose.',
  dp=['q:is the polydrug mixture of a stimulant with a depressant','wd:P527=Q41576','wd:P527=Q60168'],
  var=[('powerball','slang',['q:Speedball, powerball, or over and under']),('over and under','slang',['q:Speedball, powerball, or over and under'])],
  rel=[('hypernym','psychoactive drug',['wd:P31=Q3706669']),('meronym','cocaine',['wd:P527=Q41576']),('meronym','heroin',['wd:P527=Q60168']),('hypernym','Polysubstance use',[],'A specific polydrug combination.')],
  flags=['domain rule: preparation and administration detail from the source is omitted'])
D('enwiki:608718','A psychotic disorder caused by stimulant use, with hallucinations, delusions and paranoia.',
  'A mental disorder with psychotic symptoms such as hallucinations, delusions and severe paranoia, usually following heavy or prolonged use of stimulants such as cocaine or methamphetamine, and occasionally during stimulant therapy.',
  dp=['q:also known as stimulant-induced psychotic disorder, is a mental disorder characterized by psychotic symptoms','wd:P279=Q170082'],
  var=[('stimulant-induced psychotic disorder','clinical name',['wda:stimulant-induced psychotic disorder']),('amphetamine psychosis','narrower: amphetamine-type stimulants',['wda:amphetamine psychosis'])],
  rel=[('hypernym','psychosis',['wd:P279=Q170082']),('contrast','Stimulant use disorder',[],'The use disorder rather than the psychosis.')])
D('enwiki:51015431','A substance use disorder involving stimulants that causes clinically significant impairment or distress.',
  'A substance use disorder in which ongoing use of cocaine, amphetamine-type or other stimulant drugs causes significant distress or impairment, rated from mild to severe.',
  dp=['q:is a type of substance use disorder where the use of stimulants caused clinically significant impairment or distress','wd:P279=Q7632070'],
  rel=[('hypernym','Substance use disorder',['wd:P279=Q7632070']),('contrast','Stimulant psychosis',[],'A psychotic complication.')])
O('enwiki:11124030','a specific hoax drug scare (2007), an event rather than a term')
D('enwiki:102959','Use of a drug in amounts or ways harmful to the user or others.',
  'Taking a drug in quantities or ways that cause harm to the person or to others; definitions differ between public health, medicine and criminal justice, and clinical usage now prefers "substance use disorder".',
  dp=['q:is the use of a drug in amounts or by methods that are harmful to the individual or others','wd:P279=Q110207349'],
  var=[('drug abuse',None,['wda:drug abuse']),('drug misuse','preferred in some public-health usage',['q:Differing definitions of drug misuse are used']),('harmful use','ICD term',['wda:harmful use'])],
  rel=[('hypernym','psychoactive drug use',['wd:P279=Q110207349']),('contrast','Substance use disorder',[],'The diagnostic category.'),('hyponym','Alcohol abuse',[])],
  wn='substance_abuse.n.01',
  flags=['Wikidata lists "injecting drug use" as an alias, which is a narrower practice; not recorded','ambiguous: stigmatised term whose clinical meaning overlaps Substance use disorder'])
D('enwiki:70604921','The use and misuse of drugs, including alcohol, cannabis and opium, in ancient Rome.',
  'The use of cannabis, opium, alcohol and other drugs in ancient Rome, both as medicine and for pleasure, and what Roman authors wrote about their addictive and harmful effects.',
  dp=['q:Cannabis and opium were used as medication to treat conditions such as insomnia or earaches.'],
  rel=[('hypernym','psychoactive drug use',['wd:P279=Q110207349']),('contrast','Substance abuse',[],'General concept.')],
  flags=[TOPIC,'Wikidata error: item is typed as an instance of substance abuse, drug trafficking and drug'])
L.save(29)
