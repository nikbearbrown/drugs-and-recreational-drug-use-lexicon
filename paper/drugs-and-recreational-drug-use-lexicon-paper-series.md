# Drugs and Recreational Drug Use Lexicon

*Rough draft, not reviewed.* A paper series modelled on *Five Papers on WordNet*. Nik Bear Brown and Humanitarians AI [TODO: confirm authorship]. Drafted 2026-11-26 with Grok Bot.

**Where it stands:** the seed list (352 Wikipedia pages) and replication kit are public; one independent Grok Bot edition is drafted and checked (352/352 pass: 274 entries, 78 out of scope, 5 duplicates, 106 ambiguous). No second edition, no cross-model judging and no human review have been run. The lexicon describes terms; it gives no guidance on making, obtaining, dosing or hiding any substance.

## Part I. Introduction to the Drugs and Recreational Drug Use Lexicon

### I.1 What the lexicon is for

The vocabulary of drugs is unusually unstable. One substance has a chemical name, a class, brand names, and street names that change by city and decade; one street name can mean different substances in different places. Public-health work, harm-reduction services, researchers and moderators all need to know when two names refer to the same thing and when a familiar word means something else in a given region. This lexicon records substances, substance classes, the vocabulary of drug culture and the terminology of substance use and its disorders, with every regional or ambiguous alias qualified.

### I.2 Why a WordNet-style relational lexicon

A list of street names is easy to make and hard to trust. A relational lexicon records, for each name, what it is a kind of, what it is confused with, and under what condition an alias applies. WordNet showed that a small set of relations with explicit tests can organise a large vocabulary (Miller et al. 1990/1993). Here the same relations organise a vocabulary whose main hazard is not missing a word but mistaking one.

### I.3 The lexical matrix, adapted

Rows are concepts (one per seed page), each fixed by a work sense; columns are names, each with a condition where needed. The matrix is denser in the columns than in any of the other lexicons: slang, regional and historical names attach to a few rows. *Gateway drug effect* has the variants *gateway drug theory*, *stepping-stone theory* and *escalation hypothesis*, plus *gateway drug* with the condition "names the substance rather than the effect". Polysemy runs the other way too: *kush* names cannabis strains in one sense and a synthetic street drug in Sierra Leone in another.

### I.4 The relations

