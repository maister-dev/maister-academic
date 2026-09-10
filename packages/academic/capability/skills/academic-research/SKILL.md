---
name: academic-research
description: Use when a lesson's factual content — tool names, versions, defaults, protocol revisions, standards — must be verified against live primary sources before the lesson is written or refreshed, or when an existing source ledger may be stale.
license: MIT
metadata:
  version: "0.1.0"
  domain: course-authoring
---

# Research a lesson topic

A course has two layers, and they age at completely different rates.

The **stable layer** — concepts, models, trade-offs, failure modes — barely
moves. You already know most of it and the lesson brief scopes the rest.

The **volatile layer** — tool names, versions, flags, defaults, protocol
revisions, standards, pricing, which vendor shipped what — moves faster than a
semester. It is the only layer worth spending research on, and the only layer
that will silently make the lesson wrong six months from now.

Research the volatile layer. Write down what you verified and when. That record
is what makes the course maintainable; without it, nobody can tell a claim that
was checked last week from one that was checked two years ago.

## 1. Turn the brief into questions

Take the **Research targets** section of the lesson brief and restate each as a
question with a checkable answer.

Good: "Which transports does the current MCP specification define, and what is
the specification revision date?"
Bad: "Research MCP." A target you cannot answer with a citation is a target you
cannot verify later.

Depth comes from the run's `research_depth`:

| depth      | budget                                                                      |
| ---------- | ---------------------------------------------------------------------------- |
| `quick`    | Confirm the volatile facts the brief names. No exploration.                   |
| `standard` | The above, plus the current state of each tool or standard the lesson names.  |
| `deep`     | The above, plus competing approaches, known criticism, and recent incidents.  |

## 2. Search, then read

Search to find the source. Then **open it**. A search-result snippet is not a
source — snippets are stale, truncated, and frequently describe a version that
no longer exists.

Source ranking, best first:

1. **Primary** — the specification, the official documentation, the project's
   own repository, the release notes, the standards body's page.
2. **Secondary** — a signed technical article by someone with standing, a
   conference talk, a peer-reviewed paper.
3. **Community** — issue threads, forum answers. Usable as evidence that a
   problem exists; never as evidence of how something works.

Refuse outright:

- Marketing and pricing pages presented as technical documentation.
- Undated tutorials and listicles, especially aggregator content.
- Content that reads as machine-generated summary of other pages.
- Screenshots of interfaces, as evidence of anything. They expire fastest.

## 3. Pin the version

Every volatile claim carries the version it is true of. "The CLI supports `X`"
is not a fact; "`tool` 1.4.0 supports `X`" is. When the source itself is
versioned — a spec revision, a docs page for a release — record that revision,
not just the date you read it.

If a claim's version cannot be established, it does not go in the ledger, and
the lecture must not assert it.

## 4. Write the ledger

Write to the `sources` artifact path from `course.yaml`:

```yaml
schemaVersion: 1
verified: 2026-09-10
sources:
  - id: mcp-spec
    title: "Model Context Protocol — specification"
    url: https://modelcontextprotocol.io/specification
    kind: primary
    publisher: "Anthropic"
    version: "2025-06-18"
    accessed: 2026-09-10
    supports:
      - "MCP servers expose three primitives: tools, resources, prompts"
      - "Transport is defined separately from the primitive model"
    notes: "Section 'Server features' is the load-bearing part for this lesson."
open_questions:
  - "Whether A2A message framing is stable enough to teach beyond concept level."
```

Rules the ledger has to hold:

- **`supports` is the point.** Each entry lists the claims it backs, phrased as
  the lecture will phrase them. An entry with no `supports` is a bookmark, not
  evidence — drop it.
- **Every volatile claim in the lesson appears in exactly one `supports` list.**
  This is what the didactic review checks. A claim with no entry must be cut or
  verified, never softened into vagueness to survive review.
- **`accessed` is the date you actually opened it.** Never copy it forward.
- **`open_questions` is not a failure.** Recording that something could not be
  established is more useful than a confident sentence nobody can check.

## 5. On a refresh run

Read the existing ledger first. For every entry older than `sources.maxAgeDays`
in `course.yaml`, re-open the source and either bump `accessed`/`version` or
record what changed. An entry whose source moved, changed meaning, or vanished
is a finding — it usually means a passage in the lecture is now wrong, and that
belongs in `open_questions` for the writing step to act on.

Do not delete history silently. If a claim stopped being true, say so.

## What breaks this step

- **Researching the stable layer.** Spending the budget re-deriving concepts you
  already know, and arriving at the volatile claims with nothing left.
- **Citing the search result.** The snippet said 1.2; the page says 2.0.
- **One source, many claims, no reading.** A single primary page cited under
  eight `supports` lines you never checked against its text.
- **Dateless entries.** A ledger without dates is indistinguishable from no
  ledger the moment the field moves.
