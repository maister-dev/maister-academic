# `academic` — package reference

Course-content authoring for a git-backed course repository. One run fills or
refreshes **one lesson**: it surveys what the repository already has, researches
the topic against live sources, writes the lecture, the deck, the in-class lab
and the homework, puts them through a didactic judge, and hands the instructor
something worth reviewing.

## Why a flow

Two properties of course material justify the machinery, and neither is about
saving typing.

**Traceability.** A course about a fast-moving field goes wrong silently. A
version, a default, a capability changes; the lecture keeps asserting the old
thing; nobody notices until a student does. The flow's answer is the source
ledger: every volatile claim is bound to a source that was opened on a recorded
date, the judge checks the binding, and the instructor gate blocks without it.

**Repeatability.** Sixteen lessons authored ad hoc drift in depth, in
terminology, and in how homework is graded. The same graph over every lesson
produces material that reads as one course.

## The flow — `academic-lesson`

```
intake ─▶ survey ─▶ research ─▶ lecture ─▶ slides ─▶ lab ─▶ homework ─▶ didactics
                                                                          │
                                              revise ◀── revise ──────────┤
                                                 │                        │
                                                 └──▶ didactics    publish│
                                                                          ▼
                                                        commit ◀── review (human)
```

| node | type | what it does |
| ---- | ---- | ------------ |
| `intake` | form | Two knobs: `mode` (`create` \| `refresh`) and `research_depth` (`quick` \| `standard` \| `deep`). Everything else is `course.yaml`. |
| `survey` | ai_coding | Reads `course.yaml` (creating it if absent), resolves the lesson against the syllabus, inventories what exists, reads the neighbouring lessons, and writes the brief. |
| `research` | ai_coding | Researches the volatile layer against primary sources and writes the dated ledger. |
| `lecture` | ai_coding | Theory, worked case, and the instructor's demo script. |
| `slides` | ai_coding | Marp deck projecting the lecture. |
| `lab` | ai_coding | Timeboxed in-class exercise with observables, a checkpoint, and a catch-up path. |
| `homework` | ai_coding | Assignment sized to the self-study budget, plus an observable rubric. |
| `didactics` | judge | Ten checks; routes `revise` or `publish` from its own structured output. |
| `revise` | ai_coding | Clears the listed defects and nothing else. |
| `review` | human | The instructor. Blocking artifact gates on the ledger and on the four documents. |
| `commit` | ai_coding | One conventional commit scoped to the lesson. |

### Sessions

`research`, `write` (lecture + slides), `practice` (lab + homework), `judge`,
`revise`, and `commit` are separate first-class sessions. Each starts with a
fresh context and reads its predecessor's work off disk rather than inheriting
it.

The judge is the reason this matters. A reviewer that shares the context which
wrote the lecture reads it charitably — it fills the gaps from memory instead of
noticing them, which is the same reason self-review of code is weak. The rest is
a smaller effect in the same direction: a deck composed inside the lecture's
context mirrors its phrasing instead of compressing it.

The cost is one agent respawn per session boundary. `intake`, `survey` and
`review` stay on the implicit `default` session.

### Runner

`runner_profiles` declares one profile, `claude-code` — the `claude` adapter on
`claude-opus-5`. It names no provider, so the instance's own runner
configuration supplies that.

The profile is the flow's declared intent, not a lock. Resolution still runs
highest-wins: a launch override beats it, and a project or platform binding can
map the slot onto a different registered runner.

### Loops

The judge owns a bounded revise loop, `maxLoops: 3`, each iteration on a fresh
session. Exhaustion routes to the instructor with the standing defects rather
than publishing. The instructor's own rework re-baselines that budget
(`resetTargets`), so new guidance gets a full loop instead of landing
post-exhaustion.

### Gates

`review` cannot complete without a current source ledger, or without all four
documents. Both are blocking `artifact_required` gates. A lesson whose claims
are not traceable does not reach a student.

## The edit flow — `academic-lesson-edit`