| Relation | Test the drafter must pass with the real names filled in | WordNet analogue |
|---|---|---|
| synonym | the target can replace the concept in a source excerpt without changing the concept | membership in one synset |
| hypernym | "[concept] is a kind of [target]" is true | hypernymy (@) |
| hyponym | "[target] is a kind of [concept]" is true | hyponymy (~) |
| meronym | the concept includes the target as a component by definition | part meronymy (%p) |
| holonym | the concept is a component of the target by definition | part holonymy (#p) |
| uses | the concept is characteristically associated with the target tool, material or substance | none (new) |
| requires | an explicit conceptual prerequisite supported by a source | none; compare verb entailment |
| certifies | the concept is a credential and attests to the target | none (new) |
| contrast | the target is often confused with the concept but differs from it, including look-alike names | none; replaces antonymy |

Antonyms and pertainyms are not recorded. Every relation also carries a `basis` (`source`, with pointers, or `model_knowledge`, with none) and a target that is either a seed ID or marked `proposed_new`.

**Certifies** is not used. In the Grok Bot edition, contrast (257 edges) and hypernym (256) carry almost all the structure, followed by hyponym (38), uses (3), meronym (3) and requires (1) [counted from `drafts.jsonl` on 2026-11-26]. That contrast edges are as common as hypernyms is the main structural finding about this vocabulary: much of what a user needs is a warning that two names differ, as between *Physical dependence* and *Addiction*.

### I.5 Built with AI: what changes and what does not

As in the other lexicons, a model drafts from pinned evidence, a checker rejects drafts that break the rules, independent editions are compared, and people decide. One difference is the weight of the domain rule. The drafter was told not to carry forward preparation, procurement, dosing or concealment details even when the source page contains them, and to record each omission. The RUN.md lists 25 records where source content was deliberately left out.

## Part II. The vocabulary by category

The seeds come from five populated Wikipedia categories: *Drug culture* (157 direct members), *Substance-related disorders* (88), *Drugs* (58), *Psychoactive drugs* (50) and *Substance abuse* (19). Two intended roots, *Recreational drugs* and *Substance use disorders*, had no members when the list was pulled, so recreational-drug terms enter only through the other five.

### II.1 Substances and substance classes

The *Drugs* and *Psychoactive drugs* categories supply substances, classes and pharmacological terms. The hypernym carries this part, as in WordNet's nouns: a named substance is a kind of a class, and the class a kind of drug. *Kush (drug)* is drafted as a kind of designer drug, with a contrast to the cannabis sense and a flag that the term is regional to Sierra Leone and West Africa. The entry gives no composition beyond what identifies the term.

### II.2 Drug culture: practices, slang and settings

The largest category is the least clinical. It holds practices, slang, events, paraphernalia, cultural movements and media. Here conditions on variants and contrast edges matter most, because the same word changes meaning with setting. Many of the domain-rule omissions fall here: for *Lean (drug)*, *Mushroom tea* and *Free base* the source's preparation details were left out and only the term is described; for *Whipped-cream charger* the entry does not say how the cartridge is opened.

### II.3 Substance use, harms and disorders

The *Substance-related disorders* and *Substance abuse* categories supply the public-health terminology: dependence, withdrawal, tolerance, use disorders. These terms are often used loosely, so contrast is again central. *Physical dependence* is drafted as a kind of dependence syndrome and contrasted with both *Addiction* and *psychological dependence*. Demographic framing in sources is not carried into entries: for *Substance-related disorder*, the source's age, sex and urban–rural prevalence claims were left out.

### II.4 What the categories pulled in

The Grok Bot edition abstained on 78 seeds as out of scope: biographies, organisations, websites, creative works, lists, specific places, events, programmes, laws and statistics pages. Five are redirects to other seeds (*Cutting agent* to *Lacing (drugs)*, *Hangxiety* to *Hangover*, and others), and eleven redirect to pages that are not seeds (*Biobetter*, *Pentastack*, *Whoonga*, *ΔFosB* and others), left unmapped for the maintainer.

## Part III. Design and implementation

### III.1 Seed list and manifest

352 seeds, `data/seeds.tsv` SHA-256 `caa4f3ae910f11ca4ec72ce3ac7f9123f1566a28b05242fa7c5cc3fdffede372`, seed commit `538d4f3e` (24 Nov 2026, 4:00 PM EST). Retrieved 2026-11-24, about 3:52–3:53 PM EST. Columns as in the clinical lexicon.

### III.2 Evidence bundles

English Wikipedia (pinned revision, plain-text extract and redirect target; for a redirect to a section, the section text at the same revision), Wikidata (label, aliases, item revision, and the claims P31, P279, P361, P527, P366, P2868, P1889, P460, P3781, P2175, P769 and P106, with one level of P31/P279 ancestors), and WordNet 3.0 through NLTK 3.10.4. Neighbours: seeds linked from the article or its redirect target, plus seeds named in the item's Wikidata claims. No external glossaries and no usage examples. No patient records, private documents or social posts.

### III.3 Drafting prompt and kit

Prompt gen-v2. The domain rule: "Describe substances, substance classes and public health terminology. Qualify regional or ambiguous aliases. Do not give synthesis, procurement, dosing, or concealment guidance or infer demographics from individual mentions." The Grok Bot run added a dose-pattern regular expression to its save step, in addition to the repository's verifier.

### III.4 Flags

`out-of-scope:`, `ambiguous:` and `duplicate:`, plus prefixes the run added: `possible-duplicate:` (8 records in 4 pairs), `domain rule:` (25 records), regional-term flags (9 records) and `wikidata error:` [counts from `drafts.jsonl` flags].

### III.5 Checking

352/352 pass. Thirteen records failed the verifier on their first save (quotes over 20 words, copied definitions, an alias pointer to an unlinked item, an unknown relation type) and passed after one revision. Ninety-eight records carry the warning "most claims rest on model knowledge": 78 out-of-scope records by design and 20 entries with thin evidence.

### III.6 Provenance

Run folder `drugs-lexicon-grok-run-20261124`. `_meta.run_mode` reads "batched, same session (protocol deviation approved by Nik Bear Brown, 24 Nov 2026)"; `_meta.model` is Grok Bot and the version unknown. The folder is backed up privately, not pushed.

### III.7 The Grok Bot edition: what was done and how it deviated

The protocol asks for each seed in a fresh model context. That was not possible: there was no model API or local model to call. The run stopped after setup and the hash check and reported this. Professor Bear approved drafting by the agent itself on 24 Nov 2026 at about 10:09 PM EST. The edition was then drafted in a 10-seed pilot and 33 batches of 10 to 15, in seed order, in one session, between about 10:14 and 10:28 PM EST, with the final check at about 10:30 PM EST. Two redirect target sections were missing at the pinned revision (*Solar puffing*, *ΔFosB*); their Wikipedia links abstain and their definitions are marked model knowledge.

### III.8 Parallel editions and agreement

Paste-in prompt `03-drugs-and-recreational-drug-use.md`. Judging kit on `grok-agreement-method` (commit `ab145901`), adapted from the clinical kit, with a draft trap list and placeholder human worked examples.

### III.9 Human in the loop

As in the other lexicons, with one addition: a domain-safety reviewer must read the 25 omission records first, to confirm the omitted content did not reappear.

## Part IV. Evaluation (to do): what humans do after the AI comparison

### IV.1 Status

Not run. One edition exists.

### IV.2 Prerequisites on the AI side

A second blind edition, `drafters.tsv` rows, `agreement.py run`, model judges, the leak check and the panel code. See [HUMAN-EVALUATION-TODO.md](HUMAN-EVALUATION-TODO.md), Part 1.

### IV.3 Human steps in order

The steps below are the same for every lexicon and are written out once, with owners and checkboxes, in [HUMAN-EVALUATION-TODO.md](HUMAN-EVALUATION-TODO.md). They run **after** the AI side has produced its blinded, pairwise comparison of the independent editions. Every step is a human step. None has started.

| # | Human step | What it produces | Gate before the next step | Owner | Status |
|---|---|---|---|---|---|
| H1 | Settle the open decisions (IV.6): judge invitations, `drafters.tsv` rows, trap list, worked examples, weights, acceptance threshold | a committed decision record | Bear signs off | Bear | not started |
| H2 | Recruit and register human judges (`agreement.py register`) | registry rows, seeded samples | at least 2 judges for the pilot; about 10 for full scale | Bear | not started |
| H3 | Pilot: Bear and at least one other judge label the whole pilot pool; tune the rubric on the development half only; freeze the prompts (`agree-v1`) and tag the analysis plan | adjudicated pilot labels, frozen rubric | rubric frozen and tagged | Bear + 1 judge | not started |
| H4 | Human–human overlap pool: about 30% of each judge's items come from a shared pool of about 50, each item judged by at least 2 people | the **human ceiling** (Krippendorff's α, pairwise κ, before adjudication) | ceiling reported per field | human judges | not started |
| H5 | Calibrate the AI judges against people: judge–human κ per field, for the panel, for the outside-family judge alone and for each judge | acceptance per field | κ ≥ 0.6 **and** no more than 0.1 below human–human; otherwise revise the rubric on the development split only and redraw the validation sample | Bear | not started |
| H6 | Targeted review queues (IV.4): disagreements, `FAMILY_SPLIT`, low agreement, flagged records, redirects, Wikidata errors, consensus gaps | a human label for each queued item | every queued item labelled or marked `UNSURE` with a note | human judges | not started |
| H7 | Random audit of agreed items: a seeded sample of items every model agreed on | the false-agreement rate | reported with an interval | human judges | not started |
| H8 | Adjudicate: majority of human judges, ties to Bear, judges' own words kept in `notes` | one adjudicated label per reviewed item | no open ties | Bear | not started |
| H9 | Verify claims (correctness, not agreement): for every claim kept, a reviewer opens the cited source and marks `supports`, `contradicts` or `unsure`; claims with only `model_knowledge` basis are sourced or withheld | per-claim decisions | no kept claim without a named check | reviewers | not started |
| H10 | Domain-safety review against the lexicon's rule (IV.4) | a pass or a list of removals | zero open safety items | Bear or a named domain reviewer | not started |
| H11 | Scope, duplicate and redirect decisions, with a crosswalk to the original seed IDs | decision list and crosswalk | every flagged seed decided | Bear | not started |
| H12 | Accept or reject merged entries into the reviewed edition (`lexicon/entries.jsonl`), with per-claim decisions, contributing run IDs and a named reviewer | the first reviewed entries | each accepted entry has a named reviewer and no unresolved contradiction | Bear | not started |
| H13 | Held-out task and coverage evaluations (IV.5) | task scores with intervals | analysis plan fixed before annotation | Bear + raters | not started |
| H14 | Write up: human ceiling, judge–human agreement, false-agreement rate, safety outcome, accepted-entry counts | the evaluation section of this paper | Bear approves | Bear | not started |

