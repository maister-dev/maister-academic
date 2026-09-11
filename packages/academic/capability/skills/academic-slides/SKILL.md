---
name: academic-slides
description: Use when producing or revising a lesson's slide deck from an existing lecture document.
license: MIT
metadata:
  version: "0.1.0"
  domain: course-authoring
---

# Build the deck

The deck is not the lecture with smaller margins. The lecture carries the
argument; the deck carries the room's attention through it. Anything a student
must be able to re-read belongs in the lecture, and putting it on a slide
instead is how lectures end up unreadable and slides end up unwatchable.

## The file you own

You write **the slide deck** and nothing else in the lesson directory.

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

The lecture document, and `course.yaml` for `slides.format`, `slides.theme`,
language, and `lesson.rhythm`. The deck is **derived**: it may compress, order,
and illustrate, but it introduces no claim the lecture does not make. A claim
that belongs on a slide and not in the lecture is a defect in the lecture.

## Size

`slides.perMinute` slides per minute of `lesson.rhythm.theory` — one per minute
by default — plus a section divider per major move and one closing slide. A
deck at double that will be rushed in the room, and the material that gets
rushed is always the end. Take both numbers from `course.yaml`; do not assume a
slot length.

## Marp mechanics

When `slides.format` is `marp`, the file opens with Marp frontmatter and
separates slides with `---` on its own line:

```markdown
---
marp: true
theme: default
paginate: true
lang: ru
---

# Lesson 8 — Agent-assisted debugging

Module 2 · Agentic SDLC

<!-- Speaker note: open on the failed run from last week. -->

---

## One claim per slide

- at most six lines
- fragments, not sentences
- no paragraph ever

<!-- Speaker note: this is where the demo hooks in. -->
```

- **Speaker notes are HTML comments.** Marp exports them as presenter notes.
  Every content slide gets one: the sentence the instructor says while the slide
  is up. This is the part that makes the deck runnable by a colleague.
- **No Mermaid.** Marp core does not render Mermaid; a fenced diagram ships as
  a code block on the slide. Diagrams belong in the lecture. If the room needs
  one, render it to an image under the lesson's assets directory and reference
  the file.
- **Images are relative** to the deck file so the repository stays portable.

When `slides.format` is `plain`, drop the Marp frontmatter and the `---`
separators, keep every other rule, and use `##` per slide-equivalent section.

## Rules

**One claim per slide.** The title states the claim. The body supports it. If
the title is a noun phrase — "Agent loop" — the slide has no claim and will be
narrated instead of read.

**The budget is checked by a machine.** The node will not finish until
`scripts/slide-density.py` passes: it counts every slide body, speaker notes
excluded, and fails the deck when the average exceeds
`slides.maxWordsPerSlide` or any single slide runs past double it. Run it
yourself before you finish — `python3 .claude/skills/academic-slides/scripts/slide-density.py`
from the repository root — rather than discovering the refusal at the gate.

**Six lines AND a word budget.** At most six lines, and at most
`slides.maxWordsPerSlide` words in the body — 25 by default, speaker notes
excluded. The line limit alone does not hold: measured on a real deck, 53
slides out of 53 obeyed it while averaging 41 words each, because six
sentence-length lines pass a line count and are still a wall of text. A slide
the audience reads is a slide during which nobody is listening.

**No wall of code.** Show the three lines that matter. The full listing lives in
the lecture or the repository.

**Failure modes get their own slides.** They are the part the room remembers,
and folding them into a bullet under the happy path loses them.

**Section dividers.** One before each major move, so a student who looks up
knows where the argument is.

## What breaks this step

- **The lecture, pasted.** Paragraphs on slides.
- **Titles that are labels.** "Context engineering" instead of "Context is
  engineered, not prompted".
- **Decks with no notes.** Only the author can run them, and only this month.
- **New claims.** Something appears on a slide that the lecture never argued and
  no ledger entry supports.
