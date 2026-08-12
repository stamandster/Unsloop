# Functional Specification Document

> **Product:** Unsloop · **Status:** v0.1 baseline
>
> **Upstream:** [`PRD.md`](PRD.md)
>
> **Operational implementation:** [`.agents/skills/unsloop/SKILL.md`](.agents/skills/unsloop/SKILL.md)

## Purpose

This document defines how the product requirements are executed by the portable Markdown/YAML Agent Skill, its progressive references, optional harness adapters, and project-owned maintenance scripts. It specifies behavior, data concepts, states, decision rules, failure handling, and verification without binding the method to one model provider or agent runtime.

## System boundary

The v0.1 system consists of:

- one canonical repository skill at `.agents/skills/unsloop`;
- one core `SKILL.md` that selects modes and orchestrates the workflow;
- one-level-deep references that hold detailed procedures;
- optional Codex UI metadata in `agents/openai.yaml`;
- project specifications and method documentation outside the runtime bundle;
- `scripts/validate.py` for deterministic structural checks; and
- `scripts/link_global_skill.py` for optional Codex, shared Agent Skills, Claude, or Pi discovery through the canonical directory.

No database, background service, model endpoint, provider account, or persistent user profile is required. A host must be able to load Markdown instructions and provide the task materials; every other capability has a bounded fallback.

## Functional components

| ID | Function | Inputs | Outputs | Product requirements |
|---|---|---|---|---|
| FS-001 | Mode and depth selection | User request, supplied artifact | Review, Write, or Audit; brief, standard, or deep depth | PR-001 |
| FS-002 | Topic-path resolution | Explicit topic, rough direction, or minimal seed context | Accepted topic or distinct topic proposals | PR-002, PR-012 |
| FS-003 | Progressive brief construction | Request, artifact, governing directions, references | `WritingBrief` with certainty, content roles, and constraints | PR-003, PR-004, PR-012 |
| FS-004 | Evidence and voice boundary construction | Draft, sources, verification access, voice samples, authorization | `EvidenceBoundary` and optional `VoiceBrief` | PR-005, PR-008, PR-013 |
| FS-005 | Integrity analysis | Draft plus available comparison evidence | Source relationships, claim findings, dependence assessment | PR-006, PR-011 |
| FS-006 | Human-voice analysis | Draft, writing brief, optional voice brief | Voice/slop findings, example and emotional-integrity findings | PR-007, PR-008 |
| FS-007 | Requirement and constraint audit | Brief, directions, artifact | `RequirementCoverage` records and constraint status | PR-004, PR-009 |
| FS-008 | Result assembly and readiness | Findings, coverage, evidence boundary, requested output | Mode-specific output and `ReadinessState` when material | PR-009 |
| FS-009 | Optional scoring | Supported findings and comparison evidence | Separated strength, risk, dependence, fidelity, and severity values | PR-010 |
| FS-010 | Source verification | Citation, claim, source/version, available access | Verification status and bounded result | PR-005, PR-011 |
| FS-011 | Discovery and distribution | Repository path, selected harness or shared Agent Skills path | Repo discovery or one or more filesystem links to the canonical core | PR-014, PR-015 |
| FS-012 | Structural validation | Project files | Pass/fail diagnostics with actionable errors | PR-014; NFR-001, NFR-002, NFR-005 |
| FS-013 | Harness and model adaptation | Host capabilities, model limits, discovery and invocation conventions | Capability map, adapter selection, and explicit fallbacks | PR-012, PR-015; NFR-006, NFR-007 |

## Requirements traceability

| Requirement | Implemented by |
|---|---|
| PR-001 | FS-001 |
| PR-002 | FS-002 |
| PR-003 | FS-003 |
| PR-004 | FS-003, FS-007 |
| PR-005 | FS-004, FS-005, FS-010 |
| PR-006 | FS-005 |
| PR-007 | FS-006 |
| PR-008 | FS-004, FS-006 |
| PR-009 | FS-007, FS-008 |
| PR-010 | FS-009 |
| PR-011 | FS-005, FS-010 |
| PR-012 | FS-002, FS-003 |
| PR-013 | FS-004–FS-010 and governing ethics rules |
| PR-014 | FS-011, FS-012 |
| PR-015 | FS-011, FS-013 |
| NFR-001 | FS-011, FS-012 |
| NFR-002 | FS-012 |
| NFR-003 | FS-004–FS-008 |
| NFR-004 | FS-004 and privacy controls |
| NFR-005 | Progressive references and FS-012 |
| NFR-006 | FS-002, FS-008, FS-009 |
| NFR-007 | FS-011, FS-012, FS-013 |

## Logical data model

These are conceptual records. The current skill may hold them in working context rather than serialized files.

### `WritingBrief`

