#!/usr/bin/env python3
"""Portable, non-destructive operations for Unsloop fiction projects."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = SKILL_ROOT / "assets" / "fiction-project"
PROJECT_PHASES = {
    "Discovery", "Contract", "Foundation", "Architecture",
    "Drafting", "Revision", "Complete", "Archived",
}
UNIT_STATES = {"Planned", "Drafted", "Revised", "Accepted", "Cut", "Archived"}
CANON_STATES = {"Proposed", "Confirmed", "Superseded"}
VOICE_PROFILE_STATES = {"Proposed", "Confirmed", "Superseded"}
EXTRAS = {"world": "WORLD.md", "glossary": "GLOSSARY.md", "knowledge": "KNOWLEDGE.md", "branches": "BRANCHES.md"}
BASE_PROFILES = {
    "compact": ("BRIEF.md", "STATUS.md", "SCENES.md"),
    "full": (
        "BRIEF.md", "STATUS.md", "SCENES.md", "CANON.md", "CHARACTERS.md", "CHARACTER-VOICES.md",
        "TIMELINE.md", "ARCS.md", "RESEARCH.md", "DECISIONS.md",
    ),
}
SCENE_ID_RE = re.compile(r"\bSCN-[A-Za-z0-9_-]+\b")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_relative(root: Path, value: str) -> Path:
    candidate = (root / value).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"path escapes project root: {value}") from exc
    return candidate


def write_template(
    source_name: str,
    destination: Path,
    apply: bool,
    replacements: dict[str, str] | None = None,
) -> None:
    if destination.exists():
        raise FileExistsError(f"refusing to overwrite: {destination}")
    print(f"CREATE {destination}")
    if apply:
        destination.parent.mkdir(parents=True, exist_ok=True)
        source = TEMPLATES / source_name
        if replacements:
            content = source.read_text(encoding="utf-8")
            for old, new in replacements.items():
                content = content.replace(old, new)
            destination.write_text(content, encoding="utf-8")
        else:
            shutil.copyfile(source, destination)


def init_command(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    extras = tuple(dict.fromkeys(args.extra or ()))
    plan: list[tuple[str, Path]] = []

    if args.profile in BASE_PROFILES:
        for name in BASE_PROFILES[args.profile]:
            plan.append((name, root / "story" / name))
        plan.append(("MANUSCRIPT.md", root / "manuscript" / "001-opening.md"))
    else:
        slug = args.book_slug
        if not slug:
            raise ValueError("--book-slug is required for the series profile")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError("book slug must use lowercase hyphen-case")
        for name in ("SERIES.md", "STATUS.md", "CANON.md", "CHARACTERS.md", "CHARACTER-VOICES.md", "TIMELINE.md"):
            plan.append((name, root / "story" / name))
        for name in ("BRIEF.md", "STATUS.md", "ARCS.md", "SCENES.md"):
            plan.append((name, root / "story" / "books" / slug / name))
        plan.append(("MANUSCRIPT.md", root / "manuscript" / slug / "001-opening.md"))

    for extra in extras:
        plan.append((EXTRAS[extra], root / "story" / EXTRAS[extra]))
    if args.voice:
        if not args.voice_authorized:
            raise ValueError("--voice requires --voice-authorized")
        plan.append(("VOICE.md", root / "story" / "VOICE.md"))

    collisions = [destination for _, destination in plan if destination.exists()]
    if collisions:
        for collision in collisions:
            print(f"COLLISION {collision}", file=sys.stderr)
        return 2

    print(f"Fiction project initialization ({'apply' if args.apply else 'dry-run'}):")
    for source, destination in plan:
        replacements = None
        if source == "VOICE.md":
            replacements = {
                "[explicit authorization and scope]":
                    "Explicitly affirmed for this project during initialization."
            }
        write_template(source, destination, args.apply, replacements)
    if not args.apply:
        print("No files created. Re-run with --apply after approving this plan.")
    return 0


def table_rows(path: Path) -> list[list[str]]:
    if not path.is_file():
        return []
    rows: list[list[str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r"[-: ]+", cell or "-") for cell in cells):
            continue
        rows.append(cells)
    return rows


def find_field(text: str, label: str) -> str | None:
    match = re.search(rf"^- {re.escape(label)}:\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def check_command(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    story = root / "story"
    brief = story / "BRIEF.md"
    status_candidates = [story / "STATUS.md", *sorted((story / "books").glob("*/STATUS.md"))] if (story / "books").exists() else [story / "STATUS.md"]
    scenes_candidates = [story / "SCENES.md", *sorted((story / "books").glob("*/SCENES.md"))] if (story / "books").exists() else [story / "SCENES.md"]

    if not story.is_dir():
        errors.append("missing story directory")
    if not (root / "manuscript").is_dir():
        errors.append("missing manuscript directory")
    if not brief.is_file() and not (story / "SERIES.md").is_file():
        errors.append("missing story/BRIEF.md or story/SERIES.md")

    for status in status_candidates:
        if not status.is_file():
            if status == story / "STATUS.md":
                errors.append("missing story/STATUS.md")
            continue
        text = status.read_text(encoding="utf-8")
        phase = find_field(text, "Project phase")
        if phase not in PROJECT_PHASES:
            errors.append(f"invalid or missing project phase in {status.relative_to(root)}: {phase}")
        for field in ("Last accepted unit", "Last completed checkpoint", "Next approved action"):
            if not find_field(text, field):
                errors.append(f"missing {field} in {status.relative_to(root)}")
        if "## Resume context" not in text:
            errors.append(f"missing Resume context in {status.relative_to(root)}")

    seen: dict[str, Path] = {}
    for scenes in scenes_candidates:
        rows = table_rows(scenes)
        for cells in rows[1:]:
            if len(cells) < 3 or not SCENE_ID_RE.fullmatch(cells[0]):
                continue
            scene_id, manuscript_path, state = cells[:3]
            if scene_id in seen:
                errors.append(f"duplicate scene ID {scene_id}: {seen[scene_id].relative_to(root)} and {scenes.relative_to(root)}")
            else:
                seen[scene_id] = scenes
            if state not in UNIT_STATES:
                errors.append(f"invalid scene state for {scene_id}: {state}")
            if manuscript_path and not manuscript_path.startswith("["):
                try:
                    target = safe_relative(root, manuscript_path)
                except ValueError as exc:
                    errors.append(str(exc))
                else:
                    if state != "Planned" and not target.is_file():
                        errors.append(f"missing manuscript path for {scene_id}: {manuscript_path}")
                    elif state == "Planned" and not target.exists():
                        warnings.append(f"planned manuscript path does not yet exist for {scene_id}: {manuscript_path}")

    canon = story / "CANON.md"
    for cells in table_rows(canon)[1:]:
        if len(cells) < 6 or not cells[0].startswith("CAN-"):
            continue
        state = cells[2]
        if state not in CANON_STATES:
            errors.append(f"invalid canon state for {cells[0]}: {state}")
        if state == "Superseded" and cells[5] in {"", "—", "-", "[decision ID]"}:
            errors.append(f"Superseded canon lacks decision reference: {cells[0]}")

    character_ids = {
        cells[0] for cells in table_rows(story / "CHARACTERS.md")[1:]
        if cells and cells[0].startswith("CHR-")
    }
    voice_profiles = table_rows(story / "CHARACTER-VOICES.md")[1:]
    seen_profiles: set[str] = set()
    confirmed_scopes: set[tuple[str, str]] = set()
    for cells in voice_profiles:
        if len(cells) < 16 or not cells[0].startswith("CVP-"):
            continue
        profile_id, character_id, state, scope = cells[0], cells[1], cells[3], cells[4]
        if profile_id in seen_profiles:
            errors.append(f"duplicate character voice profile ID: {profile_id}")
        seen_profiles.add(profile_id)
        if character_id not in character_ids:
            errors.append(f"unknown character {character_id} referenced by {profile_id}")
        if state not in VOICE_PROFILE_STATES:
            errors.append(f"invalid character voice profile state for {profile_id}: {state}")
        decision = cells[14]
        if state == "Confirmed":
            if decision in {"", "—", "-", "[decision ID or pending]"} or decision.startswith("["):
                errors.append(f"Confirmed character voice profile lacks author approval: {profile_id}")
            key = (character_id, scope)
            if key in confirmed_scopes:
                errors.append(f"multiple Confirmed voice profiles for {character_id} in scope {scope}")
            confirmed_scopes.add(key)
        if state == "Superseded" and (
            decision in {"", "—", "-", "[decision ID or pending]"} or cells[15] in {"", "—", "-"}
        ):
            errors.append(f"Superseded character voice profile lacks change linkage: {profile_id}")

    voice = story / "VOICE.md"
    if voice.is_file():
        authorization = find_field(voice.read_text(encoding="utf-8"), "Storage authorization")
        if not authorization or authorization.startswith("["):
            errors.append("story/VOICE.md lacks explicit storage authorization")

    for warning in warnings:
        print(f"WARNING {warning}")
    for error in errors:
        print(f"ERROR {error}")
    if errors:
        print(f"Fiction project check failed: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    print(f"Fiction project check passed: {len(warnings)} warning(s).")
    return 0


def checkpoint_command(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    destination = safe_relative(root, f"checkpoints/{args.name}")
    if destination.exists():
        print(f"ERROR refusing to overwrite checkpoint: {destination}", file=sys.stderr)
        return 2
    sources: list[Path] = []
    for value in args.include:
        source = safe_relative(root, value)
        if not source.is_file():
            print(f"ERROR checkpoint source is not a file: {value}", file=sys.stderr)
            return 2
        sources.append(source)
    manifest = {
        "name": args.name,
        "reason": args.reason,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "mechanism": "unsloop fiction_project.py checkpoint",
        "parent_checkpoint": args.parent,
        "restore": "Copy the checkpoint's project-relative files back only after confirming the intended target and preserving newer work.",
        "files": [
            {"path": source.relative_to(root).as_posix(), "sha256": sha256(source)}
            for source in sorted(sources)
        ],
    }
    print(f"Fiction checkpoint ({'apply' if args.apply else 'dry-run'}): {destination}")
    for entry in manifest["files"]:
        print(f"COPY {entry['path']}")
    if not args.apply:
        print("No checkpoint created. Re-run with --apply after approving this plan.")
        return 0
    destination.mkdir(parents=True)
    for source in sorted(sources):
        relative = source.relative_to(root)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    (destination / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Checkpoint created: {destination}")
    return 0


def accepted_units(root: Path) -> tuple[list[Path], list[str]]:
    story = root / "story"
    candidates = [story / "SCENES.md"]
    if (story / "books").exists():
        candidates.extend(sorted((story / "books").glob("*/SCENES.md")))
    units: list[Path] = []
    errors: list[str] = []
    seen_paths: set[Path] = set()
    for scenes in candidates:
        for cells in table_rows(scenes)[1:]:
            if len(cells) < 3 or not SCENE_ID_RE.fullmatch(cells[0]) or cells[2] != "Accepted":
                continue
            try:
                path = safe_relative(root, cells[1])
            except ValueError as exc:
                errors.append(str(exc))
                continue
            if path in seen_paths:
                errors.append(f"duplicate accepted manuscript path: {cells[1]}")
            elif not path.is_file():
                errors.append(f"missing accepted manuscript path: {cells[1]}")
            else:
                units.append(path)
                seen_paths.add(path)
    return units, errors


def assemble_command(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    output = safe_relative(root, args.output)
    manifest_path = output.with_suffix(output.suffix + ".manifest.json")
    if output.exists() or manifest_path.exists():
        print(f"ERROR refusing to overwrite assembly output or manifest: {output}", file=sys.stderr)
        return 2
    units, errors = accepted_units(root)
    if not units:
        errors.append("no Accepted manuscript units found")
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1
    print(f"Fiction assembly ({'apply' if args.apply else 'dry-run'}):")
    for unit in units:
        print(f"INCLUDE {unit.relative_to(root).as_posix()}")
    print(f"OUTPUT {output}")
    if not args.apply:
        print("No manuscript assembled. Re-run with --apply after approving this plan.")
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    sections = [unit.read_text(encoding="utf-8").rstrip() for unit in units]
    output.write_text("\n\n".join(sections) + "\n", encoding="utf-8")
    manifest = {
        "output": output.relative_to(root).as_posix(),
        "units": [
            {"path": unit.relative_to(root).as_posix(), "sha256": sha256(unit)}
            for unit in units
        ],
        "sha256": sha256(output),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Assembled manuscript: {output}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="preview or initialize an approved fiction project")
    init.add_argument("--root", default=".")
    init.add_argument("--profile", choices=("compact", "full", "series"), required=True)
    init.add_argument("--book-slug")
    init.add_argument("--extra", action="append", choices=tuple(EXTRAS))
    init.add_argument("--voice", action="store_true", help="include the optional VOICE.md template")
    init.add_argument("--voice-authorized", action="store_true", help="confirm explicit storage authorization")
    init.add_argument("--apply", action="store_true")
    init.set_defaults(func=init_command)

    check = subparsers.add_parser("check", help="run read-only fiction project checks")
    check.add_argument("--root", default=".")
    check.set_defaults(func=check_command)

    checkpoint = subparsers.add_parser("checkpoint", help="preview or create a recoverable checkpoint")
    checkpoint.add_argument("--root", default=".")
    checkpoint.add_argument("--name", required=True)
    checkpoint.add_argument("--reason", required=True)
    checkpoint.add_argument("--parent")
    checkpoint.add_argument("--include", action="append", required=True)
    checkpoint.add_argument("--apply", action="store_true")
    checkpoint.set_defaults(func=checkpoint_command)

    assemble = subparsers.add_parser("assemble", help="preview or assemble Accepted Markdown units")
    assemble.add_argument("--root", default=".")
    assemble.add_argument("--output", required=True)
    assemble.add_argument("--apply", action="store_true")
    assemble.set_defaults(func=assemble_command)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except (FileExistsError, OSError, ValueError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