Minor edits are how a course actually degrades. Someone corrects a version in
the lecture, the ledger keeps describing the old one, no judge runs, and a
semester later nobody can tell which claims were ever checked. A scratch run
does not catch this — it materializes none of the authoring skills and runs no
judge. So the small change gets its own, small flow:

```
edit ─▶ check ─publish─▶ commit ─▶ done
          │ revise (≤2, fresh session)
          ▼
        edit
          │ exhausted
          ▼
      escalate (human, rework only) ─▶ edit
```

| node | type | what it does |
| ---- | ---- | ------------ |
| `edit` | ai_coding | `academic-edit`: resolves the lesson and passage, classifies the change, applies the smallest diff, and keeps `sources.yaml` consistent with any claim that moved — or refuses the change. |
| `check` | judge | `academic-review` in scoped mode: judges only what the diff touched and the ledger entries it depends on. Scope overrun is itself blocking. |
| `escalate` | human | Reached only through exhaustion; its one decision restarts the loop with a fresh budget. |
| `commit` | ai_coding | One conventional commit naming the change and the ledger action. |

No intake form: the task prompt *is* the request. No research node: a factual
change verifies its own source inside `edit`, or is refused. No instructor node
on the happy path: the promotion review is where the instructor sees the diff,
and a two-node loop does not need a second gate. Only the judge leaves the
default session — the reviewer of an edit must not be the context that made it.

**Which flow.** A lesson that does not exist, or a week whose sources went
stale, is `academic-lesson` (`mode: refresh` for the latter). A change the
prompt can fully describe — "week 3, lab, replace the export example with the
import one" — is `academic-lesson-edit`.

## The skills

| skill | role |
| ----- | ---- |
| `academic-course-map` | Resolve conventions, inventory, read neighbours, write the brief. |
| `academic-research` | Search discipline, source ranking, version pinning, the ledger format. |
| `academic-lecture` | Lecture structure, the no-claim-without-a-source rule, length calibration, terminology. |
| `academic-slides` | Marp mechanics, one claim per slide, speaker notes, deck-vs-lecture fidelity. |
| `academic-lab` | Timeboxing, observables, the checkpoint, the catch-up path, project-agnostic phrasing. |
| `academic-homework` | Sizing, deliverable, and rubric observability. |
| `academic-review` | The ten checks, blocking-vs-advisory calibration, scoped mode for edits, and the routing output. |
| `academic-edit` | Resolve, classify, the ledger rule for factual changes, the smallest diff, and where a change must propagate. |

Each carries its templates or references alongside `SKILL.md`.

## Requirements

- MAIster engine **≥ 3.0.0**.
- A `claude` ACP runner. The flow's `claude-code` profile targets
  `claude-opus-5`; a launch override or a project/platform binding redirects it.
- Web access for the `research` node. It runs on the adapter's own web tools, so
  the package ships no MCP. To route research through a dedicated search
  provider, add a template to `mcps[]` in `maister-package.yaml` and reference
  its id from the `research` node's `settings.mcps`.

## Setting up a course repository

1. Create the repository and register it as a MAIster project.
2. Add the package to its `maister.yaml`:

   ```yaml
   packages:
     - id: academic
       source: https://github.com/maister-dev/maister-academic
       version: academic/v0.1.0
       path: packages/academic
   ```

3. Commit the syllabus at the path `course.yaml` will declare.
4. Write `course.yaml` — see [`course-yaml.md`](course-yaml.md). Optional; the
   first run creates one and flags its guesses.
5. Create a task per lesson and launch `academic-lesson`.
6. For a minor change to a written lesson, create a task whose prompt is the
   request and launch `academic-lesson-edit`.

## Not in scope

- **Designing the curriculum.** The syllabus is an input. A course's structure
  is the instructor's judgement, and it changes rarely enough that a flow would
  cost more than it saves.
- **Rendering.** Decks stay Markdown. Marp CLI, Pandoc, or a static site
  generator are the course repository's business.
- **Grading submissions.** The package writes rubrics; it does not apply them.
