import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=23
def RNS(t): return f'ambiguous: redirect to non-seed page "{t}"; mapping left to the maintainer'
D('enwiki:8306877','Using drugs to enhance or prolong sexual activity, often in group sessions.',
  'The practice of taking drugs to enhance sexual activity, often over long sessions and with high-risk sexual behaviour; also known as chemsex.',
  dp=['q:refers to the practice of consuming drugs to enhance sexual activity','wd:P279=Q7708739'],
  var=[('PnP','abbreviation',['wda:PnP']),('chemsex','UK and European public-health usage',['wda:chemsex']),('wired play','slang',['wda:wired play']),('slamsex','when drugs are injected; narrower',['wda:slamsex'])],
  rel=[('hypernym','recreational drug use',['wd:P279=Q7708739']),('hypernym','sexual risk behavior',['wd:P279=Q2990601']),('contrast','Sex and drugs',[],'Broader topic.')],
  flags=['domain rule: the source associates the practice with "specific sub-groups"; no demographic group is named in the entry'])
D('enwiki:4192177','Colloquial name for recreational pills originally based on benzylpiperazine, later many compounds.',
  'A colloquial name for recreational pills, at first based mainly on benzylpiperazine and later containing a wide range of compounds, often marketed as legal or herbal highs.',
  dp=['q:is a colloquialism for a type of recreational drug whose main ingredient was originally benzylpiperazine (BZP)'],
  var=[('herbal highs','marketing term; broader',['q:also known as "herbal highs"']),('BZP party pills','when benzylpiperazine-based',[])],
  rel=[('hypernym','Designer drug',[]),('contrast','Club drug',[],'Grouped by setting rather than product type.')],
  wd=False,wdr="Item Q17144296 ('Party pills') is classed as a subclass of recreational drug use, an activity, so the item does not match a substance sense.",
  flags=['regional term: mainly New Zealand, Australia and the UK'])
D('enwiki:84330009','A hazardous five-drug mixture discussed in online looksmaxxing communities.',
  'A name for a dangerous combination of five stimulant and depressant drugs promoted in online looksmaxxing communities around 2026.',
  wp=1,dp=['q:The pentastack is a hazardous five-drug mixture discussed in looksmaxxing communities'],
  rel=[('hypernym','Polysubstance use',[])],
  wdr="Item Q141694221 ('Pentastack') is the seed term's own item; it has no statements but names this term.",
  flags=[RNS('Looksmaxxing#Pentastack'),'domain rule: the component list is not reproduced'])
O('enwiki:84130041','a biography (journalist), not a term')
D('enwiki:2335987','Alleged gatherings where people exchange and randomly take prescription drugs to get intoxicated.',
  'Reported, largely unverified, gatherings at which prescription drugs are pooled and taken at random for intoxication; the story is widely treated as a media myth.',
  dp=['q:is a term describing alleged get-togethers where prescription drugs are exchanged and randomly ingested'],
  var=[('pharm party',None,['q:The pharm party story']),('skittles party','slang',[])],
  rel=[('contrast','Urban legends about drugs',[],'Often cited as one.')],
  wd=False,wdr="Item Q7180843 has no statements; the bundle cannot confirm it.",
  flags=['ambiguous: the phenomenon is alleged and poorly evidenced'])
D('enwiki:5442632','A GABA analogue used as an anxiolytic and sedative medicine in some countries and recreationally elsewhere.',
  'A central nervous system depressant related to GABA, prescribed for anxiety and insomnia in some countries and sold as a supplement or used recreationally elsewhere.',
  dp=['q:is a central nervous system (CNS) depressant with anxiolytic effects','wd:P279=Q74034622'],
  var=[('Anvifen','brand name',['q:sold under the brand name Anvifen']),('β-phenyl-GABA',None,['wda:β-phenyl-GABA']),('4-amino-3-phenylbutyric acid','chemical name',['wda:4-amino-3-phenylbutyric acid'])],
  rel=[('hypernym','Gamma-amino acids',['wd:P279=Q74034622']),('contrast','Γ-Hydroxybutyric acid',[],'Different GABA-related depressant.')])
D('enwiki:1553275','A state in which stopping a tolerance-forming drug causes physical withdrawal symptoms.',
  'A bodily state that develops with long-term use of a drug to which tolerance builds, so that stopping or cutting down brings on physical withdrawal symptoms; it can arise even from ordinary therapeutic use.',
  dp=['q:is a physical condition caused by chronic use of a tolerance-forming drug','wd:P279=Q16697828'],
  var=[('physical dependence syndrome',None,['wda:physical dependence syndrome'])],
  rel=[('hypernym','dependence syndrome',['wd:P279=Q16697828']),('contrast','Addiction',[],'Addiction involves compulsive use; physical dependence alone does not.'),('contrast','psychological dependence',[],'Emotional rather than physical.')])
D('enwiki:83259132','A WHO naming stem for non-prostanoid prostaglandin receptor antagonists.',
  'A class of pharmacological substances acting as prostaglandin receptor antagonists, named with the WHO stem "-piprant" for compounds that lack a prostanoid structure.',
  dp=['q:are a class of substances within pharmacology that act as prostaglandin antagonists','wd:P31=Q17339814'],
  var=[('-piprant','INN suffix',['q:The suffix -piprant was published in 2013'])],
  rel=[('hypernym','group or class of chemical substances',['wd:P31=Q17339814'])],
  flags=['ambiguous: pharmacology naming class with no substance-use or public-health sense; peripheral to the domain'])
D('enwiki:26612233','A former DSM-IV diagnostic label for dependence on three or more substances.',
  'A DSM-IV diagnostic term for dependence on three or more drugs, including alcohol, considered as a group; the category was dropped in DSM-5.',
  dp=['q:to refer to three or more drugs (including alcohol) to which an individual has become dependent','q:The criteria were changed in the DSM-5.'],
  var=[('polysubstance dependence','full diagnostic name',['q:polysubstance dependence (diagnostic code 304.80)'])],
  rel=[('hypernym','Substance dependence',[]),('contrast','Polysubstance use',[],'Use of combined substances, not a dependence diagnosis.')],
  wd=False,wdr="Item Q7227002 ('Polysubstance') has no statements; it cannot be confirmed as the diagnostic sense.",
  flags=[L.pdup('Polysubstance use','diagnostic term versus usage term; often conflated')])
D('enwiki:3588536','The use of combinations of psychoactive substances.',
  'Using more than one psychoactive substance together or in close succession, for recreational, ritual or off-label purposes, with legal or illegal drugs.',
  dp=['q:refers to the use of combined psychoactive substances'],
  var=[('poly drug use',None,['wda:poly drug use']),('polydrug use','spelling variant',[])],
  rel=[('contrast','Polysubstance',[],'Former DSM-IV dependence diagnosis.'),('contrast','Dual diagnosis',[],'Mental illness plus substance use disorder.')],
  flags=[L.pdup('Polysubstance','diagnostic term versus usage term; often conflated')])
L.save(23)
