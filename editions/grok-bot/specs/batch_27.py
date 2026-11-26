import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=27
def RNS(t): return f'ambiguous: redirect to non-seed page "{t}"; mapping left to the maintainer'
D('enwiki:52145687','Smoking hand-rolled tobacco with the lit end inside the mouth.',
  'A form of tobacco smoking in which the burning end of a hand-rolled cigar is held inside the mouth; it is a recognised risk factor for oral cancer and is practised in a few regions.',
  dp=['q:the burnt end of a hand rolled tobacco leaf is put in the mouth','wd:P279=Q662860'],
  rel=[('hypernym','Smoking',['wd:P279=Q662860'])],
  flags=['regional practice: parts of India, Zambia and the Philippines per the source','domain rule: the source\'s claims about which sex practises it more are not carried into the entry'])
D('enwiki:68856575','A theory explaining drug-related harms through physical, economic, social and political environments.',
  'A framework, associated with Tim Rhodes, that explains substance-use harms as arising from interactions between behaviour and the physical, economic, social and political environment, and argues that harm reduction should address all of these.',
  dp=['q:explains substance use harms as results of reciprocal relationships between human behavior'],
  var=[('risk environment framework',None,[])],
  rel=[('contrast','Harm reduction',[],'A field the framework informs.')],
  wd=False,wdr="Item Q108898404 has no statements; the bundle cannot confirm it.")
D('enwiki:6464447','The remaining end of a cannabis joint after most of it has been smoked.',
  'The butt end left over after most of a cannabis joint or blunt has been smoked.',
  dp=['q:A roach is the remains of a joint or blunt after most of it has been smoked.'],
  rel=[('contrast','roach clip',['q:Small metal clips to facilitate the smoking of a "roach" are called roach clips.'],'A holder used with the roach.')],
  wd=False,wdr="Item Q7339230 is a bare 'roach' label without statements; it cannot be confirmed as this sense.",
  wn='roach.n.02',flags=['ambiguous: "roach" also means a cockroach, a fish, a hairstyle and, in WordNet, a street name for flunitrazepam','In some countries "roach" also names the filter tip of a joint; not covered by the source'])
O('enwiki:1157115','a specific institution (a former Toronto co-operative college), not a term')
D('enwiki:334816','The way a drug or other substance is introduced into the body.',
  'The path by which a drug, poison or other substance enters the body, such as by mouth, by injection or by inhalation, classified by where it is applied or where it acts.',
  dp=['q:is the way by which a drug, fluid, poison, or other substance is introduced into the body'],
  var=[('ROA','abbreviation',['wda:ROA']),('administration route',None,['wda:administration route'])],
  rel=[('hypernym','technique',['wd:P279=Q2695280']),('hyponym','Drug injection',[]),('hyponym','Smoking',[],'Inhalation of smoke as a route.'),('hyponym','Skin popping',[])])
D('enwiki:67637847','A North Korean soybean-derived health supplement marketed as a blood purifier.',
  'A health supplement made in North Korea from soybeans and marketed, mainly to foreigners, as a blood purifier and a preventive against deep-vein thrombosis.',
  dp=['q:is a traditional Korean medicine (Koryo medicine) health supplement derived from soybeans'],
  rel=[('hypernym','medicinal product',['wd:P31=Q12034612']),('contrast','Kumdang-2',[],'Another North Korean product.')],
  flags=['ambiguous: a single named commercial product rather than a general term'])
D('enwiki:61091006','A public-health model of routine screening, brief intervention and referral for substance use.',
  'A public-health approach in which people are routinely screened for risky substance use, given a brief intervention where appropriate, and referred to specialist treatment if needed.',
  wp=1,dp=['q:Screening, Brief Intervention and Referral to Treatment (SBIRT) is a healthcare model'],
  var=[('SBIRT','abbreviation',['q:Screening, Brief Intervention and Referral to Treatment (SBIRT)'])],
  rel=[('hypernym','public health intervention',['wd:P279=Q1814351']),('uses','Alcohol Use Disorders Identification Test',[],'A common screening tool used within SBIRT.')],
  wdr="Item Q65049697 is the seed term's own item and matches the sense.",
  flags=[RNS('Brief intervention#Screening, brief intervention and referral to treatment')])
D('enwiki:21488622','A person or animal giving a drug to itself; in research, drug-reinforced operant behaviour.',
  'The giving of a drug to oneself, as when a patient injects insulin; in animal research, an operant-conditioning procedure in which the reward is a drug, used to model addiction.',
  dp=['q:the process of a subject administering a pharmacological substance to themself','q:self-administration is a form of operant conditioning where the reward is a drug'],
  rel=[('hypernym','pharmacotherapy',['wd:P279=Q701216']),('contrast','Self-medication',[],'Self-treatment decisions rather than the act of administering.')],
  flags=['ambiguous: medical sense and experimental-psychology sense'])
D('enwiki:578436','Using a substance to treat one\'s own physical or psychological conditions without medical supervision.',
  'Treating one\'s own physical or psychological complaints with a substance, most often over-the-counter drugs or supplements but also alcohol or illicit drugs, without professional direction.',
  dp=['q:is a human behavior in which an individual uses a substance or any exogenous influence to self-administer treatment'],
  var=[('DIY medicine','informal',['q:sometimes called do-it-yourself (DIY) medicine'])],
  rel=[('hypernym','self-care',['wd:P279=Q4519653']),('contrast','Recreational drug use',[],'Use for pleasure rather than relief.')])
D('enwiki:63793847','An immunomodulatory drug of heat-killed Mycobacterium w for gram-negative sepsis.',
  'An immunomodulating drug developed in India whose active ingredient is a heat-killed non-pathogenic mycobacterium, used in the treatment of gram-negative sepsis.',
  dp=['q:is a drug developed by Cadila Pharmaceuticals to treat gram-negative sepsis','q:The active ingredient is heat-killed Mycobacterium w'],
  rel=[('hypernym','immunomodulator',[])],
  wd=False,wdr="Item Q97358478 has no statements; the bundle cannot confirm it.",
  flags=['ambiguous: a single named therapeutic product with no substance-use or public-health sense; peripheral to the domain'])
L.save(27)
