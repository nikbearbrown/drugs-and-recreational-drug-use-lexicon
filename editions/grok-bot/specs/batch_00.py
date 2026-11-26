import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=0
D('enwiki:10329013','A ring-brominated amphetamine derivative of MDA, discussed as a psychoactive research compound.',
  'A substituted amphetamine of the methylenedioxy family in which a bromine atom is added to the ring of MDA. It is described in the literature as a psychoactive compound with little documented activity.',
  dp=['q:is a psychoactive drug of the phenethylamine, amphetamine, and MDxx families','q:It is the 6-bromo derivative of MDA.'],
  var=[('6-Bromo-MDA',None,['q:6-Bromo-MDA, also known as']),('6-bromo-3,4-methylenedioxyamphetamine',None,['q:6-bromo-3,4-methylenedioxyamphetamine']),('2-bromo-4,5-MDA',None,['q:(2-bromo-4,5-MDA)']),('6-Br-MDA',None,['wda:6-Br-MDA'])],
  rel=[('hypernym','Psychoactive drug',['q:is a psychoactive drug of the phenethylamine']),('hypernym','phenethylamine',['wd:P279=Q422693']),('contrast','6-Chloro-MDA',[],'Look-alike halogenated MDA analogue; chlorine rather than bromine.')],
  flags=['ambiguous: two numbering conventions (2-bromo-4,5- vs 6-bromo-3,4-) name the same compound; the article title uses 6-Bromo-MDA'])
D('enwiki:79469305','A sulfur analogue of isomescaline, one of three positional thioisomescaline isomers studied as phenethylamine compounds.',
  'A phenethylamine compound of the scaline group in which one methoxy group of isomescaline is replaced by a methylthio group. It is one of three positional isomers grouped as thioisomescalines.',
  dp=['q:is a chemical compound of the phenethylamine and scaline families related to mescaline','q:The compound is one of two possible thioisomescaline (TIM) positional isomers'],
  var=[('2-TIM',None,['q:2-Thioisomescaline (2-TIM)']),('2-methylthio-3,4-dimethoxyphenethylamine',None,['wda:2-methylthio-3,4-dimethoxyphenethylamine'])],
  rel=[('hypernym','TIM',['wd:P279=Q7670426'],'Thioisomescaline positional-isomer group.'),('contrast','3-Thioisomescaline',[],'Positional isomer with the sulfur at the 3 position.'),('contrast','4-Thioisomescaline',[],'Positional isomer with the sulfur at the 4 position.')],
  flags=['ambiguous: the source says "one of two possible" isomers while naming three; the count is inconsistent in the article'])
D('enwiki:3273302','A 2C-family phenethylamine with an isopropoxy group at the 4 position, reported as a low-potency psychedelic.',
  'A ring-substituted phenethylamine of the 2C series carrying an isopropoxy group at the 4 position. It is reported to have psychedelic effects but low potency and little published study.',
  dp=['q:is a phenethylamine of the 2C family','q:It produces hallucinogenic or psychedelic effects','q:Because of the low potency of 2C-O-4'],
  var=[('4-isopropoxy-2,5-dimethoxyphenethylamine',None,['q:4-isopropoxy-2,5-dimethoxyphenethylamine'])],
  rel=[('hypernym','2C',['wd:P279=Q2728188']),('contrast','isoproscaline',[],'Positional isomer per the article; different substitution pattern.')])
D('enwiki:9691431','A 2C-family phenethylamine with a cyclopropylthio group, documented as a psychoactive compound with weak effects.',
  'A sulfur-containing member of the 2C phenethylamines, carrying a cyclopropylthio group at the 4 position. Reports describe only threshold psychoactive effects.',
  dp=['q:is a psychoactive drug of the phenethylamine and 2C families','q:4-cyclopropylthio-2,5-dimethoxyphenethylamine'],
  var=[('Sesqui',None,['q:or as Sesqui']),('4-cyclopropylthio-2,5-dimethoxyphenethylamine',None,['q:4-cyclopropylthio-2,5-dimethoxyphenethylamine'])],
  rel=[('hypernym','2C',['wd:P279=Q2728188']),('hypernym','Psychoactive drug',['q:is a psychoactive drug of the phenethylamine and 2C families'])])
