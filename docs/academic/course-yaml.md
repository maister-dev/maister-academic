# `course.yaml` — the course repository's contract

The `academic` package hardcodes nothing about how a course is laid out. A
consuming course repository declares its own conventions in a `course.yaml` at
its root, and the flow reads them.

This split is deliberate: the package owns the **process** of authoring a
lesson, the course repository owns **what that course is**. A package that knew
your directory names would be a package only your course could use.

## Bootstrapping

If `course.yaml` is missing, the flow's first node creates one from the template
in the `academic-course-map` skill, filling values from what the repository
actually shows, and records every guess under **Assumptions** in the lesson
brief. The instructor confirms or corrects them at the review gate.

Pre-creating the file is better: it costs a minute and removes a round of
guessing from the first run.

## Reference

```yaml
schemaVersion: 1

course:
  title: "Agentic Software Engineering"
  language: ru
  terminology: en

layout:
  lessons: weeks
  lessonDir: "{number}-{slug}"
  numberWidth: 2
  syllabus: SYLLABUS.md
  outcomes: curriculum/outcomes.yaml
  assets: assets

artifacts:
  brief: brief.md
  lecture: lecture.md
  slides: slides.md
  lab: lab.md
  homework: homework.md
  sources: sources.yaml

lesson:
  durationMinutes: 90
  rhythm:
    theory: 20
    demo: 20
    lab: 40
    debrief: 10
  homeworkHours: [2, 4]

slides:
  format: marp
  theme: default

sources:
  maxAgeDays: 180
  requireAccessDate: true
```

### `course`

| key           | meaning                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------- |
| `title`       | Course title, used in generated frontmatter and deck headers.                              |
| `language`    | The language materials are **written in**.                                                 |
| `terminology` | The language technical terms stay in, when it differs. Omit when terms follow the prose.   |

### `layout`

| key           | meaning                                                                                     |
| ------------- | -------------------------------------------------------------------------------------------- |
| `lessons`     | Directory holding the lessons.                                                                |
| `lessonDir`   | Lesson directory name. `{number}` is zero-padded to `numberWidth`; `{slug}` is the lesson slug. **Only `{number}` identifies a lesson** — see below. |
| `numberWidth` | Zero-padding width for `{number}`.                                                            |
| `syllabus`    | The programme — the source of truth for what each lesson covers and what the course excludes. |
| `outcomes`    | Optional learning-outcome register. Drives the coverage check in review.                      |
| `assets`      | Optional per-lesson subdirectory for images and rendered diagrams.                            |

### The slug does not identify a lesson

`{slug}` is a human-readable label, and nothing derives it deterministically —
two agents given the same syllabus title will reasonably produce `03-evals` and
`03-agent-evals`. Measured, not hypothetical: one run in four diverged in
testing.

So the lesson **number** is the identity. Every flow resolves a lesson's
directory by matching `{number}` against what is already on disk, and mints a
slug only when no directory carries that number. Without that order a refresh
creates a second directory instead of updating the first — a run that passes
every gate and leaves the instructor with two copies of one lesson.

Pinning the slug in the syllabus (a `03-evals` heading anchor, or a per-lesson
front-matter key) removes the guess entirely. It is not required.

### `language`, `density`, budgets

Three keys carry the lessons of the first real run, and all three exist because
a value that lives in a skill outlives the schedule it was written for.

`course.language` splits into `prose`, `terminology` and `headings`. With a
single language key and English section names in the package templates, an
agent satisfies both instructions at once and produces a document with half its
headings in each language — measured twice on one run. Many Russian technical
courses also keep structural words in English deliberately; that should be the
course's decision, not a template's side effect.

`lesson.density` derives text budgets from minutes: `theory`, `demo` and `lab`
words per minute of the matching `rhythm` entry, with `lesson.tolerance` as the
accepted drift and `lesson.briefMaxWords` capping the one document every later
step reads. The package ships defaults measured on real output — 40 / 20 / 12 —
so a course that agrees writes nothing. The previous design stated a word count
inside the lecture skill, written for a 20-minute theory slot, and it silently
survived the move to a 60-minute one.

`slides.maxWordsPerSlide` bounds a slide BODY, speaker notes excluded. A line
limit alone does not hold: 53 slides out of 53 obeyed a six-line rule while
averaging 41 words, because six sentence-length lines pass a line count and are
still a wall of text.

### `artifacts`

Filenames inside one lesson directory. **Dropping an entry disables that
artifact** — a course with no in-class block removes `lab`.

The `sources` ledger is the one entry that should not be dropped: the didactic
review's traceability check runs against it, and the flow's instructor gate
blocks on it. Without it the course keeps working and quietly stops being
maintainable.

### `lesson`

`rhythm` calibrates three things: how long the lecture's theory section may run,
how many slides the deck gets, and how much the lab may contain.
`homeworkHours` sizes the homework and is the number the rubric is written
against.

### `slides`

`format: marp` produces a Markdown deck with Marp frontmatter and `---`
separators, renderable to HTML or PDF by the Marp CLI. `format: plain` produces
structured Markdown with no deck tooling, and every other slide rule still
applies.

### `sources`

`maxAgeDays` defines staleness: on a refresh run, older entries are re-opened
and re-dated, and the review escalates a stale entry to blocking when the claim
it supports is one that moves.

## The lesson directory

With the reference values above, lesson 8 lives at:

```
weeks/08-agent-assisted-debugging/
├── brief.md        # scope, out-of-scope, already-established, assumptions
├── lecture.md      # theory, worked case, instructor demo script
├── slides.md       # Marp deck
├── lab.md          # in-class exercise
├── homework.md     # assignment + rubric
└── sources.yaml    # dated source ledger
```

## The source ledger

```yaml
schemaVersion: 1
verified: 2026-09-10
sources:
  - id: mcp-spec
    title: "Model Context Protocol — specification"
    url: https://modelcontextprotocol.io/specification
    kind: primary # primary | secondary | community
    publisher: "Anthropic"
    version: "2025-06-18"
    accessed: 2026-09-10
    supports:
      - "MCP servers expose three primitives: tools, resources, prompts"
    notes: "Section 'Server features' is the load-bearing part for this lesson."
open_questions:
  - "Whether A2A message framing is stable enough to teach beyond concept level."
```

`supports` is what makes the ledger work: it lists the claims the source backs,
phrased as the lecture phrases them. An entry with no `supports` is a bookmark.
Every volatile claim in the lesson must appear in exactly one `supports` list —
that binding is what the review checks and what lets a refresh six months later
find the passages that went stale.
