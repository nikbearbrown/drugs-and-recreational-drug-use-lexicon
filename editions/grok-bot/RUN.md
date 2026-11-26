# RUN.md: drugs-and-recreational-drug-use-lexicon, independent edition (grok)

## Protocol deviation (read first)

- **No fresh context per seed.** The protocol asks for each seed to be drafted in a fresh model context. That was not possible on this machine: no model CLI or API key, GitHub Models retired, no local GPU. The run stopped after setup and the hash check and reported this.
- **Approved override.** On 24 Nov 2026 (about 10:09 PM EST), Nik Bear Brown approved drafting by the agent itself ("Just run it like you did the last one").
- **How the edition was drafted.** The drafting model is Grok Bot; its exact model version string is not visible to the agent. It drafted all 352 seeds in batches of 10–15, in TSV order, in one long session: a 10-seed pilot (batch 0), then batches 1–33.
- **What the session saw.** Earlier batches stayed in the session's context. No other run, entry, vote or final edition was read.
- **Run mode.** Every draft's `_meta.run_mode` is `batched, same session (protocol deviation approved by Nik Bear Brown, 24 Nov 2026)`. `_meta.model` is `Grok Bot` and `_meta.model_version` is `unknown`.

## Dates (EST)

- **Seed commit.** 538d4f3e1e82cf72f0b78bedbe76453bca4e9210, committed 24 Nov 2026 4:00 PM EST.
- **Wikipedia and Wikidata retrieval.** 24 Nov 2026, about 3:52–3:53 PM EST (20:52–20:53 UTC). Each record pins its own revision.
- **Drafting.** 24 Nov 2026, about 10:14–10:28 PM EST.
- **Final check.py run.** About 10:30 PM EST.

## Seeds

- `data/seeds.tsv` at 538d4f3e: 352 seeds.
- sha256 caa4f3ae910f11ca4ec72ce3ac7f9123f1566a28b05242fa7c5cc3fdffede372. Verified as a match; the file was not modified.
- **Missing manifest roots.** Two root categories in the manifest have no members: `Category:Recreational drugs` and `Category:Substance use disorders`. The seed set comes from the other five roots: Drugs, Psychoactive drugs, Drug culture, Substance abuse and Substance-related disorders. Recreational-drug terms reach the set only through those roots.

## Model and settings

- **Drafting.** Grok Bot (version string unknown) drafted by hand into Python spec files (`specs/batch_NN.py`). The model's sampling settings are not exposed to the agent.
- **Prompt.** The text of `replication/prompts/system.txt` was not sent through a model API, because none was available. Its rules and the domain rule were followed directly.
- **Validation.** `tools/draftlib.py` builds each record. Before saving a batch it calls the repo's own `verify_drafts.verify` and a dose-pattern regex. ERRORs block the save.

## Tools

- **Wikipedia.** MediaWiki API, through `tools/build_bundles.py`, gave the pinned `lastrevid`, the plain-text extract and the redirect target. For a redirect to a section, the section text was added at the same revision by `tools/add_redirect_sections.py`.
- **Wikidata.** `wbgetentities`, through `tools/assemble_bundles.py`, gave the label, aliases and item revision id. Claims kept: P31, P279, P361, P527, P366, P2868, P1889, P460, P3781, P2175, P769 and P106, plus one level of P31/P279 ancestors (`ancestor_of`).
- **WordNet.** WordNet 3.0 through NLTK 3.10.4 (Python venv), up to 6 synsets per term.
- **Neighbors.** Seeds linked from the article (or from its redirect target), plus seeds referenced by the item's Wikidata claims.
- **Checking.** `replication/scripts/check.py` from the seed commit.

## Evidence sources

- English Wikipedia, Wikidata and WordNet 3.0 only.
- No external glossaries and no examples: `examples` is empty in every bundle.
- No patient records, private documents or social posts.
- Source text was treated as evidence only.

## Coverage totals

- **Records.** 352 of 352, one per concept_id, in seed order, with no title prefilter.
- **Entries.** 274.
- **Out of scope.** 78: biographies, organisations, websites, creative works, lists, specific places, events, programmes, laws and statistics pages.
- **Duplicates.** 5 records are redirects to another seed. One of them, International Drug Users Remembrance Day, is also out of scope.
- **Ambiguous.** 106 records carry an ambiguous flag, including the 11 redirects to non-seed pages.
- **Possible duplicates.** 8 records (4 pairs).
- **check.py.** 352/352 pass. No unresolved failures.
- **Warnings.** 98 × "most claims rest on model knowledge". Of these, 78 are out-of-scope records, which use model_knowledge by design. The other 20 are entries whose evidence was thin, such as redirects with no usable target section or Wikidata items with no statements.

## Retries

13 records failed the repo validator (the same `verify` that check.py uses) on their first save. Each was revised once using the reported errors. These records have `_meta.attempt = 2` and `_meta.retry_errors`. No record needed a third attempt:

