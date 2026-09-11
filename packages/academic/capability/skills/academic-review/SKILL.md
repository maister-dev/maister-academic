---
name: academic-review
description: Use when a lesson's documents are complete and must be judged before an instructor sees them, or when a change to a written lesson must be checked against the lesson's source ledger and conventions.
license: MIT
metadata:
  version: "0.1.0"
  domain: course-authoring
---

# Review the lesson

You are the last check before an instructor spends their time. Read the lesson
twice: once as a student who attended nothing, once as an examiner who has to
grade thirty submissions against the rubric. Judge only what is on disk.

Defects are **BLOCKING** or **ADVISORY**. Blocking means a student is misled, a
class cannot run as written, or a submission cannot be graded consistently.
Advisory means it could be better. Do not inflate polish into blocking; do not
excuse a real defect because the rest is good.

## The checks

Run all of them. Each finding names the file and the passage.

**1. Traceability — BLOCKING.** Every volatile claim in the lecture and the deck
— a version, a default, a limit, a capability, who shipped what — is covered by
a `supports` entry in `sources.yaml`. Sample at least five claims and check them
against the ledger text, not against your own knowledge. When
`sources.requireQuote` is on, a `supports` entry without a verbatim `quote` is
itself blocking: the URL may already be dead, and then nothing is left to
re-check the claim against. A claim you believe to
be true but that the ledger does not carry is still a blocking defect: the
course cannot be maintained on your memory.

**2. Staleness — BLOCKING when it bites.** Ledger entries older than
`sources.maxAgeDays`, or entries with no `accessed` date. Blocking when a stale
entry supports a claim about something that moves; advisory when it supports a
stable one.

**3. Re-teaching — BLOCKING.** The brief lists what earlier lessons established
and what the syllabus excludes. Material that re-teaches either wastes the
session's minutes.

**4. Outcome coverage — BLOCKING.** Every outcome the brief assigns is actually
exercised by the lab or the homework, not merely mentioned in the lecture. An
outcome that only appears in prose is an outcome the course claims and does not
deliver.

**5. Lab timeboxing — BLOCKING.** Sum the lab's steps against
`lesson.rhythm.lab`, assuming students are slower than you. Check that setup is
in "Before class", that every step has an observable, that there is a
checkpoint, and that the catch-up path needs no instructor.

**6. Rubric observability — BLOCKING.** Every criterion is checkable from the
submission alone, weights sum to 100, and no criterion rewards volume. Try to
apply the rubric to an imagined mediocre submission: if two graders would
disagree on a criterion, it is not observable.

**7. Deck fidelity.** The deck must not outrun the lecture. Severity depends on
what kind of outrunning it is, and the distinction matters — treating every
extra sentence as blocking buries the two defects that are:

- **BLOCKING** — a deck claim that *contradicts* the lecture, or a *volatile*
  claim (a version, a default, a limit, a capability) that no ledger entry
  supports. Either one puts something in front of students that nothing backs.
- **ADVISORY** — a deck claim that merely elaborates: a gloss on a listed term,
  a consequence the lecture implies, an example. It belongs in the lecture and
  should move there, but it misleads nobody meanwhile. Also advisory: slides
  over six lines, titles that are labels rather than claims, missing speaker
  notes, slide count far off the theory budget.

The question to ask is not "is this sentence in the lecture?" but "would a
student be misled, or would the instructor be unable to defend it?" 

**7a. Text budget — ADVISORY, BLOCKING at double.** Compute each budget from
`course.yaml` — theory prose is `rhythm.theory x density.theory`, the demo
section `rhythm.demo x density.demo`, the lab `rhythm.lab x density.lab`, the
brief `briefMaxWords`, a slide body `slides.maxWordsPerSlide`, the deck
`rhythm.theory x slides.perMinute` slides. Report anything outside
`lesson.tolerance`. Blocking only past double the budget: that is no longer a
drifting document, it is one that cannot be delivered in its slot.

