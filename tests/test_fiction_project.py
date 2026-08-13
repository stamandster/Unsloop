from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / ".agents" / "skills" / "unsloop" / "scripts" / "fiction_project.py"
SPEC = importlib.util.spec_from_file_location("fiction_project", SCRIPT)
assert SPEC and SPEC.loader
fiction_project = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fiction_project)


class Args:
    def __init__(self, **values: object) -> None:
        self.__dict__.update(values)


class FictionProjectTests(unittest.TestCase):
    def init_args(self, root: Path, profile: str = "compact", apply: bool = True, **extra: object) -> Args:
        values: dict[str, object] = {
            "root": str(root),
            "profile": profile,
            "book_slug": None,
            "extra": None,
            "voice": False,
            "voice_authorized": False,
            "apply": apply,
        }
        values.update(extra)
        return Args(**values)

    def test_compact_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(fiction_project.init_command(self.init_args(root, apply=False)), 0)
            self.assertFalse((root / "story").exists())

    def test_compact_init_and_check(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(fiction_project.init_command(self.init_args(root)), 0)
            self.assertTrue((root / "story" / "BRIEF.md").is_file())
            self.assertTrue((root / "manuscript" / "001-opening.md").is_file())
            self.assertFalse((root / "story" / "VOICE.md").exists())
            self.assertEqual(fiction_project.check_command(Args(root=str(root))), 0)

    def test_full_and_series_profiles(self) -> None:
        with tempfile.TemporaryDirectory() as full_dir, tempfile.TemporaryDirectory() as series_dir:
            full = Path(full_dir)
            series = Path(series_dir)
            self.assertEqual(fiction_project.init_command(self.init_args(full, "full", extra=["world", "knowledge"])), 0)
            self.assertTrue((full / "story" / "CANON.md").is_file())
            self.assertTrue((full / "story" / "CHARACTER-VOICES.md").is_file())
            self.assertTrue((full / "story" / "WORLD.md").is_file())
            self.assertTrue((full / "story" / "KNOWLEDGE.md").is_file())
            self.assertEqual(fiction_project.init_command(self.init_args(series, "series", book_slug="book-one")), 0)
            self.assertTrue((series / "story" / "SERIES.md").is_file())
            self.assertTrue((series / "story" / "CHARACTER-VOICES.md").is_file())
            self.assertTrue((series / "story" / "books" / "book-one" / "SCENES.md").is_file())

    def test_collision_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = self.init_args(root)
            self.assertEqual(fiction_project.init_command(args), 0)
            original = (root / "story" / "BRIEF.md").read_text(encoding="utf-8")
            self.assertEqual(fiction_project.init_command(args), 2)
            self.assertEqual((root / "story" / "BRIEF.md").read_text(encoding="utf-8"), original)

    def test_voice_requires_authorization(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(ValueError):
                fiction_project.init_command(self.init_args(root, voice=True))
            self.assertEqual(
                fiction_project.init_command(self.init_args(root, voice=True, voice_authorized=True)), 0
            )
            self.assertTrue((root / "story" / "VOICE.md").is_file())
            self.assertEqual(fiction_project.check_command(Args(root=str(root))), 0)

    def test_check_detects_duplicate_scene_and_invalid_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(fiction_project.init_command(self.init_args(root)), 0)
            scenes = root / "story" / "SCENES.md"
            scenes.write_text(
                scenes.read_text(encoding="utf-8")
                + "\n| SCN-001 | `manuscript/001-opening.md` | Broken | A | Now | X | Y | Z | Q | R |\n",
                encoding="utf-8",
            )
            self.assertEqual(fiction_project.check_command(Args(root=str(root))), 1)

    def test_confirmed_character_voice_requires_author_approval(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(fiction_project.init_command(self.init_args(root, "full")), 0)
            profiles = root / "story" / "CHARACTER-VOICES.md"
            profiles.write_text(
                profiles.read_text(encoding="utf-8").replace("| Proposed |", "| Confirmed |"),
                encoding="utf-8",
            )
            self.assertEqual(fiction_project.check_command(Args(root=str(root))), 1)
            profiles.write_text(
                profiles.read_text(encoding="utf-8").replace(
                    "[decision ID or pending]", "DEC-voice-approved"
                ),
                encoding="utf-8",
            )
            self.assertEqual(fiction_project.check_command(Args(root=str(root))), 0)

    def test_checkpoint_dry_run_and_apply_with_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(fiction_project.init_command(self.init_args(root)), 0)
            args = Args(
                root=str(root), name="before-retcon", reason="Retcon impact approved",
                parent="initial", include=["story/BRIEF.md", "manuscript/001-opening.md"], apply=False,
            )
            self.assertEqual(fiction_project.checkpoint_command(args), 0)
            self.assertFalse((root / "checkpoints").exists())
            args.apply = True
            self.assertEqual(fiction_project.checkpoint_command(args), 0)
            manifest = root / "checkpoints" / "before-retcon" / "manifest.json"
            payload = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(len(payload["files"]), 2)
            self.assertEqual(payload["parent_checkpoint"], "initial")
            self.assertIn("restore", payload)
            self.assertEqual(fiction_project.checkpoint_command(args), 2)

    def test_assemble_includes_only_accepted_units_and_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(fiction_project.init_command(self.init_args(root)), 0)
            accepted = root / "manuscript" / "001-opening.md"
            accepted.write_text("# Accepted\n\nKeep me.\n", encoding="utf-8")
            rejected = root / "manuscript" / "002-rejected.md"
            rejected.write_text("# Rejected\n\nDo not include me.\n", encoding="utf-8")
            (root / "story" / "SCENES.md").write_text(
                "# Scene Ledger\n\n"
                "| Scene ID | Manuscript path | State | POV | Time and place | Purpose | Turn and consequence | Knowledge or reveal | Setup or payoff | Research and continuity |\n"
                "|---|---|---|---|---|---|---|---|---|---|\n"
                "| SCN-001 | `manuscript/001-opening.md` | Accepted | A | Now | X | Y | Z | Q | R |\n"
                "| SCN-002 | `manuscript/002-rejected.md` | Cut | B | Later | X | Y | Z | Q | R |\n",
                encoding="utf-8",
            )
            args = Args(root=str(root), output="assembled/manuscript.md", apply=False)
            self.assertEqual(fiction_project.assemble_command(args), 0)
            self.assertFalse((root / "assembled").exists())
            args.apply = True
            self.assertEqual(fiction_project.assemble_command(args), 0)
            output = (root / "assembled" / "manuscript.md").read_text(encoding="utf-8")
            self.assertIn("Keep me", output)
            self.assertNotIn("Do not include me", output)
            self.assertEqual(fiction_project.assemble_command(args), 2)

    def test_paths_cannot_escape_project_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(ValueError):
                fiction_project.safe_relative(root, "../outside.md")


if __name__ == "__main__":
    unittest.main()
