import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=13
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:35822485','The epigenetic and transcriptional brain mechanisms underlying cocaine addiction.',
  'The gene-regulatory changes, including histone modification and the transcription factor ΔFosB, in brain reward regions that are thought to underlie compulsive cocaine use.',
  dp=['q:It arises through epigenetic modification','q:primarily through ΔFosB\'s AP-1 complex'],
  rel=[('contrast','ΔFosB',[],'A key transcription factor in the mechanism, not the addiction itself.'),('contrast','Molecular and epigenetic mechanisms of alcoholism',[],'Parallel topic for alcohol.')],flags=[TOPIC])
O('enwiki:541389','an organisation and website (drug-information non-profit), not a term')
D('enwiki:13594085','The ethyl analogue of methylphenidate, a stimulant that inhibits norepinephrine and dopamine reuptake.',
  'A central nervous system stimulant that is the ethyl analogue of methylphenidate and acts by blocking reuptake of norepinephrine and dopamine; it has been sold as a designer drug.',
  dp=['q:is a central nervous system (CNS) stimulant and the ethyl analog of methylphenidate','q:Ethylphenidate acts as a norepinephrine–dopamine reuptake inhibitor'],
  var=[('EPH','abbreviation',['wda:EPH'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('hypernym','Designer drug',[]),('contrast','methylphenidate',[],'The parent prescription stimulant.')])
O('enwiki:47017878','an organisation (German and Swiss harm-reduction associations), not a term')
D('enwiki:53918629','Explanations of human drug use in terms of evolutionary fitness.',
  'Theories that account for why humans use drugs by appeal to evolutionary fitness, for example plant-derived substances used as self-medication during human–plant coevolution.',
  dp=['q:seek to explain human drug usage from the perspective of evolutionary fitness'],
  rel=[('contrast','Self-medication',[],'One proposed mechanism within these models.')],flags=[TOPIC])
D('enwiki:75496122','A drug that reproduces some of the biological effects of physical exercise.',
  'A drug, or candidate drug, intended to reproduce some of the biological effects of physical exercise; none matches the full benefits of exercise.',
  dp=['q:is a drug that mimics some of the biological effects of physical exercise','wd:P31=Q2585617'],
  rel=[('hypernym','Drug class',['wd:P31=Q2585617'])],
  flags=['ambiguous: experimental pharmacology concept; peripheral to substance use and public-health terminology'])
O('enwiki:5818292','a legal and ethical concept (rights of the fetus) outside drug and public-health terminology; linked to the category only through prenatal substance exposure')
D('enwiki:28019168','A practice among people who inject drugs of injecting blood taken from another user.',
  'A practice reported among people who inject drugs in which blood drawn from another user, usually after heroin use, is injected, either to obtain an effect or to ease withdrawal. It carries a high risk of blood-borne infection.',
  dp=['q:is an intravenous drug administration technique used by recreational drug users'],
  var=[('flushblood','variant name',['wda:flushblood'])],
  rel=[('hypernym','Drug injection',[]),('contrast','Needle sharing',[],'Sharing equipment rather than blood.')],
  flags=['domain rule: no procedure is described; the infection-risk statement is from model knowledge'])
D('enwiki:11725','A potent benzodiazepine hypnotic (Rohypnol), notorious for misuse.',
  'A benzodiazepine prescribed for severe insomnia and as an anaesthetic aid, sold as Rohypnol. It is widely known through its misuse, including in drug-facilitated sexual assault.',
  dp=['q:is a benzodiazepine used to treat severe insomnia and assist with anesthesia','wd:P366=Q12140'],
  var=[('Rohypnol','brand name',['wda:Rohypnol']),('roofies','slang',['wda:roofies']),('floonies','slang',['wda:floonies'])],
  rel=[('hypernym','benzodiazepine',[]),('hypernym','medication',['wd:P366=Q12140']),('contrast','Γ-Hydroxybutyric acid',[],'Another drug associated with drug-facilitated assault.')])
O('enwiki:59423083','an organisation (French drug-policy non-profit), not a term')
L.save(13)
