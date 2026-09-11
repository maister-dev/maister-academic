---
name: academic-lecture
description: Use when writing or revising the lecture notes of a lesson in a course repository, once the lesson brief and the source ledger exist.
license: MIT
metadata:
  version: "0.1.0"
  domain: course-authoring
---

# Write the lecture

The lecture document serves two readers and must not be optimised for one at the
cost of the other:

- the **instructor**, who reads it before class and needs the argument, the
  case, and the demo choreography;
- the **student**, who reads it after class and needs the model to survive
  without the room.

Write for the second reader. Add what the first one needs as its own sections.

## The file you own

You write **the lecture document** and nothing else in the lesson directory.

This is not tidiness. Every other document has its own step with its own skill
materialized; a document written here is written without those rules and gets
overwritten later, so the work is discarded and the tokens are spent twice.
Measured on a real run: the research step, given a brief that described the
whole lesson, wrote the lecture, the deck, the lab and the homework, and
rewrote the brief — none of it under the skill that governs those documents,
all of it replaced by the steps that own them.

If something outside your file looks wrong, say so in your report. Do not fix
it here.

## Inputs

The lesson brief (scope, out-of-scope, already-established, owed-to-next) and
the source ledger. Both are binding. The brief's **Already established** list
is the sharpest constraint in this skill: an audience that has been taught
something and is taught it again learns that the course does not track itself.

Language and rhythm come from `course.yaml`. If `lesson.rhythm.theory` is 20
minutes, the theory has to be deliverable in 20 minutes — not summarisable in
20 minutes.

## Shape

```markdown
---
lesson: 8
title: "..."
status: draft            # draft | reviewed | published
sources_verified: 2026-09-10
outcomes: [LO-06, LO-08]
---

# Lesson 8 — Title

## Why this lesson
The problem the students already have, stated so they recognise it. Two or
three sentences. Not a summary of what follows.

## The model
The one idea the lesson installs. Named, bounded, and distinguished from the
neighbouring idea it is most often confused with.

## How it works
The mechanism. Enough that a student can predict behaviour rather than recall
a slogan.

## Where it fails
Failure modes, named and separated. This section is what makes the lesson
engineering rather than advocacy, and it is the one most often left thin.

## Worked case
One case, followed to the end, including the part that went wrong. One case
carried through beats three sketched.

## Demo (instructor)
The choreography for the live demonstration: numbered steps, what each step is
supposed to prove, and what to say when it fails live. Written so a colleague
could run it.

## What we are not covering
The adjacent thing students will ask about, and where it actually lives.

## Sources
Links from the ledger, with the access date.
```

## Rules

**No claim without a ledger entry.** Every volatile assertion — a version, a
default, a limit, who shipped what — must be covered by a `supports` line in
`sources.yaml`. If the research did not establish it, write it as an open
question in the text. Never soften an unverified claim into a vague one; vague
claims survive review and mislead students.

**Do not re-teach the foundation.** The brief lists what the audience already
has. Reference it in one clause and move on.

**Name the failure modes.** For anything the lesson recommends, state where it
breaks. A lesson that only shows a technique working teaches students to be
surprised in production.

**Prefer the mechanism to the taxonomy.** A list of five categories is easy to
write and nearly worthless. Explain how one thing works and the categories
become derivable.

**Compute the length, do not recall it.** The budget is
`lesson.rhythm.theory x lesson.density.theory` words for everything except the
worked case and the demo, and `rhythm.demo x density.demo` for the demo
section, both from `course.yaml`; `lesson.tolerance` is how far either may
drift. A 60-minute theory block at the default density is about 2400 words.

Never carry a word count in your head: this rule used to name one, written for
a 20-minute slot, and it silently outlived the schedule it was written for when
the course moved to 60-minute theory. Overrun does not get compressed in the
room — it gets truncated, and the last section is always the one you cared
about.

**Terminology.** Use the course language for prose and keep technical terms in
the terminology language from `course.yaml`. Introduce each term once with both
forms, then stay consistent. Silently alternating between a translated term and
its original is the single most common defect in bilingual course material.

## What breaks this step

- **Restating the syllabus.** The syllabus lists topics. The lecture makes an
  argument. If your section headings are the syllabus bullets, start over.
- **Front-loading definitions.** Six paragraphs of taxonomy before anything is
  at stake loses the room before the material starts.
- **A demo nobody can run.** "Show the agent working" is not choreography.
  Steps, expected observable, recovery when it fails live.
- **Padding to length.** A short lecture that lands beats a long one that
  wanders. Cut to the argument.
