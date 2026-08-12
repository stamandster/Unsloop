# Output Contracts

Read this file before delivering a review or audit.

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

## Unsloop Write

Return the requested writing first unless the user asks for process notes. Mention only material integrity choices, preserved voice features, substantial changes, and claims or citations that still require confirmation.

When inferred or missing brief elements materially shaped the artifact, add a compact **Brief assumptions** note. Omit obvious or inconsequential assumptions.

When voice matching is material, add a compact note unless the user wants artifact-only output:

- **Voice basis:** explicit brief, current draft, and number/type of samples used
- **Target traits:** the few traits that materially shaped the result
- **Confidence:** Low, Moderate, or High, with any important limit

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
