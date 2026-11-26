# Parallel editions

Independent, machine-drafted editions of this lexicon, kept here as parallel evaluations so they can be compared side by side. Each subfolder is one model's edition.

- **Unreviewed.** Every record is a machine draft. None has been checked by a person, and none is part of the reviewed lexicon in [`lexicon/`](../lexicon/README.md).
- **Not for drafters.** If you are drafting an independent edition with the [replication kit](../replication/README.md), do not open this folder until your edition is frozen. The kit's blindness rule covers every edition here.
- **Unedited copies.** The files inside an edition folder are copied unchanged from that model's private run folder. Nothing was hand-edited after the edition's final `check.py` run. Paths inside `RUN.md` and the tools refer to the drafter's own machine.
- Wikipedia text in the bundles is CC BY-SA 4.0, with the exact revision id pinned per record; Wikidata is CC0; WordNet 3.0 is under the WordNet licence.

## Editions

| Folder | Model as recorded | Run mode | Date | Seed commit | `data/seeds.tsv` sha256 | Records | `check.py` |
|---|---|---|---|---|---|---|---|
| [`grok-bot/`](grok-bot/) | Grok Bot (exact version: unknown, not exposed to the drafter) | Batched: a 10-seed pilot, then batches 1–33 of 10–15 seeds, in one session, not a fresh context per seed. Approved by the project owner and disclosed in `RUN.md` and every `_meta.run_mode`. | 2026-11-24 (EST) | `538d4f3e1e82cf72f0b78bedbe76453bca4e9210` | `caa4f3ae910f11ca4ec72ce3ac7f9123f1566a28b05242fa7c5cc3fdffede372` | 352 / 352 seeds | 352/352 pass, 0 fail (13 records revised once after a first-save validator error) |

## `grok-bot/`: files

| File | What it is |
|---|---|
| `RUN.md` | Protocol deviation, model, seed commit and hash, method, check result |
| `drafts.jsonl` | One draft per seed, each with `_meta` |
| `report.jsonl` | `check.py` output per seed |
| `bundles.jsonl` | Evidence bundle per seed: pinned Wikipedia revision, Wikidata, WordNet 3.0, neighbors |
| `pilot/` | The 10-seed pilot drafts and report |
| `specs/batch_NN.py` | The drafter's per-batch drafting sources |
| `tools/*.py`, `tools/summary.txt` | Bundle builder, draft library and per-seed summary |

## Left out of `grok-bot/`, and why

- `parts/` (per-batch draft files; the same records are in `drafts.jsonl`).
- `tools/wp_info.json`, `tools/seed_meta.json`, `tools/build.log` (fetch caches and a log).
- No rendered entries file exists for this edition.
- No keys, secrets or judging anonymisation files are included.

More editions from other models can be added as sibling folders, for example `editions/<model>/`, with a row in the table above.
