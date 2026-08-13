# Architecture

> **Document role:** Structural view of the system. Normative functional behavior is defined in [`FSD.md`](FSD.md); product behavior and business intent are defined in [`PRD.md`](PRD.md) and [`BRD.md`](BRD.md).

## Product shape

Unsloop is an umbrella project with one shared method and three modes.

```text
Unsloop
├── Review — constructive diagnosis
├── Write  — author-led drafting and revision
│   └── Fiction workflow — scene-to-series development and continuity
└── Audit  — evidence-heavy source examination
```

Version 0.1 implements the modes in one core skill so principles, scoring, and safety limits remain consistent. A later split should happen only if mode-specific workflows become large enough to justify separate trigger descriptions or resources.

## Repository structure

```text
Unsloop/
├── README.md
├── BRD.md
├── PRD.md
├── FSD.md
├── PROJECT.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── DECISIONS.md
├── PORTABILITY.md
├── scripts/
│   ├── validate.py
│   └── link_global_skill.py
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
                ├── harness-compatibility.md
                ├── human-voice-review.md
                ├── voice-fidelity.md
                ├── writing-brief.md
                ├── scoring.md
                ├── output-contracts.md
                ├── source-verification.md
                ├── write-mode.md
                └── fiction-workflow.md
```

## Specification stack

```text
BRD — why, for whom, scope, business outcomes
 ↓
PRD — modes, user-visible behavior, acceptance criteria, NFRs
 ↓
FSD — functions, data concepts, state flow, validation, tests
 ↓
SKILL.md + references — portable operational instructions loaded by an agent
```

Requirement IDs provide traceability without forcing project-management detail into the runtime skill. The method documents under `docs/` are normative sub-specifications referenced by the PRD and FSD.

## Documentation boundaries

- Root and `docs/` files define the product for maintainers and collaborators.
- `.agents/skills/unsloop/SKILL.md` contains the minimum operational workflow a compatible agent needs after the skill triggers.
- `.agents/skills/unsloop/references/` contains task-specific procedures loaded only when relevant.
- Detailed rules live in one skill reference rather than being repeated across multiple skill files.
- `agents/openai.yaml` is an optional Codex adapter; it is not required by the portable core.

## Discovery and portability

The canonical `.agents/skills/unsloop` location follows the Agent Skills directory shape. Codex and Pi discover it directly from a repository. Claude Code uses the same core through `.claude/skills/unsloop`; Pi may alternatively use `.pi/skills/unsloop`; other clients may use a shared `.agents/skills` location or an explicit skill path.

All operational paths inside the skill are relative to `SKILL.md`. The portable core uses only standard `name` and `description` frontmatter and has no required MCP server, executable, environment variable, user-level configuration, provider, model, or network dependency. Source verification may use network access only when the user asks to check external sources.

Optional harness adapters are filesystem links to the repository skill, not independent installations. This preserves one source of truth while retaining the existing Codex global path and adding shared Agent Skills, Claude, and Pi locations.

## Execution model

```text
User purpose and materials
        ↓
Map harness capabilities and model limits
        ↓
Choose Review, Write, or Audit
        ↓
Use, refine, or brainstorm the topic
        ↓
Build the progressive writing brief
        ↓
Resolve governing directions, content roles, and constraints
        ↓
For fiction: scale the lifecycle, cadence, and approved project state
        ↓
Set evidence boundary, voice basis, and review depth
        ↓
Run integrity lens + human-voice lens
        ↓
Audit coverage, calibrate findings, and test readiness
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
- thin adapters for additional Agent Skills clients without vendor-specific forks.
- optional tooling that validates fiction ledgers against accepted manuscript facts without making creative decisions for the author.

Automation must surface evidence, not replace judgment. Any future similarity or linguistic analysis should produce inspectable signals and preserve the distinction between observation, inference, and verdict.
