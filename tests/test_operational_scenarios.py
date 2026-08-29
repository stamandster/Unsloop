from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures" / "operational-scenarios.md"


class OperationalScenarioFixtureTests(unittest.TestCase):
    def test_all_numbered_scenarios_are_present_and_ordered(self) -> None:
        text = FIXTURES.read_text(encoding="utf-8")
        numbers = [int(value) for value in re.findall(r"^## (\d+)\.", text, re.MULTILINE)]
        self.assertEqual(numbers, list(range(1, 47)))

    def test_each_scenario_defines_routing_required_and_prohibited_behavior(self) -> None:
        text = FIXTURES.read_text(encoding="utf-8")
        sections = re.split(r"^## \d+\. ", text, flags=re.MULTILINE)[1:]
        self.assertEqual(len(sections), 46)
        for section in sections:
            self.assertIn("- Expected routing:", section)
            self.assertIn("- Required:", section)
            self.assertIn("- Prohibited:", section)

    def test_all_extension_families_are_explicit(self) -> None:
        text = FIXTURES.read_text(encoding="utf-8").lower()
        for token in (
            "skill composition", "source safety", "quantitative evidence",
            "interview evidence", "multimodal evidence", "documentation systems",
            "usability validation",
            "section flow",
            "delivery and presentation",
            "writing-pattern and assistance audit",
            "style direction",
            "spoken thought chain",
        ):
            self.assertIn(token, text)

    def test_spoken_continuity_contract_is_explicit(self) -> None:
        text = FIXTURES.read_text(encoding="utf-8")
        for token in (
            "## 46. Spoken thought chain hidden by structural labels",
            "relationship that makes the next thought necessary",
            "named subjects and pronouns",
            "preserve purposeful pauses or direct turns",
            "recalculate timing",
        ):
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
