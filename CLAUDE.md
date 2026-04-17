# CLAUDE.md — Quantum Wiki Schema

This file is the authoritative schema for the quantum knowledge base. Read it at the start of every session before doing anything else. It defines the wiki structure, page conventions, and workflows you must follow.

---

## Domain

This wiki covers:
- Quantum mechanics (foundations, interpretations, formalism)
- Quantum computing (algorithms, hardware, error correction, milestones)
- Scientific breakthroughs related to the above (recent experimental results, landmark papers)

---

## Language Policy

All wiki pages are **bilingual**:
- **Title and abstract/summary block:** written in both English and Portuguese (PT-BR)
- **Body content:** written in English by default
- **Frontmatter tags:** English only
- Each summary page must include a `## Resumo` section in Portuguese immediately after the English `## Summary` section

---

## Directory Layout

| Path | Purpose | Who writes it |
|---|---|---|
| `raw/` | Immutable source documents | Human only |
| `raw/articles/` | Web-clipped markdown articles | Human only |
| `raw/papers/` | PDFs and preprints | Human only |
| `raw/transcripts/` | Video/podcast transcripts | Human only |
| `raw/assets/` | Locally downloaded images | Human only |
| `wiki/` | All LLM-generated content | LLM only |
| `wiki/index.md` | Master catalog of wiki pages | LLM (updated every ingest) |
| `wiki/log.md` | Append-only operation log | LLM (append only, never edit) |
| `wiki/overview.md` | High-level synthesis | LLM |
| `wiki/entities/` | People, labs, companies, hardware | LLM |
| `wiki/concepts/` | Scientific/technical concepts | LLM |
| `wiki/sources/` | One summary page per raw source | LLM |
| `wiki/outputs/` | Filed query answers and analyses | LLM |
| `tools/` | CLI utilities | LLM (with human direction) |

**Rules:**
- Never create files inside `raw/`. That directory is the human's domain.
- Never delete or overwrite `wiki/log.md` entries. It is append-only.
- Always update `wiki/index.md` after any ingest or new page creation.
- Always append to `wiki/log.md` after every operation (ingest, query, lint).

---

## Frontmatter Convention

Every wiki page must begin with YAML frontmatter:

```yaml
---
title: "Page Title in English"
title_pt: "Título da Página em Português"
type: concept | entity | source | output | overview
tags: [quantum-computing, error-correction, hardware]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_count: 3           # only for concept/entity pages
sources: [sources/paper-foo.md, sources/article-bar.md]  # backlinks to source summaries
---
```

---

## Page Types and Templates

### Source Summary Page (`wiki/sources/`)

One page per ingested raw document. Filename mirrors the raw file (e.g. `raw/articles/ibm-condor-2023.md` → `wiki/sources/ibm-condor-2023.md`).

```markdown
---
title: "Title of the Source"
title_pt: "Título da Fonte"
type: source
tags: [...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
raw_path: raw/articles/ibm-condor-2023.md
---

## Summary
[2–4 sentence English summary of the source's main contribution or argument.]

## Resumo
[2–4 frases em português resumindo a contribuição principal da fonte.]

## Key Points
- ...
- ...

## Entities Mentioned
- [[entities/person-name]] — role or relevance
- [[entities/lab-name]] — role or relevance

## Concepts Covered
- [[concepts/concept-name]] — how it appears in this source

## Notable Quotes or Data
> ...

## My Notes
[Space for the human to add annotations — left blank by default.]
```

### Concept Page (`wiki/concepts/`)

One page per scientific or technical concept. These are the wiki's encyclopedia entries.

```markdown
---
title: "Concept Name"
title_pt: "Nome do Conceito"
type: concept
tags: [...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_count: N
sources: [...]
---

## Summary
[English: clear, precise definition and significance of this concept in the domain.]

## Resumo
[Português: definição clara e precisa do conceito e sua relevância no domínio.]

## Explanation
[Longer English exposition. Use subsections as needed.]

## Current State of the Field
[What is known, what is debated, recent experimental or theoretical developments.]

## Key Papers and Sources
- [[sources/paper-name]] — what it contributes to understanding this concept

## Related Concepts
- [[concepts/related-concept]] — relationship

## Open Questions
- ...
```

### Entity Page (`wiki/entities/`)

One page per person, lab, company, or hardware system.

