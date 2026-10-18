"""Validate distributable skill metadata and local Markdown references."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    skills = root / "skills"
    entries = sorted(skills.glob("*/SKILL.md"))
    if not entries:
        errors.append("No distributable skills found")
    for entry in entries:
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        if not match:
            errors.append(f"{entry.relative_to(root)}: missing frontmatter")
            continue
        fields = dict(re.findall(r"^([a-z]+):\s*(.+)$", match[1], re.M))
        if fields.get("name") != entry.parent.name:
            errors.append(f"{entry.relative_to(root)}: name does not match folder")
        if not re.fullmatch(r"[a-z0-9-]{1,63}", fields.get("name", "")):
            errors.append(f"{entry.relative_to(root)}: invalid skill name")
        if not fields.get("description", "").strip():
            errors.append(f"{entry.relative_to(root)}: missing description")
    for document in sorted(root.rglob("*.md")):
        if ".git" in document.relative_to(root).parts:
            continue
        text = document.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            url = urlsplit(target.strip("<>"))
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (document.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"{document.relative_to(root)}: reference escapes repository: {target}")
                continue
            # Installed bundles cannot depend on files left in the repository.
            for entry in entries:
                bundle = entry.parent.resolve()
                if document.is_relative_to(bundle) and not resolved.is_relative_to(bundle):
                    errors.append(f"{document.relative_to(root)}: reference escapes skill: {target}")
            if not resolved.exists():
                errors.append(f"{document.relative_to(root)}: missing reference: {target}")
    return errors


if __name__ == "__main__":
    failures = validate(Path(__file__).resolve().parents[1])
    if failures:
        print("\n".join(failures), file=sys.stderr)
        raise SystemExit(1)
    print("Skill metadata and local references are valid.")
