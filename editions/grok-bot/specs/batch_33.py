import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=33
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
PERI='ambiguous: {} with no substance-use or public-health sense; peripheral to the domain'
def RNS(t): return f'ambiguous: redirect to non-seed page "{t}"; mapping left to the maintainer'
D('enwiki:11840866','Widely circulated false or exaggerated beliefs about drugs and their effects.',
  'False or exaggerated stories and beliefs about drugs, such as LSD and cannabis, that circulate among young people and the public and can obscure the real effects and dangers of drugs.',
  dp=['q:Many urban legends and misconceptions about drugs have been created and circulated'],
  var=[('misconceptions about drugs',None,[])],
  rel=[('hyponym','Strawberry Quik meth',[],'One such hoax.'),('contrast','Drug education',[],'Factual information that counters myths.')],
  wd=False,wdr="Item Q6628837 is typed as a Wikimedia list article; abstaining.",
  flags=[TOPIC])
O('enwiki:22255165','a specific organisation (Vancouver drug-user advocacy group), not a term')
D('enwiki:5508354','The effect of a substance on blood vessels, raising or lowering blood pressure or heart rate.',
  'The action of a natural agent or drug on blood vessels, through constriction or dilation, that raises or lowers blood pressure or heart rate.',
  dp=['q:has the effect of either increasing or decreasing blood pressure and/or heart rate through its vasoactivity'],
  var=[('vasoactive substance','the agent',['q:A vasoactive substance is an endogenous agent or pharmaceutical drug'])],
  rel=[('hyponym','vasodilation',[]),('hyponym','vasoconstriction',[])],
  wd=False,wdr="Item Q6159778 ('Vasoactive') has no statements; the bundle cannot confirm it.",
  flags=[PERI.format('a pharmacological property'),'domain rule: titration and dosing details in the source are omitted'])
D('enwiki:66089784','Using household wasp or hornet insecticide sprays as a substitute for or with stimulants.',
  'The use of household insecticides, especially pyrethroid wasp and hornet sprays, alone or mixed with stimulants such as methamphetamine, for intoxication; reported mainly in the southern United States since the 2020s.',
  dp=['q:refers to the ingestion of common household insecticides, in particular wasp and hornet sprays'],
  var=[('wasping','slang',['q:Wasp dope, or wasping, also known as wasp meth']),('wasp meth','slang; the product is not methamphetamine',['q:Wasp dope, or wasping, also known as wasp meth'])],
  rel=[('contrast','Inhalant',[],'Household products used for intoxication.')],
  wd=False,wdr="Item Q104880514 has no statements; the bundle cannot confirm it.",
  flags=['regional term: mainly the southern United States','domain rule: preparation and method of use are omitted','the source lists further street names (e.g. "zombie", "hot shots") that are ambiguous with other drugs; not recorded'])
D('enwiki:311354','A brain disorder from thiamine deficiency, commonly due to alcoholism, combining Wernicke encephalopathy and Korsakoff syndrome.',
  'The combined presence of Wernicke encephalopathy and Korsakoff syndrome, caused by thiamine (vitamin B1) deficiency often linked to alcohol use disorder, and marked by vision changes, unsteadiness and memory loss.',
  dp=['q:is the combined presence of Wernicke encephalopathy (WE) and Korsakoff syndrome','wd:P279=Q1573307'],
  var=[('WKS','abbreviation',['wda:WKS']),('wet brain','colloquial',['q:colloquially referred to as wet brain syndrome'])],
  rel=[('hypernym','Wernicke encephalopathy',['wd:P279=Q1573307']),('hypernym','Korsakoff\'s syndrome',['wd:P279=Q622901']),('contrast','Alcohol-related dementia',[],'Overlapping alcohol-related brain disorder.')],
  flags=['Wikidata lists "Korsakoff\'s syndrome" as an alias, which is one component; not recorded'])
D('enwiki:471687','A small steel cartridge of nitrous oxide for whipping cream, also used to inhale the gas.',
  'A small steel cartridge filled with nitrous oxide, made for whipping cream, which is also a common source of the gas for recreational inhalation.',
  dp=['q:is a steel cylinder or cartridge filled with nitrous oxide (N2O) that is used as a whipping agent'],
  var=[('whippet','slang when used recreationally (US)',['q:colloquially called a whippet, nos or nang when used recreationally']),('nang','slang (Australia, UK)',['q:colloquially called a whippet, nos or nang when used recreationally'])],
  rel=[('contrast','Recreational use of nitrous oxide',[],'The practice the chargers supply.')],
  wd=False,wdr="Item Q7993720 has no statements; the bundle cannot confirm it.",
  flags=['domain rule: how the cartridge is opened is not described'])
