# Output Contracts

Read this file before delivering a review or audit.

When a user or downstream system requests JSON, CSV, issue records, or another machine-readable contract, also read [structured-output.md](structured-output.md).

Use the lightest contract that fully communicates the requested result, its material evidence limits, and any action needed before use.

## Unsloop Review

Return:

1. **Overall assessment** — concise judgment and any material evidence limit
2. **High-priority concerns** — passage, problem, why it matters, evidence, severity, and smallest useful correction
3. **Voice and style** — only the patterns with meaningful effect
4. **What should remain unchanged** — strong material worth preserving
5. **Revised version** — only when requested

For a brief review, cap the concerns at the five most useful findings. For a standard or deep review, group repeated instances under one pattern rather than listing every occurrence.

## Unsloop Audit

Add:

- **Evidence boundary:** versions and sources inspected or unavailable
- **Source map:** draft location, source, classified relationship, dependence score, confidence
- **Claim verification:** verified, overstated or mismatched, secondary, and unverified claims
- **Integrity conclusion:** supported findings and unresolved questions without inferring intent

When an outline, rubric, policy, template, or multi-part brief governs the artifact, add a **Requirement coverage** map with requirement, role, artifact location, support or decision, and status.

## Unsloop Write

Return the requested writing first unless the user asks for process notes. Mention only material integrity choices, preserved voice features, substantial changes, and claims or citations that still require confirmation.

For a small fiction request, return the scene or story first and add only material assumptions or limitations. For a persistent fiction checkpoint, return the requested manuscript or plan first, followed by only material decisions or deviations, continuity or research concerns, Proposed details awaiting acceptance, the current checkpoint, and the next approved action. Do not bury the fiction under a project-management report.

For multi-character work, report only material voice-profile proposals, drift, or author-approved changes. Identify the `CVP-*` profile and effective scope; do not expose full character ledgers when a short diff is sufficient.

For documentary narrative or controlled documentation, return the artifact first. Add the form and version, audience and authority, acquisition mode and corpus, material source overrides, claim or chronology boundary, validation actually performed, tested and approval state, unresolved gaps, owner, and maintenance action only when they affect use.

When other skills apply, return one artifact and identify only consequential responsibility or validation boundaries. For numerical, interview, or multimodal support, state the relevant record, transformation, permission, reproduction, or inspection limit rather than calling every item a generic source.

For a documentation system, identify release scope, supported versions, affected dependencies, stale or withdrawn units, corrections or redirects, maintenance owner, and reader-validation method. Simulated, automated, expert, and observed results must remain distinguishable.

When inferred or missing brief elements materially shaped the artifact, add a compact **Brief assumptions** note. Omit obvious or inconsequential assumptions.

When voice matching is material, add a compact note unless the user wants artifact-only output:

- **Voice basis:** explicit brief, current draft, and number/type of samples used
- **Target traits:** the few traits that materially shaped the result
- **Confidence:** Low, Moderate, or High, with any important limit

When a persistent fiction project uses stored state, do not imply that a complete-looking ledger proves manuscript consistency. State unresolved contradictions, uninspected manuscript ranges, and provisional canon when they affect the next work.

## Readiness labels

Use a readiness label only when unresolved matters affect whether the artifact can be used as intended:

- **Ready:** required content, evidence, decisions, and hard constraints are satisfied within the available boundary.
- **Ready with noted limitations:** usable as intended, with disclosed limits that do not require a user decision before use.
- **Provisional—decision required:** a material choice remains unresolved, so the artifact should not be treated as final.
- **Not ready—evidence or authorization missing:** responsible completion requires missing support, permission, or a non-waivable requirement.

Do not label a simple low-stakes artifact merely to add ceremony. Never use **Ready** to imply exhaustive source verification when the evidence corpus was incomplete.

For sustained projects, readiness applies to the stated artifact version and evidence boundary. A valid project ledger, JSON document, or assembly manifest does not by itself establish factual support, stakeholder approval, policy compliance, or publication readiness.

## Score display

Use this form:

```text
Strengths: Specificity 4/5 · Authorial voice 3/5 · Source independence N/A
Risks: Redundancy 2/5 · Formulaicity 3/5 · Abstraction 2/5
Slop density: 2.3/5 — Mild
Source dependence: Not scored; no comparison source supplied
Voice fidelity: 4/5 · Confidence: Moderate · Basis: one same-genre sample plus current instructions
```

Omit scores when they would create false precision or add little value.

## Final contract check

Confirm that observations, supported inferences, unverified concerns, and out-of-scope judgments are not blended. Confirm that every High or Critical finding names concrete evidence and that any readiness limitation tells the user what decision, evidence, authorization, or constraint remains.
