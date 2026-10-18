# Review independently

Input: requirement, primary authority, candidate revision and test evidence.

Establish expected behavior independently before reading the author's reasoning.
Inspect correctness, contracts, unsupported inputs, lifecycle, privacy and
determinism where relevant. Challenge whether tests distinguish plausible wrong
behavior. Review the actual user path when interaction is part of acceptance.

Report defects by consequence and reproducible trigger, not by personal style.
Separate blocking findings from suggestions and unrelated later work. A clean
review describes its scope and unverified areas; it does not certify the whole
product. A self-review must say so.

Output: findings or bounded approval using the
[evidence template](../templates/evidence.md). Return fixes to implementation,
then review the changed risk rather than restarting an unrelated audit.
