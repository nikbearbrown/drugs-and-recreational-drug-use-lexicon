import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=28
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
def DUP(t): return f'duplicate: seed page is a redirect to seed "{t}" ({L.cid(t)})'
D('enwiki:1037005','The mindset and the physical and social environment that shape a psychoactive drug experience.',
  'The user\'s mental state and expectations ("set") together with the physical and social surroundings ("setting"), treated as factors that shape the effects of a psychedelic or other psychoactive drug.',
  dp=['q:means one\'s mindset (shortened to "set") and the physical and social environment (the "setting")'],
  rel=[('contrast','Trip sitter',[],'A person who may form part of the setting.')],
  wd=False,wdr="Item Q1752960 has no statements; the bundle cannot confirm it.")
D('enwiki:5384623','The influence of drugs on sexual function and experience.',
  'The ways in which psychoactive and other substances affect sexual desire, function and experience, a link documented throughout human history.',
  dp=['q:Sex and drugs refers to the influence of substances on sexual function and experience.'],
  var=[('drugs and sex',None,['wda:drugs and sex'])],
  rel=[('hyponym','Party and play',[],'Drug use specifically to enhance sex.'),('contrast','Drugs and sexual desire',[],'Overlapping topic focused on desire.')],
  flags=[TOPIC,'Wikidata lists "chemsex" as an alias, which names the narrower practice (Party and play); not recorded'])
O('enwiki:24731951','a specific vending area at concerts, not a term')
D('enwiki:6133004','A substance, especially a medicine, that increases saliva flow.',
  'A substance, usually a medication, that increases the production or secretion of saliva, used for example to treat dry mouth.',
  dp=['q:is a substance, especially a medication, that increases the flow rate of saliva'],
  var=[('sialagogue','spelling variant',['wda:sialagogue']),('ptyalagogue','rare',['wda:ptyalagogue'])],
  rel=[('contrast','antisialagogue',[],'A drug that reduces saliva.')],
  wdr="Item Q3482889 ('Sialogogue') carries the same spelling variants as the article; it matches.",
  flags=['ambiguous: pharmacological class with no substance-use or public-health sense; peripheral to the domain'])
D('enwiki:25716563','Scarring of the skin caused by repeated subcutaneous injection of drugs (skin popping).',
  'A skin condition consisting of scars left by skin popping, the injection of drugs under the skin.',
  wp=1,dp=['q:Skin pop scars are a cutaneous condition caused by skin popping.','wd:P279=Q206060'],
  var=[('skin popping scar',None,['wda:Skin popping scar'])],
  rel=[('hypernym','scar',['wd:P279=Q206060']),('contrast','Skin track',[],'Track marks from intravenous injection.')],
  wdr="Item Q7535419 ('skin pop scar') is the seed term's own item.",
  flags=[DUP('Skin popping')])
D('enwiki:15151817','Injecting a drug under the skin rather than into a vein.',
  'A route of illicit drug use in which the drug is injected under or into the skin rather than into a vein or muscle, so that it is absorbed slowly.',
  dp=['q:is a route of administration of street drugs where they are injected or deposited under the skin'],
  var=[('subcutaneous injection','clinical term; broader, not limited to illicit use',[])],
  rel=[('hypernym','Route of administration',['q:is a route of administration of street drugs']),('hypernym','Drug injection',[]),('contrast','intravenous injection',['q:Skin popping is distinct from intravenous injection'],'Delivers the drug straight into a vein.')],
  wd=False,wdr="Item Q7535424 has no statements; the bundle cannot confirm it.")
D('enwiki:25761832','Skin marks left along veins by repeated intravenous drug injection.',
  'A skin condition, commonly called track marks, of lines of scarring and discoloration along veins that results from repeated intravenous drug injection.',
  dp=['q:Skin tracks are a cutaneous condition that result secondary to intravenous drug abuse.','wd:P279=Q2047938'],
  var=[('track marks','common name',['wda:Track mark'])],
  rel=[('hypernym','adverse effect',['wd:P279=Q2047938']),('contrast','Skin pop scar',[],'Scars from subcutaneous rather than intravenous injection.')])
D('enwiki:1140867','A shop selling psychoactive substances such as psychedelics, plus related literature and paraphernalia.',
  'A shop, chiefly in the Netherlands, that sells psychoactive substances, typically psychedelics and "smart drugs", together with related books and paraphernalia.',
  dp=['q:is a retail establishment that specializes in the sale of psychoactive substances','wd:P279=Q213441'],
  var=[('smartshop','spelling variant',['q:A smart shop (or smartshop)'])],
  rel=[('hypernym','shop',['wd:P279=Q213441']),('contrast','Head shop',[],'Sells paraphernalia rather than psychoactive products.'),('contrast','coffeeshop',[],'Dutch cannabis outlet; a different kind of shop.')],
  flags=['Wikidata lists "coffeeshop" as an alias, which names a different Dutch establishment; not recorded','regional term: mainly the Netherlands'])
D('enwiki:12254052','Burning a substance, usually plant material, and inhaling the smoke.',
  'The burning of a substance, most often tobacco but also cannabis and other plant material, and inhaling the resulting smoke.',
  dp=['q:Smoking is the combustion of a substance, usually plant material, and the inhalation of resulting fumes.','wd:P279=Q110207349'],
  rel=[('hypernym','psychoactive drug use',['wd:P279=Q110207349']),('hypernym','Route of administration',[]),('hyponym','Reverse smoking',[]),('contrast','Electronic cigarette',[],'Vaporises without combustion.')],
  wn='smoke.n.07',wnr='smoke.n.07 is the act of smoking tobacco or other substances.')
D('enwiki:3618346','The social and cultural customs surrounding smoking.',
  'The social practices, rituals and cultural meanings associated with smoking tobacco, cannabis and other substances in different societies.',
  wp=1,dp=['q:was early on a common social activity'],
  rel=[('hypernym','Drug culture',[]),('contrast','Smoking',[],'The act rather than its culture.')],
  wd=False,wdr="The only candidate is Q662860 (smoking), the redirect target's item and a broader concept.",
  flags=[DUP('Smoking')])
L.save(28)
