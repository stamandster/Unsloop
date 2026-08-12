#!/usr/bin/env python3
"""Validate the portable Unsloop project using only the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / ".agents" / "skills" / "unsloop"

REQUIRED_FILES = (
    ROOT / "README.md",
    ROOT / "PROJECT.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "ROADMAP.md",
    ROOT / "DECISIONS.md",
    ROOT / "PORTABILITY.md",
    ROOT / "docs" / "NAMING.md",
    ROOT / "docs" / "REVIEW-MODEL.md",
    ROOT / "docs" / "SCORING-RUBRIC.md",
    ROOT / "docs" / "REVIEW-OUTPUT.md",
    ROOT / "docs" / "ETHICS-AND-LIMITS.md",
    ROOT / "docs" / "SOURCES.md",
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    SKILL / "references" / "integrity-review.md",
    SKILL / "references" / "human-voice-review.md",
    SKILL / "references" / "voice-fidelity.md",
    SKILL / "references" / "writing-brief.md",
    SKILL / "references" / "scoring.md",
    SKILL / "references" / "output-contracts.md",
    SKILL / "references" / "source-verification.md",
    SKILL / "references" / "write-mode.md",
)

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
WINDOWS_ABSOLUTE_RE = re.compile(r"(?<![A-Za-z0-9])(?:[A-Za-z]:[\\/])")
POSIX_USER_ABSOLUTE_RE = re.compile(r"(?<![A-Za-z0-9])/(?:Users|home)/[^/\s]+/")

VOICE_CONTRACT = {
    SKILL / "SKILL.md": (
        "representative samples",
        "authorized evidence",
        "Never claim exact replication",
    ),
    SKILL / "references" / "voice-fidelity.md": (
        "current explicit instructions",
        "Keep style separate from content",
        "Low, Moderate, or High",
        "Do not place samples or extracted profiles",
    ),
    ROOT / "docs" / "ETHICS-AND-LIMITS.md": (
        "unauthorized impersonation",
        "Do not infer sensitive traits",
        "Do not persist samples or voice profiles",
    ),
}

BRIEF_CONTRACT = {
    SKILL / "SKILL.md": (
        "progressive writing brief",
        "Determine topic status at the beginning",
        "wants to brainstorm topics",
        "structured user-input tool is available",
        "Do not change collaboration mode solely",
        "known, inferred, or unknown",
        "factual reference material separate from voice samples",
    ),
    SKILL / "references" / "writing-brief.md": (
        "## Start with topic status",
        "already has a topic",
        "rough subject or direction",
        "brainstorm topics from scratch",
        "do not ask the user to repeat it",
        "`request_user_input`",
        "Use my topic (Recommended)",
        "Refine a direction",
        "Brainstorm topics",
        "Never switch modes merely",
        "**Topic:**",
        "**Goal:**",
        "**Prior knowledge:**",
        "**Required content:**",
        "**Reference material:**",
        "**Known:**",
        "**Inferred:**",
        "**Unknown:**",
        "Do not ask all ten fields",
    ),
    ROOT / "docs" / "ETHICS-AND-LIMITS.md": (
        "assumed prior knowledge",
        "factual references and voice samples",
        "missing brief details",
    ),
}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter is not closed") from exc

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def validate() -> list[str]:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    skill_md = SKILL / "SKILL.md"
    if skill_md.is_file():
        try:
            metadata = parse_frontmatter(skill_md)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            extra = set(metadata) - {"name", "description"}
            if metadata.get("name") != "unsloop":
                errors.append("skill name must be 'unsloop'")
            if not SKILL_NAME_RE.fullmatch(metadata.get("name", "")):
                errors.append("skill name is not valid lowercase hyphen-case")
            if SKILL.name != metadata.get("name"):
                errors.append("skill folder name must match frontmatter name")
            if len(metadata.get("description", "")) < 80:
                errors.append("skill description is too short to express triggers and boundaries")
            if extra:
                errors.append(f"unsupported SKILL.md frontmatter fields: {sorted(extra)}")

    openai_yaml = SKILL / "agents" / "openai.yaml"
    if openai_yaml.is_file():
        ui = openai_yaml.read_text(encoding="utf-8")
        for token in ("display_name:", "short_description:", "default_prompt:", "$unsloop"):
            if token not in ui:
                errors.append(f"agents/openai.yaml is missing {token}")

    for path, safeguards in VOICE_CONTRACT.items():
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for safeguard in safeguards:
            if safeguard not in text:
                errors.append(
                    f"voice-fidelity safeguard missing from {path.relative_to(ROOT)}: {safeguard}"
                )

    for path, requirements in BRIEF_CONTRACT.items():
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for requirement in requirements:
            if requirement not in text:
                errors.append(
                    f"writing-brief requirement missing from {path.relative_to(ROOT)}: {requirement}"
                )

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)

        if "[TODO" in text or "TBD" in text:
            errors.append(f"unresolved placeholder in {relative}")
        if WINDOWS_ABSOLUTE_RE.search(text) or POSIX_USER_ABSOLUTE_RE.search(text):
            errors.append(f"machine-specific absolute path in {relative}")

        for target in LINK_RE.findall(text):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            local_target = target.split("#", 1)[0]
            if local_target and not (path.parent / local_target).resolve().exists():
                errors.append(f"broken link in {relative}: {target}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print(f"Unsloop validation failed ({len(errors)} error(s)):")
        for error in errors:
            print(f"- {error}")
        return 1

    markdown_count = sum(1 for _ in ROOT.rglob("*.md"))
    print("Unsloop validation passed.")
    print(f"- Skill: {SKILL.relative_to(ROOT)}")
    print(f"- Markdown files: {markdown_count}")
    print("- Runtime dependencies: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
