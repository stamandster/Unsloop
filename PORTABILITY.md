# Portability

> **Document role:** Deployment, harness, and transfer sub-specification for `PR-014`–`PR-047`, `NFR-001`–`NFR-002`, `NFR-007`–`NFR-021`, and `FS-011`–`FS-046` in [`PRD.md`](PRD.md) and [`FSD.md`](FSD.md).

## Guarantee

Unsloop's canonical operational core lives at `.agents/skills/unsloop`. Copying or cloning the project preserves the full writing lifecycle—from topic discovery through drafting, revision, review, audit, research, validation, maintenance, and handoff—together with its relative references, optional harness metadata, product documentation, link utility, and validator as one unit.

The core is both harness-agnostic and model-agnostic:

- `SKILL.md` uses standard `name` and `description` frontmatter;
- every operational reference is relative to the skill directory;
- no provider, model ID, proprietary tool name, hidden reasoning format, or UI control is required;
- missing host capabilities have explicit fallbacks; and
- evidence, voice, personal-perspective preservation, section-flow, delivery-readiness, artifact-synchronization, writing-pattern authorship boundaries, privacy, ethics, and non-mutating Audit rules do not change across hosts.

Compatibility means the same method can load and run. It does not promise identical reasoning quality, context capacity, tool access, latency, cost, or output across models.

## Portable core and adapters

```text
.agents/skills/unsloop/       authoritative portable core
├── SKILL.md                  standard metadata + workflow
├── references/               on-demand portable procedures
├── assets/                   optional templates and schema
├── scripts/                  optional standard-library project operations
└── agents/openai.yaml        optional Codex UI adapter

Harness discovery link/copy   optional adapter to the same core
Model and tool selection      supplied by the active harness
```

Discovery paths, invocation syntax, UI metadata, and tool mappings are adapters. They may expose the core but must not fork or rewrite its method. An adapter must not collapse Audit and revision into one mutation step merely because the host offers in-place editing.

## Harness matrix

| Harness or client | Repository scope | User scope | Explicit invocation | Notes |
|---|---|---|---|---|
| Codex | `.agents/skills/unsloop` | `$HOME/.agents/skills/unsloop`; existing project helper also supports `$CODEX_HOME/skills/unsloop` | `$unsloop`; `/skills` lists skills in CLI/IDE | Existing Codex behavior and `agents/openai.yaml` are retained. |
| Claude Code | `.claude/skills/unsloop` | `$HOME/.claude/skills/unsloop` | `/unsloop` | Link or copy the same core; do not add Claude-only frontmatter to canonical `SKILL.md`. |
| Pi | `.agents/skills/unsloop` or `.pi/skills/unsloop` | `$HOME/.agents/skills/unsloop` or `$HOME/.pi/agent/skills/unsloop` | `/skill:unsloop` | Pi can use the canonical repository path directly. |
| Other Agent Skills clients | Client-defined Agent Skills path | Client-defined | Client-defined | Point the client at the directory containing `SKILL.md`. |
| Harness without skill discovery | Project/system instruction adapter | Harness-defined | Prompt or command defined by host | Load `SKILL.md` and permit on-demand access to adjacent references. |

Verified discovery sources are recorded in [`docs/SOURCES.md`](docs/SOURCES.md). Harness paths can change; keep adapter documentation versioned and do not make them part of the writing method.

## Codex discovery remains supported

Codex scans `.agents/skills` from the current working directory upward to the repository root. Launch Codex anywhere inside this repository to make the root Unsloop skill available. If a host does not refresh after a file change, restart Codex.

This follows the [official OpenAI documentation for repository-scoped skills](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills). The existing Codex-home link remains available and is still the default behavior of `scripts/link_global_skill.py`.

## Claude discovery

Claude Code follows the Agent Skills format but discovers project skills under `.claude/skills` and user skills under `$HOME/.claude/skills`. Create a junction, symlink, or copy named `unsloop` that points to the canonical `.agents/skills/unsloop` directory. Invoke it with `/unsloop` or allow description-based activation.

## Pi discovery

Pi discovers `.agents/skills/unsloop` from the working directory or its ancestors, so this repository needs no adapter. Pi also supports `.pi/skills/unsloop`, `$HOME/.agents/skills/unsloop`, and `$HOME/.pi/agent/skills/unsloop`. Invoke it explicitly with `/skill:unsloop` when automatic selection is insufficient.

## Runtime dependencies

The baseline portable skill runtime consists only of:

- `SKILL.md`;
- relative Markdown references; and
- optional host metadata ignored safely by clients that do not use it.

Bundled project templates, the JSON schema, and standard-library project scripts are optional capabilities. A model can follow the same workflows manually when Python or file execution is unavailable.

Quantitative, interview, media, content-map, maintenance, and usability ledgers are ordinary Markdown. Format-specific tools may calculate, transcribe, OCR, render, or inspect an artifact, but the portable records retain the original-to-derived boundary and do not depend on that tool afterward.

It requires no package manager, build step, MCP server, memory service, API key, environment variable, absolute filesystem path, or user-level configuration. Durable project decisions live in checked-in Markdown, so using Unsloop does not depend on a memory service.

External access is optional and task-driven. A normal writing review works offline. An Audit that verifies online sources requires a host with source access or user-supplied source text. If neither exists, Unsloop marks the claim unverified instead of changing standards or rewriting the audited claim.

When external access exists, the portable contract governs it by capability rather than vendor: User-provided only, Scoped web, Broad web, or Hybrid. A host that cannot enforce a domain filter must navigate only approved locators or ask the user to supply pages; it may not silently approximate a scoped corpus with general search. Source suitability, verification, confidence, override, and actual test status remain separate in every harness.

