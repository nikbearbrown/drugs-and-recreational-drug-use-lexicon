# Figure 1. Two agents sharing a reviewed lexicon

```mermaid
flowchart TD
    L["Reviewed release: concept IDs, aliases, exclusions and version"]
    T["Run trigger and validated source plan"] --> S
    T --> R
    L --> S["Social Media Agent: select approved organizational sources"]
    S --> SN["Map source fields; filter the window; deduplicate comparable IDs"]
    SN --> SC["Check source coverage; report missing sources, not zero"]
    SC -->|Complete| SR["Aggregate matches; suppress small live counts; human review"]
    SC -->|Incomplete| SF["Withhold combined report; return source receipts"]
    L --> R["Research Ledger: build source-specific literature queries"]
    R --> RN["Retrieve; retry temporary failures; record source coverage"]
    RN --> RD["Normalize DOI and PMID; deduplicate; link paper versions"]
    RD --> RS["Check known corrections and retractions; preserve match reasons"]
    RS --> RC["Read-only paper catalog with source coverage"]
    RN -->|Source gaps| RC
    RC --> A["Claude Code, Codex, or another reader agent"]
    P["Private reader preferences and current question"] --> A
    A --> H["Private shortlist: why each paper matches, links and caveats"]
```

**Public-language path.** The [Social Media Agent prototype](https://github.com/nikbearbrown/social-media-agent/blob/8c70deb/agents/README.md) can demonstrate collection and normalization on fictional data. Public organizational language can suggest aliases or reveal ambiguity. It does not measure health events or validate clinical rules. Any match-level analysis in this paper is proposed for fictional data, not an existing live export.

**Literature path.** Research Ledger is a design, not a deployed system. Start with [PubMed via NCBI E-utilities](https://ncbi.nlm.nih.gov/home/develop/api/). Save query and lexicon versions, dates published and first indexed or seen, source and match field. Link preprints to journal versions when known. Use [Crossref and Retraction Watch](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/) as one source of known updates; unknown status is not a quality signal. Label source gaps and preserve the last good catalog if every source fails. Reader preferences filter and rank the catalog without changing collection; each shortlist distinguishes relevance from evidence quality. Store or export text only as permitted.

The two channels share reviewed terminology, not records, private preferences or evidence labels. Treat collected text as data, never instructions. A newly discovered phrase goes to human review before changing the lexicon. Do not join either channel to clinical records.
