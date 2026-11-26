import sys; sys.path.insert(0,'tools'); import draftlib as L; from draftlib import D,O
L.BATCH=14
O('enwiki:1827066','a biography (economist), not a term')
D('enwiki:12730565','The neutral, non-salt form of an amine such as an alkaloid; colloquially, a smokable drug form.',
  'In chemistry, the neutral form of an amine or other base, contrasted with its salt forms such as hydrochlorides. In drug culture the word, and the verb "freebasing", refers to converting a drug such as cocaine into this smokable form; how this is done is not described here.',
  dp=['q:a free base (freebase, free-base) is the neutral form of an amine or other Lewis base','q:in contrast to salt-based formulations like hydrochlorides'],
  var=[('freebase','spelling variant',['wda:freebase']),('free-base','spelling variant',['q:(freebase, free-base)'])],
  rel=[('hyponym','Crack cocaine',[],'Crack is a free-base form of cocaine.'),('contrast','salt',[],'Salt formulations, e.g. hydrochlorides.')],
  flags=['ambiguous: chemistry sense and drug-culture sense; entry covers both','domain rule: conversion procedure in the source is omitted'])
O('enwiki:325938','a specific object (a named bus in 1960s counterculture), not a term')
D('enwiki:1197243','The hypothesis that using one psychoactive substance raises the likelihood of using others.',
  'The hypothesis that using one psychoactive substance, such as cannabis, alcohol or tobacco, is linked to a higher probability of going on to use other substances; its causal basis is disputed.',
  dp=['q:is coupled to an increased probability of the use of further substances','wd:P31=Q3239681'],
  var=[('gateway drug theory',None,['wda:gateway drug theory']),('stepping-stone theory',None,['q:stepping-stone theory']),('escalation hypothesis',None,['q:escalation hypothesis']),('gateway drug','names the substance rather than the effect',['wda:gateway drug'])],
  rel=[('hypernym','scientific theory',['wd:P31=Q3239681'])])
O('enwiki:69087401','an organisation (a named drug-checking service in Vancouver), not a term')
D('enwiki:1556660','A street term for potent mixtures of synthetic opioids sold as heroin.',
  'A slang name for potent street mixtures of synthetic opioids, such as fentanyl analogues, often passed off as heroin and linked to overdose deaths.',
  dp=['q:is a slang term which refers to potent mixtures of synthetic opioids','q:which were often sold on the street misleadingly as "heroin"'],
  var=[('grey death','British spelling',[])],
  rel=[('contrast','heroin',[],'Sold as heroin but chemically different.'),('contrast','Lacing (drugs)',[],'The adulteration practice behind such mixtures.')],
  wd=False,wdr="Item Q30001024 has a label only and no statements; it is likely this concept but cannot be confirmed from the bundle.",
  flags=['ambiguous: a street name whose composition varies; not a fixed substance'])
D('enwiki:859248','A colloquial expression for drinking alcohol to relieve a hangover.',
  'A colloquial expression, short for "the hair of the dog that bit you", for alcohol taken to lessen the effects of a hangover.',
  dp=['q:is a colloquial expression in the English language predominantly used to refer to alcohol'],
  var=[('hair of the dog that bit you','full form',['q:short for "hair of the dog that bit you"'])],
  rel=[('hypernym','alcoholic beverage',['wd:P279=Q154']),('contrast','Hangover',[],'The condition it is meant to relieve.')],
  wn='hair_of_the_dog.n.01')
D('enwiki:1887121','A non-psychotic disorder of lasting perceptual disturbances after using hallucinogens.',
  'A non-psychotic disorder in which visual hallucinations or perceptual distortions persist after the effects of hallucinogens or related drugs have worn off, often with distress or impairment.',
  dp=['q:is a non-psychotic disorder in which a person experiences lasting or persistent visual hallucinations','wd:P31=Q12135'],
  var=[('HPPD','abbreviation',['wda:HPPD']),('posthallucinogen perception disorder','older term',['wda:posthallucinogen perception disorder'])],
  rel=[('hypernym','mental disorder',['wd:P31=Q12135']),('contrast','Hallucinogen-induced psychotic disorder',[],'Psychotic rather than perceptual.'),('contrast','flashback',[],'Brief recurrences; HPPD is persistent.')])
D('enwiki:82070669','A psychotic disorder following the use of hallucinogens.',
  'A mental disorder with psychotic symptoms such as hallucinations, delusions and paranoia that follows the use of hallucinogens such as psychedelics.',
  dp=['q:is a mental disorder characterized by psychotic symptoms','wd:P279=Q2151786'],
  var=[('HIPD','abbreviation',['wda:HIPD']),('hallucinogen-induced psychosis',None,['wda:hallucinogen-induced psychosis']),('psychedelic-induced psychosis','narrower: psychedelics only',['wda:psychedelic-induced psychosis'])],
  rel=[('hypernym','Substance-induced psychosis',['wd:P279=Q2151786']),('contrast','Hallucinogen persisting perception disorder',[],'Non-psychotic perceptual disorder.'),('contrast','Bad trip',[],'Acute distress during intoxication.')])
O('enwiki:38473062','a biography (journalist and chemist), not a term')
L.save(14)