| Field | Type or values | Rule |
|---|---|---|
| topic | text | Subject plus relevant boundaries. |
| goal | text | Intended reader outcome; distinct from topic. |
| audience | text/traits | Needs, concerns, resistance, emotional situation, relationship, desired response. |
| prior_knowledge | text | Known, assumed, misunderstood, or explanation needed. |
| context | text | Occasion, channel, stakes, surrounding conversation. |
| directions | ordered list | Resolved through the direction hierarchy. |
| content_items | list | Each item is Required, Optional supporting, Background only, or Excluded. |
| references | list | Factual sources or leads; never silently treated as voice evidence. |
| voice_target | text/reference | Explicit traits and authorized sample basis. |
| constraints | list | Hard constraint, Working target, Allocation, or Safety buffer. |
| certainty | per-field enum | Known, Inferred, or Unknown. |

### `EvidenceBoundary`

Record the draft version, supplied excerpts, full supplied sources, externally verified sources, inaccessible sources, similarity reports, and access level. Access level is `Full`, `Excerpt`, `Abstract/metadata`, `Secondary`, or `Unavailable`.

### `VoiceBrief`

Record only task-relevant observable traits: register, directness, cadence, vocabulary, viewpoint, certainty, warmth, transitions, punctuation, rhetorical habits, preferred or avoided expressions, useful irregularity, basis, confidence, and limitations. Do not store sample facts, identity inferences, or a persistent profile by default.

### `Finding`

| Field | Values |
|---|---|
| location | Short excerpt or precise artifact location |
| observation | Concrete visible feature |
| interpretation | Supported inference, unverified concern, or out-of-scope judgment |
| impact | Integrity, meaning, credibility, goal, requirement, or voice consequence |
| evidence | Comparison passage, claim check, brief requirement, or textual pattern |
| severity | Low, Moderate, High, or Critical |
| confidence | Calibrated narrative or Low/Moderate/High where used |
| correction | Smallest useful intervention |

### `RequirementCoverage`

Record requirement or direction, content role, artifact location, support or decision, and status: `Satisfied`, `Partial`, `Missing`, `Conflict`, or `Not applicable`. Presence and factual support are separate dimensions.

### `ReadinessState`

- `Ready`
- `Ready with noted limitations`
- `Provisional—decision required`
- `Not ready—evidence or authorization missing`

Omit readiness when it would add no practical information.

### `HostCapabilityMap`

Record only capabilities material to the task: structured choice, file or attachment access, external retrieval, artifact editing, persistent storage, reliable length measurement, and invocation/discovery behavior. For each unavailable capability, select the fallback in the harness-compatibility procedure and reduce the evidence boundary or readiness state when necessary.

## Processing flow

```text
Request and materials
  -> FS-013 identify host capabilities and material model limits
  -> FS-001 select mode and depth
  -> FS-002 resolve topic path when new writing lacks a topic
  -> FS-003 build the smallest sufficient WritingBrief
  -> FS-004 establish evidence boundary and optional VoiceBrief
  -> FS-005 and/or FS-006 apply relevant analysis lenses
  -> FS-007 check requirements and hard constraints when material
  -> FS-009 score only when justified
  -> FS-008 assemble the mode contract and readiness state
```

### FS-001 — Select mode and depth

1. Choose Audit for explicit source, citation, similarity, or evidence-heavy comparison.
2. Choose Write for requested drafting or revision.
3. Choose Review for broad diagnosis of existing writing.
4. Apply only the depth warranted by the request and available evidence.

### FS-002 — Resolve topic

If the request already supplies a topic, accept it. Otherwise ask whether to use an existing topic, refine a direction, or brainstorm topics. Use a structured selector only when available and suitable. Brainstormed options must differ materially in angle, reader value, scope, or evidence needs.

### FS-003 — Build the brief

Extract before asking. Mark material fields Known, Inferred, or Unknown. Ask only about unknowns or conflicts that could change accuracy, integrity, structure, tone, privacy, policy exposure, or usefulness. Resolve directions in this order: non-waivable obligations, current explicit instructions, applicable artifact directions, confirmed decisions, then genre defaults.

### FS-004 — Establish evidence and voice boundaries

Keep four channels distinct: governing directions, factual references, voice evidence, and verification results. When fidelity matters and evidence is thin, request representative authorized samples. If unavailable, continue where safe with lower confidence. Never import sample content merely to increase resemblance.

### FS-005 — Apply the integrity lens

Compare wording, syntax, idea order, detail selection, and rhetorical architecture. Classify only what the evidence supports: proper quotation, acceptable paraphrase, too-close paraphrase, structural dependence, unattributed borrowing, secondary-source problem, self-reuse, or unsupported/fabricated support. Do not infer intent.

### FS-006 — Apply the human-voice lens

Inspect the document as a whole, then identify repeated patterns rather than banned words. Test specificity, authorial presence, discontinuity, redundancy, formulaicity, abstraction, example function, emotional integrity, and alignment with an established voice brief. Preserve strong and useful irregularity.

### FS-007 — Audit requirements and constraints

Create coverage records only when a meaningful requirement set exists. Reconcile allocations with the total constraint, preserve safety buffers, and keep missing support separate from missing content.

### FS-008 — Assemble output

