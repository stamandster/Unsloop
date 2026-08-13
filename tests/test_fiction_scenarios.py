from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures" / "fiction-scenarios.md"


class FictionScenarioFixtureTests(unittest.TestCase):
    def test_all_numbered_scenarios_are_present_and_ordered(self) -> None:
        text = FIXTURES.read_text(encoding="utf-8")
        numbers = [int(value) for value in re.findall(r"^## (\d+)\.", text, re.MULTILINE)]
        self.assertEqual(numbers, list(range(1, 27)))

    def test_each_scenario_defines_required_and_prohibited_behavior(self) -> None:
        text = FIXTURES.read_text(encoding="utf-8")
        sections = re.split(r"^## \d+\. ", text, flags=re.MULTILINE)[1:]
        self.assertEqual(len(sections), 26)
        for section in sections:
            self.assertIn("- Required:", section)
            self.assertIn("- Prohibited:", section)

    def test_critical_mode_routes_are_explicit(self) -> None:
        text = FIXTURES.read_text(encoding="utf-8")
        for route in (
            "Write + fiction workflow",
            "Review + fiction workflow + fiction review",
            "Audit + fiction review + project operations",
            "Write + publication handoff + project tooling",
        ):
            self.assertIn(route, text)


if __name__ == "__main__":
    unittest.main()
