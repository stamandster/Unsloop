# Unsloop

**Writing integrity and human-voice review.**

Unsloop is a writing-quality project built around a simple idea: judge the text and the evidence, not a detector score or a stylistic hunch.

The project is governed by a traceable specification stack: [`BRD.md`](BRD.md) defines the business need and boundaries, [`PRD.md`](PRD.md) defines product behavior and acceptance criteria, and [`FSD.md`](FSD.md) defines the executable workflow and validation model. The project directory is authoritative across local, user-wide, and harness-specific use.

For new writing, Unsloop begins by determining whether the user already has a topic, has a rough direction to refine, or wants to brainstorm distinct topic options. If the topic is already clear, it does not ask the user to repeat it. When the active harness exposes a structured choice control—including Codex's control—Unsloop uses it for short, consequential decisions; otherwise it presents the same choices conversationally without changing execution modes. It then builds a progressive writing brief from what the user has already supplied: topic, goal, audience, prior knowledge, context, governing directions, content roles, exclusions, reference material, voice target, and format or delivery constraints. It marks material details as known, inferred, or unknown and asks only about gaps that could change the result.

For substantial or tightly constrained work, the brief also separates governing directions from factual evidence, classifies material as required, optional, background-only, or excluded, and distinguishes hard constraints from working targets. Reviews can map requirement coverage, test whether examples and emotional appeals earn their place, and label materially unresolved work as provisional instead of presenting it as final.

It supports three related jobs:

- **Unsloop Review** — diagnose clarity, integrity, specificity, and voice.
- **Unsloop Write** — draft or revise while preserving the writer's intent and matching their evidenced tone and language style.
- **Unsloop Audit** — examine source use, attribution, evidence, and source dependence in depth.

The implementation is one extensible, repository-scoped [Agent Skill](https://agentskills.io/specification) at [`.agents/skills/unsloop/SKILL.md`](.agents/skills/unsloop/SKILL.md). The operational core is model- and harness-agnostic. Codex and Pi discover the canonical repository path directly; Claude Code and other clients use thin discovery adapters pointing to the same directory. Codex support, UI metadata, invocation, and global-link behavior remain fully supported.

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

## Install Unsloop

Unsloop has no runtime dependencies: the skill itself is Markdown and YAML. Git is needed only when cloning or updating the full project, and Python is needed only for the optional validator and global-link helper.

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

Version 0.1 is a documented, portable, specification-backed foundation. It is ready for controlled use and forward-testing, but its scoring model is an interpretive rubric—not a validated measurement instrument. See [`ROADMAP.md`](ROADMAP.md) for calibration and release work still required.
