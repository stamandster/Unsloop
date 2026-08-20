# Writing-Pattern and Assistance Audit

Read this file when the user asks for an AI score, AI detection, an assessment of whether writing was machine-generated, analysis of AI-like wording or transitions, comparison with known writing samples, or interpretation of an external detector report.

This is a specialization within **Unsloop Audit**, not a new mode. Preserve the inspected text unchanged. Translate an “AI score” request into an evidence-bound writing-pattern and assistance assessment, and explain once that prose style cannot supply a defensible probability of AI authorship.

## Separate the questions

Determine which question the user actually needs answered:

1. What observable writing patterns affect quality, specificity, or voice?
2. How closely does the text align with authorized samples or a defined voice target?
3. What process evidence documents human, editorial, automated, or model assistance?
4. What does a supplied detector report actually claim, and what are its limits?

Answer only the questions supported by the available evidence. A style profile, voice comparison, provenance record, and detector result are different evidence types and must not be collapsed into one number.

## Establish the evidence boundary

Identify which of these are available:

- inspected prose only;
- authorized same-writer or same-genre comparison samples;
- task directions or an accepted voice brief;
- revision history, document metadata, tracked changes, prompts, model outputs, disclosures, or other process records;
- an external detector report with its tool, version, date, settings, threshold, and inspected input; and
- relevant genre, language, audience, or institutional context.

If only prose is available, use this exact conclusion boundary:

> **AI authorship determination:** Not assessable from prose alone.

Direct process evidence may support a narrower statement, such as “The supplied revision history documents model-assisted drafting in these passages.” It does not establish how much of the final artifact was generated, who made each decision, or whether undisclosed assistance occurred elsewhere unless the evidence actually shows that.

## Build the pattern profile

Use the existing scoring contract in [scoring.md](scoring.md). Report component scores rather than an AI score:

- **Strengths, higher is better:** Specificity and Authorial voice; add Voice fidelity only when authorized comparison evidence exists.
- **Risks, higher is worse:** Redundancy, Formulaicity, and Abstraction.
- **Slop density:** optional mean of the three risk dimensions, never an authorship probability.

Support each scored dimension with passage locations and a short rationale. Use `N/A` when the evidence cannot support a dimension. Do not create a total across strengths, risks, voice fidelity, source dependence, provenance, or detector output.

Inspect observable features that materially explain the profile:

- repeated transition families, discourse markers, sentence openings, phrases, or collocations;
- sentence-length movement, syntactic variety, paragraph-shape recurrence, and list or symmetry templates;
- specificity, selective detail, named actors and actions, qualification, and concrete consequences;
- generic importance claims, nominalization, agent omission, vague reference, or unsupported certainty;
- rhetorical direction, question-and-answer patterns, examples, conclusions, and evidence integration;
- local shifts in vocabulary, formality, punctuation, cadence, viewpoint, certainty, or technicality; and
- alignment or conflict with an authorized voice target.

Common, polished, formal, repetitive, or highly regular writing is not uniquely machine-generated. Adjust interpretation for genre, templates, translation, second-language writing, accessibility-related patterns, collaboration, editing, and required institutional language.

## Use measurements honestly

Raw counts can be objective within a declared method; their meaning remains contextual. When tools or sufficient text support measurement, record:

- the exact measure and unit;
- method, tokenization or matching rule when relevant;
- inspected range and exclusions;
- comparison baseline, if any; and
- length, genre, language, extraction, or sample-size limitations.

Useful measures may include repeated transition counts, repeated phrase counts, sentence-length distribution, paragraph-length distribution, or the proportion of sentences matching a stated structural pattern. Lexical-diversity measures are length- and language-sensitive; do not compare unequal or incompatible samples without an explicit normalization method. Never invent a count, imply that a subjective score was mechanically measured, or present any single measure as an AI marker.

When Python is available and deterministic counts would help, use the optional standard-library helper:

```text
python scripts/writing_pattern_metrics.py draft.txt --transition "however" --transition "in addition"
```

The helper emits JSON to standard output, does not modify the input, accepts `-` for standard input, and deliberately returns measurements rather than a score. Use another transparent method when the helper is unavailable or unsuitable for the language or artifact.

## Compare authorized writing samples

Use voice samples only to assess alignment with the defined target. Keep their facts, opinions, experiences, and distinctive wording out of the audited text. Report:

- sample count, genre, approximate range, and relevance;
- observable agreements and differences;
- Voice fidelity score when defensible;
- Low, Moderate, or High confidence; and
- material limits such as genre mismatch, small sample, collaboration, heavy editing, or age of the samples.

A close match does not prove human authorship, identity, or lack of assistance. A mismatch does not prove AI use, ghostwriting, misconduct, or unauthorized help.

## Handle provenance and detector reports

For assistance provenance, distinguish **Observed**, **Reported**, **Unverified**, and **Unavailable** evidence. State the exact scope supported: brainstorming, outlining, drafting, rewriting, translation, editing, research, formatting, or an unknown form of assistance. Do not infer the rest of the workflow.

For each external detector report, record the tool, version, date, inspected input, vendor result, threshold or settings when available, and known missing context. Label it **External detector result**. Do not restate a vendor percentage as the probability that AI wrote the text, average detector output with Unsloop scores, or let the report override passage evidence and provenance.

## Return the audit

Use this order when the user requests a full assessment:

1. **AI authorship determination** — normally “Not assessable from prose alone,” qualified only by direct provenance.
2. **Evidence boundary** — text, samples, process records, detector reports, context, and unavailable evidence.
3. **Writing-pattern profile** — component scores, directions, rationale, and `N/A` values.
4. **Observed measures** — values, methods, coverage, baseline, and limitations.
5. **Passage-level findings** — locations, observations, consequences, confidence, and material to preserve.
6. **Voice comparison** — only when an authorized target exists.
7. **Assistance provenance** — only what supplied process evidence establishes.
8. **External detector results** — reported separately and without endorsement.
9. **Calibrated conclusion** — the strongest supported statement and unresolved questions.

For a brief request, return the authorship boundary, compact component profile, and highest-value passage evidence without ceremonial sections.

## Preserve the safety boundary

Do not use the profile to accuse, discipline, reject, or certify a writer automatically. High-stakes academic, employment, publication, or disciplinary decisions require qualified human review, applicable policy, full evidence, and an opportunity for the affected person to respond.

If the user asks to lower an AI or detector score, offer revision for genuine writing goals—specificity, concision, clarity, voice fidelity, logical transitions, evidence, or audience fit. Do not add artificial errors, replace words mechanically, conceal assistance, or optimize against a detector. In Audit, keep every suggested change separate from the unchanged artifact.
