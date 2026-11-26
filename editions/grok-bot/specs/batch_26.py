import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=26
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:25949','Using psychoactive drugs to induce an altered state for pleasure or other non-medical purposes.',
  'Taking one or more psychoactive drugs to bring about an altered state of consciousness for pleasure or another casual, non-medical purpose.',
  dp=['q:is the use of one or more psychoactive drugs to induce an altered state of consciousness','wd:P279=Q110207349'],
  var=[('recreational drug','names the substance rather than the use',['wda:recreational drug']),('non-medical drug use','public-health phrasing; broader',[])],
  rel=[('hypernym','psychoactive drug use',['wd:P279=Q110207349']),('contrast','Substance use disorder',[],'Recreational use need not be disordered.'),('contrast','Self-medication',[],'Use to relieve symptoms rather than for pleasure.')])
D('enwiki:68773250','The apparent intentional consumption of psychoactive substances by non-human animals for pleasure.',
  'The reported deliberate consumption of psychoactive substances by non-human animals, apparently for pleasure; many such claims about wild animals are disputed.',
  dp=['q:the intentional ingestion of psychoactive substances in their environment for pleasure','wd:P279=Q2990593'],
  var=[('drug use in animals',None,['wda:drug use in animals'])],
  rel=[('hypernym','animal behavior',['wd:P279=Q2990593']),('contrast','zoopharmacognosy',['q:This is distinct from zoopharmacognosy'],'Self-medication by animals rather than intoxication.')],
  flags=[TOPIC])
D('enwiki:8879','Non-medical use of the cough suppressant dextromethorphan for its dissociative effects.',
  'The use of dextromethorphan, an ingredient of many over-the-counter cough medicines, as a recreational drug for its dissociative effects at amounts far above medical use.',
  dp=['q:is used as a recreational drug and entheogen for its dissociative effects'],
  var=[('DXM','abbreviation of the drug',['q:Dextromethorphan, or DXM']),('robo-tripping','slang for the practice',['wda:Robo-tripping']),('recreational use of DXM',None,['wda:recreational use of DXM'])],
  rel=[('hypernym','abuse of medicaments',['wd:P279=Q2258219']),('contrast','Benadryl challenge',[],'A different over-the-counter drug.'),('contrast','Lean (drug)',[],'Opioid cough syrup rather than dextromethorphan.')],
  wdr="Item Q7303086 is labelled 'Dextromethorphan (Drug)' but is a subclass of recreational drug use with aliases for the practice; it matches the sense.",
  flags=['the source lists many regional street names; only common, qualified forms are recorded'])
D('enwiki:47521175','Inhaling nitrous oxide for euphoric and dissociative effects.',
  'The non-medical inhalation of nitrous oxide, known as laughing gas, for its brief euphoric, dissociative and relaxing effects; harms include asphyxia and vitamin B12 deficiency with heavy use.',
  dp=['q:commonly referred to as laughing gas','q:which can induce euphoria, dissociation, hallucinogenic states of mind, and relaxation when inhaled'],
  var=[('laughing gas','names the substance',['q:commonly referred to as laughing gas']),('nos','slang (UK, Australia)',[])],
  rel=[('hypernym','Recreational drug use',[]),('hypernym','Inhalant',[]),('uses','Whipped-cream charger',[],'Common source of the gas.')],
  wd=False,wdr="Item Q23808207 has no statements; the bundle cannot confirm the sense.")
D('enwiki:1662513','In addiction, a return to drug use after a period of abstinence or recovery.',
  'In medicine, the return of a condition after a period of improvement; in addiction and psychiatry, the recurrence of drug use or other symptoms after a period of recovery.',
  dp=['q:is the recurrence of pathological drug use, self harm or other symptoms after a period of recovery'],
  var=[('recidivism','in medicine; in other fields means reoffending',['q:relapse or recidivism is a recurrence']),('lapse','sometimes distinguished as a brief slip',[])],
  rel=[('hypernym','recrudescence',['wd:P279=Q7303097']),('contrast','Relapse prevention',[],'The intervention aimed at preventing relapse.')],
  wn='backsliding.n.01',wnr='backsliding.n.01 (failure to maintain a higher state, with lemma relapse) is the closest noun sense.',
  flags=['ambiguous: general medical sense (disease recurrence) and addiction sense; entry centres on addiction'])
D('enwiki:41381753','A cognitive-behavioural approach to identifying and managing high-risk situations to prevent relapse.',
  'A cognitive-behavioural treatment approach that helps people anticipate and cope with high-risk situations so as to avoid returning to substance use or other problem behaviours.',
  dp=['q:is a cognitive-behavioral approach to relapse','wd:P279=Q1717246'],
  var=[('RP','abbreviation',['q:Relapse prevention (RP)'])],
  rel=[('hypernym','prevention',['wd:P279=Q1717246']),('contrast','Relapse',[],'The event being prevented.')])
D('enwiki:575912','A chemical for laboratory research only; in drug culture, a novel psychoactive sold under that label.',
  'A substance supplied for laboratory and scientific research rather than human or veterinary use; in drug culture the term labels novel psychoactive substances sold as "not for human consumption".',
  dp=['q:Research chemicals are chemical substances which scientists use for medical and scientific research purposes','q:a research chemical is not intended for human or veterinary use'],
  var=[('RC','abbreviation in drug culture',[])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','Designer drug',[],'Overlapping in the drug-culture sense.')],
  flags=['ambiguous: laboratory sense and drug-culture sense; the source leads with the laboratory sense'])
O('enwiki:35348099','a specific programme of one institution (US federal prisons), not a term')
D('enwiki:11941349','A live-in facility providing therapy for substance use disorders, mental illness or behavioural problems.',
  'A facility where people live while receiving treatment for addiction, mental illness or behavioural problems; often called a rehabilitation centre.',
  dp=['q:is a live-in health care facility providing therapy for substance use disorders','wd:P279=Q4260475'],
  var=[('RTC','abbreviation',['q:A residential treatment center (RTC)']),('residential treatment facility',None,['wda:residential treatment facility']),('rehab','informal; also names the treatment',['wda:rehab'])],
  rel=[('hypernym','medical facility',['wd:P279=Q4260475']),('contrast','Drug rehabilitation',[],'The treatment rather than the facility.')],
  flags=['Wikidata lists "therapeutic boarding school" as an alias, which is a narrower youth-specific institution; not recorded'])
D('enwiki:40513485','An approach to psychoactive drug use that aims to maximise benefits and minimise risks.',
  'An approach to using psychoactive drugs that seeks to maximise benefits and minimise risks, closely tied to harm reduction; some critics hold that illicit use cannot be responsible.',
  dp=['q:Responsible drug use seeks to maximize the benefits and minimize the risks','wd:P279=Q1458711'],
  rel=[('hypernym','Harm reduction',['wd:P279=Q1458711']),('contrast','Recreational drug use',[],'Use in general, not a risk-managing approach.')])
L.save(26)
