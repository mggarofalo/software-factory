from pathlib import Path
import tempfile
import unittest
from tools.validate import validate


class PackageBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills" / "example"
        self.skill.mkdir(parents=True)
        self.entry = self.skill / "SKILL.md"
        self.header = "---\nname: example\ndescription: Example capability.\n---\n"

    def write(self, content):
        self.entry.write_text(self.header + content, encoding="utf-8")

    def test_self_contained_skill_survives_relocation(self):
        self.write("[Role](role.md) and [web](https://example.com/reference)")
        (self.skill / "role.md").write_text("A portable role", encoding="utf-8")
        self.assertEqual([], validate(self.root))

    def test_missing_reference_is_rejected(self):
        self.write("[Role](missing.md)")
        self.assertTrue(any("missing reference" in e for e in validate(self.root)))

    def test_repository_file_cannot_be_required_by_installed_skill(self):
        (self.root / "README.md").write_text("Repository documentation", encoding="utf-8")
        self.write("[Instructions](../../README.md)")
        self.assertTrue(any("escapes skill" in e for e in validate(self.root)))

    def test_reference_cannot_escape_repository(self):
        self.write("[Secret](../../../outside.md)")
        self.assertTrue(any("escapes repository" in e for e in validate(self.root)))

    def test_mismatched_discovery_name_is_rejected(self):
        self.entry.write_text(self.header.replace("name: example", "name: wrong"), encoding="utf-8")
        self.assertTrue(any("does not match" in e for e in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
