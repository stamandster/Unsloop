# Architecture

> **Document role:** Structural view of the system. Normative functional behavior is defined in [`FSD.md`](FSD.md); product behavior and business intent are defined in [`PRD.md`](PRD.md) and [`BRD.md`](BRD.md).

## Product shape

Unsloop is a portable writing lifecycle system with one shared author-control and evidence method and three modes. The modes operate from topic discovery through drafting, revision, research, validation, maintenance, and handoff. Formulaic-writing or AI-assistance review is one Audit specialization, not the system boundary.

```text
Unsloop
├── Review — constructive diagnosis, including fiction craft review
├── Write  — author-led drafting, revision, assembly, and publication support
├── Audit  — non-mutating evidence-heavy source, continuity, canon, and research examination
├── Shared section-flow contract — logical progression across headings without forced smoothing
├── Shared delivery contract — timing, evidence flow, audience attention, media, and artifact-set readiness
├── Shared writing-pattern and assistance audit — component profile, measurements, provenance, and detector boundaries
├── Shared Style Direction specialization — author-evidenced, historical/literary, custom, or genre direction with controlled evolution
├── Shared sustained-writing specialization — long-form operations across all three modes
│   ├── Project state — onboarding, units, resume packets, assembly, recovery
│   ├── Provenance and revision — claims, sources, quotations, changes, freshness
│   ├── Documentary/documentation — biography, procedure, policy, plan, and technical form contracts
│   ├── Source acquisition — supplied, scoped-site, broad-web, and hybrid evidence governance
│   ├── Evidence types — quantitative, interview, oral-history, and multimodal lineage
│   ├── Documentation systems — content architecture, dependencies, maintenance, and reader validation
│   └── Collaboration and adaptation — authority, feedback, multilingual, structured output
├── Shared fiction specialization — scene-to-series operations across all three modes
│   ├── Project operations — onboarding, state, branches, retcons, recovery
│   ├── Character voice continuity — author-owned profiles, drift review, versioned change
│   ├── Fiction review — developmental, craft, continuity, and integrity
│   └── Publication handoff — assembly and support artifacts
└── Cross-skill composition — specialist authority, shared intake, validation handoff, and source isolation
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
│   ├── GITHUB-ABOUT.md
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
            ├── scripts/writing_pattern_metrics.py
            ├── references/
                ├── integrity-review.md
                ├── harness-compatibility.md
                ├── human-voice-review.md
                ├── voice-fidelity.md
                ├── style-direction.md
                ├── writing-brief.md
                ├── scoring.md
                ├── output-contracts.md
                ├── source-verification.md
                ├── write-mode.md
                ├── section-flow.md
                ├── delivery-and-presentation.md
                ├── writing-pattern-assistance-audit.md
                ├── fiction-workflow.md
                ├── fiction-project-operations.md
                ├── character-voice-continuity.md
                ├── fiction-review.md
                ├── fiction-publication.md
                ├── sustained-writing-projects.md
                ├── documentary-documentation.md
                ├── source-acquisition.md
                ├── source-safety.md
                ├── skill-composition.md
                ├── quantitative-evidence.md
                ├── interview-evidence.md
                ├── multimodal-evidence.md
                ├── documentation-systems.md
                ├── usability-validation.md
                ├── research-provenance.md
                ├── revision-control.md
                ├── collaborative-writing.md
                ├── multilingual-writing.md
                └── structured-output.md
            ├── assets/fiction-project/  portable author-readable templates, including optional STYLE.md
            ├── assets/writing-project/  sustained non-fiction templates, including optional STYLE.md
            ├── assets/schemas/  optional interchange contracts
            ├── scripts/fiction_project.py  optional fiction operations
            └── scripts/writing_project.py  optional sustained-writing operations
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
Compose domain and artifact skills; isolate untrusted source instructions
        ↓
Choose Review, Write, or Audit
        ↓
For Audit: lock the inspected version and separate findings from revision authority
        ↓
Use, refine, or brainstorm the topic
        ↓
Build the progressive writing brief
        ↓
Resolve governing directions, content roles, and constraints
        ↓
For fiction: scale the lifecycle, cadence, and approved project state
        ↓
For recurring speakers: load Confirmed character profiles or keep suggestions Proposed
        ↓
When applicable: onboard, review, impact-map, recover, assemble, or package
        ↓
For sustained non-fiction: scale project state, provenance, revision, collaboration, and language adaptation
        ↓
For documentary/documentation: select form contract, acquisition scope, and validation boundary
        ↓
When applicable: preserve data, interview, and multimodal lineage; map documentation dependencies and reader evidence
        ↓
Set evidence boundary, voice basis, and review depth
        ↓
Run integrity lens + human-voice lens
        ↓
Audit coverage, calibrate findings, test readiness, and serialize only when requested
        ↓
Report diagnosis; preserve Audit; revise only through a separately authorized scope
```

## Future implementation seams

The current structure leaves room for:

- separate `unsloop-review`, `unsloop-write`, and `unsloop-audit` skills;
- scripts that align source and draft passages for human inspection;
- user-approved persistent house-style or personal-voice profiles;
- benchmark fixtures for scorer calibration and regression testing;
- integrations with document, citation, and repository tools.
- thin adapters for additional Agent Skills clients without vendor-specific forks.
- richer behavioral fixtures and cross-harness evaluation without treating one model as reference truth.
- media-specific and reader-facing interactive fiction adapters only when observed demand justifies them.

Automation must surface evidence, not replace judgment. Any future similarity or linguistic analysis should produce inspectable signals and preserve the distinction between observation, inference, and verdict.
