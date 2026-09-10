# Lesson review checklist

Ten checks, with the severity each carries by default.

| # | Check | Default |
| - | ----- | ------- |
| 1 | Every volatile claim has a `supports` entry in the ledger | BLOCKING |
| 2 | No ledger entry past `maxAgeDays`; every entry dated | BLOCKING when the claim moves |
| 3 | Nothing re-teaches an established or excluded topic | BLOCKING |
| 4 | Every assigned outcome is exercised by lab or homework | BLOCKING |
| 5 | Lab fits its slot; observables, checkpoint, catch-up path | BLOCKING |
| 6 | Rubric criteria observable; weights sum to 100 | BLOCKING |
| 7 | Deck contradicts the lecture, or carries an unsupported volatile claim | BLOCKING |
| 7a | Deck merely elaborates beyond the lecture (gloss, example, implied consequence) | ADVISORY |
| 8 | Terminology introduced once, used consistently | ADVISORY |
| 9 | Recommended techniques carry their failure modes | BLOCKING |
| 10 | Frontmatter present and consistent | ADVISORY |

## Sampling

Do not claim check 1 passed without sampling. Pick five claims — two from the
lecture's mechanism section, one from its failure modes, two from the deck —
and find each in a `supports` list. Report which five you checked.

## Calibration

The trap is symmetric.

Too lenient: every lesson publishes on the first pass, the review adds nothing,
and the instructor is the real reviewer — which is the cost this step exists to
avoid.

Too strict: the loop exhausts on rewording, the instructor receives an
escalation instead of a lesson, and the revision budget is spent on prose.

A first draft with two or three blocking defects is normal. A first draft with
twelve means the brief was thin, and that belongs in `review_comments` as its
own finding.

If your blocking list runs past five, re-read it before emitting: severity
inflation is the failure mode this section exists to prevent, and check 7 is
where it starts. Ask of each one whether a student would be misled or the
instructor left undefended. The ones that survive are blocking; the rest are
advisory and still reach the instructor.