Agreement between models is not evidence that an entry is right. Steps H9 to H12 exist because two models can agree on the same mistake.

### IV.4 What humans review in this lexicon

Editions available today: **one**, the Grok Bot edition (352 records, 274 entries). The comparison needs a second blind edition (paste-in prompt `03-drugs-and-recreational-drug-use.md`).

| Queue | Source | Size in the Grok edition | What the human decides |
|---|---|---:|---|
| Ambiguous | `ambiguous` flags | 106 records (includes 11 redirects to pages that are not seeds) | sense, scope, keep or withdraw |
| Out of scope | `out-of-scope` | 78 | confirm: biographies, organisations, websites, creative works, lists, places, events, programmes, laws, statistics pages |
| Duplicates | redirects to another seed | 5 (one, International Drug Users Remembrance Day, also out of scope) | map or keep |
| Possible duplicates | `possible-duplicate` | 8 records in 4 pairs | one concept or two |
| Redirects to pages that are not seeds | RUN.md | 11 (e.g. Biobetter, Pentastack, Whoonga, ΔFosB) | new concept, map, or abstain |
| Domain-rule omissions | RUN.md list | 25 records where source content was deliberately left out | confirm nothing of the omitted content survived |
| Regional and slang aliases | `regional term` and related flags | 9 records [counted from `drafts.jsonl` flags on 2026-11-26] | the condition on the alias is right and not stigmatising |
| Thin evidence | warning "most claims rest on model knowledge" | 98 (78 out of scope by design + 20 entries) | the 20 entries go first in H9 |
| Retried drafts | `_meta.attempt = 2` | 13 | spot-check |

