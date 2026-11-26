# Human evaluation to-do: after the AI cross-model comparison

*Rough draft, not reviewed. Nothing on this list has been run.* Written 2026-11-26 for Professor Bear.

This is the working checklist behind Part IV of every lexicon paper. Part 1 lists what the AI side must finish first. Part 2 gives the human steps once, in order, with owners, tools, gates and status. Part 3 gives this lexicon's specifics (the other four lexicons have their own copy in their repositories): its review queues with counts from the Grok Bot edition, its domain-safety rule, its held-out task and its open decisions.

The principle comes from the repositories: **agreement is not evidence**. The AI comparison tells people where to look; it does not tell them what is true. A separate reviewer checks the cited source for each claim that goes into a reviewed edition (`lexicon/README.md` in each repo).

## Part 1. Before people start: the AI side

| # | Prerequisite | IHWL | Clinical | Drugs | Disease | NanoLex |
|---|---|---|---|---|---|---|
| A1 | At least two frozen, blind editions, each with its commit SHA | yes: Grok Bot, Claude Sonnet 5.5, plus the reference | Grok Bot only | Grok Bot only | Grok Bot only | Grok Bot only (the initial lexicon joins after freezing) |
| A2 | A row in `judging/drafters.tsv` for every drafter, so self-exclusion works | Sonnet 5.5 and Grok rows exist | [TODO] | [TODO] | [TODO] | no rows yet |
| A3 | `agreement.py run`: normalise editions, coverage, deterministic alignment, blinded requests | done for the pilot | smoke-tested only | smoke-tested only | smoke-tested only (932 requests on two copies of one edition) | not run |
| A4 | Model judges join (`agreement.py join`, or `export-packet` and `import` for chat-only models) and finish their packets | pilot: two judges, batches pending (50 and 44) | not started | not started | not started | not started |
| A5 | Leak check: can a judge tell which model wrote a text? | not run | not run | not run | not run | not run |
| A6 | Code not yet written: the family-weighted panel label for an open panel, leave-one-judge-out, the self-preference probe | to do | to do | to do | to do | to do |
| A7 | `agreement.py stats`: Krippendorff's α across editions, Fleiss' κ on the complete subset, pairwise scores, entry scores | pilot only | no | no | no | no |
| A8 | NanoLex only: `leak_check.py` against the initial lexicon, then `legacy_to_edition.py` | n/a | n/a | n/a | n/a | not run |

The human steps can start in parallel with A4 for the pilot (H1 to H3), but H5 onward need the model judges' results.

## Part 2. The human steps, in order

### Who and what is needed

| Item | Default from AGREEMENT-METHOD.md | Note |
|---|---|---|
| Human judges | about 10 per lexicon | background recorded; domain expertise not required for meaning comparison, but required for H9 and H10 in the medical lexicons |
| Items per judge | about 100 (or 50) | seeded, stratified by field and class, at least 10% trap items |
| Overlap | about 30% of each judge's items from a shared pool of about 50, at least 2 judges per pool item | gives the human ceiling |
| Scale | about 1,000 judgments, about 750 unique items, per lexicon at 10 judges | |
| Time | 1.5 to 3 minutes per item, so 3 to 5 hours per judge, in resumable sessions | |
| Pilot | Bear and at least one other judge label the whole pilot pool | IHWL pilot: 32 shared concepts (96 definition pairs plus other fields) |
| Tools | `agreement.py register --size --overlap --pool-size --trap-share`; `validate`; `stats`; `HUMAN-JUDGE-INSTRUCTIONS.md`; `INTERVIEWER-PROTOCOL.md` | a person judges by talking to a coding agent opened in the repo; the agent shows blinded items, maps comments to labels, reads each label back, keeps the person's words in `notes`, and never suggests a label first |
| Claim verification and safety | named reviewers with the cited sources open | not covered by the judge sample; see H9 and H10 |

### The steps

