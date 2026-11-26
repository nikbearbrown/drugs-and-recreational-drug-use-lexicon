import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=20
D('enwiki:46363582','A medicine that is a minor structural variant of an existing drug for the same conditions.',
  'A medication closely modelled on an existing drug, usually through small structural changes, and used for conditions already treated by drugs; the term is often used critically.',
  dp=['q:refers to a medication that is similar to a pre-existing drug','wd:P279=Q12140'],
  var=[('follow-on drug',None,['wda:follow-on drug']),('me-too compound',None,['wda:me-too compound'])],
  rel=[('hypernym','Medication',['wd:P279=Q12140']),('contrast','Bioparallel',[],'The proposed biologic counterpart.')],
  flags=['ambiguous: pharmaceutical industry term; peripheral to substance use and public-health terminology'])
D('enwiki:14278124','A 2-aminoindane entactogen, 5-methoxy-2-aminoindane, that releases serotonin and norepinephrine.',
  'An entactogen of the 2-aminoindane family, a ring-closed relative of the amphetamines, that acts mainly as a serotonin and norepinephrine releasing agent; it has appeared as a designer drug and has been studied as a pharmaceutical candidate.',
  dp=['q:is an entactogen of the 2-aminoindane family','q:The drug acts as a serotonin–norepinephrine releasing agent (SNRA)'],
  var=[('5-methoxy-2-aminoindane',None,['wda:5-methoxy-2-aminoindane']),('5-MeO-AI',None,['wda:5-MeO-AI']),('CMND-100','developmental code name',['q:by its developmental code name CMND-100']),('Chaperon','product name; names it only in that marketing context',['wda:Chaperon'])],
  rel=[('hypernym','indanes',['wd:P279=Q74738211']),('hypernym','Designer drug',[]),('contrast','MDAI',[],'A related 2-aminoindane entactogen.')])
D('enwiki:180121','A drug used to diagnose, cure, treat or prevent disease.',
  'A drug given for medical purposes, to detect, cure, treat or prevent illness, as distinct from substances used non-medically.',
  dp=['q:is a drug used to diagnose, cure, treat, or prevent disease','wd:P279=Q8386'],
  var=[('medicine',None,['wn:lemma=medicine']),('pharmaceutical drug',None,['wda:pharmaceutical drug']),('medicament',None,['wn:lemma=medicament']),('medicinal drug',None,['wn:lemma=medicinal drug'])],
  rel=[('hypernym','Drug',['wd:P279=Q8386']),('hyponym','Over-the-counter drug',[]),('contrast','Recreational drug use',[],'Non-medical use of drugs.')],
  wn='medicine.n.02',flags=['ambiguous: "medication" also names the act of treating with medicines (WordNet medication.n.02)'])
D('enwiki:3828753','The stopping of a medication by a clinician or by the patient.',
  'The ending of a course of medication, whether decided by the prescriber (then called deprescribing) or by the patient.',
  dp=['q:is the ceasing of a medication treatment for a patient by either the clinician or the patient themself','q:When initiated by the clinician, it is known as deprescribing.'],
  rel=[('hyponym','Deprescribing',['q:When initiated by the clinician, it is known as deprescribing.']),('contrast','Drug withdrawal',[],'A possible consequence of discontinuation.')])
D('enwiki:72439008','A proposed mechanism in which anaesthetics act mainly through the lipid membrane of cells.',
  'A proposed mechanism of anaesthetic action in which the anaesthetic works chiefly by interacting with the lipid bilayer of cell membranes, rather than directly with proteins.',
  dp=['q:is a mechanism of action that involves an anesthetic agent exerting its pharmaceutical effects'],
  var=[('membrane-mediated anaesthesia','British spelling',['q:Membrane-mediated anesthesia or anaesthesia (UK)'])],
  rel=[('contrast','Meyer–Overton correlation',[],'The older observation underlying lipid theories.')],
  flags=['ambiguous: pharmacology mechanism term; peripheral to substance use and public-health terminology'])
D('enwiki:11682712','A positional isomer of DOB with bromine and methoxy positions swapped.',
  'An amphetamine-family compound related to the psychedelic DOB, in which the bromine at position 4 and the methoxy group at position 5 are swapped.',
  dp=['q:is a psychoactive drug of the phenethylamine and amphetamine families related to the psychedelic drug DOB','q:It is a positional isomer of DOB'],
  var=[('5-bromo-2,4-dimethoxyamphetamine',None,['q:5-bromo-2,4-dimethoxyamphetamine'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','DOB',[],'Look-alike isomer.'),('contrast','4-Bromo-3,5-dimethoxyamphetamine',[],'Another DOB positional isomer.')])
D('enwiki:11694617','A 5-methylthio analogue of TMA-2, a positional isomer of Aleph (DOT).',
  'An amphetamine-family compound related to TMA-2, with the 5-position methoxy group replaced by a methylthio group; it is a positional isomer of Aleph.',
  dp=['q:is a psychoactive drug of the phenethylamine and amphetamine families related to TMA-2','q:the drug is a positional isomer of Aleph (DOT; para-DOT)'],
  var=[('5-methylthio-2,4-dimethoxyamphetamine',None,['q:5-methylthio-2,4-dimethoxyamphetamine']),('5-thio-TMA-2',None,['q:or as 5-thio-TMA-2'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','Ortho-DOT',[],'Another DOT positional isomer.'),('contrast','Aleph',[],'Look-alike isomer (para-DOT).')])
O('enwiki:71346406','an organisation (Barcelona cooperative), not a term')
D('enwiki:182719','Slang for a drink secretly dosed with an incapacitating drug.',
  'An American slang term for a drink to which an incapacitating drug, classically chloral hydrate, has been added without the drinker\'s consent in order to knock them out.',
  dp=['q:is a drink laced with an incapacitating agent, particularly chloral hydrate','wd:P31=Q42298422'],
  var=[('Mickey','short form',['wda:Mickey']),('knockout drops','names the drug rather than the drink',['q:hence the colloquial name knockout drops']),('spiked drink','broader',['q:(often called a spiked drink)'])],
  rel=[('hypernym','knockout drops',['wn:hypernym=knockout_drops.n.01'])],
  wn='mickey_finn.n.01',flags=['domain rule: no concealment detail is given'])
O('enwiki:40320035','a creative work (film), not a term')
L.save(20)