**Domain-safety review (H10).** The rule: describe substances, substance classes and public-health terminology; qualify regional or ambiguous aliases; no synthesis, procurement, dosing or concealment guidance; no inference of demographics from individual mentions. The reviewer reads every definition, variant and relation note, with the 25 omission records first. Pass criterion: no text that would help someone make, obtain, dose or hide a substance, and no claim tying a practice to a demographic group. A reviewer should also check that slang aliases are qualified by region or context, as *Kush (drug)* is qualified against the cannabis sense.

### IV.5 Held-out task and coverage evaluations

- **Alias resolution.** A held-out set of public terminology sources (for example glossaries published by public-health agencies) [TODO: choose sources], with raters linking each alias to a concept or marking it unresolved. Measures whether conditions on slang and regional aliases resolve correctly. Identifiable social-media posts are excluded.
- **Coverage.** Map a sample to the WHO ATC classification, RxNorm, MeSH (Chemicals and Drugs; Substance-Related Disorders) and ICD-11's disorders due to substance use. Measures overlap and gaps, especially for culture and slang terms that no clinical vocabulary holds. Status: not designed.
- **Scope agreement.** As for the other lexicons, once a second edition exists.

### IV.6 Open decisions

- The seven "Decisions for Bear" in `AGREEMENT-METHOD.md` §12 on `grok-agreement-method` (ab145901), including the draft `TRAP_IDS`.
- The human worked examples in the judging instructions are placeholders (RUN.md).
- Two manifest roots, `Category:Recreational drugs` and `Category:Substance use disorders`, have no members, so recreational-drug terms enter only through the other five roots. Changing that needs a new seed version, not an edit.
- The 11 redirects to pages that are not seeds and the 4 possible-duplicate pairs.
- Who drafts the second edition.

### IV.7 Resources, owners and status

About 10 human judges at about 100 items each, a pilot labelled by Bear and one other judge, and a domain-safety reviewer with public-health background. Tools: `agreement.py register`, `validate`, `stats`. Owner: Bear unless delegated. Status: not started.

## Part V. Limitations

The seed frame lacks two intended roots. Slang changes faster than any pinned revision. Demographic framing was removed by rule, so the lexicon cannot be used to study who uses what, and should not be. The edition was batched.

## Appendix A. File formats

**Seeds** (`data/seeds.tsv`): `concept_id`, `page_id`, `preferred_name`, `source_url`, `direct_categories`.

**Evidence bundle** (`bundles.jsonl`, one JSON object per seed, exactly seven top-level fields):

| Field | Content |
|---|---|
| `concept_id` | the seed ID, unchanged |
| `concept` | `id`, `preferred_name`, `kind` and `broad_class` (`unclassified` until supported), `variants` and `relations` (start empty) |
| `neighbors` | candidate relation targets, taken only from the seed list, each `{id, name}` |
| `examples` | optional public terminology excerpts `{id, source URL, text}` |
| `wikipedia` | up to three `{title, revision_id, text}`; the revision is pinned |
| `wikidata` | candidate items `{qid, label, aliases, claims, revision_id}` and ancestors marked `ancestor_of` |
| `wordnet` | matching senses `{synset, lemmas, gloss, relations}` |

