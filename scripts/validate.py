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
    ROOT / "BRD.md",
    ROOT / "PRD.md",
    ROOT / "FSD.md",
    ROOT / "PROJECT.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "ROADMAP.md",
    ROOT / "DECISIONS.md",
    ROOT / "PORTABILITY.md",
    ROOT / "scripts" / "link_global_skill.py",
    ROOT / "docs" / "NAMING.md",
    ROOT / "docs" / "REVIEW-MODEL.md",
    ROOT / "docs" / "SCORING-RUBRIC.md",
    ROOT / "docs" / "REVIEW-OUTPUT.md",
    ROOT / "docs" / "ETHICS-AND-LIMITS.md",
    ROOT / "docs" / "SOURCES.md",
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    SKILL / "references" / "harness-compatibility.md",
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
BR_ID_RE = re.compile(r"\bBR-\d{3}\b")
PRODUCT_ID_RE = re.compile(r"\b(?:PR|NFR)-\d{3}\b")

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
        "host exposes a structured user-input tool",
        "Do not change the host's collaboration or execution mode solely",
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
        "**Governing directions:**",
        "**Content roles:**",
        "**Reference material:**",
        "**Format and delivery constraints:**",
        "**Known:**",
        "**Inferred:**",
        "**Unknown:**",
        "## Establish the direction hierarchy",
        "Do not ask every brief field",
    ),
    ROOT / "docs" / "ETHICS-AND-LIMITS.md": (
        "assumed prior knowledge",
        "factual references and voice samples",
        "missing brief details",
    ),
}

PRODUCTION_CONTRACT = {
    SKILL / "SKILL.md": (
        "audit requirement coverage separately from source support",
        "emotional force is earned rather than manufactured",
        "report an honest readiness state",
    ),
    SKILL / "references" / "writing-brief.md": (
        "**Optional supporting:**",
        "**Background only:**",
        "**Hard constraint:**",
        "**Working target:**",
        "compact decision brief",
        "does not verify a factual claim",
    ),
    SKILL / "references" / "integrity-review.md": (
        "## Audit requirement coverage",
        "separately from source support",
        "**Satisfied**, **Partial**, **Missing**, **Conflict**, or **Not applicable**",
        "background-only material",
    ),
    SKILL / "references" / "human-voice-review.md": (
        "## Test examples for function",
        "## Test emotional integrity",
        "manufactured urgency",
        "Creative writing may use invented material",
    ),
    SKILL / "references" / "output-contracts.md": (
        "## Readiness labels",
        "**Ready with noted limitations:**",
        "**Provisional—decision required:**",
        "**Not ready—evidence or authorization missing:**",
        "Never use **Ready**",
    ),
    ROOT / "docs" / "ETHICS-AND-LIMITS.md": (
        "## Emotional integrity",
        "manufacture or exaggerate urgency",
        "present an invented anecdote",
        "as proof that a factual claim is true",
    ),
    ROOT / "docs" / "REVIEW-MODEL.md": (
        "governing directions",
        "A requirement may be present but unsupported",
        "### 6. Test examples and emotional integrity",
    ),
    ROOT / "docs" / "REVIEW-OUTPUT.md": (
        "### Requirement coverage",
        "## Readiness labels",
        "Do not use **Ready**",
    ),
}

GLOBAL_LINK_CONTRACT = {
    ROOT / "scripts" / "link_global_skill.py": (
        'ROOT / ".agents" / "skills" / "unsloop"',
        'os.environ.get("CODEX_HOME")',
        "os.path.samefile",
        '"mklink", "/J"',
        "Refusing to replace an existing global skill or directory",
        '"--check"',
        '"--harness"',
        'Path.home() / ".agents" / "skills" / "unsloop"',
        'Path.home() / ".claude" / "skills" / "unsloop"',
        'Path.home() / ".pi" / "agent" / "skills" / "unsloop"',
        'requested = values or ["codex"]',
    ),
    ROOT / "PORTABILITY.md": (
        "## Optional user-level links",
        "The project utility preserves its original Codex default",
        "--harness claude",
        "--harness pi",
        "refuses to replace an unrelated existing destination",
    ),
}

