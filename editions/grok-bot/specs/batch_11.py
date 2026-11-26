import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=11
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
O('enwiki:69619911','drug policy of one jurisdiction (a US state), not a term')
D('enwiki:36201623','Chemicals that can be used to manufacture illicit drugs and are therefore regulated.',
  'Substances usable in the manufacture of illicit drugs; most also have legitimate industrial and consumer uses, so they are monitored under international precursor-control rules.',
  dp=['q:are substances used to manufacture illicit drugs','q:Most precursors also have legitimate commercial uses'],
  var=[('precursor chemicals',None,['q:precursor chemicals or simply precursors']),('precursors','in drug-control contexts only',['q:or simply precursors'])],
  rel=[('hypernym','precursor',['wd:P279=Q247994'])],
  flags=['domain rule: no information on which chemicals yield which drugs or how; the entry describes the regulatory term only'])
D('enwiki:21054515','A highly characterised material used to test the identity, strength, quality and purity of pharmaceuticals.',
  'A highly characterised reference material against which the identity, strength, quality and purity of pharmaceutical substances and medicinal products are tested; pharmacopoeial standards are a subset.',
  dp=['q:is a highly characterized material suitable to test the identity, strength, quality and purity'],
  var=[('pharmaceutical reference standard',None,['q:or pharmaceutical reference standard'])],
  rel=[('hyponym','pharmacopoeial reference standard',['q:Pharmacopoeial reference standards are a subset of pharmaceutical reference standards.'])],
  flags=['ambiguous: pharmaceutical quality-control term; peripheral to substance use and public-health terminology'])
D('enwiki:427922','Medical or psychotherapeutic treatment for dependence on psychoactive substances.',
  'The process of medical or psychological treatment for dependence on alcohol, prescription drugs or illicit drugs, aimed at stopping substance misuse and its consequences.',
  dp=['q:is the process of medical or psychotherapeutic treatment for dependency on psychoactive substances','wd:P279=Q179661'],
  var=[('rehab','informal',[]),('substance abuse treatment','broadly equivalent',['wda:substance abuse treatment']),('drug treatment','ambiguous: also means pharmacotherapy generally',['wda:drug treatment'])],
  rel=[('hypernym','therapy',['wd:P279=Q179661']),('contrast','Drug detoxification',[],'Managed withdrawal, often an early stage.'),('hyponym','Residential treatment center',[],'A setting for rehabilitation.')],
  wdr="Item Q1260022 ('substance abuse treatment') has drug rehabilitation aliases and matches the sense.")
D('enwiki:33776988','References to and associations of drug use in music and music culture.',
  'The long-standing association between music and recreational drug use, including drug references in songs and drug use within music scenes.',
  dp=['q:Drug use in music has been a topic of discussion and debate since at least the 1930s'],
  var=[('drug use in songs','narrower: lyrics only',['wda:drug use in songs'])],flags=[TOPIC])
O('enwiki:81562692','an organisation (Canadian compassion club), not a term')
D('enwiki:419447','The symptoms that follow abrupt stopping or reduction of a drug on which a person is dependent.',
  'The set of symptoms that appears when someone dependent on a medication or recreational drug abruptly stops or cuts down; it presupposes physical or psychological dependence.',
  dp=['q:is the group of symptoms that occur upon the abrupt discontinuation or decrease in the intake'],
  var=[('withdrawal','in drug contexts',['wda:withdrawal']),('drug withdrawal syndrome',None,['q:drug withdrawal syndrome']),('abstinence syndrome','older clinical term',['wda:abstinence syndrome'])],
  rel=[('hypernym','syndrome',['wd:P279=Q179630']),('requires','Physical dependence',['q:one must have first developed a form of drug dependence'],'Dependence (physical or psychological) is a prerequisite.'),('contrast','Medication discontinuation',[],'Stopping a drug, which may or may not cause withdrawal.')],
  wnr='withdrawal.n.09 means the act of ending drug taking, not the symptom syndrome.')
D('enwiki:1591223','The documented association between drug use and sex work.',
  'The relationship between drug use and prostitution, which studies have found to be correlated, with the direction of the link varying between settings.',
  dp=['q:Drugs and prostitution have been documented to have a direct correlation.'],
  rel=[('contrast','Sex and drugs',[],'Broader topic of drugs in sexual contexts.')],
  flags=[TOPIC,'domain rule: population-specific claims in the source are not carried into the entry'])
D('enwiki:67269120','How drugs alter sexual desire through hormonal and neurotransmitter effects.',
  'The ways in which drugs increase or reduce sexual desire by acting on sex hormones and neurotransmitter systems in the brain.',
  dp=['q:is about sexual desire being manipulated through drugs from various approaches'],
  rel=[('contrast','Sex and drugs',[],'Drug use in sexual settings rather than effects on desire.')],flags=[TOPIC])
D('enwiki:21605714','The effects of medications and recreational drugs taken during pregnancy on the pregnant person and fetus.',
  'The effects that medications and recreational drugs can have during pregnancy, on the pregnant woman and on the fetus, which may differ from their effects outside pregnancy.',
  dp=['q:may have effects during pregnancy on the pregnant woman and fetus'],
  rel=[('contrast','Teratology',[],'The study of birth defects, broader than drugs.')],
  wd=False,wdr="Item Q5308960 is modelled as a disease (substance use disorder, teratologic disease), which does not match a topic about drug effects in pregnancy.",
  flags=[TOPIC])
L.save(11)