Each step: what to do, the tool, the gate before moving on, the owner and the status. Status is "not started" throughout.

**H1. Settle the open decisions.** Owner: Bear. Status: not started.
- [ ] Which models judge, and the `drafters.tsv` row for every edition (self-exclusion is item by item: a drafter never sees an item that involves its own edition).
- [ ] Whether Grok Bot judges pairs that do not involve its own editions, or not at all.
- [ ] Confirm or replace each lexicon's draft trap list (`TRAP_IDS`).
- [ ] Write the human worked examples left as placeholders in `HUMAN-JUDGE-INSTRUCTIONS.md`.
- [ ] Weights and hard gate for the entry score; the acceptance rule (κ ≥ 0.6 and within 0.1 of human–human).
- [ ] The lexicon's own pending decisions (Part 3).
- Gate: a committed decision record per lexicon.

**H2. Recruit and register human judges.** Owner: Bear. Status: not started.
- [ ] Name the judges and record their background.
- [ ] Register each with `agreement.py register` (size, overlap, pool size, trap share). The seed comes from the run salt and the judge id, so the sample can be redrawn.
- [ ] If model labels already exist, optionally oversample `CONFLICTING`, `DIFFERENT_SENSE` and `FAMILY_SPLIT` items; record the weights.
- Gate: at least two judges for the pilot.

**H3. Pilot and freeze.** Owner: Bear plus one judge. Status: not started.
- [ ] Both label the whole pilot pool.
- [ ] Tune the rubric on the development half only; test on the other half.
- [ ] Freeze the prompts (`agree-v1`) and commit the analysis plan with a tag before the full run.
- Gate: tag exists.

**H4. Human–human overlap and the ceiling.** Owner: the judges. Status: not started.
- [ ] Every pool item gets at least two human labels before any adjudication.
- [ ] Compute Krippendorff's α (and pairwise κ) between people, per field.
- Output: the **human ceiling**, the standard the model judges are held to.

**H5. Calibrate the AI judges against people.** Owner: Bear. Status: not started.
- [ ] Judge–human κ (weighted κ for the ordinal definition scale) on every human-judged item, for the primary panel, for the judge outside every drafter's family, and for each judge; confusion matrices; precision and recall for "same meaning" and "conflicting".
- [ ] Position-flip rate and test–retest consistency for each judge.
- [ ] Self-preference check (difference in differences against the outside-family judge) and leave-one-judge-out on the main tables.
- [ ] Accept the panel for a field only if κ ≥ 0.6 and no more than 0.1 below human–human. Otherwise revise the rubric on the development split and draw a fresh validation sample.
- Gate: a field-by-field accept or reject. Fields that fail stay human-judged.

**H6. Targeted review queues.** Owner: the judges. Status: not started. Every item in these queues gets a human label, beyond the random samples:
- [ ] **Disagreements**: definition pairs labelled `CONFLICTING` or `DIFFERENT_SENSE`; editions marked `cross_sense` at the sense gate; links labelled `CONFLICTING`; relations `REVERSED` or `CONFLICTING_TYPE`.
- [ ] **`FAMILY_SPLIT`**: items where judge families disagree.
- [ ] **Low agreement**: entry score below 0.75 for any pair, or not unanimous.
- [ ] **Flagged records**: out of scope, duplicate, possible duplicate, ambiguous, unattested (NanoLex), kind unclassified (Disease), especially where editions disagree on scope.
- [ ] **Redirects**: to pages that are not seeds, to missing sections, to sections of other seeds.
- [ ] **Wikidata errors** recorded in flags: confirm the error and that it was not used as evidence.
- [ ] **Consensus gaps**: `proposed_new` targets two or more editions proposed independently, which are candidates for new concepts.
- [ ] **Trap items**: always reviewed.
- Gate: every queued item labelled, or `UNSURE` with a note.

