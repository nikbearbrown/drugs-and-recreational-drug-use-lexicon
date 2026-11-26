import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=30
D('enwiki:14868355','Efforts to prevent the start of substance use or limit related problems.',
  'Activities that try to stop people from starting to use psychoactive substances or to limit the problems that follow from use, aimed at individuals or at their communities and policies.',
  dp=['q:is a process that attempts to prevent the onset of substance use','wd:P31=Q1773974'],
  var=[('drug abuse prevention',None,['wda:drug abuse prevention']),('drug prevention',None,['wda:drug prevention']),('environmental prevention','narrower: changing community conditions',['q:A concept that is known as "environmental prevention"'])],
  rel=[('hypernym','preventive medicine',['wd:P31=Q1773974']),('contrast','Harm reduction',[],'Reduces harms of use rather than preventing use.'),('contrast','Relapse prevention',[],'Prevents return to use after treatment.')])
D('enwiki:1778796','A state in which stopping a psychoactive drug causes withdrawal, driving continued use.',
  'An adaptive state produced by repeated use of a psychoactive substance in which stopping leads to withdrawal, so that the person needs to keep taking it to function normally.',
  dp=['q:Substance dependence, also known as drug dependence','wd:P279=Q12029'],
  var=[('drug dependence',None,['wda:drug dependence']),('psychoactive substance dependence',None,['wda:psychoactive substance dependence'])],
  rel=[('hypernym','Substance use disorder',['wd:P279=Q7632070']),('contrast','Addiction',[],'Compulsive use; dependence can occur without it.'),('contrast','Physical dependence',[],'The bodily component only.'),('hyponym','Barbiturate dependence',[])],
  wdr="Item Q3378593 is labelled 'narcomania' but its aliases include substance dependence and drug dependence; it matches.",
  flags=['ambiguous: DSM-IV diagnosis later merged into substance use disorder; overlaps Addiction and Physical dependence','Wikidata lists "drug addiction" as an alias, which conflates dependence with addiction; not recorded'])
D('enwiki:166821','A temporary, reversible state of altered consciousness and behaviour after recent substance use.',
  'A short-lived, reversible change in consciousness and behaviour following recent use of a substance, often impairing; severe cases may be described as substance intoxication delirium.',
  dp=['q:is a transient condition of altered consciousness and behavior associated with recent use of a substance','wd:P279=Q18621601'],
  var=[('acute intoxication',None,['wda:acute intoxication']),('high','slang, generic',['q:getting high (generic)']),('stoned','slang, usually cannabis',['q:being stoned, cooked, or fried (usually in reference to cannabis)'])],
  rel=[('hypernym','intoxication',['wd:P279=Q18621601']),('contrast','Drug overdose',[],'Toxic excess rather than expected intoxication.')])
D('enwiki:26477290','Persistent drug use despite substantial harm to oneself or others.',
  'A mental disorder marked by continued use of alcohol or other drugs despite significant harm and adverse consequences to the user or others.',
  dp=['q:is the persistent use of drugs despite substantial harm and adverse consequences to self and others','wd:P279=Q12135'],
  var=[('SUD','abbreviation',['wda:SUD']),('drug use disorder',None,['wda:drug use disorder']),('problematic drug use','related, non-diagnostic',['q:problematic drug or alcohol use'])],
  rel=[('hypernym','Substance-related disorder',['wd:P279=Q4134457']),('hyponym','Stimulant use disorder',[]),('hyponym','Alcoholism',[],'Alcohol use disorder.'),('hyponym','Benzodiazepine use disorder',[]),('contrast','Substance-induced psychosis',[],'A substance-induced disorder.')],
  flags=['Wikidata lists "substance-related disorder" as an alias, which is the broader class; not recorded','ambiguous: overlaps Addiction, Substance dependence and Substance abuse'])
D('enwiki:26306966','Psychosis caused by intoxication with, withdrawal from or recent use of a substance.',
  'A psychosis attributable to intoxication with, withdrawal from or recent use of a psychoactive drug, medicine, chemical or plant.',
  dp=['q:is a form of psychosis that is attributed to substance intoxication, withdrawal or recent consumption','wd:P279=Q170082'],
  var=[('drug-induced psychosis',None,['wda:drug-induced psychosis']),('toxic psychosis','older term',['wda:toxic psychosis']),('substance/medication-induced psychotic disorder','DSM-5 name',['wda:substance/medication-induced psychotic disorder'])],
  rel=[('hypernym','psychosis',['wd:P279=Q170082']),('hyponym','Stimulant psychosis',[]),('hyponym','Cannabis-induced psychotic disorder',[])])
