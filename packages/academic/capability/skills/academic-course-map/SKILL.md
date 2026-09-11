---
name: academic-course-map
description: Use when a lesson of a course repository is about to be written or refreshed and its target paths, language, learning outcomes, and what the neighbouring lessons already cover have not been established for this run.
license: MIT
metadata:
  version: "0.1.0"
  domain: course-authoring
---

# Course map — brief one lesson

You are writing into a course repository you did not design. This skill settles
where things go and what the lesson is allowed to say, so every step after it
writes instead of guessing.

## The file you own

You write **the lesson brief (and `course.yaml`, when it is missing)** and nothing else in the lesson directory.

This is not tidiness. Every other document has its own step with its own skill
materialized; a document written here is written without those rules and gets
overwritten later, so the work is discarded and the tokens are spent twice.
Measured on a real run: the research step, given a brief that described the
whole lesson, wrote the lecture, the deck, the lab and the homework, and
rewrote the brief — none of it under the skill that governs those documents,
all of it replaced by the steps that own them.

If something outside your file looks wrong, say so in your report. Do not fix
it here.

## 1. Load the conventions

Read `course.yaml` at the repository root. It is the only source of truth for
paths, filenames, language, and lesson rhythm — nothing in this package
hardcodes them. Contract:
<https://github.com/maister-dev/maister-academic/blob/master/docs/academic/course-yaml.md>

**If `course.yaml` is absent**, the repository has not been set up. Create it
from `templates/course.yaml` in this skill directory, filling values from what
the repository actually shows: an existing lessons directory, an existing
syllabus file, the language the syllabus is written in. Every value you guessed
goes in the brief under **Assumptions** — the instructor review at the end of
this run is where they get confirmed. Never invent a structure that contradicts
files already on disk.

## 2. Resolve the target lesson

The task prompt names the lesson: by number, by title, or both. Match it against
the syllabus declared in `course.yaml`. Resolve to exactly one lesson and record
number, slug, title, and module.

If the prompt matches no lesson, or more than one, stop and say which lessons it
could have meant. A lesson written into the wrong directory costs more to find
than a lesson not written.

**Resolve the directory by NUMBER, in this order — the slug never decides.**

1. A directory under the lessons root whose `{number}` matches the resolved
   lesson number **wins outright**, whatever its slug. Use it. Never create a
   second directory for a lesson that already has one, and never rename an
   existing one as part of writing a lesson.
2. Only when no such directory exists do you mint a slug: kebab-case, from the
   lesson's syllabus title, ASCII, three or four words, stripped of leading
   filler ("agent-assisted-debugging", not "the-agent-assisted-debugging").
   Record it in the brief under **Assumptions** — you invented it.

Two runs asked for the same lesson will mint different slugs from the same
title; that is expected and harmless, because step 1 means only the first run
ever mints one. Skipping step 1 is what turns a refresh into a silent duplicate
that passes every gate and leaves the instructor with two copies.

## 3. Inventory what is already there

Look in the resolved lesson directory. For each artifact declared in
`course.yaml`, record: present or absent, its frontmatter `status`, and its
source-ledger `verified` date. In `refresh` mode this inventory decides what to
rewrite and what to leave alone — a refresh that rewrites accepted material
throws away instructor review.

## 4. Read the neighbours

Read the lecture of the **previous** lesson and the brief or syllabus entry of
the **next** one.

This is the step that carries the most weight and gets skipped most often. It
produces two lists the writing steps treat as binding:

- **Already established** — concepts the students have already been taught.
  Referencing them is right; re-teaching them wastes the lesson's minutes and
  signals to students that the course does not track itself.
- **Owed to the next lesson** — what the next lesson opens by assuming. If this
  lesson does not deliver it, the seam breaks and nobody notices until class.

Also read the syllabus's own exclusion list if it has one (courses for
experienced audiences usually state what they refuse to cover). Those
exclusions are binding too.

## 5. Map the outcomes

If `course.yaml` declares an outcomes file, read it and list the outcome ids
this lesson must advance, with the artifact that carries each one — an outcome
that no lab or homework exercises is an outcome the course only claims.

## 6. Write the brief

Write it to the `brief` artifact path from `course.yaml`, with this shape.

**Stay under `lesson.briefMaxWords`** (600 by default). Every later step reads
this document, so its size is charged to the whole graph rather than to one
file. Measured on a real run, an unbounded brief reached 1899 words and was
carried into five subsequent contexts. Cut research notes and reasoning; keep
decisions.

**Language.** Body text in `course.language.prose`, technical terms in
`course.language.terminology`, section headings in `course.language.headings`.
The headings below are written in English only as placeholders — translate them
into the headings language. Copying them verbatim into a Russian document is
the exact defect this split exists to prevent, and it was measured twice.

```markdown
---
lesson: 8
slug: agent-assisted-debugging
module: "Agentic SDLC"
status: brief
outcomes: [LO-06, LO-08]
---

# Brief — Lesson 8

## Scope
What this lesson teaches, in three sentences.

## Out of scope
What it must not teach, and where that lives instead.

## Already established
Concept — established in lesson N.

## Owed to lesson 9
What lesson 9 opens by assuming.

## Research targets
The volatile claims that must be verified against live sources, as questions.

## Practice shape
What the in-class lab and the homework are anchored to: the students' own
projects, a shared sandbox, or a fixed exercise. Any budget or tooling
constraint that limits them.

## Assumptions
Anything guessed rather than read. Each on its own line.

## Open questions
Anything the instructor must decide.
```

## What breaks this step

- **Trusting the prompt over the syllabus.** The syllabus is the contract with
  the students; the prompt is one request.
- **An empty "Already established" list.** If you produced one, you did not read
  the neighbours — go back.
- **Silent assumptions.** An unrecorded guess about paths or language surfaces
  as a lesson filed in the wrong place, discovered weeks later.
