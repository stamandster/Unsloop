from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / ".agents" / "skills" / "unsloop" / "scripts" / "writing_pattern_metrics.py"
SPEC = importlib.util.spec_from_file_location("writing_pattern_metrics", SCRIPT)
assert SPEC and SPEC.loader
writing_pattern_metrics = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(writing_pattern_metrics)


class WritingPatternMetricsTests(unittest.TestCase):
    def test_analysis_reports_measurements_without_authorship_score(self) -> None:
        text = "First we test the claim. First we test the result. The evidence changes the answer."
        result = writing_pattern_metrics.analyze(text, identifier="sample.txt", transitions=["First we"])

        self.assertEqual(result["authorship_boundary"], "Not assessable from prose alone")
        self.assertNotIn("ai_score", result)
        measurements = result["measurements"]
        self.assertEqual(measurements["sentence_count"], 3)
        self.assertEqual(measurements["requested_transition_counts"][0]["count"], 2)

    def test_repeated_phrases_and_openings_use_declared_parameters(self) -> None:
        text = "We can see the pattern. We can see the reason. We can see the result."
        result = writing_pattern_metrics.analyze(
            text,
            identifier="sample.txt",
            phrase_size=3,
            minimum_repeat=2,
            opening_words=3,
        )

        measurements = result["measurements"]
        self.assertIn({"phrase": "we can see", "count": 3}, measurements["repeated_phrases"])
        self.assertIn({"opening": "we can see", "count": 3}, measurements["repeated_sentence_openings"])
        self.assertIn("Sliding 3-word sequences", result["method"]["repeated_phrase_rule"])

    def test_empty_text_returns_declared_zero_boundary(self) -> None:
        result = writing_pattern_metrics.analyze("", identifier="empty.txt")
        self.assertEqual(result["measurements"]["word_count"], 0)
        self.assertIsNone(result["measurements"]["sentence_length_words"]["mean"])
        self.assertIn("do not determine human or AI authorship", result["limitations"][-1])


if __name__ == "__main__":
    unittest.main()
