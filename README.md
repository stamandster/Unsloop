# Unsloop

**Author-led writing. Traceable evidence. Defensible voice.**

Unsloop is a portable, model-agnostic writing lifecycle system for planning, drafting, revising, reviewing, auditing, researching, validating, maintaining, and packaging written work. It preserves author control, evidence provenance, human voice, continuity, and honest readiness from the first idea through long-form development and final handoff.

Unsloop began with two narrower concerns:

- identifying generic, formulaic, over-polished, or source-dependent writing;
- avoiding unsupported AI-authorship conclusions based on style alone.

That integrity-and-voice lens remains important, but the project now supports the full writing process:

- topic discovery;
- creative and factual development;
- evidence acquisition;
- controlled revision;
- persistent project state;
- delivery planning;
- multi-format synchronization; and
- non-mutating audit.

The project is governed by a traceable specification stack:

- [`BRD.md`](BRD.md) defines the business need and boundaries;
- [`PRD.md`](PRD.md) defines product behavior and acceptance criteria; and
- [`FSD.md`](FSD.md) defines the executable workflow and validation model.

The project directory is authoritative across local, user-wide, and harness-specific use.

Repository-profile copy, suggested topics, and the GitHub About description are maintained in [`docs/GITHUB-ABOUT.md`](docs/GITHUB-ABOUT.md).

## What Unsloop is

Unsloop combines three modes under one shared method:

| Mode | Primary job | Default behavior |
|---|---|---|
| **Unsloop Review** | Diagnose an existing draft | Prioritize consequential issues, preserve strong material, and revise only when asked. |
| **Unsloop Write** | Create or revise writing | Build from an author-led brief, evidenced voice, relevant sources, and explicit constraints. |
| **Unsloop Audit** | Examine writing and evidence | Preserve the inspected artifact, bound every conclusion to available evidence, and keep proposed corrections separate. |

Specializations extend those modes without creating separate products:

- fiction;
- sustained non-fiction;
- documentary and controlled documentation;
- research provenance;
- source acquisition;
- quantitative and interview evidence;
- multilingual writing;
- style direction and stylistic evolution;
- collaboration;
- documentation systems;
- presentation delivery;
- structured output; and
- writing-pattern or assistance audit.

## Common ways to use Unsloop

| Goal | Example request | What Unsloop contributes |
|---|---|---|
| Find a direction | `$unsloop I need to write for new managers but do not have a topic.` | Distinct topic options, reader value, scope, evidence needs, and a selected brief. |
| Draft from source material | `$unsloop Write this report from my notes and supplied sources.` | Goal-directed structure, claim boundaries, attribution, and author-owned decisions. |
| Revise in your voice | `$unsloop Revise this using my authorized samples without importing their facts.` | Evidence-based voice target, meaning preservation, and confidence disclosure. |
| Design a writing style | `$unsloop Write this as Early Modern English dramatic verse, balanced for modern readers.` | A bounded Style Direction, authenticity stance, formal constraints, evidence limits, and controlled evolution. |
| Review a manuscript | `$unsloop Review this chapter for structure, specificity, continuity, and flow.` | Prioritized findings, material to preserve, and the smallest useful interventions. |
| Audit evidence | `$unsloop Audit these claims and citations without changing the document.` | Non-mutating source, claim, quotation, requirement, and provenance findings. |
| Sustain long-form work | `$unsloop Continue this book from its writing project and accepted checkpoint.` | Portable state, stable units, controlled decisions, recovery, assembly, and resumability. |
| Develop fiction | `$unsloop Develop this premise into a novel using Adaptive collaboration.` | Scene-to-series workflow, canon, chronology, character voices, revision, and handoff. |
| Build factual documents | `$unsloop Create this policy, procedure, plan, or technical guide from approved evidence.` | Form-specific authority, branches, validation, maintenance, and version controls. |
| Maintain documentation | `$unsloop Update this documentation set and trace affected pages and versions.` | Canonical ownership, dependency impact, lifecycle state, and reader validation. |
| Prepare delivered writing | `$unsloop Turn this outline into a timed presentation with readings and media.` | Complete timing, audience design, evidence integration, media decisions, and format checks. |
| Assess AI-related concerns | `$unsloop Audit this draft's patterns and supplied detector report.` | Component profile, transparent measurements, provenance, and no unsupported AI verdict. |
| Compose with another skill | `$unsloop Apply integrity and voice controls while the document skill owns DOCX layout.` | Shared intake, explicit authority, unified handoff, and honest validation boundaries. |