Count slide bodies WITHOUT speaker notes, and check the average rather than the
maximum — measured, a deck kept every slide inside a six-line rule while
averaging 41 words per slide. A line count passing is not the same as a slide
being readable.

**7b. Heading language — BLOCKING when mixed.** Section headings must all be in
`course.language.headings`, body prose in `course.language.prose`, technical
terms in `course.language.terminology`. A document with half its headings in
one language and half in another is the measured failure mode of copying a
template verbatim; it reads as unfinished and it was found twice on one run.

**8. Terminology — ADVISORY, BLOCKING when it confuses.** Terms are introduced
once and used consistently. Alternating between a translated term and its
original across a lesson is blocking when a student could take them for two
different things.

**9. Failure modes — BLOCKING when absent.** A lecture that recommends a
technique and never says where it breaks is advocacy, not engineering.

**10. Frontmatter — ADVISORY.** `status`, `sources_verified`, and `outcomes`
present and consistent with what the files actually contain.

## Judgement

The question is not "how bad is this" but **"can it be fixed without
judgement?"**. A defect nobody has to weigh should never reach the instructor
as homework.

- **Any BLOCKING defect → `revise`.**
- **Advisory findings that are MECHANICAL → `revise`.** Mechanical means the
  correction is determined, not chosen: slides over the word budget, a document
  outside its derived budget, headings in the wrong language, a slide title
  that is a label rather than a claim, missing speaker notes, frontmatter that
  disagrees with the file. There is one right answer and the revision step can
  apply it.
- **Only judgement calls left, or nothing → `publish`.** A judgement call is a
  finding where a competent instructor could reasonably disagree with you:
  whether a worked case is the right one, whether a topic deserves more depth,
  whether an exclusion is correct. Those belong in `review_comments` for the
  instructor to weigh — they are not defects to be silently "fixed".

Reporting a mechanical defect instead of fixing it looks careless: the run had
a revision step available, spent it on nothing, and handed a person work a
machine could have done. The loop is bounded at `maxLoops`, so a stream of
small corrections cannot run away — exhaustion escalates with whatever still
stands.

Nothing is rewritten to satisfy this. The revision step changes only the
passages a finding names; accepted material stays as it was.

Do not recommend `publish` because a revision loop already ran, and do not
recommend `revise` for defects you cannot state concretely. If you cannot name
the file and the passage, you do not have a finding.

## Scoped review

When the prompt asks you to review a CHANGE rather than a lesson — the
`academic-lesson-edit` flow — read the diff first, then judge only:

- the passages the diff touches, under every check above;
- the ledger entries those passages depend on: a changed volatile claim whose
  `supports` line still describes the old claim is BLOCKING (check 1); a
  changed lecture claim the deck still states the old way is BLOCKING (check 7);
- the lab steps and homework criteria that build on a touched passage, where
  the change could break them (checks 5 and 6).

Do not re-open the rest of the lesson. A finding about an untouched passage is
out of scope: at most one ADVISORY line so it is not lost, and never a reason
to recommend `revise`. The scope of the edit is the request itself — a change
that went beyond it is a BLOCKING defect on its own
(`edit exceeded the request: <what changed that was not asked for>`).

## Flow routing output

End the response with exactly one sentinel block:

````
```json maister:output
{
  "recommendation": "revise",
  "review_comments": "BLOCKING lecture.md §'How it works': claims the adapter resumes via a CLI flag; sources.yaml has no entry supporting this and no supports line mentions resume. Verify or cut.\nBLOCKING homework.md rubric row 2: 'demonstrates understanding' is not observable from the submission; restate as the artifact that shows it.\nADVISORY slides.md slide 7: title 'Agent loop' is a label, not a claim."
}
```
````

`review_comments` is what the next revision works from, so each line is one
defect: severity, file, location, what is wrong, and what would clear it.
Prose paragraphs and severity-free lists both produce revisions that miss half
the findings.
