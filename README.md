# Unsloop

**Writing integrity and human-voice review.**

Unsloop is a writing-quality project built around a simple idea: judge the text and the evidence, not a detector score or a stylistic hunch.

The project is governed by a traceable specification stack: [`BRD.md`](BRD.md) defines the business need and boundaries, [`PRD.md`](PRD.md) defines product behavior and acceptance criteria, and [`FSD.md`](FSD.md) defines the executable workflow and validation model. The project directory is authoritative across local, user-wide, and harness-specific use.

For new writing, Unsloop begins by determining whether the user already has a topic, has a rough direction to refine, or wants to brainstorm distinct topic options. If the topic is already clear, it does not ask the user to repeat it. When the active harness exposes a structured choice control—including Codex's control—Unsloop uses it for short, consequential decisions; otherwise it presents the same choices conversationally without changing execution modes. It then builds a progressive writing brief from what the user has already supplied: topic, goal, audience, prior knowledge, context, governing directions, content roles, exclusions, reference material, voice target, and format or delivery constraints. It marks material details as known, inferred, or unknown and asks only about gaps that could change the result.

For substantial or tightly constrained work, the brief also separates governing directions from factual evidence, classifies material as required, optional, background-only, or excluded, and distinguishes hard constraints from working targets. Reviews can map requirement coverage, test whether examples and emotional appeals earn their place, and label materially unresolved work as provisional instead of presenting it as final.

For manuscripts with chapters, headings, subheadings, scene breaks, or procedural phases, Unsloop evaluates the transition across the preceding close, the visible boundary, and the next opening. It makes the logical relationship legible without adding canned bridges, and it preserves deliberate hard breaks when they serve the narrative, argument, chronology, or task.

For speeches, presentations, lessons, narrated scripts, podcasts, voiceovers, demonstrations, and other delivered writing, Unsloop treats the real delivery as part of the artifact. It reconciles overall and section constraints; counts readings, pauses, questions, media, and interaction; gives evidence a clear audience-facing function; and keeps unresolved consequential media choices provisional. When multiple formats are required, it identifies the authoritative source and reports which derivatives were actually refreshed, rendered, played, compared, or otherwise validated.

It supports three related jobs:

- **Unsloop Review** — diagnose clarity, integrity, specificity, and voice.
- **Unsloop Write** — draft or revise while preserving the writer's intent and matching their evidenced tone and language style; its fiction workflow scales from a single scene to a novel, serial, or series.
- **Unsloop Audit** — examine source use, attribution, evidence, and source dependence in depth without changing the audited artifact.

Audit is information-preserving by default: it may change the assessment of a passage, but not the passage itself. Incorrect, unsupported, contradictory, misleading, or overly source-dependent information is reported as a finding with a separate proposed correction. If the user requests Audit plus revision, Unsloop preserves the Audit as a distinct stage, classifies presentation-only versus meaning-changing edits, and applies only the explicitly bounded revision scope.

The implementation is one extensible, repository-scoped [Agent Skill](https://agentskills.io/specification) at [`.agents/skills/unsloop/SKILL.md`](.agents/skills/unsloop/SKILL.md). The operational core is model- and harness-agnostic. Codex and Pi discover the canonical repository path directly; Claude Code and other clients use thin discovery adapters pointing to the same directory. Codex support, UI metadata, invocation, and global-link behavior remain fully supported.

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
python .agents/skills/unsloop/scripts/fiction_project.py init --root PATH --profile full --apply
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
python .agents/skills/unsloop/scripts/writing_project.py init --root PATH --profile research --apply
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
- [`.agents/skills/unsloop/references/fiction-project-operations.md`](.agents/skills/unsloop/references/fiction-project-operations.md) — onboarding, acceptance, branches, retcons, and recovery
- [`.agents/skills/unsloop/references/character-voice-continuity.md`](.agents/skills/unsloop/references/character-voice-continuity.md) — immutable-until-approved character personality and speech profiles
- [`.agents/skills/unsloop/references/fiction-review.md`](.agents/skills/unsloop/references/fiction-review.md) — focused developmental, craft, continuity, and integrity review
- [`.agents/skills/unsloop/references/fiction-publication.md`](.agents/skills/unsloop/references/fiction-publication.md) — assembly, completion stages, and publication-support handoff
- [`.agents/skills/unsloop/references/sustained-writing-projects.md`](.agents/skills/unsloop/references/sustained-writing-projects.md) — portable long-form non-fiction state and resumption
- [`.agents/skills/unsloop/references/research-provenance.md`](.agents/skills/unsloop/references/research-provenance.md) — claim, source, quotation, conflict, and freshness tracking
- [`.agents/skills/unsloop/references/integrity-review.md`](.agents/skills/unsloop/references/integrity-review.md) — non-mutating Audit, source relationships, evidence testing, and proposed corrections
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

Unsloop has no required runtime dependencies: the baseline skill is Markdown and YAML. Git is needed only when cloning or updating the full project, and Python is needed only for the optional validator, global-link helper, and project-operation commands.

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

Factual references and voice samples have different jobs: references support what the writing says; samples help establish how it should sound. Unsloop does not treat a sample's claims or experiences as evidence for the new work.

## Status

Version 0.1 is a documented, portable, specification-backed foundation with scalable fiction and sustained non-fiction operations across the existing modes. It is ready for controlled use and forward-testing; its scoring model remains interpretive, and behavioral matrices are structurally specified rather than empirically validated across models. See [`ROADMAP.md`](ROADMAP.md) for calibration and release work still required.
