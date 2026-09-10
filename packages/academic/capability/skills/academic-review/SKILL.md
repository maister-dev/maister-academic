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
against the ledger text, not against your own knowledge. A claim you believe to
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

**8. Terminology — ADVISORY, BLOCKING when it confuses.** Terms are introduced
once and used consistently. Alternating between a translated term and its
original across a lesson is blocking when a student could take them for two
different things.

**9. Failure modes — BLOCKING when absent.** A lecture that recommends a
technique and never says where it breaks is advocacy, not engineering.

**10. Frontmatter — ADVISORY.** `status`, `sources_verified`, and `outcomes`
present and consistent with what the files actually contain.

## Judgement

- Any BLOCKING defect → `revise`.
- Only advisory findings, or none → `publish`. Advisory findings still go into
  `review_comments`; the instructor sees them at the review gate.

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
