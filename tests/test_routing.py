import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RoutingPolicyTest(unittest.TestCase):
    def test_policy_has_portable_fallback_rules(self):
        text = (ROOT / "SKILL_ROUTING.md").read_text(encoding="utf-8")
        self.assertIn("unavailable", text.lower())
        self.assertIn("reproducible-project-runner", text)
        self.assertIn("Do not assume a skill name exists", text)

    def test_manifest_entrypoints_exist(self):
        for relative in ("SKILL.md", "SKILL_ROUTING.md", "AGENT_INSTRUCTIONS.md", "MANIFEST.json"):
            self.assertTrue((ROOT / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
