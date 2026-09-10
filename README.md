# maister-academic

Package source repository for [MAIster](https://github.com/maister-dev/maister):
packages that turn a course into a git-backed, reviewable, maintainable
repository — one run fills or refreshes one lesson.

The packages here own the **process** of authoring course material. The
**structure** of any particular course — its lessons, its directory layout, its
filenames, its language — stays with that course's own repository and reaches
the flows through a `course.yaml` at its root.

## Layout

```
packages/
  <name>/
    maister-package.yaml     # package manifest (flows, capability bundles, mcps)
    flows/<flow-id>/flow.yaml
    capability/…             # skills/ + agents/ bundles
    schemas/…                # form + result schemas, materialized into each flow
    README.md                # provenance + package-specific notes
```

| Package | Contents |
| ------- | -------- |
| [`academic`](packages/academic/) | Course-content authoring: 2 flows (`academic-lesson` fills or refreshes a lesson; `academic-lesson-edit` applies one minor change under the same invariants) + 8 skills covering the course map, web research with a dated source ledger, lecture notes, Marp slides, in-class lab, homework with rubric, targeted edits, and didactic review. |

## Documentation

- [`docs/academic/`](docs/academic/) — package reference and the `course.yaml`
  contract every consuming course repository implements.

## Versioning

Per-package git tags: **`<name>/vX.Y.Z`** (e.g. `academic/v0.1.0`). The tag is
the user-facing pin; MAIster resolves it to a commit SHA at install time and the
SHA is runtime truth. A release tags only its own package — packages version
independently.

## Consuming from MAIster

One `packages[]` entry in the consuming project's `maister.yaml`:

```yaml
packages:
  - id: academic
    source: https://github.com/maister-dev/maister-academic
    version: academic/v0.1.0
    path: packages/academic
```

Or add this repository as a package source in `/settings` and install/attach it
from the UI.

## Releasing a package

Tag through the release wrapper, so the compatibility gate runs against the
exact clean checkout before the tag exists:

```sh
MAISTER_REPO=/path/to/mAIster ./scripts/release-package.sh academic v0.1.0
```

The gate validates the package manifest, every graph-only `nodes[]` manifest,
the engine range, and package-root schema materialization.

## License

MIT — see [LICENSE](LICENSE).
