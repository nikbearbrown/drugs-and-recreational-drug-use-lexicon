import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=15
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
def DUP(t): return f'duplicate: seed page is a redirect to seed "{t}" ({L.cid(t)})'
O('enwiki:52189828','a creative work (television docuseries), not a term')
D('enwiki:12274183','The unpleasant physical and psychological after-effects that follow drinking alcohol.',
  'The set of unpleasant bodily and mental after-effects, such as headache, fatigue and nausea, that usually follows drinking alcohol and can last a day or more.',
  dp=['q:A hangover is the experience of various unpleasant physiological and psychological effects','wd:P279=Q11290178'],
  var=[('katzenjammer','dated, literary',['wn:lemma=katzenjammer'])],
  rel=[('hypernym','alcohol-induced disorders',['wd:P279=Q11290178']),('contrast','Drug withdrawal',[],'Withdrawal requires dependence; a hangover does not.'),('contrast','Afterglow (drug culture)',[],'Positive rather than negative after-effects.')],
  wn='hangover.n.01',flags=['WordNet sense 1 extends hangover to after-effects of other drugs; the source sense is mainly alcohol'])
D('enwiki:77404898','A colloquial term for anxiety experienced during an alcohol hangover.',
  'A popular-culture blend of "hangover" and "anxiety" naming the anxious feelings that can accompany an alcohol hangover.',
  wp=1,dp=['q:anxiety, and a feeling of general discomfort'],
  rel=[('hypernym','Hangover',[],'A symptom aspect of a hangover.')],
  wdr="Item Q128579806 ('Hangxiety') is the seed term's own item; it has no statements but names this term.",
  flags=[DUP('Hangover')])
D('enwiki:137986','Practices and policies aimed at reducing the negative consequences of drug use and other risky behaviours.',
  'A range of intentional public-health practices and policies that seek to reduce the harmful social and physical consequences of behaviours such as drug use, without requiring that the behaviour stop.',
  dp=['q:refers to a range of intentional practices and public health policies designed to lessen the negative social'],
  var=[('harm minimization','synonym, common in Australia',['wda:harm minimization']),('harm minimisation','British spelling',[])],
  rel=[('hypernym','prevention',['wd:P279=Q1717246']),('hyponym','Drug checking',[]),('hyponym','Needle and syringe programmes',[]),('hyponym','Supervised injection site',[]),('contrast','abstinence-based treatment',[],'Requires stopping use, unlike harm reduction.')])
D('enwiki:471649','A shop that sells drug paraphernalia and counterculture goods.',
  'A retail shop selling drug-related paraphernalia, chiefly for cannabis and tobacco use, along with counterculture items such as magazines and posters.',
  dp=['q:A head shop is a store that sells drug-related paraphernalia.'],
  rel=[('hypernym','specialty shop',['wd:P279=Q1374250']),('contrast','Smart shop',[],'Sells psychoactive products themselves rather than paraphernalia.')],
  wn='head_shop.n.01')
D('enwiki:2176855','An early-1990s fashion style evoking the appearance associated with heroin use.',
  'A fashion style popular in the early 1990s that featured pale skin, dark under-eye circles and an emaciated look, traits associated with heroin use.',
  dp=['q:is a style popularized in early-1990s fashion','wd:P31=Q12684'],
  rel=[('hypernym','fashion',['wd:P31=Q12684'])],
  flags=['ambiguous: a fashion term connected to drugs by association; peripheral to the domain'])
O('enwiki:1992423','a specific commercial product (a 1960s candy), not a term')
D('enwiki:40542151','The history and cultural role of amphetamine, methamphetamine and related stimulants.',
  'The history of amphetamine and methamphetamine from their first synthesis and medical use to their place in recreational drug culture, where they are known by names such as "speed".',
  dp=['q:When used recreationally, they are colloquially known as "speed" or sometimes "crank".'],
  rel=[('contrast','Stimulant use disorder',[],'A disorder, not the history.')],flags=[TOPIC])
D('enwiki:68146713','The history of the use of entheogenic drugs by different groups.',
  'The historical record of the use of entheogens, substances taken in religious, shamanic or spiritual contexts, by many groups over thousands of years.',
  dp=['q:Entheogenic drugs have been used by various groups for thousands of years.'],
  rel=[('contrast','Entheogen',[],'The substance concept rather than its history.')],
  flags=[TOPIC,L.pdup('Entheogenic drugs and the archaeological record','overlapping historical topic pages')])
D('enwiki:7379660','Australian and New Zealand slang for crude illicitly produced opioid mixtures.',
  'A slang name, used mainly in Australia and New Zealand, for crude non-prescription opioid mixtures produced outside pharmaceutical manufacture from pharmaceutical opioids when heroin is hard to obtain.',
  dp=['q:is a slang name most commonly used in Australia, and New Zealand for non-prescription opioids'],
  var=[('home-bake','spelling variant',['q:Homebake (or home-bake)'])],
  rel=[('contrast','heroin',[],'Homebake is a crude substitute, not pharmaceutical-grade heroin.')],
  wd=False,wdr="Item Q5889252 ('Homebake') has no statements; the label alone cannot confirm the drug sense.",
  flags=['regional term: Australia and New Zealand','domain rule: production details in the source are omitted'])
L.save(15)
