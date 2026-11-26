import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=1
TW='q:is a psychoactive drug of the phenethylamine, 2C, and TWEETIO families'
for cid,parent,pos,chem,extra in [
 ('enwiki:82929250','2C-I','2','2-ethoxy-5-methoxy-4-iodophenethylamine',None),
 ('enwiki:82915433','2C-T','2','2-ethoxy-5-methoxy-4-methylthiophenethylamine',None),
 ('enwiki:82904918','2C-T-4','2','2-ethoxy-5-methoxy-4-isopropylthiophenethylamine','Tenderness')]:
    var=[(chem,None,[f'q:{chem}'])]
    if extra: var.append((extra,'informal name; names this compound only in that context',[f'q:or as {extra}']))
    D(cid,f'An analogue of {parent} with an ethoxy group at the {pos} position, in the TWEETIO group of phenethylamines.',
      f'A TWEETIO phenethylamine made by replacing the {pos}-position methoxy group of the psychedelic {parent} with an ethoxy group. Only limited reports of its psychoactive effects exist.',
      dp=[TW,f'q:related to the psychedelic drug {parent}'],var=var,
      rel=[('hypernym','Psychoactive drug',[TW]),('contrast',parent,[],'Parent compound; differs by one ethoxy substitution.')])
D('enwiki:82938294','An analogue of 2C-T-2 with ethoxy groups at the 2 and 5 positions, in the TWEETIO group of phenethylamines.',
  'A TWEETIO phenethylamine made by replacing both ring methoxy groups of the psychedelic 2C-T-2 with ethoxy groups. It is known mainly from Shulgin\'s reports.',
  dp=[TW,'q:related to the psychedelic drug 2C-T-2'],var=[('2,5-diethoxy-4-ethylthiophenethylamine',None,['q:2,5-diethoxy-4-ethylthiophenethylamine'])],
  rel=[('hypernym','Psychoactive drug',[TW]),('contrast','2C-T-2',[],'Parent compound.')])
