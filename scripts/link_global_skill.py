#!/usr/bin/env python3
"""Expose the canonical Unsloop skill through user-level agent-harness directories."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / ".agents" / "skills" / "unsloop"
HARNESS_ORDER = ("codex", "standard", "claude", "pi")
ALL_HARNESSES = ("codex", "claude", "pi")


def codex_destination() -> Path:
    configured = os.environ.get("CODEX_HOME")
    codex_root = Path(configured).expanduser() if configured else Path.home() / ".codex"
    return codex_root / "skills" / "unsloop"


def global_destination(harness: str = "codex") -> Path:
    """Return the user-level discovery path for a supported harness adapter."""
    destinations = {
        "codex": codex_destination(),
        "standard": Path.home() / ".agents" / "skills" / "unsloop",
        "claude": Path.home() / ".claude" / "skills" / "unsloop",
        "pi": Path.home() / ".pi" / "agent" / "skills" / "unsloop",
    }
    return destinations[harness]


def points_to_source(destination: Path) -> bool:
    try:
        return destination.exists() and os.path.samefile(destination, SOURCE)
    except OSError:
        return False


def harness_label(harness: str) -> str:
    return "Global" if harness == "codex" else harness.capitalize()


def check(destination: Path, harness: str = "codex") -> int:
    if not SOURCE.is_dir():
        print(f"Canonical skill is missing: {SOURCE}", file=sys.stderr)
        return 1
    if not points_to_source(destination):
        print(
            f"{harness_label(harness)} Unsloop is not linked to the canonical project skill: "
            f"{destination}",
            file=sys.stderr,
        )
        return 1
    required = [Path("SKILL.md"), Path("references") / "harness-compatibility.md"]
    if harness == "codex":
        required.append(Path("agents") / "openai.yaml")
    for relative in required:
        if not (destination / relative).is_file():
            print(f"Linked skill is missing {relative}", file=sys.stderr)
            return 1
    print(f"{harness_label(harness)} Unsloop link is healthy.")
    print(f"- Canonical: {SOURCE}")
    print(f"- {harness_label(harness)}: {destination}")
    return 0


def install(destination: Path, harness: str = "codex") -> int:
    if not SOURCE.is_dir():
        print(f"Canonical skill is missing: {SOURCE}", file=sys.stderr)
        return 1
    if os.path.lexists(destination):
        if points_to_source(destination):
            print(
                f"{harness_label(harness)} Unsloop already points to the canonical project skill."
            )
            return check(destination, harness)
        print(
            f"Refusing to replace an existing global skill or directory for {harness}: "
            f"{destination}",
            file=sys.stderr,
        )
        return 1

    destination.parent.mkdir(parents=True, exist_ok=True)
    if os.name == "nt":
        result = subprocess.run(
            ["cmd", "/d", "/c", "mklink", "/J", str(destination), str(SOURCE)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            detail = result.stderr.strip() or result.stdout.strip()
            print(f"Could not create {harness} junction: {detail}", file=sys.stderr)
            return 1
    else:
        destination.symlink_to(SOURCE, target_is_directory=True)

    return check(destination, harness)


def selected_harnesses(values: Optional[list[str]]) -> list[str]:
    requested = values or ["codex"]
    expanded: list[str] = []
    for value in requested:
        candidates = ALL_HARNESSES if value == "all" else (value,)
        for candidate in candidates:
            if candidate not in expanded:
                expanded.append(candidate)
    return sorted(expanded, key=HARNESS_ORDER.index)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify the selected user-level link or links without changing them",
    )
    parser.add_argument(
        "--harness",
        action="append",
        choices=(*HARNESS_ORDER, "all"),
        help=(
            "Target codex, standard (~/.agents), claude, or pi discovery. "
            "Repeat for multiple targets; 'all' selects Codex, Claude, and Pi. "
            "Default: codex."
        ),
    )
    args = parser.parse_args()
    result = 0
    for harness in selected_harnesses(args.harness):
        destination = global_destination(harness)
        operation = check if args.check else install
        if operation(destination, harness) != 0:
            result = 1
    return result


if __name__ == "__main__":
    sys.exit(main())
