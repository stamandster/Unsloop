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
| FS-014 | Fiction lifecycle orchestration | Fiction request, `FictionBrief`, existing materials, collaboration cadence | Proportionate discovery, architecture, drafting, revision, checkpoint, or handoff action | PR-016, PR-017; NFR-008 |
| FS-015 | Fiction project state and continuity | Approved layout, manuscript, story records, accepted decisions | Resumable `StoryProjectState`, classified canon, updated scene state, and bounded continuity result | PR-017; NFR-001, NFR-004, NFR-008 |

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
| PR-016 | FS-002, FS-003, FS-006, FS-008, FS-014 |
| PR-017 | FS-004, FS-007, FS-008, FS-013–FS-015 |
| NFR-001 | FS-011, FS-012 |
| NFR-002 | FS-012 |
| NFR-003 | FS-004–FS-008 |
| NFR-004 | FS-004 and privacy controls |
| NFR-005 | Progressive references and FS-012 |
| NFR-006 | FS-002, FS-008, FS-009 |
| NFR-007 | FS-011, FS-012, FS-013 |
| NFR-008 | FS-013, FS-014, FS-015 |

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

### `CollaborationCadence`

| Value | Checkpoint rule |
|---|---|
| `Guided` | Approve every major development phase and each requested drafting unit. |
| `Adaptive` | Approve the creative contract, architecture, and drafting batches; pause again for consequential deviations or unresolved choices. This is the default. |
| `Autonomous` | Approve the creative contract and maximum batch, then work through that checkpoint while preserving every locked decision. |

The cadence may change prospectively at the user's direction. It never authorizes a silent retcon, a change to a content boundary, or work beyond the approved batch.

### `FictionBrief`

Extend the applicable `WritingBrief` fields with:

| Field | Type or values | Rule |
|---|---|---|
| form_scale | scene, flash, short story, novella, novel, serial, or series | Controls workflow ceremony, not quality expectations. |
| starting_state | idea, notes, outline, partial draft, complete draft, revision, or continuation | Inspect existing artifacts before proposing new state. |
| premise | text | Situation, destabilizing pressure, and narrative engine. |
| reader_experience | text | Intended tension, question, feeling, or movement; no moral or lesson is required. |
| genre_tone | text/list | Genre expectations, atmosphere, realism, humor, darkness, and boundaries. |
| narration | record | POV system, person, tense, narrative distance, reliability, and switching rules. |
| story_elements | references | Characters, setting, conflict, chronology, arcs, ending direction, and known scenes. |
| research_boundary | record | Real-world facts, sources, unresolved questions, and invented rules kept separate. |
| cadence | `CollaborationCadence` | Ask only when sustained work needs a checkpoint contract and the preference is unknown. |
| batch_limit | unit/count/target | Maximum planning or manuscript work before the next checkpoint. |
| locked_decisions | list | Author-owned choices that require approval to change. |

### `CanonEntry`

| Field | Type or values | Rule |
|---|---|---|
| fact_or_rule | text | A story-world fact, relationship, rule, event, or constraint. |
| state | Proposed, Confirmed, or Superseded | New autonomous details remain Proposed until the user accepts the batch. |
| scope | project, series, book, timeline, viewpoint, or version | Prevent a local fact from becoming universal silently. |
| basis | user direction, accepted manuscript, accepted plan, or approved retcon | Identify why the state is authoritative. |
| superseding_decision | optional reference | Required when a Confirmed entry becomes Superseded. |

### `SceneRecord`

Record a stable scene ID, manuscript location, status, POV, time, place, entry state, purpose, objective or pressure, obstacle, turn, consequence, exit state, knowledge and reveals, setup/payoff effects, affected arcs, research needs, and continuity notes. Do not require artificial conflict or identical beats when another scene function is intentional.

### `StoryProjectState`

Represent the author-approved portable project through relative Markdown paths under `story/` and `manuscript/`. At minimum for a persistent project, record the creative brief, compact status, scene ledger, and manuscript. Add canon, characters, timeline, arcs, research, decisions, series, or book-level files only when relevant.

`story/STATUS.md` must state the current phase and cadence, last accepted unit, last completed checkpoint, immediate story state, Proposed details awaiting acceptance, open decisions and risks, next approved action, batch limit, and files needed to resume. It is a resume packet, not a replacement for the accepted manuscript or other authoritative records.

## Processing flow

