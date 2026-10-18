# Software Factory

Portable agent roles and workflows for delivering accepted software in small, coherent increments.

The unit of progress is a useful capability with evidence. The current objective survives sessions; implementation, review and integration work serve it. This package supplies an operating model, not a background service or permission to publish changes.

## Start

Install the self-contained `skills/software-factory` directory into your agent's skill directory. For Codex:

```sh
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo mggarofalo/software-factory --path skills/software-factory
```

For another runtime, copy that directory into its supported skill location, or load `SKILL.md` directly. The role files are portable prompts, not runtime-specific agent configurations. See [adapters](skills/software-factory/references/adapters.md).

Start a session with: **Use $software-factory to deliver [outcome]. Inspect our current objective and tracker first.**

The workflow can run sequentially with one agent. When delegation is authorized and available, the lead assigns bounded work using the role definitions. It does not require a particular model, tracker, language or hosting provider.

## Contents

- [Entrypoint](skills/software-factory/SKILL.md): choose the next operation without loading the whole package.
- [Operating guidance](skills/software-factory/references/operating-model.md): decision rights, scope, evidence and work in progress.
- [Roles](skills/software-factory/roles/delivery-lead.md): lead, investigator, implementer, reviewer and integrator.
- [Operations](skills/software-factory/operations/frame.md): frame, assess, plan, investigate, implement, review, deliver and improve.
- [Templates](skills/software-factory/templates/objective.md): small working records; reuse existing tracker fields where possible.
- [Evaluation cases](evals/scenarios.md): behavioral exercises for checking the instructions against realistic requests.

## Working state

Keep the objective and work status in the project's existing tracker or established documentation. Link one source of truth from repository guidance. Do not create a second backlog. With no existing system, use one `delivery/current.md` record based on the objective template.

Reviewable code is not automatically accepted product behavior. Record both separately. Preserve the repository's required checks and authorization rules.

## Validate this package

```sh
python tools/validate.py
python -m unittest discover -s tests -v
```

Validation checks packaging, references and executable safety properties. It does not prove that an agent makes good decisions. Use the evaluation cases and actual deliveries to improve the guidance.

Licensed under MIT.
