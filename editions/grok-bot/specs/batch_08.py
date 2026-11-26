import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=8
def DUP(t): return f'duplicate: seed page is a redirect to seed "{t}" ({L.cid(t)})'
D('enwiki:19681345','A smokable free-base form of cocaine.',
  'A smokable free-base preparation of cocaine that gives a brief, intense high and is considered the most addictive way cocaine is used.',
  dp=['q:is a free base form of the stimulant cocaine that can be smoked','wd:P31=Q211036'],
  var=[('crack','common short form',['q:commonly known simply as crack']),('rock','slang; also names other drugs',['q:and also known as rock'])],
  rel=[('hypernym','stimulant',['wd:P31=Q211036']),('hypernym','Free base',['q:is a free base form of the stimulant cocaine'],'Crack is one free-base form of cocaine.'),('contrast','cocaine hydrochloride',[],'Powder salt form, usually snorted or injected.')],
  wn='crack.n.08',flags=['WordNet lists "tornado" as a lemma of this synset; it is an obscure slang name and is not recorded'])
D('enwiki:16767087','A substance or procedure that resolves a medical condition.',
  'Anything, such as a medicine, surgery or lifestyle change, that ends a medical condition rather than only easing it.',
  dp=['q:A cure is a substance or procedure that resolves a medical condition.'],
  var=[('remedy','broader: also treatments that only relieve',['wda:remedy'])],
  rel=[('hypernym','therapy',['wd:P279=Q179661']),('contrast','symptomatic treatment',[],'Relieves symptoms without resolving the condition.')],
  wn='remedy.n.02',wnr='remedy.n.02 is the noun sense of a medicine or therapy that cures; the other candidates are verbs.',
  flags=['ambiguous: general medical term with no specific drug-use sense; "cure" also has non-medical senses (preserving, hardening)'])
D('enwiki:2707303','A substance used to dilute or adulterate an illicit drug.',
  'A substance added to a street drug to dilute or bulk it out, or to replace part of it with something cheaper.',
  wp=1,dp=['q:(referred to as the lacing agent or cutting agent)','q:it is most commonly done to bulk up the original product'],
  var=[('lacing agent','when the added substance is active rather than a diluent',['q:referred to as the lacing agent or cutting agent'])],
  rel=[('hypernym','Adulterant',['wd:P279=Q1658591']),('contrast','Lacing (drugs)',[],'Lacing is the practice; the cutting agent is the substance.')],
  wdr="Item Q17051702 ('cutting agent') is the seed term's own item, not the redirect target's.",
  flags=[DUP('Lacing (drugs)')])
D('enwiki:54185451','A synthetic pregnane steroid developed as a psychotropic agent in the 1950s but never marketed.',
  'A synthetic steroid of the pregnane type developed in the 1950s as a psychiatric drug but never marketed after a larger study found it no better than placebo.',
  dp=['q:is a synthetic pregnane steroid which was developed in the 1950s as a "psychotropic agent"','wd:P279=Q177911'],
  var=[('neurosterone',None,['q:also known as neurosterone'])],
  rel=[('hypernym','steroid',['wd:P279=Q177911']),('hypernym','Psychoactive drug',[])])
O('enwiki:54157249','an organisation (South African cannabis lobby group), not a term')
O('enwiki:214830','an organisation (US harm-reduction non-profit), not a term')
O('enwiki:84525439','a biography (physician), not a term')
D('enwiki:39196397','The planned tapering or stopping of medicines that may be harmful or no longer needed.',
  'The planned process of tapering or stopping medications to improve health by reducing exposure to drugs that are potentially harmful or no longer needed, often in polypharmacy.',
  dp=['q:Deprescribing is a process of tapering or stopping medications to achieve improved health outcomes'],
  var=[('deprescription',None,['wda:Deprescription'])],
  rel=[('hypernym','pharmacotherapy',['wd:P279=Q701216']),('contrast','Medication discontinuation',[],'Discontinuation may be unplanned or patient-initiated.'),('contrast','Drug withdrawal',[],'A possible adverse consequence, not the process.')])
D('enwiki:1012823','A structural or functional analogue of a controlled drug made to mimic it while evading law or detection.',
  'A drug designed as a structural or functional analogue of a controlled substance so as to reproduce its effects while avoiding legal control or standard drug tests. Many are now regulated as new psychoactive substances.',
  dp=['q:is a structural or functional analog of a controlled substance','q:while avoiding classification as illegal and/or detection in standard drug tests'],
  var=[('new psychoactive substance','regulatory term (EU, Australia, New Zealand); broadly overlapping',['wda:new psychoactive substances']),('NPS','abbreviation of new psychoactive substance',['wda:NPS']),('synthetic drugs','loose lay usage',['wda:synthetic drugs'])],
  rel=[('hypernym','Psychoactive drug',['wd:P279=Q3706669']),('hyponym','Bath salts (drug)',[]),('hyponym','Research chemical',[],'Often marketed as research chemicals.'),('contrast','Synthetic cannabinoids',[],'One family of designer drugs; not a synonym.')],
  wn='designer_drug.n.01')
D('enwiki:900035','A historical term for an uncontrollable, often episodic craving for alcohol.',
  'A historical medical term for an uncontrollable craving for alcohol or other drugs; it now occasionally names periodic compulsive bouts of drinking.',
  dp=['q:Dipsomania is a historical term describing a medical condition','q:periodic, compulsive bouts of alcohol intake','wd:P31=Q61915880'],
  rel=[('hypernym','addiction',['wd:P279=Q12029']),('contrast','Alcoholism',[],'Overlapping in nineteenth-century usage; now distinct.'),('contrast','potomania',[],'Excessive drinking of fluids, especially beer; WordNet groups it here.')],
  wn='dipsomania.n.01')
L.save(8)
