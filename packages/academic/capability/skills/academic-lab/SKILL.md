---
name: academic-lab
description: Use when writing or revising the in-class practical block of a lesson — a timeboxed exercise students run on machines the instructor does not control.
license: MIT
metadata:
  version: "0.1.0"
  domain: course-authoring
---

# Write the in-class lab

The lab runs once, in a fixed slot, on hardware you have never seen, with an
instructor who cannot help thirty people at the same time. Every rule here comes
from that.

## The file you own

You write **the in-class lab document** and nothing else in the lesson directory.

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

The brief (especially **Practice shape** — whether students work on their own
project, a shared sandbox, or a fixed exercise, and what constrains them), the
lecture, and `course.yaml` for `lesson.rhythm.lab` and `lesson.rhythm.debrief`.

## Budget

The lab section must fit `rhythm.lab` minutes **including setup and stumbles**.
Plan for about 70% of the nominal slot: the rest goes to the machine that will
not install, the account that is not activated, and the question that has to be
answered out loud. A lab planned to fill the whole slot never finishes, and the
part that gets cut is the debrief — the part where the learning actually lands.

## Shape

```markdown
# Lab — Lesson N

## Goal
What the student will have observed by the end. Observed, not "understood".

## Before class
Everything that must be installed, cloned, or authorised beforehand, with the
one command that proves it worked. Anything here that fails in the room costs
the whole group.

## Steps
1. Action → **you should see:** the observable.
2. ...

## Checkpoint (minute N)
The state everyone should be in. The instructor calls this out loud.

## If you fall behind
The shortest path back to the checkpoint — a prepared branch, a fixture, a
copy-paste block. Never "ask the instructor".

## Debrief
Three questions that only someone who ran the lab can answer.
```

## Rules

**Every step has an observable.** "Run the agent" is not a step; "run the agent
and watch which files it reads first — you should see it open the test file
before the source" is. A step without an observable can fail silently, and a
silently failing lab teaches the wrong lesson confidently.

**One mid-lab checkpoint.** It lets the instructor re-synchronise the room and
lets a lost student know they are lost while there is still time.

**A catch-up path that needs nobody.** A prepared branch, a fixture directory, a
block to paste. Without it the slowest third of the room drops out of the lab
and does not come back.

**Project-agnostic when the brief says so.** If students bring their own
projects, the lab cannot name a file, a function, or a framework. Write the
steps against properties instead: "pick a module with at least one failing
test", "point the agent at the component you understand least". State the
precondition the student's project must meet, so a student whose project cannot
support the lab finds out before class, not during it.

**Honour the constraints.** If the brief records a budget, an offline
requirement, or a free-tier limit, the lab has to run inside it — including a
low-cost variant when the constraint is a spend cap.

**The debrief is not a summary.** Three questions answerable only by someone who
ran it: what surprised you, where did it go wrong, what would you change.

## What breaks this step

- **A lab that is a tutorial.** Twenty steps with no decision. Nothing is
  learned by transcription.
- **Setup inside the lab.** Installation belongs to "Before class". Setup in the
  room eats the whole slot.
- **No failure path.** Real exercises fail for a third of the room. Plan the
  return.
- **Silent success criteria.** If the student cannot tell whether it worked, it
  did not.