```markdown
---
title: "Entity Name"
title_pt: "Nome da Entidade"
type: entity
tags: [person | lab | company | hardware]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_count: N
sources: [...]
---

## Summary
[Who or what this is, why it matters to this wiki.]

## Resumo
[Quem ou o que é, e por que é relevante para este wiki.]

## Details
[Background, history, key contributions or specifications.]

## Contributions to the Field
[Specific breakthroughs, papers, hardware milestones.]

## Appearances in Sources
- [[sources/source-name]] — context
```

### Output Page (`wiki/outputs/`)

Filed answers to queries, analyses, comparisons. These compound the knowledge base.

```markdown
---
title: "Query or Analysis Title"
title_pt: "Título da Consulta ou Análise"
type: output
tags: [...]
created: YYYY-MM-DD
query: "The original question asked"
---

## Answer / Analysis
[The synthesized answer, with citations to wiki pages.]

## Sources Consulted
- [[wiki/concepts/...]]
- [[wiki/sources/...]]

## Follow-up Questions
- ...
```

---

## `wiki/index.md` Format

This file is the master catalog. Update it on every ingest and every new page creation. It must always be current.

```markdown
# Wiki Index
_Last updated: YYYY-MM-DD_

## Overview
- [[overview]] — High-level synthesis of the knowledge base

## Sources (N total)
| Page | Title | Date | Type |
|---|---|---|---|
| [[sources/foo]] | Title | YYYY-MM-DD | article |

## Concepts (N total)
| Page | Title | Source Count |
|---|---|---|
| [[concepts/foo]] | Title | 3 |

## Entities (N total)
| Page | Title | Type |
|---|---|---|
| [[entities/foo]] | Name | person |

## Outputs (N total)
| Page | Title | Date |
|---|---|---|
| [[outputs/foo]] | Query title | YYYY-MM-DD |
```

---

## `wiki/log.md` Format

Append-only. Never edit existing entries. Each entry header must follow this exact pattern so it's grep-parseable:

```
## [YYYY-MM-DD] TYPE | Title or Description
```

Types: `ingest`, `query`, `lint`, `setup`

Example entries:

```markdown
## [2026-04-17] setup | Initial wiki bootstrap

Created directory structure and CLAUDE.md. Stub files initialized.

---

## [2026-04-17] ingest | IBM Condor 2023 — Nature Paper

Processed: raw/papers/ibm-condor-2023.pdf
Created: wiki/sources/ibm-condor-2023.md
Updated: wiki/concepts/superconducting-qubits.md, wiki/entities/ibm-quantum.md
Index updated. 

---
```

---

## Workflows

### Ingest Workflow

When I drop a new source into `raw/` and ask you to process it:

1. Read the source file fully. If it contains images, note their paths and view them.
2. Briefly discuss the key takeaways with me before writing anything.
3. Write a source summary page in `wiki/sources/`.
4. Identify all concepts and entities mentioned. Update or create their pages.
5. Update `wiki/index.md`.
6. Update `wiki/overview.md` if the source materially changes the big picture.
7. Append an entry to `wiki/log.md`.

**One source at a time.** I prefer to stay involved in ingestion. Wait for my confirmation before moving to the next source.

### Query Workflow

When I ask a question:

1. Read `wiki/index.md` to identify relevant pages.
2. Read the relevant pages in full.
3. Synthesize an answer with citations to wiki pages (use `[[page]]` links).
4. Ask me if I want the answer filed back into `wiki/outputs/`.
5. If yes, write an output page and update `wiki/index.md` and `wiki/log.md`.

### Lint Workflow

When I ask you to health-check the wiki:

1. Scan all pages for: contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, concepts mentioned but lacking their own page, missing cross-references.
2. Report findings as a structured list.
3. Ask which issues I want to fix before changing anything.
4. After fixes, append a lint entry to `wiki/log.md`.

---

## Handling Images

Raw sources often reference images. Since you cannot read markdown with inline images in one pass:
1. Read the markdown text first.
2. Then explicitly view each image file referenced in the document using the file path.
3. Incorporate image content into the source summary and relevant concept pages.

---

## Backlink Convention

Use Obsidian-style wiki links throughout: `[[path/to/page]]` or `[[path/to/page|Display Text]]`. Always use relative paths from the `wiki/` root. This keeps the wiki navigable in Obsidian.

---

## Session Start Checklist

At the beginning of every new Claude Code session:
1. Read this file (`CLAUDE.md`).
2. Read `wiki/index.md` to understand the current state of the wiki.
3. Read the last 5 entries in `wiki/log.md` (use `grep "^## \[" wiki/log.md | tail -5` to find them quickly).
4. Ask me what I want to do today.
