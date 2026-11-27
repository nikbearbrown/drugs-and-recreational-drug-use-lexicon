# Context Before Counts: An Auditable Lexicon of Drugs and Recreational Drug Use

Humanitarians AI | Rough research protocol for author review | November 2026

## Abstract

Public health teams need to distinguish references to substances from ordinary words, program announcements and historical discussion. We propose an evidence-reviewed vocabulary built by comparing independent model editions and preserving ambiguous senses rather than merging them prematurely. We specify a controlled test on fictional organizational text and a separate literature-discovery test. Social Media Agent and Research Ledger consume the reviewed vocabulary independently. The seed manifest has 352 Wikipedia article pages; it does not establish 352 verified concepts. No concordance, classification performance, prevalence estimates or population findings are reported.

## Introduction

A keyword hit can be accurate as a string match but still irrelevant to the reader. It can denote an unrelated sense, a general education program or an explicit substance reference without establishing any event. A useful lexicon should make these distinctions visible. The research question is whether reviewer-approved context rules reduce wrong-sense matches at a tolerable loss of target-sense examples, and whether the same versioned vocabulary helps readers find relevant public-policy and prevention literature. These are separate hypotheses with different reference labels.

## Methods: construction and reconciliation

Use the [direct-member seed inventory](../data/README.md), and record the [manifest and seed hash](../data/source-manifest.json). Treat list pages, redirects and pages with several concepts as adjudication cases rather than silently dropping them. Use the [replication kit](../replication/README.md) to produce independently sourced editions in isolated contexts; record model and prompt versions, preserve abstentions and freeze each run before comparison. Report structural completion separately from semantic agreement. Review evidence for each retained claim even when editions agree. Store alias senses, evidence pointers, decision status and the version on which a downstream match depends. Do not publish unpublished editions or source bundles. This paper does not document manufacturing, procurement, routes of use or concealment.

## Methods: public-language and retrieval tests

**Language test.** On a held-out set of fictional notices, compare literal matching with the same vocabulary plus explicit, development-set context rules. Include target references, ambiguous ordinary senses, outreach announcements and plain negatives. Annotators independently label both spans and unique notices; adjudicate disagreement using a frozen rulebook and keep unclear cases visible. Distinguish a text that refers to a substance from a claim that anyone used it. Report the number of target-reference matches retained and other-sense matches removed, plus one table of false inclusions and omissions. Split by document template so rewrites of the same notice do not cross the split.

**Literature test.** Compare a fixed title/abstract and applicable [MeSH](https://www.nlm.nih.gov/mesh/meshhome.html) baseline with a reviewed-alias version on the same snapshot. Independent reviewers assess pooled paper-topic pairs without seeing which query returned them. Report precision at a fixed shortlist size, disagreements and incremental relevant papers within the judged pool. Mark records with insufficient context as unknown, and never estimate whole-index recall from the judged pool alone. Report retrieval relevance separately from publication status and evidence strength.

**Prespecification.** [NEEDS: frozen seed, rubric and release IDs for the experiment; review staffing; evaluation sample size; shortlist size; thresholds and uncertainty method.] Split rules and decide all thresholds before opening test outcomes. Report both match-level and document-level denominators rather than mixing units.

## Findings available now

The manifest and replication kit are available. No independent-model agreement, labeled benchmark performance, or live-source outcome is claimed. An illustrative table should show one known target sense, one irrelevant homograph, and one uncertain sense; use fabricated alias labels, not a guide to identifying or targeting people.

## Agentic workflows

[Figure 1](agentic-workflows.md) shows Social Media Agent for fictional demonstrations of language ambiguity and Research Ledger for retrieval and private personalization. Only approved wording and version identifiers are shared across agents. The latter is a design, not a live feed. Neither channel identifies individuals, infers demographics, tracks drug markets, estimates use, or recommends policy or clinical action on its own.

## Discussion

The design makes a reviewer decision traceable: what term matched, which sense was intended and how the evidence was checked. A synthetic test answers whether the rules handle the cases planted in it; it cannot estimate how often mistakes occur in real public language. A reader study could ask whether the shortlist is useful, after obtaining appropriate review and permission. The first publication target is a methods contribution, not a surveillance product.
