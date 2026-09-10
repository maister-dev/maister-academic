---
name: academic-edit
description: Use when an instructor asks for one specific, minor change to an already-written lesson — a wording fix, a replaced example, a corrected version or claim — rather than a new or refreshed lesson.
license: MIT
metadata:
  version: "0.1.0"
  domain: course-authoring
---

# Edit a lesson

The request names a lesson and a change. Your job is that change and nothing
around it. The lesson was reviewed and accepted as it stands; every passage you
touch beyond the request spends a reviewer's earlier work and has to be
defended in your report.

## 1. Resolve

Read `course.yaml` at the repository root for paths and filenames. Resolve the
lesson by number, title, or both against the syllabus `course.yaml` declares, to
exactly one lesson — or stop and name the candidates. Then resolve the file and
passage the request names. If the request could mean two passages, stop and say
which two.

Match the directory by lesson **number**, never by slug, and never create or
rename one: an edit acts on a lesson that already exists. If no directory
matches the number, the lesson has not been written — say so and stop, rather
than writing a new one.

A guessed passage is the worst outcome this skill has: the requested change is
still missing, and an accepted passage is now different.

## 2. Classify the change

| kind         | what moved                                              | extra obligation                                   |
| ------------ | ------------------------------------------------------- | -------------------------------------------------- |
| wording      | phrasing, order inside a passage, a heading it names    | none                                               |
| exercise     | a lab step, a homework deliverable, a rubric row        | timebox and observability still hold (academic-lab, academic-homework) |
| factual      | a version, a default, a capability, a limit, a name     | the ledger rule below                              |

Most requests are wording. The factual ones are the reason this flow exists.

## 3. The ledger rule

**A factual change is not done until `sources.yaml` agrees with it.** One of
three things happens, and the report says which:

- the existing entry already supports the new claim — update its `supports`
  line to the new phrasing, and `accessed` if you re-opened the source;
- no entry supports it — open the source now and add or update an entry in the
  format `academic-research` defines, with today's `accessed` date;
- you could not verify it — do not make the change. Say so, with what you
  tried. A refused edit is recoverable; a changed claim over a stale ledger is
  the silent failure this course cannot afford.

Never change a claim and leave the ledger describing the old one. Never delete
the old entry silently: if the claim moved, the ledger should show that it did.

## 4. Apply

The smallest diff that satisfies the request. Do not reflow untouched
paragraphs, rename headings the request did not name, reorder sections,
"improve" nearby text, or bump frontmatter `status`. Update `sources_verified`
only if you re-verified a source.

Follow the change where it propagates, and no further:

- a lecture claim the deck repeats — change the deck too; the deck may not
  assert what the lecture no longer does;
- a lecture passage a lab step or homework criterion builds on — check that
  step or criterion still holds, and change it only if it no longer does.

## 5. Report

End with a short report: files touched; the change in one sentence; the ledger
action (none / updated `<id>` / added `<id>` / refused — why); and anything the
request could be read to include that you deliberately left alone.

## What breaks this step

- **Editing more than asked.** The judge treats scope overrun as a blocking
  defect, and it is right to.
- **Changing the claim but not the ledger.**
- **Guessing the passage.**
- **Fixing the lecture but not the deck**, or the reverse.