- Adaptive design (medicine) (quote over 20 words)
- Buscaline (quote over 20 words)
- Crack cocaine (definition copies 9+ consecutive words from Wikipedia)
- Gateway drug effect (quote over 20 words)
- Medication (definition copies 9+ consecutive words from Wikipedia)
- Physical dependence (definition copies 9+ consecutive words from Wikipedia)
- Rave (definition copies 9+ consecutive words from Wikipedia)
- Residential treatment center (definition copies 9+ consecutive words from Wikipedia)
- Reverse smoking (quote over 20 words)
- Sialogogue (variant alias pointer to an unlinked Wikidata item)
- Speedball (drug) (unknown relation type)
- Stimulant use disorder (definition copies 9+ consecutive words from Wikipedia)
- Substance abuse (definition copies 9+ consecutive words from Wikipedia)

## Redirects

### Redirects to non-seed pages

These are flagged and listed for the maintainer. None is mapped.

- Biobetter: "Biosimilar#Biobetter"
- Bioparallel: "Biosimilar#Bioparallel"
- Buccal tablet: "Buccal administration#Tablets"
- Life-process model of addiction: "Stanton Peele"
- Pentastack: "Looksmaxxing#Pentastack"
- Screening, brief intervention and referral to treatment: "Brief intervention#Screening, brief intervention and referral to treatment"
- Solar puffing: "Drug paraphernalia#Magnifying lens"
- Topical prednisolone: "Prednisolone"
- Tweaking (behavior): "Stereotypy"
- Whoonga: "Heroin#Claims that 'whoonga' or 'nyaope' is made from anti-retrovirals, rat poison, etc."
- ΔFosB: "FOSB#Delta FosB"

### Redirects to seeds

These are flagged as duplicates.

- Cutting agent: "Lacing (drugs)" (enwiki:4223023)
- Hangxiety: "Hangover" (enwiki:12274183)
- International Drug Users Remembrance Day: "Australian Injecting and Illicit Drug Users League" (enwiki:41650632)
- Skin pop scar: "Skin popping" (enwiki:15151817)
- Smoking culture: "Smoking" (enwiki:12254052)

## Domain-rule omissions

- No synthesis, procurement, dosing or concealment guidance.
- No demographic inference.
- Regional and slang aliases carry conditions.
- Records where source content was deliberately left out:

  - Cold water extraction: preparation steps in the source are deliberately omitted; only the term is described
  - Drug precursors: no information on which chemicals yield which drugs or how; the entry describes the regulatory term only
  - Drugs and prostitution: population-specific claims in the source are not carried into the entry
  - Flashblood: no procedure is described; the infection-risk statement is from model knowledge
  - Free base: conversion procedure in the source is omitted
  - Homebake (slang): production details in the source are omitted
  - Kush (drug): the source notes use "particularly among young people"; demographic framing is not carried into the entry
  - Lean (drug): preparation details in the source are omitted
  - List of drug combinations: list content (combinations) not reproduced
  - Mickey Finn (drugs): no concealment detail is given
  - Mushroom tea: preparation details are omitted
  - Native Americans and reservation inequality: the page centres on one population group; no demographic inference is drawn
  - Online illicit drug vendor: no procurement information is given; the entry describes the category only
  - Parachute (drugs): method details in the source are omitted
  - Party and play: the source associates the practice with "specific sub-groups"; no demographic group is named in the entry
  - Pentastack: the component list is not reproduced
  - Recreational drug tourism: no destinations or procurement details are given
  - Reverse smoking: the source's claims about which sex practises it more are not carried into the entry
  - Speedball (drug): preparation and administration detail from the source is omitted
  - Substance-related disorder: the source's age, sex and urban/rural prevalence claims are not carried into the entry
  - Synthetic cannabinoids: the source's description of how the products are prepared is omitted
  - Vasoactivity: titration and dosing details in the source are omitted
  - Wasp dope: preparation and method of use are omitted
  - Whipped-cream charger: how the cartridge is opened is not described
  - Γ-Hydroxybutyric acid: dosing and synthesis details from the source are omitted

## Other deviations and notes

- **Validation during drafting.** Records were checked with `verify` while drafting, not only after. The first full check.py run therefore passed 352/352.
- **Missing redirect sections.** Two target sections were not found at the pinned revision: Drug paraphernalia#Magnifying lens (Solar puffing) and FOSB#Delta FosB (ΔFosB). The Wikipedia link was abstained on for both. Their definitions are model knowledge and flagged as such.
- **Biography redirect.** Life-process model of addiction redirects to a biography (Stanton Peele). The Wikipedia link was abstained on, and the definition is model knowledge.
- **Wikidata problems.** Wikidata classification and alias errors are recorded in record flags. Wrong aliases were not used.
- **Distribution.** The run folder is not published or pushed. It is backed up as a tgz to the maintainer's store.

## Judging kit

- **Branch.** `grok-agreement-method` on nikbearbrown/drugs-and-recreational-drug-use-lexicon, commit ab145901, branched from the seed commit and pushed on its own.
- **Contents.** The kit was adapted from clinical-treatments-and-procedures-lexicon `grok-agreement-method` (51774fbd). It carries no drafts, bundles or source text.
- **Left for the maintainer.** `TRAP_IDS` is a draft for the maintainer's review. The human worked examples are placeholders.
