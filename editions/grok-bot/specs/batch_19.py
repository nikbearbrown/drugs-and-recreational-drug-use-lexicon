import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=19
O('enwiki:1702752','a list article (cities nicknamed Sin City), not a term')
O('enwiki:81210794','an organisation (a research-chemical vendor company), not a term')
D('enwiki:19441490','A peaceful 1960s-style public gathering centred on love, music, meditation or drug use.',
  'A peaceful public gathering, coined in 1967 Los Angeles, focused on meditation, love, music, sex or recreational drug use, associated with the counterculture.',
  dp=['q:A love-in is a peaceful public gathering focused on meditation, love, music, sex, or use of recreational drugs.'],
  rel=[('contrast','Rave',[],'A later dance-music gathering.')],
  flags=['ambiguous: a counterculture event term connected to drugs by association; peripheral to the domain'])
D('enwiki:35200902','Harm-reduction services that make minimal demands on people who use drugs.',
  'Harm-reduction health services for people who use substances that place minimal requirements on users, not requiring abstinence or control of drug intake and offering counselling only on request.',
  dp=['q:are harm reduction-based health care centers targeted towards people who use substances','q:offering services without attempting to control their intake of drugs'],
  var=[('low-threshold care',None,['wda:low-threshold care'])],
  rel=[('hypernym','Harm reduction',['q:are harm reduction-based health care centers']),('contrast','high-threshold program',['q:Low-threshold programs may be contrasted with "high-threshold" programs'],'Requires users to accept conditions such as abstinence.')])
D('enwiki:4133160','A historical Chinese blend of opium and tobacco smoked recreationally.',
  'A smoking blend of opium and tobacco used recreationally in China in the seventeenth and eighteenth centuries, later replaced by smoking pure opium.',
  dp=['q:Madak was a blend of opium and tobacco used as a recreational drug'],
  rel=[('contrast','opium',[],'Pure opium displaced madak.')],
  wd=False,wdr="Item Q6726191 ('Madak') has only a 'different from' statement; it is plausibly this concept but the bundle cannot confirm the sense.")
D('enwiki:55695401','The sclerotia of psilocybin-producing fungi, containing psilocybin and psilocin.',
  'The sclerotia, compact masses of mycelium, of psilocybin-producing fungi, which contain the hallucinogens psilocybin and psilocin; they are distinct from the mushrooms themselves.',
  dp=['q:Magic truffles are the sclerotia of psilocybin mushrooms','q:the hallucinogenic chemicals psilocybin and psilocin'],
  var=[('psilocybin truffles',None,[]),('philosopher\'s stones','trade name used in some markets',[])],
  rel=[('hypernym','drug',['wd:P279=Q8386']),('contrast','psilocybin mushroom',[],'The fruiting bodies rather than the sclerotia.'),('contrast','truffle',[],'Culinary truffles are unrelated fungi.')])
D('enwiki:83259994','The 3-desmethoxy analogue of allylescaline, a phenethylamine described as a mood elevator.',
  'A phenethylamine related to allylescaline, lacking one of its methoxy groups, described as a mood elevator rather than a psychedelic.',
  dp=['q:It is the 3-desmethoxy analogue of allylescaline.','q:The drug is said to be a "mood elevator"'],
  var=[('3-methoxy-4-allyloxyphenethylamine',None,['q:3-methoxy-4-allyloxyphenethylamine']),('3-desmethoxyallylescaline',None,['q:or as 3-desmethoxyallylescaline'])],
  rel=[('contrast','allylescaline',[],'Psychedelic parent compound.'),('contrast','3-Methoxy-4-ethoxyphenethylamine',[],'Analogous desmethoxy compound with ethoxy instead of allyloxy.')])
O('enwiki:5084026','an organisation (a twelve-step fellowship), not a term')
O('enwiki:69001474','a specific place (an area of Boston), not a term')
D('enwiki:82519052','The trifluoroethyl analogue of MDEA, a possible psychoactive amphetamine.',
  'An MDxx amphetamine derived from the entactogen MDEA by replacing the N-ethyl group with a trifluoroethyl group; its activity is uncertain.',
  dp=['q:is a chemical compound and possible psychoactive drug of the phenethylamine, amphetamine, and MDxx families','q:It is the derivative of MDEA'],
  var=[('3,4-methylenedioxy-N-(2,2,2-trifluoroethyl)amphetamine',None,['q:3,4-methylenedioxy-N-(2,2,2-trifluoroethyl)amphetamine'])],
  rel=[('contrast','MDEA',[],'Parent entactogen.')])
L.save(19)
