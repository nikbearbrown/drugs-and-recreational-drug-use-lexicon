import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=16
def DUP(t): return f'duplicate: seed page is a redirect to seed "{t}" ({L.cid(t)})'
D('enwiki:15501','Household and industrial chemicals whose vapours or gases are breathed in to produce intoxication.',
  'A broad group of volatile household and industrial products, such as solvents, fuels and aerosol gases, whose vapours are deliberately breathed in to become intoxicated, in a way the manufacturer did not intend.',
  dp=['q:Inhalants are a broad range of household and industrial chemicals','wd:P279=Q3706669'],
  var=[('volatile inhalant',None,['wda:volatile inhalant']),('volatile substance','UK public-health usage',[])],
  rel=[('hypernym','Psychoactive drug',['wd:P279=Q3706669']),('hyponym','Poppers',[]),('contrast','inhaled medication',[],'Medicines taken by inhalation, WordNet sense 2.')],
  wnr='WordNet senses are "something inhaled" in general and an inhaled medication; neither is the intoxicant sense.')
O('enwiki:71292021','an organisation (international network of people who use drugs), not a term')
O('enwiki:6220860','a specific facility (a supervised injection site in Vancouver), not a term')
O('enwiki:65796827','an organisation (Spanish ethnobotany non-profit), not a term')
O('enwiki:77421630','a named event (annual remembrance day), not a term',flags=[DUP('Australian Injecting and Illicit Drug Users League')])
O('enwiki:58508521','a named event (annual awareness day), not a term')
D('enwiki:19868570','A benzylamine compound known for being passed off as or mixed into methamphetamine.',
  'A simple amine compound with limited legitimate use that became known to drug-control agencies because it was used to dilute or imitate illicit methamphetamine, which it resembles physically.',
  dp=['q:as a diluent of or substitute for methamphetamine','wd:P279=Q11173'],
  var=[('N-isopropylbenzylamine','full chemical name',['q:N-isopropylbenzylamine is a compound'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('hypernym','Cutting agent',[]),('contrast','methamphetamine',[],'Look-alike substance it imitates.')])
O('enwiki:29601819','a vernacular language variety (jazz-era slang), not a drug or public-health term')
O('enwiki:82066952','a biography (drug researcher and content creator), not a term')
O('enwiki:81946627','a biography (psychologist and pharmacologist), not a term')
L.save(16)
