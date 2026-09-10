---
name: academic-homework
description: Use when writing or revising a lesson's homework assignment and the rubric it will be graded by.
license: MIT
metadata:
  version: "0.1.0"
  domain: course-authoring
---

# Write the homework

Homework is where the lesson is actually learned and the only place the
instructor sees whether it was. Two things decide whether it works: the size of
the deliverable, and whether the rubric can be applied by someone who was not
there.

## Inputs

The brief (**Practice shape** and its constraints), the lab — homework extends
it, never repeats it — and `course.yaml` for `lesson.homeworkHours`.

## Size

The deliverable must fit `homeworkHours`, for a student of median speed, on
their own machine, including the write-up. Estimate honestly and cut. An
assignment that overruns gets finished badly by the diligent and abandoned by
everyone else, and both outcomes destroy the signal it was meant to produce.

## Shape

```markdown
# Homework — Lesson N

**Effort:** 2–4 hours · **Deliverable:** …

## Task
What to do, in the imperative. Two or three sentences.

## Deliverable
Exactly what gets submitted: files, format, where.

## Constraints
Budget, tooling, time — whatever the brief records.

## Rubric
| Criterion | Weight | Evidence in the submission |
| --------- | ------ | -------------------------- |

## Not graded
What deliberately carries no marks.
```

## The rubric is the hard part

**Every criterion is observable from the submission alone.** "Understands the
material" is not gradeable. "The report names the hypothesis that was rejected
and the evidence that rejected it" is. Write the *evidence* column first — if
you cannot name where in the submission the criterion is visible, the criterion
is not real.

**Grade decisions, not volume.** Length, number of commits, number of runs, and
size of diff all reward the wrong behaviour and are trivially inflated. Grade
what was decided and why.

**Project-agnostic criteria.** When students work on their own projects the
rubric cannot assume a stack, a size, or a domain. Phrase criteria against the
student's own baseline: "the harness catches a defect that the pre-existing
suite missed" holds on any codebase, and is checkable.

**State what is not graded.** It steers effort more effectively than the rubric
does, and it protects students from optimising for something the course does not
value.

**Weights sum to 100.** Three to six criteria. More than six cannot be applied
consistently across thirty submissions.

## Rules

**Extend the lab, do not repeat it.** The lab shows the mechanism under
supervision; the homework applies it where nobody is watching, at a size the lab
could not reach.

**One deliverable.** Multiple artifacts multiply the ways to submit incompletely
and the ways to grade inconsistently.

**Say what an incomplete attempt should look like.** A student who could not
finish should still submit something gradeable — what they tried, where it
broke. Otherwise you get nothing and learn nothing.

## What breaks this step

- **The essay.** "Describe the role of X" is unmeasurable and answerable by
  anyone with a browser.
- **Effort criteria.** Rewarding hours, words, or commits.
- **A rubric written after the task.** It ends up describing the ideal answer
  rather than the observable distinctions, and it cannot separate a good
  submission from a long one.
- **Overrun.** Four hours planned is six hours in practice. Cut before shipping.