D('enwiki:7725935','Slang for feeling faint, going pale and vomiting after drug use, usually cannabis.',
  'Drug slang for an episode in which someone, usually after using cannabis, turns pale, feels faint and vomits.',
  dp=['q:is a drug slang term for when a recreational drug user','q:begins to feel faint and vomits'],
  var=[('white-out',None,['q:A whitey or white-out (sometimes greening or green-out)']),('green-out','variant',['q:A whitey or white-out (sometimes greening or green-out)'])],
  rel=[('contrast','Bad trip',[],'A distressing psychological reaction rather than a physical one.')],
  wd=False,wdr="Item Q7996391 is typed as 'physical conditioning', which does not match; abstaining.",
  wn=None,wnr='whitey.n.01 is an unrelated slur sense.',
  flags=['ambiguous: "whitey" is also an offensive slang term for a white person; this entry covers only the drug sense','regional term: mainly UK and Australian slang'])
D('enwiki:29359671','South African slang for low-grade street heroin, also called nyaope.',
  'A South African street name for low-grade heroin, also called nyaope; media claims that it contains antiretrovirals or rat poison have been shown by laboratory studies to be unfounded.',
  wp=1,dp=['q:and that \'whoonga\' and \'nyapoe\' are in fact simply heroin','wd:P31=Q169336'],
  var=[('nyaope','South African name, used in other regions',['q:is a uniquely South African drug'.replace('is a uniquely South African drug','claimed that ‘whoonga’ or ‘nyaope’ is')])],
  rel=[('hypernym','heroin',[]),('contrast','Urban legends about drugs',[],'The adulterant claims are debunked myths.')],
  wdr="Item Q907673 ('Whoonga') is the seed term's own item.",
  flags=[RNS("Heroin#Claims that 'whoonga' or 'nyaope' is made from anti-retrovirals, rat poison, etc."),'regional term: South Africa'])
O('enwiki:83954312','biography (online content creator), not a term')
D('enwiki:83391508','A mescaline-related psychoactive phenethylamine alkaloid with a beta-hydroxy group.',
  'A psychoactive phenethylamine alkaloid closely related to mescaline, reported in a Pereskia cactus and possibly formed as a minor mescaline metabolite.',
  dp=['q:is a psychoactive drug and alkaloid of the phenethylamine, scaline, and BOx families','wd:P279=Q11173'],
  var=[('β-HOM','abbreviation',['q:β-Hydroxymescaline (β-HOM), also known as mescalol']),('mescalol',None,['q:β-Hydroxymescaline (β-HOM), also known as mescalol'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','BOH (drug)',[],'A related BOx-family compound.')],
  wdr="Item Q27215715 is named by the compound's systematic name and matches the substance.")
D('enwiki:12962','GHB, a natural neurotransmitter and depressant drug used medically and recreationally.',
  'A naturally occurring neurotransmitter and central nervous system depressant, used medically for narcolepsy and alcohol use disorder and recreationally as a club drug.',
  dp=['q:is a naturally occurring neurotransmitter and a depressant drug','wda:GHB'],
  var=[('GHB','abbreviation',['wda:GHB']),('γ-hydroxybutyrate','the salt/anion form',['wda:γ-hydroxybutyrate']),('sodium oxybate','pharmaceutical salt, not the same molecule',[]),('G','slang',[])],
  rel=[('hypernym','hydroxybutyric acid',['wd:P279=Q101208434']),('hypernym','Club drug',[]),('contrast','Flunitrazepam',[],'Another sedative misused in drink spiking.')],
  flags=['domain rule: dosing and synthesis details from the source are omitted','Wikidata lists brand names (Xyrem, Alcover) as aliases; not recorded'])
D('enwiki:42007831','A truncated FosB protein that builds up in the brain\'s reward system with repeated drug use and is linked to addiction.',
  'A truncated splice variant of the FosB transcription factor that accumulates in reward-related brain regions after repeated exposure to drugs and other rewards and is studied as a molecular switch in addiction.',
  rel=[('contrast','FosB',[],'The full-length protein and gene.'),('contrast','Addiction',[],'The condition it is implicated in.')],
  wp=None,wpr='The target section "Delta FosB" was not found in the FOSB article at the pinned revision; FOSB is the broader gene.',
  wd=False,wdr='The only candidate is Q17929096, the FOSB gene, which is broader even though it lists ΔFosB as an alias.',
  flags=[RNS('FOSB#Delta FosB'),'definition is model knowledge: the target section was absent from the pinned revision'])
L.save(33)
