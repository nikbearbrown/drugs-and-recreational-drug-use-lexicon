import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=32
def RNS(t): return f'ambiguous: redirect to non-seed page "{t}"; mapping left to the maintainer'
D('enwiki:8684798','Progressive damage to the brain\'s white matter caused by toxins, drugs or chemotherapy.',
  'A rare condition of progressive damage to the white matter of the brain, especially myelin, caused by substance use, environmental toxins or chemotherapy drugs.',
  dp=['q:due to causes such as exposure to substance use, environmental toxins, or chemotherapeutic drugs','wd:P279=Q3237081'],
  rel=[('hypernym','leukoencephalopathy',['wd:P279=Q3237081']),('hypernym','toxic encephalopathy',['wd:P279=Q7830379']),('contrast','Chasing the dragon',[],'Heroin-vapour inhalation, a known cause.')])
O('enwiki:71652174','a specific organisation and database (European drug-checking network), not a term')
O('enwiki:73850567','biography (Tre Borràs Cabacés), not a term')
O('enwiki:11343855','a specific publication series (SAMHSA manuals), not a term')
D('enwiki:654147','A sober person who stays with a drug user to keep them safe during a trip.',
  'A person who stays sober and keeps watch over someone under the influence of a drug, especially a psychedelic or dissociative, to help keep them safe; regarded as a harm-reduction practice.',
  dp=['q:a person who remains sober to ensure the safety of the drug user while they are under the influence'],
  var=[('sober sitter',None,['q:sometimes known as a sober sitter, spotter, or co-pilot']),('spotter',None,['q:sometimes known as a sober sitter, spotter, or co-pilot']),('guide','in psychedelic therapy',[])],
  rel=[('hypernym','Harm reduction',['q:This practice can be seen as a means of harm r'.rsplit(' ',1)[0]]),('contrast','Set and setting',[],'The sitter forms part of the setting.'),('contrast','Bad trip',[],'An experience a sitter helps manage.')],
  wd=False,wdr="Item Q1720485 is typed as an instance of 'profession', which misdescribes an informal role; abstaining.",
  flags=['Wikidata error: trip sitter is typed as a profession'])
D('enwiki:31231','A colloquial name for psychoactive drugs used to try to extract information from people.',
  'A popular name for any of various psychoactive drugs, such as scopolamine, sodium thiopental or amobarbital, used in attempts to make people reveal information; their reliability is widely doubted.',
  dp=['q:is a colloquial name for any of a range of psychoactive drugs used in an effort to obtain information','wd:P279=Q3706669'],
  var=[('truth drug',None,['wn:lemma=truth drug'])],
  rel=[('hypernym','Psychoactive drug',['wd:P279=Q3706669'])],
  wn='truth_serum.n.01',wnr='truth_serum.n.01 matches the name; its gloss (an intravenous anaesthetic) is narrower than the article.')
O('enwiki:11973706','a specific organisation (Melbourne treatment centre), not a term')
D('enwiki:2535126','Slang for repetitive, compulsive behaviour during heavy stimulant use.',
  'Slang, mainly in methamphetamine use, for a state of restless, compulsive and repetitive activity and agitation during or after a prolonged stimulant binge.',
  rel=[('hypernym','stereotypy',[],'The redirect target describes repetitive behaviour in general.'),('contrast','Stimulant psychosis',[],'A more severe stimulant-induced state.')],
  wp=None,wpr='The page redirects to Stereotypy, a broader concept with no section on tweaking at the pinned revision.',
  wd=False,wdr='The only candidate is Q1198115 (stereotypy), the broader redirect-target concept.',
  wn=None,wnr='WordNet has only unrelated verb senses of tweak.',
  flags=[RNS('Stereotypy'),'definition is model knowledge: the redirect target does not describe the drug-culture sense','ambiguous: "tweaking" also has unrelated everyday senses (adjusting, pinching)'])
O('enwiki:59027109','a specific company (UK treatment provider), not a term')
O('enwiki:62913110','a statistics article (US overdose death data), not a term')
L.save(32)
