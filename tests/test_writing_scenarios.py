from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures" / "writing-scenarios.md"


class WritingScenarioFixtureTests(unittest.TestCase):
    def test_all_numbered_scenarios_are_present_and_ordered(self) -> None:
        text = FIXTURES.read_text(encoding="utf-8")
        numbers = [int(value) for value in re.findall(r"^## (\d+)\.", text, re.MULTILINE)]
        self.assertEqual(numbers, list(range(1, 28)))

    def test_each_scenario_defines_routing_required_and_prohibited_behavior(self) -> None:
        text = FIXTURES.read_text(encoding="utf-8")
        sections = re.split(r"^## \d+\. ", text, flags=re.MULTILINE)[1:]
        self.assertEqual(len(sections), 27)
        for section in sections:
            self.assertIn("- Expected routing:", section)
            self.assertIn("- Required:", section)
            self.assertIn("- Prohibited:", section)

    def test_critical_specializations_are_explicit(self) -> None:
        text = FIXTURES.read_text(encoding="utf-8")
        for specialization in (
            "sustained writing project",
            "research provenance",
            "revision control",
            "collaborative writing",
            "multilingual writing",
            "structured output",
        ):
            self.assertIn(specialization, text)


if __name__ == "__main__":
    unittest.main()
