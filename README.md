# Quantum Knowledge Base — A Curated Hub for Deep Research

This is a **personal knowledge hub** dedicated to deep, structured research into **quantum mechanics, quantum computing, and scientific breakthroughs** in these domains. It is inspired by the pattern of building curated knowledge bases (like [Andrej Karpathy's LLM Wiki](https://github.com/karpathy/llm.c)) but focused on quantum physics and computing.

## Purpose

This project serves as a **single source of truth** for understanding quantum physics concepts, tracking breakthroughs, and synthesizing knowledge from diverse sources. It is designed to:

- **Aggregate knowledge** from papers, articles, transcripts, and other sources
- **Organize and cross-reference** scientific concepts, entities (people, labs, hardware), and findings
- **Provide synthesis** through LLM-assisted analysis and comparison
- **Maintain a living record** of evolving understanding through append-only operation logs
- **Support bilingual access** with content in both English and Portuguese

## Structure

```
/
├── CLAUDE.md              ← Schema document (read this first)
├── raw/                   ← Immutable source documents (never modified by LLM)
│   ├── articles/          ← Web-clipped markdown articles
│   ├── papers/            ← PDF papers and preprints
│   ├── transcripts/       ← Video/podcast transcripts
│   └── assets/            ← Local images referenced by raw docs
├── wiki/                  ← LLM-maintained knowledge base
│   ├── index.md           ← Master catalog of all wiki pages
│   ├── log.md             ← Append-only chronological log of operations
│   ├── overview.md        ← High-level synthesis of the knowledge base
│   ├── entities/          ← Pages for people, labs, companies, hardware
│   ├── concepts/          ← Pages for scientific/technical concepts
│   ├── sources/           ← Summary pages for each ingested raw source
│   └── outputs/           ← Filed query answers and analyses
└── tools/
    └── search.py          ← CLI search engine over wiki content
```

## Key Principles

### 1. **Immutable Sources**
Raw documents in `raw/` are never modified. This preserves the original source material and enables tracking of how understanding evolves as new sources are added.

### 2. **LLM-Maintained Knowledge**
Content in `wiki/` is generated and maintained by Claude Code. This includes:
- Summaries of ingested sources
- Encyclopedia-style concept pages
- Entity profiles (researchers, labs, hardware systems)
- Synthesized analyses and answers

### 3. **Bilingual Foundation**
All pages include titles and summaries in both **English and Portuguese (PT-BR)**. This makes the knowledge base accessible to speakers of both languages.

### 4. **Append-Only Operations**
The `wiki/log.md` file is append-only. Every ingest, query, and update is recorded with a timestamp and description. This creates an auditable history of how the wiki has evolved.

### 5. **Cross-Referencing**
Pages use Obsidian-style wiki links (`[[path/to/page]]`) to create a rich network of connections between concepts, entities, and sources. This supports both machine navigation and human exploration.

## Workflows

### Ingesting a Source

1. Place a new document in one of the `raw/` subdirectories
2. Ask Claude Code: *"Ingest `raw/articles/filename.md`"*
3. Claude will:
   - Read and summarize the source
   - Create concept and entity pages as needed
   - Update the master index and operation log

### Querying the Knowledge Base

1. Ask a question (e.g., *"What is the current state of quantum error correction?"*)
2. Claude will:
   - Search relevant pages
   - Synthesize an answer with citations
   - Optionally file the answer back into `wiki/outputs/`

### Searching

Use the CLI search tool to find content:

```bash
# Search all content
python tools/search.py "quantum error correction"

# Search titles and frontmatter only
python tools/search.py --titles-only "superconducting qubits"
```

## Frontmatter Convention

Every wiki page begins with YAML frontmatter:

```yaml
---
title: "Page Title in English"
title_pt: "Título em Português"
type: concept | entity | source | output | overview
tags: [quantum-computing, error-correction, hardware]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_count: 3
sources: [sources/paper-foo.md, sources/article-bar.md]
---
```

This ensures consistent metadata, makes pages machine-readable, and supports Obsidian integration.

## Getting Started

### Setting Up Locally

Clone the repository:
```bash
git clone https://github.com/vitordalca/claude_knowledge_base_for_quantum_physics.git
cd claude_knowledge_base_for_quantum_physics
```

View the schema and conventions:
```bash
cat CLAUDE.md
```

Check the current state of the wiki:
```bash
cat wiki/index.md
cat wiki/log.md
```

### Adding Your First Source

1. Save or download a source document to one of the `raw/` directories:
   - `raw/articles/` for web articles or clipped content
   - `raw/papers/` for PDFs and preprints
   - `raw/transcripts/` for video/podcast transcripts

2. Open Claude Code and run:
   ```
   Ingest raw/articles/my-article.md
   ```

3. Claude will process the source, create summaries, and update the wiki.

## Philosophy

This knowledge base is built on the belief that **understanding emerges from careful curation and synthesis**. It's not a collection of links or summaries—it's an active, interconnected workspace where:

- Sources are preserved as-is
- Knowledge is synthesized and cross-referenced
- Understanding compounds as new sources are added
- The history of discovery is recorded and transparent

It is a tool for **deep learning** about quantum physics and computing, suitable for researchers, students, and anyone pursuing serious understanding of these domains.

## For More Details

See `CLAUDE.md` for the complete schema, page templates, and LLM behavior guidelines.

---

**Status:** Active, awaiting first source ingest.

**Languages:** English, Portuguese (PT-BR)

**Maintained by:** Claude Code + human curator
