import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=6
def RNS(t): return f'ambiguous: redirect to non-seed page "{t}"; mapping left to the maintainer'
D('enwiki:46592885','A US regulatory term for a plant-derived product marketed to diagnose or treat disease.',
  'In US law, a finished, labelled product containing plant ingredients that is marketed for diagnosing, mitigating, treating or curing disease. Highly purified plant chemicals fall outside the definition.',
  dp=['q:is defined in the United States Federal Food, Drug, and Cosmetic Act as a botanical product','q:Chemicals that are purified from plants, like paclitaxel'],
  rel=[('hypernym','plant based medication',['wd:P279=Q2089545']),('hypernym','crude drug',['wd:P279=Q735160'])],
  flags=['ambiguous: regulatory medicines term specific to the United States; peripheral to recreational drug use'])
D('enwiki:23623716','A toxic syndrome from long-term intake of bromide, historically from bromide sedatives.',
  'A syndrome caused by long-term consumption of bromide, usually from bromide-based sedatives, which were widely used medicines in the late nineteenth and early twentieth centuries.',
  dp=['q:Bromism is the syndrome which results from the long-term consumption of bromine','q:usually through bromine-based sedatives such as potassium bromide and lithium bromide'],
  rel=[('hypernym','bromine exposure',['wd:P279=Q21173316'])])
D('enwiki:70299509','A solid dosage form held between the gum and cheek so the drug acts on or is absorbed through the oral mucosa.',
  'A tablet placed in the buccal pouch between gum and cheek, where it acts locally or is absorbed through the lining of the cheek, avoiding first-pass metabolism.',
  dp=['q:Buccal tablets are a type of solid dosage form','q:either act on the oral mucosa or are rapidly absorbed through the buccal mucosal membrane'],
  rel=[('hypernym','dosage form',[],'A tablet dosage form.'),('contrast','sublingual tablet',[],'Placed under the tongue rather than against the cheek.')],
  wdr="Item Q112228174 ('Buccal tablets') names this dosage form directly; it is the seed's own item, not the redirect target's.",
  flags=[RNS('Buccal administration#Tablets')])
D('enwiki:10210904','The 4-butoxy analogue of mescaline, a phenethylamine of the scaline group.',
  'A mescaline analogue of the scaline group in which the 4-position methoxy group is replaced by a butoxy group.',
  dp=['q:the methoxy group at the 4 position has been replaced with a butoxy group'],
  var=[('B','Shulgin shorthand; ambiguous outside that context',['wda:B']),('4-butoxy-3,5-dimethoxyphenethylamine',None,['wda:4-butoxy-3,5-dimethoxyphenethylamine'])],
  rel=[('hypernym','phenethylamine',['wd:P279=Q422693']),('contrast','mescaline',[],'Parent compound.')])
O('enwiki:26061936','an organisation (state professional society), not a term')
D('enwiki:79145033','A compound that binds cannabinoid receptors and stimulates or inhibits them.',
  'Any compound that binds to the CB1 or CB2 cannabinoid receptors and activates or blocks them, altering responses such as pain, mood and appetite.',
  dp=['q:is a compound that bind to the cannabinoid receptors','q:By stimulating or inhibiting these receptors'],
  rel=[('hypernym','neurotransmitter agent',['wd:P279=Q73112927']),('hyponym','Synthetic cannabinoids',[],'Synthetic cannabinoid receptor agonists are one kind.')],
  flags=['Wikidata also classes this as a hormone (Q11364), which does not fit; not used'])
D('enwiki:81098240','A rare peripheral arterial disease associated with chronic cannabis use.',
  'A rare peripheral vascular disease linked to long-term cannabis use, marked by reduced blood flow and tissue death, usually in the legs.',
  dp=['q:is a rare, peripheral vascular disease that has been associated with chronic cannabis use','wd:P31=Q26695607'],
  var=[('CA','abbreviation used in the source',['q:patients with CA (cannabis arteritis)'])],
  rel=[('hypernym','peripheral vascular disease',['wd:P31=Q26695607'])])
D('enwiki:83847884','A psychotic disorder occurring with or after cannabis use or withdrawal.',
  'A mental disorder with psychotic symptoms, such as hallucinations, delusions and paranoia, that follows cannabis use or withdrawal.',
  dp=['q:is a mental disorder characterized by psychotic symptoms','q:that occurs following the use of or withdrawal from cannabis'],
  var=[('CIPD','abbreviation',['q:Cannabis-induced psychotic disorder (CIPD)']),('cannabis-induced psychosis',None,['q:also known as cannabis-induced psychosis']),('cannabis psychosis',None,['q:or cannabis psychosis'])],
  rel=[('hypernym','Substance-induced psychosis',[]),('contrast','Stimulant psychosis',[],'Same category, different drug class.')])
D('enwiki:5342540','A slang term for inhaling the vapour of a drug heated on foil, especially heroin.',
  'A drug-culture term for inhaling the vapour given off when a powdered drug, typically heroin, is heated on foil. It is a route of use distinct from injecting.',
  dp=['q:is the act of inhaling the vapor of a powdered psychoactive drug off a heated sheet of aluminium foil'],
  var=[('CTD','abbreviation',['q:"Chasing the dragon" (CTD)']),('foily','Australian English',['q:or "foily" in Australian English'])],
  rel=[('hypernym','Route of administration',[]),('contrast','Drug injection',[],'Another route; chasing avoids needles.')],
  flags=['The phrase is also used figuratively for pursuing an unattainable first high; that sense is not covered'])
D('enwiki:185896','A loose category of recreational drugs associated with nightclubs, raves and dance parties.',
  'A loosely defined, context-based group of recreational drugs linked with discos, nightclubs, dance-music parties and raves, rather than a pharmacological class.',
  dp=['q:are a loosely defined category of recreational drugs','wd:P279=Q8386'],
  var=[('rave drugs',None,['wda:rave drugs']),('party drugs','broader in some usage',['wda:party drugs'])],
  rel=[('hypernym','drug',['wd:P279=Q8386']),('contrast','Drug class',[],'Club drugs are grouped by setting, not by chemistry.'),('contrast','Party pills',[],'Party pills are specific legal-high products.')],
  wn='club_drug.n.01',flags=['WordNet gloss ties the term to "young people"; that demographic framing is not adopted'])
L.save(6)
