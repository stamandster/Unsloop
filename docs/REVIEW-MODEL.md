# Review Model

## Overview

Unsloop uses two review lenses. Apply them together for a standard review, or emphasize one when the user's request is narrower.

## Progressive writing brief

For new writing, begin by determining topic status: the user has a topic, has a rough direction to refine, or wants to brainstorm topics. Do not ask when the request or supplied material already establishes the topic. Use a structured user-input control for this and other short, consequential choices when the current Codex mode exposes one; otherwise use the same options in concise plain text. Do not switch modes solely to obtain the control. When brainstorming is requested, gather only enough seed context to generate genuinely distinct, feasible options; briefly distinguish their angle, reader value, scope, and evidence needs before helping the user choose. For Review or Audit, normally infer the topic from the supplied writing.

Before applying either lens, extract the brief already present in the request and supplied materials:

1. topic;
2. goal—the intended reader outcome;
3. audience;
4. audience prior knowledge;
5. context and occasion;
6. required content;
7. exclusions;
8. factual reference material;
9. voice target and authorized voice samples;
10. format constraints.

Mark material fields as **Known**, **Inferred**, or **Unknown**. Do not ask all ten fields as a questionnaire. Ask only about an unknown that could materially affect factual accuracy, evidence, claim selection, explanation level, tone, relationship risk, privacy, policy exposure, format, or usefulness. State a consequential inference rather than hiding it.

Keep factual references separate from voice samples. References support what the writing says; voice samples provide evidence about how it should sound. Neither the audience's beliefs nor a required claim becomes verified merely because it appears in the brief.

For a short, low-stakes request, infer safe defaults and proceed. For substantial drafting, ask the smallest useful batch of questions. Pause when a missing fact, source, authorization, or high-stakes choice cannot be safely inferred. Review uses the brief as evaluative context; Write uses it as the drafting specification; Audit records it separately from the evidence corpus.

## Lens A — Writing integrity

### 1. Establish the evidence boundary

Record what is available:

- the draft only;
- draft plus named source passages;
- draft plus full supplied sources;
- sources verified through external research;
- a similarity report without full source text.

The evidence boundary controls the claim. A draft-only review can flag passages that warrant inspection, but it cannot establish source dependence. A similarity report identifies matches, not plagiarism.

### 2. Review source relationships

Compare wording, syntax, concept sequence, detail selection, and rhetorical architecture.

Classify supported relationships as:

- **Proper quotation:** exact wording is marked and attributed, with a locator when appropriate.
- **Acceptable paraphrase:** the idea is credited and expressed through independent wording and structure.
- **Too-close paraphrase:** the source is credited, but distinctive wording or syntax remains.
- **Structural dependence:** wording differs, but the source's unusual idea order, details, or argumentative path remains.
- **Unattributed borrowing:** source-dependent wording, ideas, or structure appear without adequate credit.
- **Secondary-source problem:** the writer presents an original source as consulted when the wording or knowledge came through an intermediary.
- **Self-reuse:** the writer reuses earlier work; treat policy and disclosure separately from plagiarism.
- **Unsupported or fabricated support:** a source is missing, misrepresented, or does not support the claim attributed to it.

### 3. Test evidence quality

For material claims, ask:

- What supports the claim?
- Does the cited source support this wording?
- Has the draft strengthened probability into certainty?
- Has association become causation?
- Is a secondary source presented as primary?
- Is the citation close enough to the claim to make attribution clear?

### 4. Assess source dependence

Score source dependence only when a comparison source is available. Evaluate five channels:

1. wording;
2. syntax;
3. idea order;
4. detail selection;
5. rhetorical architecture.

Use the rubric in [`SCORING-RUBRIC.md`](SCORING-RUBRIC.md). Treat the score as a reasoned summary of visible evidence, not a probability of misconduct.

## Lens B — Human voice

### 1. Establish purpose and voice target

Use the writing brief to identify audience, purpose, prior knowledge, genre, appropriate formality, and whether the target is the writer's own voice or a publication style. Do not equate “better” with “more formal.”

When close fidelity to the user's own voice matters, use this evidence order:

1. current explicit instructions;
2. a user-confirmed voice brief;
3. authorized samples in the same genre;
4. broader samples by the user;
5. the current draft and conversation;
6. genre defaults.

If the available evidence is thin, request two or three representative samples, preferably about 500–2,000 words total. Do not block if the user declines; proceed with a lower confidence label. Derive only observable, task-relevant traits and keep sample facts, opinions, anecdotes, and distinctive sentences separate from the new content.

### 2. Inspect the document as a whole

Look for abrupt changes in sentence length, vocabulary, abstraction, technicality, point of view, certainty, punctuation, transitions, and paragraph construction.

A discontinuity is a prompt for closer review. It is not proof of plagiarism or AI use.

### 3. Inspect concrete slop patterns

Flag patterns rather than isolated words:

- **Empty abstraction:** the sentence announces importance without stating the claim.
- **Generic importance:** the sentence could fit almost any topic.
- **Template transitions:** connectors recur mechanically rather than expressing logic.
- **Over-signposting:** prose explains its structure more than the reader needs.
- **Artificial symmetry:** ideas are forced into uniform triplets or identical paragraph shapes.
- **Rhetorical polish without content:** impressive phrasing hides unspecified actors, actions, or consequences.
- **Restatement as elaboration:** several sentences repeat one idea at increasing levels of abstraction.
- **Synonym and adjective stacking:** near-duplicates create bulk without precision.
- **Inflated verbs:** formal vocabulary replaces a clearer ordinary word without adding meaning.
- **Metaphor accumulation:** multiple stock metaphors compete in a short span.
- **Manufactured balance or caution:** qualifications appear without a real tension or specific limitation.
- **Canned openings and conclusions:** the prose introduces or summarizes a generic topic instead of advancing the writer's actual point.

### 4. Test for authorial presence

Ask whether the reader can tell what the writer thinks and why. Look for concrete judgment, selective detail, real examples, natural emphasis, clear priorities, and sentence rhythm that follows thought rather than a template.

When a voice target exists, separately test fidelity across register, directness, cadence, vocabulary, viewpoint, certainty, warmth, transitions, punctuation, rhetorical habits, and useful irregularity. Treat differences required by the new audience or genre as adaptation, not failure.

### 5. Run the deletion and specificity tests

For each suspect sentence, ask:

- Can it be deleted without losing information?
- Could it appear in a paper on almost any subject?
- Does it repeat the previous sentence?
- Does an abstract noun hide a direct verb?
- Is a transition doing logical work?
- Does a polished phrase obscure who did what?

## Review depths

### Brief

Return the overall assessment and up to five high-value findings. Do not score unless asked.

### Standard

Run both lenses, identify strengths, rank findings by severity, and include the voice profile when it would help revision.

### Deep

Map claims and sources, compare source relationships passage by passage, apply the full scoring rubric, document uncertainties, and distinguish verified findings from leads requiring more evidence.

## Revision rule

Diagnose by default. Rewrite only when requested. When rewriting, preserve meaning, position, natural vocabulary, intended audience, and legitimate irregularity. If voice fidelity is material, report the evidence basis and Low, Moderate, or High confidence. Do not rewrite good prose merely because it is imperfect.
