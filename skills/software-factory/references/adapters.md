# Runtime and project adapters

The portable unit is the whole `software-factory` skill directory. Relative
references must remain inside it. Roles are Markdown prompts that a lead can load
or pass to an available worker; no native agent configuration is assumed.

## Codex

Install into the runtime's skill directory using its skill installer. In the
standard local layout this is `~/.codex/skills/software-factory`. Invoke
`$software-factory`, or let the runtime discover it. Do not edit global runtime
configuration to install these role prompts. If delegation is authorized and
available, supply the chosen role, bounded task, relevant repository instructions,
acceptance criteria, allowed paths and evidence requirements to the worker.

## Other skill-aware tools

Copy the complete directory to the tool's documented skill location. For tools
without skills, load `SKILL.md` and follow its relative links. Native agent wrappers
may point to the role definitions; keep the definitions authoritative and avoid
duplicating their prose. Verify tool-specific installation conventions separately.

## Project integration

Identify the tracker, module/milestone, repository checks, release permissions and
acceptance owner. Store that mapping in existing project guidance or the current
objective. Keep domain rules, platform commands and sensitive configuration out of
the portable package. Use existing credentials without printing them.

On Windows, use the environment's approved shell execution mode. For this package's
local development, use PTY-backed commands and hidden background helpers.
