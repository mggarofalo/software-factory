# Working on Software Factory

Keep this package portable and self-contained under `skills/software-factory`.
Changes must improve a concrete agent decision, handoff or delivery outcome.
Do not add a framework, scheduler, telemetry service or universal approval ceremony.
Repository-specific commands belong in adapters or consuming projects.

Use conventional commits and pull requests. Run `python tools/validate.py` and
`python -m unittest discover -s tests -v`. Evaluate changed decision guidance with
at least one relevant case in `evals/scenarios.md`, documenting what was and was
not exercised. Avoid tests that merely pin prose.

When executing on Windows, use a PTY and keep background process windows hidden.
