# Drugs and Recreational Drug Use Lexicon

**A checked vocabulary of drugs and recreational drug use, built from independent model editions.**

[Working abstract](#abstract) · [How to contribute](CONTRIBUTING.md) · [Seed list](data/README.md) · [Replication kit](replication/README.md)

**We're inviting collaborators.** Review the method, check a source, review entries in your field, or take on one of the tasks listed below. You don't need to review the whole project to help. To join, follow [Getting started](CONTRIBUTING.md#getting-started) in the contributor guide.

> **Drafting an independent edition?** Follow [AGENTS.md](AGENTS.md) and the [replication kit](replication/README.md), and nothing else in this README. Don't read other model runs or the reviewed edition while you draft.

A Humanitarians AI terminology project, led by Nik Bear Brown. It is one of [Humanitarians AI's papers in progress](https://github.com/nikbearbrown/hai-research).

## Abstract

*Working abstract. No manuscript exists yet, so this describes what the paper sets out to do. It reports no results.*

Drug names, street names and the vocabulary of drug use vary widely and change quickly, and a model-written glossary can read as authoritative when no one has checked it. This project builds a lexicon of drugs and recreational drug use that can be audited claim by claim. The starting list is 352 English Wikipedia article pages, each a direct member of the categories Drugs, Psychoactive drugs, Drug culture, Substance abuse or Substance-related disorders, with no title filter. Several language models each draft an independent edition of every seed from public sources they cite, without seeing one another's work. Automated checks reject an edition that misses a seed, breaks the entry shape or cites evidence it did not link. The frozen editions are then compared term by term, and a reviewer checks the cited source for every claim that enters the reviewed lexicon. The paper will report the method, how far the independent editions agree, and what review finds. Agreement between models is not treated as evidence. The lexicon describes terms; it is not medical advice.

## Where the draft is

There is no draft yet. The closest documents are the [seed list and its provenance](data/README.md), the [replication kit](replication/README.md) and the [rules for the reviewed edition](lexicon/README.md).

## What needs to be done

- **Draft independent editions** with several model families, following the [replication kit](replication/README.md). None exists yet.
- **Run the evidence checks** on each edition with `replication/scripts/check.py`.
- **Compare the editions** term by term once they are frozen.
- **Review entries** against their cited sources, with people who know the field, to build the reviewed edition.
- **Review the seed list** for pages that don't name a single substance, substance class or public-health term. The list stays fixed, so findings go in issues (see the [contributor guide](CONTRIBUTING.md#pick-a-way-to-help)).
- **Decide how to handle** redirects, lists and pages that don't name a single concept, which the seed list keeps on purpose.
- **Place the work** against established vocabularies such as MeSH, RxNorm or UMLS.
- **Write the paper:** the method, the agreement results and what review found.
- **Recommend a journal** Northeastern covers in full (see the [contributor guide](CONTRIBUTING.md#recommend-a-journal-northeastern-covers-in-full)).

## How to contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). In short: read this README, pick one task, and email Nik at bear@bearbrown.co with the subject "Drugs and Recreational Drug Use Lexicon: contributor" to be added to the repository. Anyone can [open an issue](https://github.com/nikbearbrown/drugs-and-recreational-drug-use-lexicon/issues/new) without emailing first.

## Executive summary

**What this is:** the working repository for a paper on building a checked vocabulary of substances, substance classes and public-health terms from several independent model-drafted editions. It holds the seed list and the kit a coding agent uses to draft an edition. The reviewed lexicon will be added here.

**Why read it:** to see what the paper will claim, how far the work has got, and where you could help.

**Where it stands (November 27, 2026):**

- **The seed list is fixed.** [data/seeds.tsv](data/seeds.tsv) holds 352 pages, and its hash is in [data/source-manifest.json](data/source-manifest.json).
- **The replication kit is ready.** It has the instructions, the two prompt files, and the scripts that render the messages and check an edition.
- **No independent drafts or consensus entries exist in this repo yet.** Editions are drafted and handed in privately.
- **No manuscript exists.** There is a working abstract, above.

## About this lexicon

A Humanitarians AI terminology project. The starting manifest has **352 unique English Wikipedia article pages**, deduplicated by page ID. Every page is a direct member of a listed seed category. No subcategory-only pages or title filters were used. Category membership supplies candidates, not medical authority or proof that a page names a single concept.

- [Seed list and provenance](data/README.md)
- [Independent-agent replication kit](replication/README.md)
- [Canonical edition and review](lexicon/README.md)

No independent drafts or consensus entries exist in this repo yet. This vocabulary is not diagnostic, treatment, or substance-use advice.

## What is here

| Path | What it holds |
|---|---|
| [data/](data/README.md) | The seed list (`seeds.tsv`) and where it came from (`source-manifest.json`): the retrieval window, the root categories including the missing and empty ones, the count and the hash. |
| [replication/](replication/README.md) | The kit for one independent edition: instructions, prompt files, and the scripts that render messages and check a finished edition. |
| [lexicon/](lexicon/README.md) | Where the reviewed lexicon will go, and how editions are reconciled. No entries yet. |
| [AGENTS.md](AGENTS.md) | Where a coding agent starts. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Ways to help, the rules for this lexicon, and how credit works. |