Use the mode contract in [`docs/REVIEW-OUTPUT.md`](docs/REVIEW-OUTPUT.md). Rank findings by consequence and confidence. Include only requested revisions. Add assumptions, voice basis, scores, tables, or readiness labels only when they materially improve usability or honesty.

### FS-009 — Score

Use the anchors in [`docs/SCORING-RUBRIC.md`](docs/SCORING-RUBRIC.md). Never combine all dimensions into one total. Use N/A when the evidence cannot support a dimension. A score must remain subordinate to passage-level evidence and rationale.

### FS-010 — Verify sources

Identify the exact source version, prefer the original, inspect relevant context, compare the draft's strength and scope, and label the result Verified, Partially verified, Secondary confirmation, or Unverified. Follow current browsing and citation requirements when external verification is requested.

### FS-011 — Discover and distribute

Keep `.agents/skills/unsloop` canonical. Codex and Pi can discover that repository path directly. Claude uses a `.claude/skills/unsloop` adapter, while Pi may also use `.pi/skills/unsloop`; other clients use their documented Agent Skills path or an explicit path to `SKILL.md`. Optional user-wide exposure may use `scripts/link_global_skill.py`; the utility creates harness-selected junctions or symlinks to the project skill, behaves idempotently, and refuses to replace unrelated content. Existing Codex behavior remains the default.

### FS-012 — Validate

The project validator must check required files, standard frontmatter and name, optional Codex UI metadata, normative tokens, unresolved placeholders, local Markdown links, portability hazards, harness-compatibility rules, and the multi-harness link utility. The core must pass an Agent Skills-compatible validator; Codex validation must continue to pass for both the canonical path and its existing global link.

### FS-013 — Adapt to harness and model

Inspect the active host's exposed capabilities rather than inferring them from a vendor name. Map structured questions, file access, source retrieval, editing, storage, and length checks to native tools when present and to the documented plain-text or user-supplied fallback when absent. Keep model-specific context, modality, and consistency limits visible, scale the task when necessary, and never relax evidence or ethics rules. Do not require private chain-of-thought or a named model.

## Failure and boundary handling

| Condition | Required behavior |
|---|---|
| Topic or goal materially unresolved | Ask the smallest consequential question or mark the result provisional. |
| Required fact or source missing | Do not invent; identify the missing evidence and reduce readiness. |
| Voice authorization ambiguous | Confirm authorization or use general style adaptation rather than identity imitation. |
| User declines voice samples | Continue when safe with available evidence and lower confidence. |
| Source only partly accessible | Limit the claim and use the corresponding verification status. |
| Directions conflict | Surface the conflict and apply the direction hierarchy; do not silently choose. |
| Hard constraints cannot all be met | Explain the conflict and request a decision when the user has authority. |
| High-stakes verdict requested | Provide decision support only and require qualified human review. |
| Global destination already contains unrelated files | Refuse replacement and report the collision. |

## Verification matrix

| Test | Requirement coverage | Expected result |
|---|---|---|
| Clear topic in request | PR-002 / FS-002 | No redundant topic question. |
| No topic, structured control unavailable | PR-002, PR-012 / FS-002 | Equivalent three-path plain-text question. |
| Sparse voice evidence | PR-008 / FS-004 | Sample request or disclosed Low confidence; no exact-match claim. |
| Draft-only plagiarism request | PR-005, PR-006 / FS-004, FS-005 | Review leads only; no source-dependence verdict. |
| Full draft and sources | PR-006, PR-011 / FS-005, FS-010 | Classified relationships with bounded verification. |
| Multi-part rubric | PR-004, PR-009 / FS-007, FS-008 | Coverage map separate from factual support. |
| Scoring without comparison source | PR-010 / FS-009 | Source independence and dependence are N/A/not scored. |
| Unresolved required authorization | PR-009, PR-013 / FS-008 | Not ready—evidence or authorization missing. |
| Repository copied to another machine | PR-014 / FS-011, FS-012 | No machine path required; validation passes. |
| Global link already correct | PR-014 / FS-011 | Idempotent success; no duplicate copy. |
| Claude project adapter | PR-015 / FS-011, FS-013 | `.claude/skills/unsloop` resolves to the canonical core and `/unsloop` can load it. |
| Pi repository use | PR-015 / FS-011, FS-013 | Pi discovers canonical `.agents/skills/unsloop` or a selected `.pi/skills` adapter. |
| Harness lacks structured input | PR-012, PR-015 / FS-013 | The same consequential choices appear in concise plain text. |
| Model context cannot hold the corpus | PR-005, PR-015 / FS-004, FS-013 | Work is partitioned explicitly and conclusions are bounded to inspected material. |

## Change control

Changes to business scope begin in [`BRD.md`](BRD.md). Changes to user-visible behavior or acceptance criteria begin in [`PRD.md`](PRD.md). Changes to workflow, data concepts, operational references, or validation begin here and in the corresponding implementation files. Record durable tradeoffs in [`DECISIONS.md`](DECISIONS.md) and staged work in [`ROADMAP.md`](ROADMAP.md).
