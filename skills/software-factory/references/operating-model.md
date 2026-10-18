# Operating guidance

## Direction and decision rights

The owner sets the product outcome, constraints and acceptance expectations.
The delivery lead selects and sequences work within them. Implementers choose
routine technical details under repository guidance. Reviewers challenge evidence;
they do not silently expand the product scope. The integrator owns the combined
candidate. One agent may perform these responsibilities sequentially.

Current user instructions and environment permissions take precedence. Preserve
standing authorization; do not repeatedly ask permission already given. Material
scope changes and irreversible actions without authorization return to the owner.
Prepare a concrete reviewable result before requesting its final approval.
Never imply that delegating a task grants additional permissions.

## Objective and flow

Keep a brief objective: user outcome, observable acceptance, exclusions, present
constraint, next delivery and conditions for changing course. Prefer the existing
tracker. A repository pointer can identify the tracker record without copying it.

One integrated delivery is the default work-in-progress limit. Split it into
reviewable changes with explicit dependencies. Parallelize only independent work
whose interfaces and ownership are understood; read project collision guidance.
Use isolated worktrees when needed. The lead reviews integration capacity before
starting more work. Never merge another worker's partial filesystem changes by
blindly staging everything.

## Handling discoveries

Classify a discovery immediately:

- Required now: it blocks the current acceptance criteria.
- Small adjacent fix: low-risk, local, and cheaper to fix than carry; explain scope.
- Bounded investigation: its answer could materially change the plan.
- Later: record its consequence and return to the objective.

For a material diversion state: consequence for the outcome, displaced work,
recommendation, and evidence. Do not turn every finding into an issue or redesign.
Timebox investigations, not correctness. If the question remains open at the bound,
report what is known and choose a smaller reversible step or request the missing
decision. Do not convert elapsed time into approval.

## Evidence

Separate rule/requirement correctness, reproducibility, regression detection,
interaction usability and owner acceptance. One does not establish the others.
Derive expected behavior from the real authority before copying current outputs.
Record product choices where no authority decides. Never hide a supported-behavior
failure behind a weaker assertion, skip, fallback or silently changed baseline.

Use focused tests for decisions, invalid inputs and meaningful boundaries. Use
integration and real interaction checks where layers meet. Follow required project
gates; do not prescribe full-system tests for every prose change. For important
new decisions, use a distinguishing negative control or mutation when supported.
Record exact revisions and command results; distinguish partial runs from a final
combined run. A reviewer receives raw requirements and evidence, not a suggested
verdict. If independent review is unavailable, explicitly label self-review.

## Delivery and learning

Track implemented, verified, released and accepted as separate facts. Report gaps
without claiming the objective is complete. Publishing and merging follow the
user's authorization and repository rules. A preview build can be ready for owner
review while acceptance remains pending.

Measure elapsed time to reviewable/accepted behavior, waiting, review cycles,
escaped defects and check duration when those observations are available. Do not
rank productivity by commits, lines, test counts or agent utilization. After a
delivery, change at most the process elements supported by observed friction.
The factory is itself bounded software: avoid speculative orchestration services.
