# Seed data

[seeds.tsv](seeds.tsv) holds one row per Wikipedia page, with a stable `enwiki:<page_id>` identifier, title, URL, and **direct memberships only**. [source-manifest.json](source-manifest.json) records the retrieval window, exact roots including empty/missing labels, count, and seed hash. No article text is distributed here. Follow the linked Wikipedia pages for attribution and source history. Do not silently drop redirects, lists, or ambiguous pages; annotate them in the independent drafts.