Retrieved content is never a harness instruction. Every adapter must isolate source text, metadata, repositories, transcripts, images, and datasets from tool authority, permissions, credentials, private context, and project mutation. Hosts with different security models may narrow acquisition further but cannot relax this boundary.

Persistent fiction projects use visible, relative Markdown beneath an author-approved `story/` and `manuscript/` layout. These are outputs in the user's writing project, not runtime dependencies or hidden Unsloop state. `story/STATUS.md` provides a compact resume packet so another compatible model can continue from the accepted checkpoint without a memory service or the complete conversation. Existing coherent project layouts remain authoritative and need not be migrated to this default.

Unsloop bundles reusable fiction templates as optional assets and `scripts/fiction_project.py` as an optional standard-library utility. The utility is not required to write or review fiction. It defaults mutation-capable operations to dry-run, confines paths to the selected project, refuses existing destinations, and has a manual Markdown fallback. Projects created from the templates remain ordinary author-owned files with no Unsloop runtime dependency.

Interactive presentation adapts to the host. A native structured-input control may present short choices; plain text preserves the same decision when no such control exists. In Write or separately authorized revision, a native file editor may apply changes; otherwise Unsloop returns a delimited revision. Audit alone never invokes in-place mutation. Voice samples remain task inputs and are not persisted unless the user explicitly authorizes storage through an available mechanism.

## Optional user-level links

The project utility preserves its original Codex default:

```text
python scripts/link_global_skill.py
python scripts/link_global_skill.py --check
```

Select another harness without changing the canonical source:

```text
python scripts/link_global_skill.py --harness standard
python scripts/link_global_skill.py --harness claude
python scripts/link_global_skill.py --harness pi
```

Repeat `--harness` to manage multiple explicit targets, or use `--harness all` for Codex, Claude, and Pi user locations. The `standard` target is `$HOME/.agents/skills/unsloop`; select it instead of a harness-specific location when the clients you use all discover the shared path. Avoid installing the same skill in both a shared and harness-specific path if that host would show duplicates.

On Windows the utility creates directory junctions; on other supported systems it creates directory symlinks. It is idempotent and refuses to replace an unrelated existing destination. Links contain no independent copy, so project edits are immediately visible through every selected path.

## Model and capability adaptation

Unsloop supports text-capable models that can follow the skill and inspect the required material. At runtime:

1. identify only the host capabilities material to the request;
2. map semantic needs to native tools rather than assuming tool names;
3. use the fallback in `references/harness-compatibility.md` when a capability is absent;
4. partition large corpora explicitly when model context is insufficient;
5. retain a precise evidence boundary for every inspected section; and
6. report concise conclusions and rationale without requesting private chain-of-thought.

A weaker model or smaller context may justify a narrower task, more explicit checkpoints, or lower confidence. It never justifies fabricated support, weaker attribution, unauthorized voice imitation, or an unqualified readiness claim.

## Validation

Run from the project root:

```text
python scripts/validate.py
```

The dependency-free validator checks:

- repository-local canonical placement;
- Agent Skills frontmatter and skill naming;
- optional Codex UI metadata;
- required project documents and operational references;
- harness-compatibility, writing-brief, voice-fidelity, evidence, and ethics safeguards;
- fiction routing, onboarding, state-transition, retcon, recovery, review, publication, template, and tooling contracts;
- character voice profile, contextual-variation, drift, author-override, and profile-version contracts;
- sustained non-fiction, provenance, revision, collaboration, multilingual, structured-output, template, and tooling contracts;
- documentary/documentation form, source-acquisition scope, source-override, chronology, and validation-state contracts;
- skill-composition, untrusted-source isolation, quantitative, interview, multimodal, documentation-system, maintenance, and reader-validation contracts;
- Audit information preservation, semantic-change classification, structured artifact state, and separate revision authorization;
- the project-owned multi-harness link utility;
- BRD, PRD, and FSD traceability;
- unresolved placeholders and broken relative Markdown links; and
- accidental machine-specific absolute paths.

Python is not required to use Unsloop; it is required only for these optional maintenance checks and link operations.

## Transfer checklist

After copying or cloning the project:

1. Keep `.agents/skills/unsloop` intact as the canonical core.
2. Run `python scripts/validate.py` if Python is available.
3. Use the canonical location directly when the harness supports it; otherwise create one adapter link or copy in the harness's documented discovery path.
4. Start or refresh the harness and use its explicit invocation once to confirm discovery.
5. Test any material optional capability—structured input, browsing, file editing, storage, or length validation—before relying on it.
6. For a transferred fiction project, open `story/STATUS.md`, verify its referenced files exist, and bound continuation to the manuscript and ledgers actually inspected.
7. For a transferred sustained non-fiction project, open `writing/STATUS.md`, verify its relative references, and recheck any claim whose source version, wording, or inspected boundary changed.
8. For transferred research, confirm `SOURCE-POLICY.md` still reflects the intended corpus and that scoped domains, overrides, last-checked dates, and validation evidence remain current.
9. Confirm that active specialist skills still own the same domain and artifact properties and that no transferred source content has been promoted to instructions.
10. For transferred documentation systems, inspect `CONTENT-MAP.md`, `MAINTENANCE.md`, and relevant evidence ledgers before claiming currentness or usability.
11. For a transferred Audit, retain the authoritative inspected artifact or identifier, confirm its unchanged state, and keep proposed corrections separate from any revised artifact and authorization record.
12. For a transferred Writing-Pattern and Assistance Audit, preserve the inspected range, authorized sample boundary, measurement method, provenance records, detector-report metadata, and the rule that no host may convert them into a composite AI probability.

Do not maintain divergent independent copies under the same skill name. The root specifications and method documents need not load during every invocation, but they must travel with the authoritative repository so maintainers can reproduce the product's rationale, requirements, and validation contract.
