# Agent usage incident and correction

## Observed evidence

Three resumed Marvel worker logs recorded 645, 636 and 390 token-usage events
at the audit snapshot. Median input per event was 138,481, 141,551 and 158,817
tokens; median output was 192, 185 and 229. Recorded model contexts named
gpt-6-astra. Their initial calls already contained roughly 141k input tokens.
The dispatches inherited the parent history and assigned whole-product completion
without a spending checkpoint. Workers subsequently coordinated and expanded
required implementation work over many calls while the lead was not supervising.

Earlier counter snapshots showed about 236M processed tokens, roughly 232M cached
input and 0.51M output. These are approximate snapshots, not unique text or a
billing conversion. Account-wide weekly usage rose from 4% to 37% over roughly
132 minutes; another project was active, so attribution of all 33 points to these
workers would be unsupported. Usage events are not asserted to be a deduplicated
provider-request ledger. No hard per-worker budget mechanism was exposed.

## Root cause and remediation

The lead optimized for continued progress without bounding aggregate execution.
Full-history inheritance supplied a large initial context; long-lived workers
repeatedly processed it, and small responses did not constrain input consumption.
Premium-model inheritance and lack of renewal/stop ownership compounded the risk.
The task's correctness requirements do not justify this orchestration pattern.

All three workers were interrupted. Five worktrees were recorded with exact
revisions; staged and unstaged binary diffs and untracked files were archived
outside the repositories. No worker was restarted to summarize itself.

The global skill now requires fresh concise handoffs, bounded work packets,
explicit model consideration, aggregate limits, and lead-owned renewal. Global
AGENTS guidance routes future delegation through that policy. Limits are expressly
soft unless the execution tool enforces them. Correctness and whole-product
acceptance remain unchanged; incomplete work is reported as incomplete.

## Evaluation and limits

Actual incident response exercised the spending-control case: interruption before
analysis, external preservation of dirty work, metadata-only usage inspection,
and no new review agents. This is direct observed behavior, not an independent
forward test of the revised skill.

Manual walkthrough of the remaining three cases yields: one fresh-context packet
for the large assignment; saved diffs/process ID with pending tests at the limit;
and pending review rather than budget evasion. These are hypothetical walkthroughs,
not measured runtime enforcement. Structural validation checks links/metadata only.
No additional agents are launched for evaluation during this spending incident.

A future authorized bounded packet should measure actual initial context, usage
delta and stop behavior before any renewed parallel operation. No savings or hard
spending guarantee is claimed in advance of that measurement.
