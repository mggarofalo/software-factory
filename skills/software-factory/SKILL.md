---
name: software-factory
description: Plan and execute a software delivery around an explicit user outcome, bounded work, review and acceptance evidence. Use when coordinating a feature, resuming project work, or improving delivery flow; keep routine small fixes proportionate.
---

# Software Factory

Read the project's instructions and current objective before selecting work.
Use the existing tracker and authorized scope; installation does not authorize
external mutations or background work. For a small well-specified fix, proceed
directly with focused implementation and verification rather than creating a plan.

For a substantial delivery, read [operating guidance](references/operating-model.md)
and act as [delivery lead](roles/delivery-lead.md). Load only the operation and
role needed next:

| Situation | Operation |
|---|---|
| Outcome is unclear or new | [Frame](operations/frame.md) |
| Implementation or evidence is uncertain | [Assess](operations/assess.md) |
| Choose and sequence the next delivery | [Plan](operations/plan.md) |
| A specific unknown blocks that delivery | [Investigate](operations/investigate.md) |
| A bounded capability is ready | [Implement](operations/implement.md) |
| Challenge the candidate independently | [Review](operations/review.md) |
| Integrate, verify and prepare acceptance | [Deliver](operations/deliver.md) |
| A delivery finished or repeated friction appeared | [Improve](operations/improve.md) |

Keep one current objective and one integrated delivery in progress by default.
Parallel work is an option only when authorized, independent and reviewable;
it is never a prerequisite. Use the [handoff template](templates/handoff.md).
Before delegating or renewing a worker, apply [bounded agent execution](references/bounded-agents.md).

At a session boundary, record the exact revision, evidence, unresolved work and
next executable action in the authoritative record. Do not mark work accepted
because implementation or automated checks are complete. Resume from that record
without repeating completed research. See [runtime adapters](references/adapters.md)
for installation and delegation conventions.
