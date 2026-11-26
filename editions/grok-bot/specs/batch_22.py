import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=22
TOPIC='ambiguous: topic or overview article rather than a single term; entry describes the topic'
D('enwiki:320340','A harm-reduction service giving people who inject drugs sterile needles and syringes at little or no cost.',
  'A harm-reduction service through which people who inject drugs can get sterile needles, syringes and related equipment free or cheaply, to reduce transmission of blood-borne infections such as HIV and hepatitis.',
  dp=['q:is a social service that allows injection drug users (IDUs) to obtain clean and unused hypodermic needles','q:It is based on the philosophy of harm reduction'],
  var=[('NSP','abbreviation',['wda:NSP']),('needle exchange programme','when used equipment is returned; often used generally',['wda:needle exchange programme']),('NEP','abbreviation',['wda:NEP']),('syringe services program','current US usage',[])],
  rel=[('hypernym','Harm reduction',['q:It is based on the philosophy of harm reduction']),('contrast','Supervised injection site',[],'A place to inject under supervision, not equipment supply.'),('contrast','Needle sharing',[],'The risk behaviour these programmes address.')])
D('enwiki:373100','The sharing of a needle or syringe between people who inject drugs.',
  'The use of the same needle or syringe by more than one person to inject drugs, a major route for transmitting blood-borne infections such as HIV and hepatitis C.',
  dp=['q:is the practice of intravenous drug-users by which a needle or syringe is shared by multiple individuals','wd:P31=Q1475848'],
  rel=[('hypernym','risk factor',['wd:P31=Q1475848']),('contrast','Needle and syringe programmes',[],'The service designed to prevent sharing.')])
D('enwiki:1018946','Treatment of tobacco dependence by supplying nicotine through means other than tobacco.',
  'A medically approved treatment for tobacco use disorder that provides nicotine without tobacco, for example through patches or gum, to help people stop smoking or chewing tobacco.',
  dp=['q:is a medically approved way to treat people with tobacco use disorder','q:by taking nicotine through means other than tobacco'],
  var=[('NRT','abbreviation',['q:Nicotine replacement therapy (NRT)'])],
  rel=[('hypernym','replacement therapy',['wd:P279=Q110196705']),('contrast','Electronic cigarette',[],'Consumer nicotine products not licensed as NRT in most places.')])
D('enwiki:57043182','Workplace health and employment issues raised by cannabis use among workers.',
  'The workplace safety, testing and employment issues raised by workers\' use of cannabis, such as impairment at work and detection of past use, particularly where cannabis has become legal.',
  dp=['q:employers have concerns of workers either coming to work acutely impaired'],
  rel=[('hypernym','effects of cannabis',['wd:P279=Q4358078'])],flags=[TOPIC,'regional focus: United States'])
D('enwiki:81312721','A seller that sells illicit or unregulated drugs online, on the dark web or the open web.',
  'A seller that offers illicit drugs, including recreational and performance-enhancing drugs, through the internet, either on the dark web or the open web; some sell controlled substances, others legal designer drugs.',
  dp=['q:An online illicit drug vendor is an online vendor that sells illicit drugs.','q:operate both on the dark web and on the clear web'],
  rel=[('hypernym','drug trafficker',['wd:P279=Q10384029'])],
  flags=['domain rule: no procurement information is given; the entry describes the category only'])
D('enwiki:11798983','A 2-methylthio analogue of TMA-2, a positional isomer of Aleph (DOT).',
  'An amphetamine-family compound related to TMA-2, with the 2-position methoxy group replaced by a methylthio group; it is a positional isomer of Aleph.',
  dp=['q:is a psychoactive drug of the phenethylamine and amphetamine families related to TMA-2','q:the drug is a positional isomer of Aleph (DOT; para-DOT)'],
  var=[('4,5-dimethoxy-2-methylthioamphetamine',None,['wda:4,5-dimethoxy-2-methylthioamphetamine']),('2-thio-TMA-2',None,['q:or as 2-thio-TMA-2'])],
  rel=[('hypernym','chemical compound',['wd:P279=Q11173']),('contrast','Meta-DOT',[],'Another DOT positional isomer.')])
D('enwiki:192042','Medicines sold directly to consumers without a prescription.',
  'Medicines that consumers can buy without a prescription, usually because a regulator judges their ingredients safe for self-care, in contrast to prescription-only drugs.',
  dp=['q:are medicines sold directly to a consumer without a requirement for a prescription','wd:P279=Q12140'],
  var=[('OTC drug','abbreviation',['wda:OTC drug']),('over-the-counter medicine',None,['wn:lemma=over-the-counter medicine']),('nonprescription drug',None,[])],
  rel=[('hypernym','Medication',['wd:P279=Q12140']),('contrast','prescription drug',[],'Requires a prescription.')],
  wn='over-the-counter_drug.n.01')
D('enwiki:8607369','Excessive use of prescription or over-the-counter medicines by a person.',
  'The use of more prescription or over-the-counter medicine than a person needs, which can cause harm through adverse effects and drug interactions.',
  dp=['q:Overmedication describes the excessive use of over-the-counter or prescription medicines for a person.'],
  var=[('polypharmacy','overlapping: use of many medicines, not necessarily excessive',['wda:polypharmacy'])],
  rel=[('hypernym','medication error',['wd:P279=Q3057458']),('contrast','Drug overdose',[],'An acute excess dose rather than ongoing overuse.'),('contrast','Deprescribing',[],'A remedy for overmedication.')])
D('enwiki:22799','A semi-synthetic opioid painkiller with high potential for addiction and misuse.',
  'A semi-synthetic opioid prescribed for moderate to severe pain, sold under names such as OxyContin, and widely misused because of its high addictive potential.',
  dp=['q:is a semi-synthetic opioid used medically for the treatment of moderate to severe pain','q:It is a highly addictive and commonly abused drug.'],
  var=[('OxyContin','brand name (extended-release form)',['q:Roxicodone and OxyContin']),('Roxicodone','brand name',['q:sold under the brand names Roxicodone']),('dihydrohydroxycodeinone','chemical name',['wda:dihydrohydroxycodeinone'])],
  rel=[('hypernym','morphinan alkaloid',['wd:P279=Q4303473']),('hypernym','opioid',[]),('contrast','oxymorphone',[],'Look-alike name; different opioid.')])
D('enwiki:11962589','A slang term for swallowing a powdered drug wrapped in paper.',
  'A drug-culture term for taking a powdered or crushed drug by mouth wrapped in a piece of paper rather than loose.',
  dp=['q:Parachuting or bombing is a method of swallowing drugs'],
  var=[('bombing',None,['q:Parachuting or bombing']),('parachuting','verbal form',['q:Parachuting or bombing']),('snow bomb','when the drug is cocaine',['q:It is sometimes called a "snow bomb"'])],
  rel=[('hypernym','Route of administration',[])],
  wd=False,wdr="Item Q7133915 is a bare 'Parachute' label without statements; it cannot be confirmed as the drug-culture sense.",
  wnr='WordNet parachute senses are the rescue device and the verb to jump; neither is the drug sense.',
  flags=['domain rule: method details in the source are omitted'])
L.save(22)