for cid,name,parent,pos,chem in [
  ('enwiki:82938157','2CB-2,5-DiEtO','2C-B','2 and 5','2,5-diethoxy-4-bromophenethylamine'),
  ('enwiki:82938233','2CD-2,5-DiEtO','2C-D','2 and 5','2,5-diethoxy-4-methylphenethylamine')]:
    D(cid,f'An ethoxy-substituted analogue of {parent} in the TWEETIO group of phenethylamines.',
      f'A phenethylamine of the 2C and TWEETIO groups made by replacing the methoxy groups of {parent} at positions {pos} with ethoxy groups. It is documented as a weakly active or poorly characterized psychoactive compound.',
      dp=['q:is a psychoactive drug of the phenethylamine, 2C, and TWEETIO families',f'q:related to the psychedelic drug {parent}'],
      var=[(chem,None,[f'q:{chem}'])],
      rel=[('hypernym','Psychoactive drug',['q:is a psychoactive drug of the phenethylamine, 2C, and TWEETIO families']),('hypernym','TWEETIO',['q:2C, and TWEETIO families'],'TWEETIO is a family named in the source; not a seed.'),('contrast',parent,[],'Parent compound; differs by ethoxy substitution.')])
D('enwiki:82915362','An analogue of 2C-B with an ethoxy group at the 5 position, in the TWEETIO group of phenethylamines.',
  'A 2C-B analogue in which the 5-position methoxy group is replaced by ethoxy, placing it in the TWEETIO group. Unlike its sibling compounds it was not described by Shulgin, and little is documented about it.',
  dp=['q:is a psychoactive drug of the phenethylamine, 2C, and TWEETIO families','q:2CB-5-EtO was not described by Alexander Shulgin'],
  var=[('2-methoxy-5-ethoxy-4-bromophenethylamine',None,['q:2-methoxy-5-ethoxy-4-bromophenethylamine'])],
  rel=[('hypernym','Psychoactive drug',['q:is a psychoactive drug of the phenethylamine, 2C, and TWEETIO families']),('contrast','2CB-2,5-DiEtO',[],'Sibling TWEETIO with both positions ethoxylated.'),('contrast','2C-B',[],'Parent compound.')])
D('enwiki:82892657','An analogue of 2C-D with an ethoxy group at the 2 position, in the TWEETIO group of phenethylamines.',
  'A TWEETIO phenethylamine derived from 2C-D by replacing the 2-position methoxy group with ethoxy. It is reported to produce feelings of closeness with little intoxication.',
  dp=['q:is a psychoactive drug of the phenethylamine, 2C, and TWEETIO families','q:feelings of closeness and intimacy between couples without an appreciable state of intoxication'],
  var=[('2-ethoxy-5-methoxy-4-methylphenethylamine',None,['q:2-ethoxy-5-methoxy-4-methylphenethylamine'])],
  rel=[('hypernym','Psychoactive drug',['q:is a psychoactive drug of the phenethylamine, 2C, and TWEETIO families']),('contrast','2CD-5EtO',[],'Positional isomer: ethoxy at the 5 position instead.'),('contrast','2C-D',[],'Parent compound.')])
D('enwiki:27839636','An analogue of 2C-D with an ethoxy group at the 5 position, in the TWEETIO group of phenethylamines.',
  'A TWEETIO phenethylamine derived from 2C-D by extending the 5-position methoxy group to ethoxy. It is described as producing long-lasting, sociable psychoactive effects.',
  dp=['q:is a psychoactive drug of the phenethylamine, 2C, and TWEETIO families','q:the methoxy group at the 5 position has been extended to an ethoxy group'],
  var=[('5-ethoxy-2-methoxy-4-methylphenethylamine',None,['q:5-ethoxy-2-methoxy-4-methylphenethylamine'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','2CD-2-EtO',[],'Positional isomer: ethoxy at the 2 position instead.')])
D('enwiki:82832395','An analogue of 2C-E with an ethoxy group at the 5 position, in the TWEETIO group of phenethylamines.',
  'A TWEETIO phenethylamine derived from the psychedelic 2C-E by replacing its 5-position methoxy group with ethoxy. It is described as very long-acting compared with its parent.',
  dp=['q:is a psychoactive drug of the phenethylamine, 2C, and TWEETIO families','q:related to the psychedelic drug 2C-E'],
  var=[('Eternity','street or nickname use; names this compound only in that informal context',['q:or as Eternity']),('4-ethyl-2-methoxy-5-ethoxyphenethylamine',None,['q:4-ethyl-2-methoxy-5-ethoxyphenethylamine'])],
  rel=[('hypernym','Psychoactive drug',['q:is a psychoactive drug of the phenethylamine, 2C, and TWEETIO families']),('contrast','2C-E',[],'Parent compound.')])
L.save(0)
