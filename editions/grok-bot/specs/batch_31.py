import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=31
PERI='ambiguous: {} with no substance-use or public-health sense; peripheral to the domain'
def RNS(t): return f'ambiguous: redirect to non-seed page "{t}"; mapping left to the maintainer'
O('enwiki:53172960','a specific named treatment programme, not a term')
D('enwiki:3084027','Cancer treatment with drugs that act on specific molecules needed for tumour growth.',
  'A form of cancer drug treatment that blocks the growth of cancer cells by acting on particular molecules they need, rather than on all rapidly dividing cells.',
  dp=['q:blocks the growth of cancer cells by interfering with specific targeted molecules'],
  var=[('molecularly targeted therapy',None,['q:Targeted therapy or molecularly targeted therapy'])],
  rel=[('hypernym','chemotherapy',['wd:P279=Q974135']),('contrast','cytotoxic chemotherapy',['q:others being hormonal therapy and cytotoxic chemotherapy'],'Acts on all rapidly dividing cells.')],
  flags=[PERI.format('an oncology treatment term')])
D('enwiki:223011','The study of abnormal development and birth defects, including those caused by substances.',
  'The study of abnormal physiological development, especially birth defects caused by teratogens such as certain drugs, alcohol and chemicals acting on the embryo or fetus.',
  dp=['q:Teratology is the study of abnormalities of physiological development in organisms during their life span.','wd:P279=Q213713'],
  rel=[('hypernym','developmental biology',['wd:P279=Q213713']),('contrast','teratogen',['q:Teratogens are substances that may cause non-heritable birth defects'],'The agent studied.')],
  wn='teratology.n.01',flags=[PERI.format('a scientific discipline; relevant via substance-caused birth defects but')])
D('enwiki:67640100','A North Korean injectable anaesthetic said to contain tetrodotoxin.',
  'An injectable product made in North Korea and said by state media to use tetrodotoxin from pufferfish as an anaesthetic.',
  dp=['q:the main ingredient of the injection is tetrodotoxin','wd:P31=Q28885102'],
  rel=[('hypernym','pharmaceutical product',['wd:P31=Q28885102']),('contrast','Royal Blood-Fresh',[],'Another North Korean product.')],
  flags=['ambiguous: a single named commercial product rather than a general term; claims rest on state media'])
O('enwiki:312626','a specific book (creative work); its drug-manufacture content is also outside the domain rule')
O('enwiki:18802880','a specific film (creative work), not a term')
D('enwiki:44634486','A recent name for roughly 1870 to 1914, when narcotics were widely available and popular.',
  'A 21st-century name for the period of about 1870 to 1914, when opium, morphine, heroin, cocaine and absinthe were widely sold and used in many parts of the world.',
  dp=['q:is a 21st-century neologism describing the period in history covering roughly 1870 to 1914'],
  rel=[('hypernym','History of drug use',[])],
  wd=False,wdr="Item Q25098773 has no statements; the bundle cannot confirm it.",
  flags=['ambiguous: names a historical period; borderline between a term and an event'])
O('enwiki:62139283','a specific organisation (a former US youth rehabilitation programme), not a term')
O('enwiki:31088','biography (Timothy Leary), not a term')
D('enwiki:70323500','Prednisolone, a corticosteroid, applied to the skin or eye rather than taken internally.',
  'The corticosteroid prednisolone used as a topical preparation, such as eye drops, to treat local inflammation.',
  wp=1,dp=['q:Prednisolone is a corticosteroid','wd:P31=Q12140'],
  rel=[('hypernym','medication',['wd:P31=Q12140']),('contrast','prednisolone',[],'The drug in general, by any route.')],
  wdr="Item Q112151249 ('topical prednisolone') is the seed term's own item.",
  flags=[RNS('Prednisolone'),PERI.format('a specific medication form')])
L.save(31)