D('enwiki:9820566','The N-methyl analogue of MDPH (alpha-methyl-MDMA), a little-studied amphetamine-family compound.',
  'A lesser-known methylenedioxy amphetamine-family compound, structurally MDMA with an extra alpha-methyl group. It is reported to produce few psychoactive effects.',
  dp=['q:is a lesser-known psychoactive drug of the phenethylamine, amphetamine, and MDx families','q:MDMP produces few to no effects, and is slightly similar to MDMA.'],
  var=[('MDMP',None,['wda:MDMP']),('α-methyl-MDMA',None,['q:or as α-methyl-MDMA'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','3,4-Methylenedioxyphentermine',[],'MDPH lacks the N-methyl group.'),('contrast','MDMA',[],'Look-alike name; MDMP is alpha-methylated MDMA.')])
D('enwiki:10079409','A phentermine analogue of MDA (alpha-methyl-MDA), an amphetamine-family psychoactive compound.',
  'An amphetamine-family psychoactive compound that is MDA with an extra alpha-methyl group, first made by Alexander Shulgin. Little is known about its pharmacology or toxicity.',
  dp=['q:is a psychoactive drug of the amphetamine family','q:MDPH was first synthesized by Alexander Shulgin','q:Very little data exists about the pharmacological properties, metabolism, and toxicity of MDPH.'],
  var=[('MDPH',None,['q:MDPH, also known as']),('α-methyl-MDA',None,['q:or as α-methyl-MDA']),('methylenedioxyphentermine',None,['wda:methylenedioxyphentermine'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','3,4-Methylenedioxy-N-methylphentermine',[],'MDMP is the N-methyl analogue.')])
D('enwiki:11109233','An escaline analogue lacking one methoxy group (3-desmethoxyescaline), a weak mescaline-related phenethylamine.',
  'A phenethylamine related to mescaline, formed from escaline by removing the 5-position methoxy group. It is reported to be weakly psychoactive and short-acting.',
  dp=['q:is a psychoactive drug of the phenethylamine family related to the psychedelic drug mescaline','q:It is the analogue of escaline in which the methoxy group at the 5 position has been removed.'],
  var=[('MEPEA',None,['wda:MEPEA']),('3-desmethoxyescaline',None,['q:or as 3-desmethoxyescaline'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','escaline',[],'Parent compound with three ring substituents.')])
for cid,n,chem in [('enwiki:79469307','3','2,4-dimethoxy-3-methylthiophenethylamine'),('enwiki:79469310','4','2,3-dimethoxy-4-methylthiophenethylamine')]:
    others=[x for x in ('2','3','4') if x!=n]
    D(cid,f'A sulfur analogue of isomescaline with the methylthio group at the {n} position, one of the thioisomescaline isomers.',
      f'A phenethylamine of the scaline group in which the {n}-position methoxy group of isomescaline is replaced by a methylthio group. It is one of the positional thioisomescaline isomers.',
      dp=['q:is a chemical compound of the phenethylamine and scaline families related to mescaline',f'q:in which the methoxy group at the {n} position has been replaced with a methylthio group'],
      var=[(f'{n}-TIM',None,[f'wda:{n}-TIM']),(chem,None,[f'wda:{chem}'])],
      rel=[('hypernym','TIM',['wd:P279=Q7670426'],'Thioisomescaline isomer group.')]+[('contrast',f'{o}-Thioisomescaline',[],'Positional isomer.') for o in others],
      flags=['ambiguous: the source says "one of two possible" isomers while naming three; the count is inconsistent in the article'])
D('enwiki:81469027','The beta-methoxy derivative of MDA, a psychoactive amphetamine of the BOx group.',
  'A methylenedioxy amphetamine carrying a methoxy group on the beta carbon, related to MDA and to BOH. It is reported to have amphetamine-like effects.',
  dp=['q:It is the β-methoxy derivative of MDA','q:It is said to produce "amphetamine-like effects"'],
  var=[('β-methoxy-MDA',None,['q:(β-methoxy-MDA)']),('BOMDA',None,['q:or as BOMDA'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','BOH (drug)',[],'BOH is the phenethylamine (non-alpha-methyl) analogue.')])
D('enwiki:75459317','An experimental engineered variant of activated protein C studied as a drug for stroke.',
  'An investigational recombinant protein drug: an engineered form of activated protein C with reduced anticoagulant activity, studied for treating stroke.',
  dp=['q:is an experimental drug for the treatment of stroke','q:It is a genetically engineered variant of activated protein C','wd:P31=Q5421154'],
  var=[('3K3A-APC',None,['wda:3K3A-APC'])],
  rel=[('hypernym','experimental drug',['wd:P31=Q5421154'])],
  flags=['ambiguous: an experimental therapeutic protein with no recreational or public-health use; included as a drug but peripheral to the lexicon domain'])
D('enwiki:10328937','A brominated amphetamine analogue of TMA in the 3C-desoxyscaline group, a positional isomer of DOB.',
  'A ring-substituted amphetamine related to mescaline, in which the 4-position methoxy group of TMA is replaced by bromine. It is a positional isomer of the psychedelic DOB.',
  dp=['q:is a psychoactive drug of the phenethylamine, amphetamine, and 3C-desoxyscaline families related to mescaline','q:is a positional isomer of DOB'],
  var=[('4-Br-3,5-DMA',None,['q:4-Br-3,5-DMA, also known as']),('3C-DBR',None,['q:3C-DBR']),('4-bromo-TMA',None,['q:or 4-bromo-TMA'])],
  rel=[('hypernym','phenethylamine',['wd:P279=Q422693']),('contrast','DOB',[],'Positional isomer; often confused by name.'),('contrast','Meta-DOB',[],'Another DOB positional isomer.')],
  flags=['Wikidata item lists the alias "4-ethyl-2-methoxy-5-methylthioamphetamine", which names a different compound; not used'])
D('enwiki:83694670','A 4-bromo analogue of DMT, a tryptamine that acts on serotonin receptors.',
  'A tryptamine compound with a bromine at the 4 position of DMT, related to psilocin. It binds many serotonin receptors and releases serotonin.',
  dp=['q:is a non-selective serotonin receptor modulator and serotonin releasing agent of the tryptamine family'],
  var=[('4-Br-DMT',None,['wda:4-Br-DMT']),('4-bromo-N,N-dimethyltryptamine',None,['wda:4-bromo-N,N-dimethyltryptamine'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','4-Fluoro-DMT',[],'Sibling 4-halogenated DMT.'),('contrast','5-bromo-DMT',[],'Look-alike positional isomer.')])
D('enwiki:79505563','A 4-fluoro analogue of DMT, a serotonin 5-HT2C-preferring tryptamine seen as a designer drug.',
  'A tryptamine closely related to DMT and psilocin, with fluorine at the 4 position. It acts mainly at the 5-HT2C serotonin receptor and has appeared online as a designer drug.',
  dp=['q:is a serotonin receptor agonist of the tryptamine family','q:It has been encountered online as a novel designer drug'],
  var=[('4-F-DMT',None,['q:(or 4-F-DMT)']),('4-fluoro-N,N-dimethyltryptamine',None,['wda:4-fluoro-N,N-dimethyltryptamine'])],
  rel=[('hypernym','tryptamines',['wd:P279=Q10705510']),('hypernym','Designer drug',['q:It has been encountered online as a novel designer drug']),('contrast','4-Bromo-DMT',[],'Sibling 4-halogenated DMT.')])
D('enwiki:11111108','A sulfur analogue of MMDA-2 in which one ring oxygen is replaced by sulfur, an amphetamine-family compound.',
  'An amphetamine-family compound related to MDA, made from MMDA-2 by replacing one oxygen of the methylenedioxy ring with sulfur. It is known from Shulgin\'s reports.',
  dp=['q:is a psychoactive drug of the phenethylamine and amphetamine families related to 3,4-methylenedioxyamphetamine (MDA)'],
  var=[('3,4-methyleneoxythio-6-methoxyamphetamine',None,['q:3,4-methyleneoxythio-6-methoxyamphetamine']),('2-methoxy-4,5-methylenethiooxyamphetamine',None,['wda:2-methoxy-4,5-methylenethiooxyamphetamine'])],
  rel=[('hypernym','phenethylamine',['wd:P279=Q422693']),('contrast','MMDA-2',[],'Oxygen parent compound.')])
L.save(1)
