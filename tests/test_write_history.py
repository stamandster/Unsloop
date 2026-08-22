from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / ".agents" / "skills" / "unsloop" / "scripts" / "write_history.py"
SPEC = importlib.util.spec_from_file_location("write_history", SCRIPT)
assert SPEC and SPEC.loader
write_history = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(write_history)


class Args:
    def __init__(self, **values: object) -> None:
        self.__dict__.update(values)


class WriteHistoryTests(unittest.TestCase):
    def values(self, root: Path, **overrides: object) -> dict[str, object]:
        values: dict[str, object] = {
            "root": str(root),
            "batch_id": "WRT-20260822T120000Z-001",
            "kind": "response",
            "reason": "First response",
            "include": ["manuscript/chapter.md"],
            "parent": None,
            "history_dir": "unsloop-history",
            "apply": False,
        }
        values.update(overrides)
        return values

    def test_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "manuscript" / "chapter.md"
            source.parent.mkdir()
            source.write_text("First version.\n", encoding="utf-8")

            self.assertEqual(write_history.snapshot_command(Args(**self.values(root))), 0)
            self.assertFalse((root / "unsloop-history").exists())

    def test_apply_copies_all_files_and_writes_hash_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            chapter = root / "manuscript" / "chapter.md"
            status = root / "writing" / "STATUS.md"
            chapter.parent.mkdir()
            status.parent.mkdir()
            chapter.write_text("First version.\n", encoding="utf-8")
            status.write_text("Current state.\n", encoding="utf-8")

            values = self.values(
                root,
                include=["manuscript/chapter.md", "writing/STATUS.md"],
                apply=True,
            )
            self.assertEqual(write_history.snapshot_command(Args(**values)), 0)

            destination = root / "unsloop-history" / values["batch_id"]
            manifest = json.loads((destination / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["write_policy"], "Immutable versions")
            self.assertEqual([item["path"] for item in manifest["files"]], [
                "manuscript/chapter.md", "writing/STATUS.md",
            ])
            for item in manifest["files"]:
                archived = destination / item["archived_path"]
                self.assertTrue(archived.is_file())
                self.assertEqual(item["sha256"], write_history.sha256(archived))

    def test_existing_batch_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "manuscript" / "chapter.md"
            source.parent.mkdir()
            source.write_text("First version.\n", encoding="utf-8")
            values = self.values(root, apply=True)

            self.assertEqual(write_history.snapshot_command(Args(**values)), 0)
            source.write_text("Second version.\n", encoding="utf-8")
            self.assertEqual(write_history.snapshot_command(Args(**values)), 2)
            archived = root / "unsloop-history" / values["batch_id"] / "files" / "manuscript" / "chapter.md"
            self.assertEqual(archived.read_text(encoding="utf-8"), "First version.\n")

    def test_paths_cannot_escape_or_snapshot_history(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            outside = root.parent / "outside.md"
            source = root / "manuscript" / "chapter.md"
            source.parent.mkdir()
            source.write_text("First version.\n", encoding="utf-8")
            outside.write_text("Outside.\n", encoding="utf-8")
            try:
                values = self.values(root, include=[str(outside)])
                self.assertEqual(write_history.snapshot_command(Args(**values)), 2)

                history_file = root / "unsloop-history" / "prior" / "files" / "chapter.md"
                history_file.parent.mkdir(parents=True)
                history_file.write_text("History.\n", encoding="utf-8")
                values = self.values(root, include=["unsloop-history/prior/files/chapter.md"])
                self.assertEqual(write_history.snapshot_command(Args(**values)), 2)
            finally:
                outside.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
