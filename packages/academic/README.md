# Academic package

Course-content authoring for MAIster: a flow that fills or refreshes one
lesson of a course repository, a flow that applies one minor change to a written
lesson without letting its invariants slip, and the eight skills that carry the
craft.

Full reference:
[`docs/academic/README.md`](../../docs/academic/README.md).
The contract every consuming course repository implements:
[`docs/academic/course-yaml.md`](../../docs/academic/course-yaml.md).

## Contents

```
maister-package.yaml         # package manifest
flows/lesson/flow.yaml       # academic-lesson — 11 nodes
flows/lesson-edit/flow.yaml  # academic-lesson-edit — 4 nodes
schemas/
  lesson-intake.json         # form node: mode, research_depth
  lesson-review.json         # judge result: recommendation, review_comments (both flows)
capability/skills/
  academic-course-map/       # + templates/course.yaml
  academic-research/         # + references/source-quality.md
  academic-lecture/          # + templates/lecture.md
  academic-slides/           # + templates/slides.md
  academic-lab/              # + templates/lab.md
  academic-homework/         # + templates/homework.md
  academic-review/           # + references/checklist.md
  academic-edit/
```

## Design boundary

The package owns the process of authoring a lesson. The course repository owns
what the course is — its lessons, layout, filenames, language, and rhythm — and
declares them in a `course.yaml` at its root. Nothing here hardcodes a path.

## Compatibility

MAIster engine **≥ 3.0.0**: graph-only `nodes[]` (3.0.0), typed artifacts
(1.2.0), `output.result` (1.3.0), `decide` routing (1.7.0), first-class sessions
(2.0.0), `onExhaustion` / `resetTargets` (2.1.0).

One runner profile, `claude-code` — the `claude` adapter on `claude-opus-5`, no
provider pinned. Overridable at launch and by project or platform bindings.

## Version

Pinned by git tag `academic/vX.Y.Z`. This file carries no version field.
