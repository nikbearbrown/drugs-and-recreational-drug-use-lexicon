import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=5
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
def RNS(t): return f'ambiguous: redirect to non-seed page "{t}"; mapping left to the maintainer'
D('enwiki:76259802','The practice and history of chewing betel (areca) nut in China.',
  'The chewing of betel or areca nut in China, long established in the southern provinces and now widespread, and subject to public debate and some government restriction.',
  dp=['q:Betel chewing in China has a long history, particularly in the southern provinces.','q:the Chinese government to introduce some restrictions'],
  rel=[('hypernym','betel chewing',[],'Regional instance of the practice.')],flags=[TOPIC,'ambiguous: country-specific topic page'])
D('enwiki:79409683','An informal term for a biological drug that improves on an existing biological drug.',
  'A biological medicine designed as an improved version of an existing biologic, rather than a close copy. The term is informal and has no official regulatory definition.',
  dp=['q:The term biobetter refers to a biological drug that is an improved version of an existing biological drug.','q:the term biobetter is used informally without any official and universally accepted definition'],
  rel=[('contrast','biosimilar',['q:While biosimilars try to copy an existing biological drug'],'Biosimilars copy the reference medicine; biobetters improve on it.')],
  wd=False,wdr='The only candidate is Q864715 (biosimilar), the redirect target\'s item and a different concept.',
  flags=[RNS('Biosimilar#Biobetter')])
D('enwiki:5161942','The dependence of medicine and drug discovery on the diversity of plants, animals and fungi.',
  'The role of biological diversity as a source of medicines: many plants, animals and fungi yield drugs and natural products used in medicine.',
  dp=['q:numerous plants, animals, and fungi are used in medicine'],
  flags=[TOPIC])
D('enwiki:79458585','A proposed term for biologics that differ structurally from a reference drug but are functionally similar.',
  'A proposed name for biological drugs built to be structurally different from a reference biologic, often to avoid patents, while acting in a very similar way. No established term exists, and "me-too biologics" is also proposed.',
  dp=['q:There is no established term for such biologics','q:but the terms "bioparallels" or "me-too biologics" (in reference to me-too drugs) have been proposed'],
  var=[('me-too biologic','proposed alternative term',['q:or "me-too biologics"'])],
  rel=[('contrast','biosimilar',['q:Different from biosimilars, many new antibodies are being developed'],'Biosimilars aim to be near-identical copies.'),('contrast','Me-too drug',[],'The small-molecule analogue of the idea.')],
  wd=False,wdr='The only candidate is Q864715 (biosimilar), the redirect target\'s item and a different concept.',
  flags=[RNS('Biosimilar#Bioparallel')])
D('enwiki:10310849','A DOM analogue in which two methoxy groups are replaced by methylthio groups.',
  'An amphetamine-family compound related to DOM, with both ring methoxy groups replaced by methylthio groups. It is reported as having little psychoactive effect.',
  dp=['q:is a chemical compound of the phenethylamine and amphetamine families related to DOM'],
  var=[('2,5-TOM',None,['q:Bis-TOM, or 2,5-TOM']),('2,5-dithio-DOM',None,['q:or as 2,5-dithio-DOM']),('4-methyl-2,5-dimethylthioamphetamine',None,['q:4-methyl-2,5-dimethylthioamphetamine'])],
  rel=[('hypernym','phenethylamine',['wd:P279=Q422693']),('contrast','DOM',[],'Parent compound with oxygen instead of sulfur.')])
D('enwiki:20759927','A poster printed in fluorescent inks that glow under ultraviolet light.',
  'A poster printed with phosphor-containing inks that fluoresce under a blacklight, associated with 1960s and 1970s psychedelic culture.',
  dp=['q:is a poster printed with inks which fluoresce under a blacklight'],
  var=[('black light poster','spelling variant',['wda:black light poster'])],
  rel=[('hypernym','poster',['wd:P279=Q429785'])],
  flags=['ambiguous: an art object linked to drug culture only by association; peripheral to the domain'])
D('enwiki:9660402','A period of memory loss for events during substance intoxication, especially alcohol.',
  'A gap in memory caused by alcohol or another substance, during which new memories are not formed, so events cannot later be recalled, resembling anterograde amnesia.',
  dp=['q:is a phenomenon caused by the intake of any substance or medication','wd:P279=Q572111'],
  var=[('black-out','spelling variant',['wda:black-out']),('alcohol blackout','when caused by alcohol; narrower',[])],
  rel=[('hypernym','anterograde amnesia',['wd:P279=Q572111']),('contrast','loss of consciousness',[],'A blackout is memory loss, not passing out.')],
  wnr='WordNet senses cover broadcast or power blackouts, momentary unconsciousness and amnesia in general; none is drug-related memory loss specifically.',
  flags=['Wikidata classes the blackout as a substance use disorder (Q7632070), which is not accurate; not used'])
O('enwiki:42298206','a website and organisation (harm-reduction web forum), not a term')
D('enwiki:10312047','The beta-methoxy analogue of MDPEA, a phenethylamine of the BOx group.',
  'A methylenedioxy phenethylamine carrying a methoxy group on the beta carbon, the beta-methoxy analogue of MDPEA, described by Shulgin.',
  dp=['q:is a drug of the phenethylamine, MDxx, and BOx families','q:It is the β-methoxy analogue of 3,4-methylenedioxyphenethylamine (MDPEA)'],
  var=[('β-methoxy-MDPEA',None,['q:or as β-methoxy-MDPEA']),('3,4-methylenedioxy-β-methoxyphenethylamine',None,['wda:3,4-methylenedioxy-β-methoxyphenethylamine'])],
  rel=[('hypernym','phenethylamine',['wd:P279=Q422693']),('contrast','3C-BOH',[],'The alpha-methyl (amphetamine) analogue.'),('contrast','BOM (drug)',[],'Sibling BOx compound derived from mescaline.')],
  flags=['ambiguous: "BOH" is a short acronym with other meanings; the drug sense is fixed by the page title'])
D('enwiki:10327884','The beta-methoxy derivative of mescaline, a phenethylamine of the BOx group.',
  'A phenethylamine related to mescaline that carries an extra methoxy group on the beta carbon. Only threshold effects have been reported.',
  dp=['q:It is the β-methoxy derivative of mescaline.','q:is a psychoactive drug of the phenethylamine, scaline, and BOx families'],
  var=[('β-methoxymescaline',None,['q:or as β-methoxymescaline']),('3,4,5,β-tetramethoxyphenethylamine',None,['q:3,4,5,β-tetramethoxyphenethylamine'])],
  rel=[('hypernym','phenethylamine',['wd:P279=Q422693']),('contrast','mescaline',[],'Parent compound.'),('contrast','BOH (drug)',[],'Sibling BOx compound.')],
  flags=['ambiguous: "BOM" is a short acronym with other meanings; the drug sense is fixed by the page title'])
L.save(5)