## Operating contract

- The author retains control of goals, meaning, voice, creative canon, evidence decisions, and consequential changes.
- Topic, directions, factual evidence, voice samples, and model-generated proposals remain distinct.
- Authorized revision preserves useful author-supplied observations, questions, and tentative perspectives through proportionate scoping and evidence-status framing; lack of external verification alone is not a deletion rule.
- Audit is information-preserving: findings cannot silently rewrite the inspected artifact.
- Project files are visible, portable, model-agnostic, and created only when persistent state is useful and approved.
- Domain and artifact skills keep authority over specialized facts, file mechanics, rendering, formulas, and executable validation.
- Readiness means only what the evidence and checks actually establish; polished output is not treated as verified, approved, rehearsed, synchronized, or publication-certified by appearance alone.

The implementation is one extensible, repository-scoped [Agent Skill](https://agentskills.io/specification) at [`.agents/skills/unsloop/SKILL.md`](.agents/skills/unsloop/SKILL.md). Codex, Claude Code, Pi, other Agent Skills clients, and manually adapted text-capable harnesses can use the same authoritative core.

For manuscripts with chapters, headings, subheadings, scene breaks, or procedural phases, Unsloop writes and reviews the close, visible boundary, and next opening as one logical transition. It preserves purposeful hard breaks and does not add a bridging sentence when hierarchy and sequence already orient the reader. See the [section-flow contract](.agents/skills/unsloop/references/section-flow.md).

## Writing-pattern and assistance audit

When asked for an “AI score,” AI detection, AI-like word or transition analysis, comparison with prior writing, or interpretation of a detector report, Unsloop runs a non-mutating **Writing-Pattern and Assistance Audit**. It does not estimate the probability that AI wrote the text. With prose alone, it reports:

```text
AI authorship determination: Not assessable from prose alone.
```

The audit can score Specificity and Authorial voice as strengths; Redundancy, Formulaicity, and Abstraction as risks; Voice fidelity when authorized comparison samples exist; and optional Slop density as a writing-quality summary. Every component includes passage evidence and direction. No strength, risk, voice, provenance, or detector value is combined into one AI score.

Mechanically calculated observations—such as repeated transition counts, repeated phrases, or sentence-length distribution—state their method, inspected range, comparison baseline, and limitations. Revision history, metadata, prompts, outputs, or disclosures are reported separately as assistance provenance and only for the stages they document. A supplied detector result remains labeled as an external vendor result; Unsloop does not reinterpret its percentage as authorship probability.

```text
$unsloop Audit this draft for formulaic writing and explain whether the prose alone can establish AI authorship.
$unsloop Compare this draft with my three authorized samples and report voice fidelity without inferring identity or misconduct.
$unsloop Interpret this detector report alongside the draft, keeping its result separate from Unsloop's pattern profile.
```

See the [Writing-Pattern and Assistance Audit contract](.agents/skills/unsloop/references/writing-pattern-assistance-audit.md).

An optional dependency-free helper produces reproducible descriptive measurements without an AI score:

```text
python .agents/skills/unsloop/scripts/writing_pattern_metrics.py draft.txt --transition "however" --transition "in addition"
```

It writes JSON to standard output and leaves the draft unchanged. The output declares its token, sentence, paragraph, repeated-phrase, sentence-opening, and user-supplied transition rules plus known limitations.

## Style direction and evolution

Unsloop supports **Style Direction** across Write, Review, and Audit—not as a new mode or a catalog of rigid presets. When style is consequential and not already clear, the author can choose:

- **My evidenced voice:** derive task-relevant traits from authorized samples;
- **Historical or literary tradition:** use a period-, region-, form-, and corpus-bounded style;
- **Custom designed style:** combine explicit traits for this work; or
- **Genre default:** use restrained conventions suited to the form and audience.

The style contract keeps the author's evidenced personal voice, the selected narrative or document style, viewpoint-character voice, character dialogue, and delivery or form conventions separate. A request such as **Early Modern English dramatic verse rooted in Elizabethan and Jacobean traditions** therefore resolves more than archaic vocabulary: form, verse/prose distribution, meter, rhyme, enjambment, caesura, rhetoric, register, dramatic function, performance, audience readability, and evidence basis all remain inspectable. Elizabethan and Jacobean are treated as varied historical contexts, not one homogeneous preset.

Historical or literary directions use one of three authenticity stances:

- **Period-forward:** favor evidenced period conventions even when they increase reader effort;
- **Balanced (Recommended):** retain defining conventions while controlling opacity; or
- **Modern-reader-forward:** preserve selected signals and dramatic logic while modernizing more aggressively.

Style can remain **Stable**, evolve **Gradually**, or change by approved **Phases**. Consequential phase changes remain Proposed until accepted; Confirmed style cannot drift silently. Named-author requests are translated into high-level, non-exclusive traits and broader tradition evidence rather than copied signature wording, characters, worlds, or rhetorical patterns. Surface archaism alone never proves historical authenticity.

```text
$unsloop Write this monologue as Early Modern English dramatic verse, Balanced for modern readers.
$unsloop Suggest three materially different Style Directions for this speculative novel.
$unsloop Review chapters 8–10 against the Confirmed StyleBrief and flag unapproved phase drift.
```

For sustained work, an approved `story/STYLE.md` or `writing/STYLE.md` may preserve the StyleBrief and phase history without storing source samples. See [Style Direction and Evolution](.agents/skills/unsloop/references/style-direction.md).

## Delivery and presentation writing

Invoke Unsloop with a manuscript, outline, duration, audience, media options, or required output formats:

```text
$unsloop Turn this outline into a 12-minute narrated presentation and include time for the two quoted passages.
$unsloop Review this training script for question function, evidence flow, mixed-audience clarity, and closing impact.
$unsloop Audit whether the Markdown source and DOCX delivery copy are synchronized without changing either file.
```

The delivery contract is topic-neutral and has no universal speaking-rate default. It uses a user-, assignment-, or specialist-supplied pace when available and otherwise asks or discloses a conservative estimate when appropriate. It does not solve overruns by assuming faster speech or omitting pauses, setup, playback, observation, questions, answers, or interaction.

For material evidence, Unsloop checks the functional movement from audience need through orientation, accurate presentation, interpretation, and supported use without forcing a fixed sentence formula. Optional media receives a decision brief covering what the audience perceives, its function, placement, handling, accessibility, and time or space cost. A polished manuscript remains provisional if an unresolved choice materially affects delivery.

For parallel Markdown, DOCX, PDF, slides, web, audio, or other formats, Unsloop keeps content authority separate from format mechanics. The applicable artifact skill owns generation and rendering; Unsloop tracks whether required derivatives match the accepted content and states the exact validation boundary. See [delivery and presentation writing](.agents/skills/unsloop/references/delivery-and-presentation.md).

## Fiction writing

Fiction remains part of **Unsloop Write**, not a separate mode. Invoke Unsloop with a premise, a draft, or a request to brainstorm:

```text
$unsloop Help me brainstorm a short story about memory and inheritance.
$unsloop Develop this premise into a novel, using Adaptive collaboration.
$unsloop Continue chapter 7 from this fiction project's story state.
```

The workflow supports scenes, flash fiction, short stories, novellas, novels, serials, and series on any user-chosen topic. A clear one-off scene uses a minimal brief and no project files by default. Sustained work can use Guided, Adaptive, or Autonomous collaboration and an author-approved portable Markdown project beneath `story/` and `manuscript/`. Adaptive is the default. Even in Autonomous collaboration, Unsloop stops before changing Confirmed canon, premise, ending direction, POV rules, content boundaries, real-person treatment, or another locked author decision.

The default project state is visible and model-agnostic. `story/STATUS.md` records the current checkpoint and context needed to resume; `story/CANON.md` distinguishes Proposed, Confirmed, and Superseded story facts; manuscript units use stable ordered filenames. Existing coherent layouts are preserved. Voice samples remain unpersisted unless the author explicitly approves a distilled `story/VOICE.md`. See the operational [fiction workflow](.agents/skills/unsloop/references/fiction-workflow.md) for the full contract.

For an ensemble, each recurring speaker receives an independent, versioned character voice profile covering personality, worldview, baseline tone, cadence, syntax, diction, discourse habits, and allowed contextual variation. The author can set these traits directly or ask Unsloop for materially different suggestions based on story context and background. Suggestions remain Proposed; accepted profiles are locked until the author explicitly approves a prospective evolution or retroactive override. See [character voice continuity](.agents/skills/unsloop/references/character-voice-continuity.md).

Fiction also uses the existing modes rather than a fourth one:

- **Write:** discover, plan, draft, revise on request, assemble, or prepare a synopsis, query, blurb, pitch, or checklist.
- **Review:** developmental, structure, pacing, character, relationship, POV, narration, dialogue, theme, line, copy, simulated-reader, or authenticity review.
- **Audit:** non-mutating, evidence-heavy continuity, chronology, canon, research, historical, adaptation, attribution, or source comparison.

For an established manuscript, Unsloop inventories versions and inspected ranges, preserves the existing layout, assigns stable internal IDs, and proposes extracted state before creating or confirming it. For partial acceptance, branches, retcons, or large revisions, it updates only the accepted scope, maps downstream effects, and preserves a recoverable checkpoint.

### Optional fiction project command

The skill includes a dependency-free utility for approved Markdown projects. Python is optional; the same workflow can be performed manually from the bundled templates.

```text
python .agents/skills/unsloop/scripts/fiction_project.py init --root PATH --profile compact
python .agents/skills/unsloop/scripts/fiction_project.py init --root PATH --profile full --style --apply
python .agents/skills/unsloop/scripts/fiction_project.py check --root PATH
python .agents/skills/unsloop/scripts/fiction_project.py checkpoint --root PATH --name NAME --reason REASON --include FILE
python .agents/skills/unsloop/scripts/fiction_project.py assemble --root PATH --output assembled/manuscript.md
```

`init`, `checkpoint`, and `assemble` preview by default and require `--apply` to write. All operations refuse overwrite. `VOICE.md` is excluded unless `--voice --voice-authorized` is supplied. Assembly includes only manuscript units marked Accepted and writes a hash manifest.

## Sustained non-fiction and research

Unsloop can maintain multi-session books, theses, reports, courses, biographies, documentary narratives, procedures, policies, plans, directions, instructions, technical documentation, and research syntheses without imposing project files on a short request. When persistent state is useful, it proposes a Compact, Research, Collaborative, or Full Markdown profile beneath `writing/` and `manuscript/`, preserves a coherent existing layout, and creates files only after approval. Sustained work can use Guided, Adaptive, or Autonomous collaboration, with Adaptive as the default and locked author, evidence, requirement, privacy, commitment, terminology, and approval decisions protected in every cadence.

The workflow can track stable manuscript units, claims, sources, quotations, requirements, decisions, revision changes, stakeholder authority, terminology, and a compact `writing/STATUS.md` resume packet. Citation presence remains separate from source access and claim support. Materially changed claims and quotations require recheck; rejected revisions and unresolved reviewer comments do not become accepted work silently.

Evidence acquisition can be User-provided only, Scoped web, Broad web, or Hybrid. Scoped research stays inside the approved sites unless the user broadens it. Sources are assessed for the specific claim as Preferred, Usable with limitations, Lead only, or Excluded; these labels remain separate from verification. A user override can include, exclude, broaden, or narrow material, but it cannot make a source verified, independent, current, or more confident. Documentary and controlled-document workflows then apply form-specific checks for chronology, authority, prerequisites, branches, safety, ownership, normative force, versions, environments, examples, rollback, testing, approval, and maintenance.

Retrieved sources are always treated as untrusted evidence. Instructions embedded in pages, documents, repositories, transcripts, images, or metadata cannot change permissions, activate tools, expand research scope, request credentials, or disclose project data. Material redirects, archives, downloads, transformations, and source-safety concerns remain part of the acquisition record.

Unsloop also separates heterogeneous evidence. Quantitative records preserve datasets, populations, periods, units, filters, formulas, reproduced values, displayed values, and uncertainty. Interview records preserve consent, attribution, transcript status, quotation rights, corrections, corroboration, subject response, and restrictions. Multimodal records preserve the original artifact, inspected page/time/sheet range, extraction method, derived artifact, transformations, missing content, and confidence.

For documentation portals and interconnected manuals, Unsloop adds content architecture, canonical ownership, reader journeys, dependencies, reused content, navigation, versions, lifecycle state, maintenance triggers, corrections, deprecation, withdrawal, and archival. Reader validation distinguishes simulated hypotheses, automated checks, expert review, and observed human testing.

When another skill applies, Unsloop composes with it rather than replacing it. Domain skills govern specialized facts and rules; artifact skills govern layout, rendering, formulas, executable code, and format-specific validation; Unsloop governs integrity, voice, provenance, revision, and readiness.

Unsloop also supports translation, localization, bilingual drafting, cross-language voice adaptation, and optional JSON, CSV, or other structured results. These preserve the same evidence, privacy, confidence, readiness, and approval limits as human-readable output.

### Optional sustained writing project command

```text
python .agents/skills/unsloop/scripts/writing_project.py init --root PATH --profile compact
python .agents/skills/unsloop/scripts/writing_project.py init --root PATH --profile research --style --apply
python .agents/skills/unsloop/scripts/writing_project.py init --root PATH --profile research --extra chronology --extra validation --apply
python .agents/skills/unsloop/scripts/writing_project.py init --root PATH --profile full --extra data --extra interviews --extra media --extra content-map --extra maintenance --extra usability --apply
python .agents/skills/unsloop/scripts/writing_project.py check --root PATH
python .agents/skills/unsloop/scripts/writing_project.py checkpoint --root PATH --name NAME --reason REASON --include FILE
python .agents/skills/unsloop/scripts/writing_project.py assemble --root PATH --output assembled/manuscript.md
python .agents/skills/unsloop/scripts/writing_project.py export --root PATH --output reports/project-state.json
```

`init`, `checkpoint`, `assemble`, and `export` preview by default and require `--apply` to write. Paths are confined to the selected project, existing destinations are never overwritten, checkpoints and outputs use hashes, assembly includes Accepted units only, and an optional `VOICE.md` requires `--voice --voice-authorized`.

## Harness and model compatibility

Unsloop uses standard `SKILL.md` metadata, portable Markdown instructions, and relative references. It does not require a particular AI provider, model name, proprietary tool, context size, or UI. It supports:

- **Codex** through the existing `.agents/skills` core, `$unsloop` invocation, `agents/openai.yaml`, and Codex-home link;
- **Claude Code** through a `.claude/skills/unsloop` link or copy and `/unsloop` invocation;
- **Pi** directly through `.agents/skills/unsloop`, or through `.pi/skills` and user-level Pi paths, with `/skill:unsloop` invocation;
- **other Agent Skills clients** through their documented skill directory or explicit skill path; and
- **other text-capable harnesses** by loading `SKILL.md` as project/system instructions and exposing adjacent references on demand.

Host capabilities are negotiated by function. Structured questions fall back to plain text; unavailable source access becomes an explicit evidence limit; unavailable file editing returns a delimited revision; unavailable persistence keeps voice data task-local. Compatibility does not promise identical output quality across models.

## Start here

- [`BRD.md`](BRD.md) — business need, stakeholders, scope, requirements, and success measures
- [`PRD.md`](PRD.md) — modes, use cases, functional and nonfunctional requirements, and acceptance criteria
- [`FSD.md`](FSD.md) — functional components, data concepts, processing flow, failure handling, and test traceability
- [`PROJECT.md`](PROJECT.md) — concise vision, principles, scope, and success definition
- [`HISTORY.md`](HISTORY.md) — narrative of how Unsloop evolved and which principles remained constant
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — project and skill structure
- [`docs/NAMING.md`](docs/NAMING.md) — naming system and mode boundaries
- [`docs/REVIEW-MODEL.md`](docs/REVIEW-MODEL.md) — the two-part method
- [`docs/SCORING-RUBRIC.md`](docs/SCORING-RUBRIC.md) — source-dependence and voice-profile scales
- [`docs/REVIEW-OUTPUT.md`](docs/REVIEW-OUTPUT.md) — output contracts
- [`docs/ETHICS-AND-LIMITS.md`](docs/ETHICS-AND-LIMITS.md) — claims Unsloop may and may not make
- [`docs/SOURCES.md`](docs/SOURCES.md) — research and guidance behind v0.1
- [`ROADMAP.md`](ROADMAP.md) — path from v0.1 to a validated release
- [`DECISIONS.md`](DECISIONS.md) — durable design decisions
- [`PORTABILITY.md`](PORTABILITY.md) — discovery, dependencies, and transfer guarantees
- [`.agents/skills/unsloop/references/fiction-workflow.md`](.agents/skills/unsloop/references/fiction-workflow.md) — scalable fiction lifecycle, project state, and continuity controls
- [`.agents/skills/unsloop/references/style-direction.md`](.agents/skills/unsloop/references/style-direction.md) — selectable Style Direction, authenticity stance, channel separation, and controlled evolution
- [`.agents/skills/unsloop/references/fiction-project-operations.md`](.agents/skills/unsloop/references/fiction-project-operations.md) — onboarding, acceptance, branches, retcons, and recovery
- [`.agents/skills/unsloop/references/character-voice-continuity.md`](.agents/skills/unsloop/references/character-voice-continuity.md) — immutable-until-approved character personality and speech profiles
- [`.agents/skills/unsloop/references/fiction-review.md`](.agents/skills/unsloop/references/fiction-review.md) — focused developmental, craft, continuity, and integrity review
- [`.agents/skills/unsloop/references/fiction-publication.md`](.agents/skills/unsloop/references/fiction-publication.md) — assembly, completion stages, and publication-support handoff
- [`.agents/skills/unsloop/references/sustained-writing-projects.md`](.agents/skills/unsloop/references/sustained-writing-projects.md) — portable long-form non-fiction state and resumption
- [`.agents/skills/unsloop/references/research-provenance.md`](.agents/skills/unsloop/references/research-provenance.md) — claim, source, quotation, conflict, and freshness tracking
- [`.agents/skills/unsloop/references/integrity-review.md`](.agents/skills/unsloop/references/integrity-review.md) — non-mutating Audit, source relationships, evidence testing, and proposed corrections
- [`.agents/skills/unsloop/references/writing-pattern-assistance-audit.md`](.agents/skills/unsloop/references/writing-pattern-assistance-audit.md) — calibrated pattern scoring, measurements, sample comparison, assistance provenance, and detector-report interpretation
- [`.agents/skills/unsloop/references/documentary-documentation.md`](.agents/skills/unsloop/references/documentary-documentation.md) — biography, documentary, procedure, policy, plan, instruction, and technical-document contracts
- [`.agents/skills/unsloop/references/source-acquisition.md`](.agents/skills/unsloop/references/source-acquisition.md) — supplied, scoped-site, broad-web, and hybrid research with override and confidence controls
- [`.agents/skills/unsloop/references/skill-composition.md`](.agents/skills/unsloop/references/skill-composition.md) — responsibility and authority when Unsloop runs beside another skill
- [`.agents/skills/unsloop/references/source-safety.md`](.agents/skills/unsloop/references/source-safety.md) — embedded-instruction isolation, safe acquisition, and sensitive-data protection
- [`.agents/skills/unsloop/references/quantitative-evidence.md`](.agents/skills/unsloop/references/quantitative-evidence.md) — numerical, dataset, table, chart, and calculation provenance
- [`.agents/skills/unsloop/references/interview-evidence.md`](.agents/skills/unsloop/references/interview-evidence.md) — consent, attribution, transcripts, corrections, and subject response
- [`.agents/skills/unsloop/references/multimodal-evidence.md`](.agents/skills/unsloop/references/multimodal-evidence.md) — OCR, audio/video, image, spreadsheet, and extraction boundaries
- [`.agents/skills/unsloop/references/documentation-systems.md`](.agents/skills/unsloop/references/documentation-systems.md) — content architecture, dependencies, maintenance, corrections, and archival
- [`.agents/skills/unsloop/references/usability-validation.md`](.agents/skills/unsloop/references/usability-validation.md) — comprehension, findability, task, accessibility, and observed-use validation
- [`.agents/skills/unsloop/references/revision-control.md`](.agents/skills/unsloop/references/revision-control.md) — bounded, recoverable, partially acceptable revision
- [`.agents/skills/unsloop/references/collaborative-writing.md`](.agents/skills/unsloop/references/collaborative-writing.md) — stakeholder authority and feedback reconciliation
- [`.agents/skills/unsloop/references/multilingual-writing.md`](.agents/skills/unsloop/references/multilingual-writing.md) — translation, localization, cross-language evidence, and voice
- [`.agents/skills/unsloop/references/structured-output.md`](.agents/skills/unsloop/references/structured-output.md) — machine-readable output contract
- [`.agents/skills/unsloop/references/output-contracts.md`](.agents/skills/unsloop/references/output-contracts.md) — Review, Write, and information-preserving Audit delivery contracts
- [`.agents/skills/unsloop/references/section-flow.md`](.agents/skills/unsloop/references/section-flow.md) — logical progression across chapters, headings, subheadings, scene breaks, and procedural phases
- [`.agents/skills/unsloop/references/delivery-and-presentation.md`](.agents/skills/unsloop/references/delivery-and-presentation.md) — timing, evidence flow, questions, audience layers, media decisions, closings, and synchronized output formats

## Install Unsloop

Unsloop has no required runtime dependencies:

- The baseline skill is Markdown and YAML.
- Git is needed only when cloning or updating the full project.
- Python is needed only for the optional validator, global-link helper, and project-operation commands.

Choose one primary installation method. The linked methods preserve this project as the authoritative source and are preferred for active development. Copied installations are independent snapshots and must be updated separately.

| Method | Scope | Updates | Best use |
|---|---|---|---|
| Clone and use in place | Canonical project; direct for Codex and Pi | `git pull` | Development, auditing, and full documentation |
| Copy or link into another repository | Codex/Pi `.agents`, Claude `.claude`, Pi `.pi`, or another client path | Link follows; copy must be replaced | Project-scoped use in any harness |
| Run the multi-harness link helper | Codex, shared Agent Skills, Claude, or Pi user path | Follows this checkout immediately | One authoritative checkout across harnesses |
| Create a shared Agent Skills user link | User-wide `$HOME/.agents/skills` | Follows this checkout immediately | Codex, Pi, and other clients that discover the shared path |
| Install with Codex `$skill-installer` | User-wide `$CODEX_HOME/skills` | Reinstall intentionally | One-command Codex installation without the full project |
| Install for an administrator-managed Codex host | `/etc/codex/skills` | Administrator-controlled | Shared Unix or container environments |
| Use a manual adapter | Harness-defined | Adapter-controlled | Clients without automatic Agent Skills discovery |

The [Agent Skills specification](https://agentskills.io/specification) defines the portable core. The current [OpenAI](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills), [Claude Code](https://code.claude.com/docs/en/slash-commands), and [Pi](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md) documentation establishes the harness paths and invocation forms below.

### Option 1 — Clone and use the repository directly

This is the simplest full-project installation and the authoritative development setup:

```text
git clone https://github.com/stamandster/Unsloop.git
cd Unsloop
python scripts/validate.py
```

Launch Codex or Pi anywhere inside the checkout. Both discover `.agents/skills/unsloop` from the repository without a user-level installation. Claude Code needs the project adapter in Option 2.

### Option 2 — Copy or link Unsloop into another repository

Copy the complete skill directory—not only `SKILL.md`—into the target repository:

**Windows PowerShell**

```powershell
$UnsloopRepo = Resolve-Path "..\Unsloop"
New-Item -ItemType Directory -Force ".agents\skills" | Out-Null
Copy-Item -Recurse "$UnsloopRepo\.agents\skills\unsloop" ".agents\skills\unsloop"
```

**macOS or Linux**

```bash
UNSLOOP_REPO="../Unsloop"
mkdir -p .agents/skills
cp -R "$UNSLOOP_REPO/.agents/skills/unsloop" .agents/skills/unsloop
```

Place the folder at the target repository root to make it available throughout that repository, or at a nested `.agents/skills` location to limit discovery to that subtree. Codex and Pi use this standard location directly. This copied version is no longer synchronized with the Unsloop project.

For Claude Code, link the canonical core from the target repository:

**Windows PowerShell**

```powershell
$UnsloopRepo = Resolve-Path "..\Unsloop"
New-Item -ItemType Directory -Force ".claude\skills" | Out-Null
New-Item -ItemType Junction -Path ".claude\skills\unsloop" -Target "$UnsloopRepo\.agents\skills\unsloop"
```

**macOS or Linux**

```bash
UNSLOOP_REPO="../Unsloop"
mkdir -p .claude/skills
ln -s "$UNSLOOP_REPO/.agents/skills/unsloop" .claude/skills/unsloop
```

Pi already reads the canonical `.agents/skills` path. If a Pi-specific project adapter is preferred, use the same commands with `.pi/skills/unsloop` as the destination.

### Option 3 — Link the project into user-level harness directories

From the Unsloop repository root, run:

```text
python scripts/link_global_skill.py
```

The helper targets `$CODEX_HOME/skills/unsloop`, falling back to `~/.codex/skills/unsloop`. It creates a Windows directory junction or a Unix directory symlink, is idempotent, and refuses to replace an unrelated destination. Check it without making changes:

```text
python scripts/link_global_skill.py --check
```

This is the established Codex global setup for this project and remains the default. Editing or updating the project immediately updates the globally discovered skill.

Select another harness or the shared Agent Skills location:

```text
python scripts/link_global_skill.py --harness standard
python scripts/link_global_skill.py --harness claude
python scripts/link_global_skill.py --harness pi
```

Repeat `--harness` for selected targets, or use `--harness all` for Codex, Claude, and Pi user directories. Use `--check` with the same selection to verify without changing it. Avoid both shared and harness-specific paths when the same host would discover duplicate `unsloop` entries.

### Option 4 — Link into the shared Agent Skills user location

The shared `$HOME/.agents/skills` location is documented by Codex and Pi and may be supported by other Agent Skills clients. Create the link manually when one shared user path is preferable to harness-specific paths.

**Windows PowerShell**

```powershell
$UnsloopRepo = Resolve-Path "."
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
New-Item -ItemType Junction -Path "$HOME\.agents\skills\unsloop" -Target "$UnsloopRepo\.agents\skills\unsloop"
```

**macOS or Linux**

```bash
mkdir -p "$HOME/.agents/skills"
ln -s "$PWD/.agents/skills/unsloop" "$HOME/.agents/skills/unsloop"
```

Run these commands from the Unsloop repository root. The destination must not already contain an unrelated `unsloop` skill.

### Option 5 — Install a standalone Codex user copy from GitHub

Invoke the built-in installer in Codex:

```text
$skill-installer Install the skill from https://github.com/stamandster/Unsloop/tree/main/.agents/skills/unsloop
```

The installer places a standalone copy under `$CODEX_HOME/skills/unsloop`—normally `~/.codex/skills/unsloop`. This method does not clone the BRD, PRD, FSD, project validator, or other maintainer documentation, and the installed copy does not automatically follow later repository changes.

For a manual standalone copy, copy the complete `.agents/skills/unsloop` directory into either the documented user location `$HOME/.agents/skills/unsloop` or the Codex-home compatibility location used by your host. Do not maintain both as independent copies.

### Option 6 — Install for an administrator-managed Codex host

Administrators may place or link the complete skill folder at `/etc/codex/skills/unsloop` for a shared machine or container. For example, from a stable Unsloop checkout:

```bash
sudo mkdir -p /etc/codex/skills
sudo ln -s "$PWD/.agents/skills/unsloop" /etc/codex/skills/unsloop
```

Use an administrator-controlled stable target. Bundled system skills are supplied by OpenAI; Unsloop does not modify that system bundle.

### Option 7 — Adapt a harness without Agent Skills discovery

Configure the harness to load `.agents/skills/unsloop/SKILL.md` as project or system instructions and allow it to read files under `.agents/skills/unsloop/references` when the main skill directs it there. Map semantic capabilities—asking a question, reading material, retrieving a source, editing an artifact, or storing an approved profile—to the host's native tools. If the host cannot perform one, use the fallback in [`harness-compatibility.md`](.agents/skills/unsloop/references/harness-compatibility.md).

Do not convert the core into vendor-specific syntax. Keep any wrapper, manifest, or invocation command outside the canonical skill directory so another harness can continue to use the same files.

### Plugin installation

Unsloop v0.1 is a standalone skill project, not a packaged plugin. There is currently no plugin-directory installation. A future plugin could distribute Unsloop beyond local and repository scopes, but it must preserve the same evidence, voice, ethics, and project-authority contracts.

## Verify, activate, and update

For a full checkout, run:

```text
python scripts/validate.py
```

For the project global-link method, also run:

```text
python scripts/link_global_skill.py --check
```

| Harness | Discovery check | Explicit invocation |
|---|---|---|
| Codex CLI or IDE | `/skills` | `$unsloop` |
| ChatGPT desktop Codex | **Skills** sidebar | `$unsloop` or skill picker |
| Claude Code | Skill/command listing | `/unsloop` |
| Pi | Startup skill list or settings | `/skill:unsloop` |
| Other client | Client documentation | Client-defined |

Unsloop can also activate implicitly when a compatible host matches the request to its description. If a newly created top-level skill directory is not detected, refresh or restart the harness according to its documentation.

Update a cloned checkout with `git pull`; linked installations follow that checkout automatically. Repository or user copies—including `$skill-installer` installations—are snapshots and must be deliberately replaced or reinstalled. Harnesses may merge, override, reject, or list same-named skills differently, so avoid divergent copies and use one authoritative location per discovery scope.

## Voice matching

For a close match, Unsloop may request two or three representative pieces previously written by the user, ideally in a similar genre. It derives an observable voice brief from those samples while keeping their facts, anecdotes, and distinctive wording out of the new work unless the user explicitly makes them relevant. Voice matching always reports its evidence basis and confidence; it never claims exact replication.

Factual references and voice samples have different jobs:

- Factual references support what the writing says.
- Voice samples help establish how it should sound.

Unsloop does not treat a sample's claims or experiences as evidence for the new work.

## Status

Version 0.1 is a documented, portable, specification-backed foundation with scalable fiction and sustained non-fiction operations across the existing modes. It is ready for controlled use and forward-testing; its scoring model remains interpretive, and behavioral matrices are structurally specified rather than empirically validated across models. See [`ROADMAP.md`](ROADMAP.md) for calibration and release work still required.