**Draft** (`drafts.jsonl`, one JSON object per seed, prompt gen-v2):

| Field | Content |
|---|---|
| `concept_id` | the seed ID |
| `work_sense` | one sentence fixing the sense every later decision is about (the name is kept from the first lexicon for schema compatibility) |
| `links.{wikipedia,wikidata,wordnet}` | `{choice, reason}`; `choice` is a revision ID, QID or synset ID, or `null` to abstain |
| `definition` | `{text, basis, pointers}`; one to three sentences, never more than eight consecutive words from a source |
| `variants[]` | `{text, condition, basis, pointers}`; `condition` says when the form names the concept |
| `relations[]` | `{type, target_label, target_id, proposed_new, basis, pointers, note}` |
| `flags[]` | strings, each a prefix and a reason (Appendix B) |
| `_meta` | added after drafting: model and version (or `unknown`), run mode, attempt count, and for retries the errors that triggered them |

**Pointer forms:** `wd:QID#PID=VALUE_QID`, `wd:QID#alias=TEXT`, `wn:SYNSET#lemma=TEXT`, `wn:SYNSET#RELATION=TARGET`, `wp:REVISION_ID#quote=TEXT` (at most 20 words, copied exactly), `ex:EXAMPLE_ID`.

**Check report** (`report.jsonl`): one line per seed, `{concept_id, status: pass|fail, errors[], warnings[]}`.

**RUN.md:** dates, seed commit and hash, model and settings, tools, evidence sources, deviations, coverage totals, retries and unresolved failures.

## Appendix B. Flags

| Prefix | Meaning |
|---|---|
| `out-of-scope: <reason>` | no usable sense in this domain |
| `ambiguous: <reason>` | unresolved evidence or more than one sense |
| `duplicate: <id and title>` | redirect to another seed (added by the run) |
| `possible-duplicate:` | two seeds may name one concept (added by the run) |
| `domain rule:` | source content omitted under the domain rule (added by the run) |
| regional-term flags | alias or practice tied to a region (added by the run) |

## Appendix C. Scripts

As in the clinical lexicon: `render.py`, `check.py`, `verify_drafts.py`, and `agreement.py` on `grok-agreement-method`.

## References

- Miller, G. A., Beckwith, R., Fellbaum, C., Gross, D., and Miller, K. J. 1990. Introduction to WordNet: An on-line lexical database. *International Journal of Lexicography* 3(4): 235–244. Revised in *Five Papers on WordNet*, CSL Report 43, Princeton University, 1990, revised 1993.
- Miller, G. A. 1990. Nouns in WordNet: A lexical inheritance system. *International Journal of Lexicography* 3(4): 245–264.
- Gross, D., and Miller, K. J. 1990. Adjectives in WordNet. *International Journal of Lexicography* 3(4): 265–277. Revised as Fellbaum, Gross and Miller in *Five Papers on WordNet*, 1993.
- Fellbaum, C. 1990. English verbs as a semantic net. *International Journal of Lexicography* 3(4): 278–301.
- Beckwith, R., Miller, G. A., and Tengi, R. 1993. Design and implementation of the WordNet lexical database and searching software. In *Five Papers on WordNet*.
- Miller, G. A. 1995. WordNet: A lexical database for English. *Communications of the ACM* 38(11): 39–41.
- Fellbaum, C., ed. 1998. *WordNet: An Electronic Lexical Database*. MIT Press.
- Vrandečić, D., and Krötzsch, M. 2014. Wikidata: A free collaborative knowledgebase. *Communications of the ACM* 57(10): 78–85.
- Krippendorff, K. 2018. *Content Analysis: An Introduction to Its Methodology*, 4th ed. SAGE.
- Fleiss, J. L. 1971. Measuring nominal scale agreement among many raters. *Psychological Bulletin* 76(5): 378–382.
- Shared methods paper: *Building WordNet-style lexica with AI: process and provenance* (`building-wordnet-style-lexica-with-ai.md` in this folder).
- WHO ATC classification, RxNorm, MeSH and ICD-11 are named in IV.5 as candidate reference vocabularies [TODO: add citations when the coverage study is designed].