```text
Request and materials
  -> FS-013 identify host capabilities and material model limits
  -> FS-001 select mode and depth
  -> FS-002 resolve topic path when new writing lacks a topic
  -> FS-003 build the smallest sufficient WritingBrief
  -> FS-014 when fiction, build the FictionBrief and select the proportionate lifecycle action
  -> FS-015 when persistent fiction is approved, load or maintain portable story state
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

### FS-014 — Orchestrate fiction

1. Route every fiction request through Unsloop Write and the fiction reference; do not create a fourth mode or assume a subject domain.
2. Scale intake and state to the form: use a minimal in-context brief for a clear isolated unit, a compact project for continuing multi-scene work, and full or series state for sustained long-form work.
3. For sustained work, establish the creative contract and select Guided, Adaptive, or Autonomous cadence. Use Adaptive when no preference is supplied.
4. Move proportionately through discovery, contract, foundation, architecture, scene design, drafting, revision, and completion. Do not force one plotting framework or exhaustive outlining.
5. In every cadence, preserve locked author decisions. In Autonomous cadence, stop at the approved batch and pause before a consequential change.
6. Return the requested creative artifact before checkpoint notes. Keep Proposed discoveries visible until the user accepts them.

### FS-015 — Maintain fiction project state

1. Inspect existing project and manuscript files before proposing state. Adopt a coherent existing layout and never overwrite, move, or normalize it silently.
2. For a new persistent project, propose the smallest useful visible Markdown layout once and create it only after approval.
3. Use relative paths under `story/` and `manuscript/` by default. Keep series-wide state separate from book-specific planning and prose.
4. Treat accepted manuscript as primary evidence for what appears in the story. Reconcile conflicts with project records explicitly.
5. Classify canon as Proposed, Confirmed, or Superseded. Require an explicit retcon decision before superseding Confirmed canon.
6. After each drafting batch, update affected scene, status, canon, character, timeline, arc, research, and decision records only as needed. Promote accepted Proposed details to Confirmed.
7. When context is limited, load `story/STATUS.md`, the relevant records, and the necessary manuscript range; disclose that boundary and avoid global continuity claims.
8. Persist a distilled `story/VOICE.md` only with explicit authorization and never persist the source samples by default.

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
| Clear isolated fiction request | Draft from the smallest sufficient brief; do not require project files or long-form architecture. |
| Persistent fiction layout not approved | Keep state conversational or return a proposed layout; do not create files. |
| Existing fiction layout differs from the default | Adopt the coherent existing layout; do not reorganize it silently. |
| Confirmed canon conflicts with a requested direction | Surface options and require an explicit retcon or scope decision. |
| Autonomous work reaches its batch limit | Stop at the checkpoint, report Proposed decisions, and wait for acceptance or a new batch. |
| Manuscript exceeds model context | Resume from `story/STATUS.md` plus relevant records and prose; bound every continuity claim to inspected material. |

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
| Clear isolated scene request | PR-016 / FS-014 | No redundant topic question, cadence selector, project layout, or novel-scale ceremony. |
| Fiction brainstorming without a topic | PR-002, PR-016 / FS-002, FS-014 | Materially distinct premises identify narrative engine, experience, scope, genre fit, and research needs. |
| Short story becomes multi-session work | PR-017 / FS-014, FS-015 | Compact project is proposed once and created only after approval. |
| Novel or serial project | PR-016, PR-017 / FS-014, FS-015 | Full story state and resumable drafting loop scale to accepted decisions. |
| Existing manuscript and custom layout | PR-017 / FS-015 | Existing structure is inspected and preserved; no silent overwrite or reorganization. |
| Autonomous batch introduces new details | PR-017 / FS-014, FS-015 | Details remain Proposed until acceptance and no locked decision changes silently. |
| Confirmed canon contradiction | PR-017 / FS-015 | Conflict is surfaced and Confirmed canon changes only through an explicit retcon. |
| Historical or research-based fiction | PR-005, PR-016 / FS-004, FS-010, FS-014 | Verified facts, unresolved research, story canon, and invention remain separate. |
| Named-author style request | PR-008, PR-013, PR-016 / FS-004, FS-006, FS-014 | Request becomes broad non-exclusive traits; no exact imitation or signature copying. |
| Fiction project exceeds context | PR-017, NFR-008 / FS-013, FS-015 | Resume packet and relevant records support bounded continuation without full conversational history. |

## Change control

Changes to business scope begin in [`BRD.md`](BRD.md). Changes to user-visible behavior or acceptance criteria begin in [`PRD.md`](PRD.md). Changes to workflow, data concepts, operational references, or validation begin here and in the corresponding implementation files. Record durable tradeoffs in [`DECISIONS.md`](DECISIONS.md) and staged work in [`ROADMAP.md`](ROADMAP.md).
