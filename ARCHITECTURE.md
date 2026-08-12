# Architecture

## Product shape

Unsloop is an umbrella project with one shared method and three modes.

```text
Unsloop
├── Review — constructive diagnosis
├── Write  — author-led drafting and revision
└── Audit  — evidence-heavy source examination
```

Version 0.1 implements the modes in one core skill so principles, scoring, and safety limits remain consistent. A later split should happen only if mode-specific workflows become large enough to justify separate trigger descriptions or resources.

## Repository structure

```text
Unsloop/
├── README.md
├── PROJECT.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── DECISIONS.md
├── PORTABILITY.md
├── scripts/
│   └── validate.py
├── docs/
│   ├── NAMING.md
│   ├── REVIEW-MODEL.md
│   ├── SCORING-RUBRIC.md
│   ├── REVIEW-OUTPUT.md
│   ├── ETHICS-AND-LIMITS.md
│   └── SOURCES.md
└── .agents/
    └── skills/
        └── unsloop/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
            ├── integrity-review.md
            ├── human-voice-review.md
            ├── voice-fidelity.md
            ├── writing-brief.md
            ├── scoring.md
            ├── output-contracts.md
            ├── source-verification.md
            └── write-mode.md
```

## Documentation boundaries

- Root and `docs/` files define the product for maintainers and collaborators.
- `.agents/skills/unsloop/SKILL.md` contains the minimum operational workflow another Codex instance needs after the skill triggers.
- `.agents/skills/unsloop/references/` contains task-specific procedures loaded only when relevant.
- Detailed rules live in one skill reference rather than being repeated across multiple skill files.

## Discovery and portability

Codex scans `.agents/skills` from the working directory to the repository root. Keeping Unsloop at `.agents/skills/unsloop` makes it available to the entire repository without copying it into a user's home directory.

All operational paths inside the skill are relative to `SKILL.md`. The skill has no required MCP server, executable, environment variable, user-level configuration, or network dependency. Source verification may use network access only when the user asks to check external sources.

## Execution model

```text
User purpose and materials
        ↓
Choose Review, Write, or Audit
        ↓
Use, refine, or brainstorm the topic
        ↓
Build the progressive writing brief
        ↓
Set evidence boundary, voice basis, and review depth
        ↓
Run integrity lens + human-voice lens
        ↓
Calibrate findings and optional scores
        ↓
Report diagnosis; revise only if requested
```

## Future implementation seams

The current structure leaves room for:

- separate `unsloop-review`, `unsloop-write`, and `unsloop-audit` skills;
- scripts that align source and draft passages for human inspection;
- machine-readable review output alongside Markdown;
- user-approved persistent house-style or personal-voice profiles;
- benchmark fixtures for scorer calibration and regression testing;
- integrations with document, citation, and repository tools.

Automation must surface evidence, not replace judgment. Any future similarity or linguistic analysis should produce inspectable signals and preserve the distinction between observation, inference, and verdict.
