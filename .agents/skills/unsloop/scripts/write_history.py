#!/usr/bin/env python3
"""Create append-only, response-batch snapshots for persistent Unsloop writing."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path


BATCH_ID_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_path(root: Path, value: str) -> Path:
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = root / candidate
    candidate = candidate.resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"path escapes project root: {value}") from exc
    return candidate


def validate_batch_id(value: str) -> str:
    if not BATCH_ID_RE.fullmatch(value):
        raise argparse.ArgumentTypeError(
            "batch ID must start with an alphanumeric character and contain only "
            "letters, digits, dot, underscore, or hyphen"
        )
    return value


def snapshot_command(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"ERROR project root is not a directory: {root}", file=sys.stderr)
        return 2

    try:
        history_root = safe_path(root, args.history_dir)
    except ValueError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2

    destination = history_root / args.batch_id
    if destination.exists():
        print(f"ERROR refusing to overwrite history batch: {destination}", file=sys.stderr)
        return 2

    if args.parent:
        parent_manifest = history_root / args.parent / "manifest.json"
        if not parent_manifest.is_file():
            print(f"ERROR parent history batch does not exist: {args.parent}", file=sys.stderr)
            return 2

    sources: list[tuple[Path, Path]] = []
    seen: set[Path] = set()
    for value in args.include:
        try:
            source = safe_path(root, value)
        except ValueError as exc:
            print(f"ERROR {exc}", file=sys.stderr)
            return 2
        try:
            relative = source.relative_to(root)
        except ValueError:
            print(f"ERROR path escapes project root: {value}", file=sys.stderr)
            return 2
        if source == history_root or history_root in source.parents:
            print(f"ERROR history cannot snapshot itself: {relative}", file=sys.stderr)
            return 2
        if not source.is_file():
            print(f"ERROR snapshot input is not a file: {relative}", file=sys.stderr)
            return 2
        if relative not in seen:
            sources.append((source, relative))
            seen.add(relative)

    print(f"Unsloop write-history snapshot ({'apply' if args.apply else 'dry-run'}):")
    print(f"BATCH {args.batch_id}")
    for _, relative in sources:
        print(f"COPY {relative.as_posix()}")
    print(f"DESTINATION {destination}")

    if not args.apply:
        print("No snapshot created. Re-run with --apply after approving this plan.")
        return 0

    history_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{args.batch_id}-", dir=history_root) as temporary:
        staging = Path(temporary)
        records: list[dict[str, object]] = []
        for source, relative in sources:
            archived = staging / "files" / relative
            archived.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, archived)
            records.append(
                {
                    "path": relative.as_posix(),
                    "archived_path": (Path("files") / relative).as_posix(),
                    "bytes": archived.stat().st_size,
                    "sha256": sha256(archived),
                }
            )

        manifest = {
            "schema_version": 1,
            "batch_id": args.batch_id,
            "kind": args.kind,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "reason": args.reason,
            "parent_batch": args.parent,
            "write_policy": "Immutable versions",
            "project_root": ".",
            "current_files_maintained_separately": True,
            "files": records,
        }
        (staging / "manifest.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        staging.rename(destination)

    print(f"Snapshot created: {destination}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Preview or create append-only snapshots of persistent writing batches."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    snapshot = subparsers.add_parser("snapshot", help="preview or create one history batch")
    snapshot.add_argument("--root", required=True)
    snapshot.add_argument("--batch-id", required=True, type=validate_batch_id)
    snapshot.add_argument("--kind", choices=("baseline", "response"), required=True)
    snapshot.add_argument("--reason", required=True)
    snapshot.add_argument("--include", action="append", required=True)
    snapshot.add_argument("--parent", type=validate_batch_id)
    snapshot.add_argument("--history-dir", default="unsloop-history")
    snapshot.add_argument("--apply", action="store_true")
    snapshot.set_defaults(func=snapshot_command)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
