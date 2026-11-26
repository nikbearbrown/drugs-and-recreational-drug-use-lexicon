import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=18
def RNS(t): return f'ambiguous: redirect to non-seed page "{t}"; mapping left to the maintainer'
O('enwiki:3342582','a protein (an interleukin-6 class cytokine) described by its biology, with no drug or public-health terminology sense in the source')
D('enwiki:605525','A model of addiction, associated with Stanton Peele, that sees it as a response to life circumstances rather than a disease.',
  'A model of addiction, developed by the psychologist Stanton Peele, that treats addiction as a pattern of behaviour arising from a person\'s circumstances, values and coping, which people commonly outgrow, rather than as a chronic brain disease.',
  wp=None,wpr='The seed page is a redirect to a biography (Stanton Peele) whose pinned lead does not describe the model; no candidate states this sense.',
  rel=[('contrast','disease model of addiction',[],'The model is framed as an alternative to the disease model.')],
  wdr="Item Q6544584 ('Life-process model of addiction') is the seed term's own item; it has no statements but names this concept.",
  flags=[RNS('Stanton Peele'),'definition rests on model knowledge because the redirect target is a biography'])
D('enwiki:958884','An imprecise, often pejorative term for medicines treating non-serious conditions.',
  'An imprecise and sometimes pejorative label for medicines that treat conditions seen as minor or not medical, such as baldness, wrinkles, acne or erectile dysfunction.',
  dp=['q:Lifestyle drug is an imprecise term commonly applied to medications','q:It is sometimes intended as a pejorative'],
  rel=[('hypernym','medication',['wd:P279=Q12140']),('contrast','Recreational drug use',[],'Lifestyle drugs are medical products used for quality of life, not intoxication.')])
O('enwiki:5671648','a list article (causes of death by rate), not a term')
O('enwiki:69814358','a list article (drug combinations), not a term',flags=['domain rule: list content (combinations) not reproduced'])
O('enwiki:285921','a list article (psychiatric medications), not a term')
O('enwiki:51369085','a list article (psychoactive drugs), not a term')
O('enwiki:5759586','a list article (psychoactive plants), not a term')
O('enwiki:7381681','a list article (psychotropic medications by brand), not a term')
O('enwiki:69819769','a list article (reagent colour charts), not a term')
L.save(18)