**H7. Random audit of agreed items.** Owner: the judges. Status: not started.
- [ ] A seeded random sample of items that every edition and judge agreed on (for example 50 per lexicon [TODO: size]).
- Output: the **false-agreement rate**, which shows how often models agree on something people reject. This sample is separate from the ceiling pool in H4.

**H8. Adjudicate.** Owner: Bear. Status: not started.
- [ ] Majority of the human judges decides. Ties go to Bear.
- [ ] Keep each judge's words verbatim in `notes`. The interviewing agent records labels only.
- Gate: no open ties.

**H9. Verify claims.** Owner: named reviewers. Status: not started. This measures correctness, not agreement.
- [ ] For each claim proposed for the reviewed edition, open the cited source and mark `supports`, `contradicts` or `unsure`.
- [ ] Claims whose basis is `model_knowledge` are sourced or withheld. Thin-evidence records (check warning "most claims rest on model knowledge") go first.
- [ ] Legitimate ambiguity is preserved; aliases merge only after evidence confirms the same sense.

**H10. Domain-safety review.** Owner: Bear or a named domain reviewer. Status: not started.
- [ ] Read every proposed entry against the lexicon's rule (Part 3).
- Gate: zero open safety items. A failed item is withdrawn or rewritten and re-reviewed; it is not patched silently.

**H11. Scope, duplicate and redirect decisions.** Owner: Bear. Status: not started.
- [ ] Decide each flagged seed; record each redirect or duplicate as an explicit decision with a crosswalk to the original seed IDs.

**H12. Accept or reject merged entries.** Owner: Bear. Status: not started.
- [ ] Write accepted entries to `lexicon/entries.jsonl` in the draft shape; record per-claim decisions, evidence links, contributing run IDs and review status separately.
- [ ] An entry is accepted only with a named reviewer and no unresolved contradiction. Do not copy run bundles or source text into the reviewed lexicon.
- [ ] Decide whether the reviewed edition counts as an edition in α (default: reported separately).

**H13. Held-out task and coverage evaluations.** Owner: Bear plus raters. Status: not designed. Fix the analysis plan, the inventory version and the strata before annotation (Part 3 for each lexicon).

**H14. Write up.** Owner: Bear. Status: not started. Report the human ceiling, judge–human agreement per field, the false-agreement rate, `FAMILY_SPLIT` and `UNSURE` rates, safety outcomes, accepted-entry counts and the task results, each with its interval.

## Part 3. Drugs and Recreational Drug Use Lexicon

Paper: [drugs-and-recreational-drug-use-lexicon-paper-series.md](drugs-and-recreational-drug-use-lexicon-paper-series.md), Part IV.

#### What humans review in this lexicon

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

#### Held-out task and coverage evaluations

- **Alias resolution.** A held-out set of public terminology sources (for example glossaries published by public-health agencies) [TODO: choose sources], with raters linking each alias to a concept or marking it unresolved. Measures whether conditions on slang and regional aliases resolve correctly. Identifiable social-media posts are excluded.
- **Coverage.** Map a sample to the WHO ATC classification, RxNorm, MeSH (Chemicals and Drugs; Substance-Related Disorders) and ICD-11's disorders due to substance use. Measures overlap and gaps, especially for culture and slang terms that no clinical vocabulary holds. Status: not designed.
- **Scope agreement.** As for the other lexicons, once a second edition exists.

#### Open decisions

- The seven "Decisions for Bear" in `AGREEMENT-METHOD.md` §12 on `grok-agreement-method` (ab145901), including the draft `TRAP_IDS`.
- The human worked examples in the judging instructions are placeholders (RUN.md).
- Two manifest roots, `Category:Recreational drugs` and `Category:Substance use disorders`, have no members, so recreational-drug terms enter only through the other five roots. Changing that needs a new seed version, not an edit.
- The 11 redirects to pages that are not seeds and the 4 possible-duplicate pairs.
- Who drafts the second edition.