D('enwiki:256038','The DSM-5 class of disorders related to taking a drug of abuse, including alcohol.',
  'A DSM-5 class of mental disorders related to taking a drug of abuse, including alcohol, comprising substance use disorders and substance-induced disorders.',
  dp=['q:are a class of disorders listed in the DSM-5 that are "related to the taking of a drug of abuse','wd:P527=Q7632070'],
  var=[('substance-related and addictive disorders','DSM-5 chapter title',['wda:substance-related and addictive disorders'])],
  rel=[('hypernym','chemically induced disorder',['wd:P279=Q54930906']),('meronym','Substance use disorder',['wd:P527=Q7632070']),('hyponym','Substance-induced psychosis',[])],
  flags=['domain rule: the source\'s age, sex and urban/rural prevalence claims are not carried into the entry','Wikidata lists "drug addiction" as an alias; not recorded'])
D('enwiki:63601386','An oral iron supplement of ferric pyrophosphate in a phospholipid and sucrose-ester coating.',
  'An oral iron preparation in which ferric pyrophosphate is enclosed in a phospholipid and sucrose-ester matrix, designed to be absorbed with fewer stomach side effects.',
  dp=['q:is a new oral iron preparation containing ferric pyrophosphate covered by phospholipids'],
  rel=[('hypernym','iron supplement',[])],
  wd=False,wdr="Item Q96406653 has no statements; the bundle cannot confirm it.",
  flags=['ambiguous: a nutritional/pharmaceutical product with no substance-use or public-health sense; peripheral to the domain'])
D('enwiki:321614','A supervised facility where people can use illicit drugs with sterile equipment and trained staff.',
  'A fixed or mobile harm-reduction facility where people can use pre-obtained illicit drugs with sterile equipment under the supervision of trained staff.',
  dp=['q:can use illicit drugs under the supervision of trained staff','wd:P31=Q1458711'],
  var=[('SIS','abbreviation',['q:Supervised injection sites (SIS)']),('drug consumption room','common in Europe',['q:or drug consumption rooms (DCRs)']),('overdose prevention centre','term used in some jurisdictions',[]),('medically supervised injecting centre','Australian usage',['wda:medically supervised injecting centre'])],
  rel=[('hypernym','Harm reduction',['wd:P31=Q1458711']),('hypernym','facility',['wd:P279=Q13226383']),('contrast','Needle and syringe programmes',[],'Supply equipment without supervised use.')])
D('enwiki:20866399','Designer drugs that act on the same receptors as cannabis cannabinoids.',
  'A class of designer drugs, novel psychoactive substances that bind to the cannabinoid receptors also targeted by THC, often far more potent and toxic than cannabis.',
  dp=['q:are a class of designer drug molecules that bind to the same receptors to which cannabinoids','wd:P279=Q422936'],
  var=[('neocannabinoids',None,['wda:neocannabinoids']),('synthetic marijuana','misleading popular name',['wda:synthetic marijuana']),('spice','brand-derived slang',[]),('K2','brand-derived slang (US)',[])],
  rel=[('hypernym','Designer drug',[]),('hypernym','cannabinoids',['wd:P279=Q422936']),('contrast','synthetic phytocannabinoids',['q:should not be confused with synthetic phytocannabinoids'],'Lab-made copies of plant cannabinoids.')],
  flags=['domain rule: the source\'s description of how the products are prepared is omitted'])
D('enwiki:58247419','A programme giving naloxone kits to people at risk of opioid overdose.',
  'A public-health programme that distributes naloxone kits to people at risk of opioid overdose, and to those around them, so an overdose can be reversed before help arrives.',
  dp=['q:is a governmental program that provides naloxone drug kits to those that are at risk of an opioid overdose'],
  var=[('THN','abbreviation',[])],
  rel=[('hypernym','Harm reduction',[]),('contrast','Drug overdose',[],'The event it responds to.')],
  wd=False,wdr="Item Q60741482 has no statements; the bundle cannot confirm it.")
L.save(30)
