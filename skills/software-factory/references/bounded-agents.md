# Bounded agent execution

Apply when delegation is authorized. Completing a whole product is the acceptance
goal, not an instruction for a worker to run without an execution limit.

## Dispatch

- Default to one active implementation worker. Add concurrency only for independent
  owned paths with review capacity and a stated aggregate budget. A reviewer is a
  separate short assignment, not another permanent worker.
- Start fresh context (`fork_turns="none"` where supported). Supply a concise,
  self-contained handoff: objective, exact revision/worktree, owned paths, relevant
  instruction/authority links, acceptance checks, known findings and stop condition.
  Aim for at most 1,500 words; reference artifacts rather than copying histories.
  Full-history inheritance requires a concrete reason recorded before dispatch.
- Inspect the inherited model/effort. Use the least costly model suitable for the
  work within user/runtime instructions; do not silently inherit premium reasoning
  from an earlier design review. If choice is unavailable, report that limitation
  and constrain work instead of inventing a model override.
- Assign one reviewable result. Do not dispatch "finish all packs", "keep finding
  issues", or unrestricted recursive delegation. Workers cannot reassign themselves,
  spawn successors or renew their own budget.

## Limits and supervision

Use user-specified limits when present. Otherwise use this conservative operating
policy: one worker packet, at most 25 tool invocations or 15 minutes of active
agent work before returning a checkpoint. If per-worker token counters are
available, also stop at 1 million cumulative input tokens, including cached input.
These are soft orchestration thresholds, not claims of a runtime hard cap.
Do not stop a safe running test merely because its elapsed time crosses a limit;
stop further model work, record the process identifier and leave results pending.

The lead owns the aggregate limit, including reviewers and replacement workers.
Do not evade it by repeatedly launching fresh packets. At the limit, report the
result and remaining scope before further delegation; do not automatically renew.
When unattended budget enforcement is unavailable, do not leave open-ended workers
running after the lead yields. Return with them stopped or completed, with work saved.

At a checkpoint, record observed usage, model, elapsed time, exact changes, evidence
and next action. End the worker rather than keeping its growing context alive for
unrelated work. Repeated prompts above 50k input tokens are a signal to checkpoint
and supply a smaller handoff, not to continue hundreds of tiny calls.

## Reduce repeated context work

Batch independent reads and commands. Bound search output, retain full logs on disk,
and return summaries with paths. Use notifications or suitable tool waits instead
of model-driven status polling. Coordinate ownership once; send new findings or
handoffs rather than repeated status requests. Run focused checks during edits and
the required combined gates at the integration boundary; repeat only for changed
code, failures or a concrete unresolved concern. Never omit mandated checks or
declare incomplete work accepted to fit a budget.

## Usage and recovery

Report cached input, uncached input and output separately. Token totals are repeated
processing, not distinct text. Use counter deltas with reset/lineage awareness;
do not sum inherited histories, duplicate events or reasoning already included in
output. Account-wide allowance changes are not attributable to one project when
other sessions are active, and raw tokens are not a billing conversion.

On unexpected spending, interrupt workers first. Preserve committed revisions,
staged/unstaged diffs, untracked files and pending process IDs without resuming
large agents merely to request a summary. Verify worker state. Audit bounded usage
metadata, identify the cause, and repair guidance before restarting. Never claim a
hard token cap unless the execution mechanism actually enforces it.