HARNESS_CONTRACT = {
    SKILL / "SKILL.md": (
        "any compatible agent harness or text-capable model",
        "host-native tools by capability",
        "references/harness-compatibility.md",
    ),
    SKILL / "references" / "harness-compatibility.md": (
        "## Preserve the portable contract",
        "## Negotiate capabilities",
        "## Adapt to model capability",
        "**Codex:**",
        "**Claude Code:**",
        "**Pi:**",
        "Harnesses without Agent Skills discovery",
        "compatibility does not guarantee equivalent output quality",
    ),
    ROOT / "PORTABILITY.md": (
        "## Portable core and adapters",
        "## Harness matrix",
        "## Codex discovery remains supported",
        "## Claude discovery",
        "## Pi discovery",
        "## Model and capability adaptation",
    ),
    ROOT / "PRD.md": (
        "PR-015",
        "NFR-007 Interoperability",
        "### Harness and model independence",
    ),
    ROOT / "FSD.md": (
        "FS-013",
        "`HostCapabilityMap`",
        "### FS-013 — Adapt to harness and model",
    ),
}

SPECIFICATION_CONTRACT = {
    ROOT / "BRD.md": (
        "## Business requirements",
        "BR-001",
        "BR-013",
        "[`PRD.md`](PRD.md)",
        "[`FSD.md`](FSD.md)",
    ),
    ROOT / "PRD.md": (
        "## Functional requirements",
        "PR-001",
        "PR-015",
        "NFR-001 Portability",
        "[`BRD.md`](BRD.md)",
        "[`FSD.md`](FSD.md)",
    ),
    ROOT / "FSD.md": (
        "## Functional components",
        "FS-001",
        "FS-013",
        "`WritingBrief`",
        "`EvidenceBoundary`",
        "`VoiceBrief`",
        "`RequirementCoverage`",
        "`ReadinessState`",
        "## Verification matrix",
    ),
    ROOT / "README.md": (
        "[`BRD.md`](BRD.md)",
        "[`PRD.md`](PRD.md)",
        "[`FSD.md`](FSD.md)",
        "## Install Unsloop",
        "### Option 1 — Clone and use the repository directly",
        "### Option 2 — Copy or link Unsloop into another repository",
        "### Option 3 — Link the project into user-level harness directories",
        "### Option 4 — Link into the shared Agent Skills user location",
        "### Option 5 — Install a standalone Codex user copy from GitHub",
        "### Option 6 — Install for an administrator-managed Codex host",
        "### Option 7 — Adapt a harness without Agent Skills discovery",
        "### Plugin installation",
        "$skill-installer Install the skill from",
        "## Harness and model compatibility",
        "/skill:unsloop",
        "## Verify, activate, and update",
    ),
    ROOT / "ARCHITECTURE.md": (
        "## Specification stack",
        "BRD — why, for whom, scope, business outcomes",
        "SKILL.md + references — portable operational instructions loaded by an agent",
    ),
    ROOT / "DECISIONS.md": (
        "## D-015 — Use a three-level specification stack",
        "## D-016 — Separate the portable core from harness adapters",
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

    for path, requirements in PRODUCTION_CONTRACT.items():
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for requirement in requirements:
            if requirement not in text:
                errors.append(
                    f"production safeguard missing from {path.relative_to(ROOT)}: {requirement}"
                )

    for path, requirements in GLOBAL_LINK_CONTRACT.items():
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for requirement in requirements:
            if requirement not in text:
                errors.append(
                    f"global-link safeguard missing from {path.relative_to(ROOT)}: {requirement}"
                )

    for path, requirements in HARNESS_CONTRACT.items():
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for requirement in requirements:
            if requirement not in text:
                errors.append(
                    f"harness-compatibility safeguard missing from "
                    f"{path.relative_to(ROOT)}: {requirement}"
                )

    for path, requirements in SPECIFICATION_CONTRACT.items():
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for requirement in requirements:
            if requirement not in text:
                errors.append(
                    f"specification contract missing from {path.relative_to(ROOT)}: {requirement}"
                )

    brd = ROOT / "BRD.md"
    prd = ROOT / "PRD.md"
    fsd = ROOT / "FSD.md"
    if brd.is_file() and prd.is_file():
        business_ids = set(BR_ID_RE.findall(brd.read_text(encoding="utf-8")))
        product_text = prd.read_text(encoding="utf-8")
        for requirement_id in sorted(business_ids):
            if requirement_id not in product_text:
                errors.append(f"business requirement is not traced in PRD.md: {requirement_id}")

    if prd.is_file() and fsd.is_file():
        product_ids = set(PRODUCT_ID_RE.findall(prd.read_text(encoding="utf-8")))
        functional_text = fsd.read_text(encoding="utf-8")
        for requirement_id in sorted(product_ids):
            if requirement_id not in functional_text:
                errors.append(f"product requirement is not traced in FSD.md: {requirement_id}")

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
