# Scoring

Read this file when the user requests scores, comparison across versions, or a deep review that benefits from a compact profile.

## General rules

- Treat every score as an interpretive summary, not a detector probability or validated measurement.
- Cite passage-level evidence and explain the score briefly.
- Use `N/A` when the evidence cannot support a dimension.
- Do not combine all dimensions into one total.

## Source dependence — higher means more risk

| Score | Anchor |
|---:|---|
| 1 | Independent wording, syntax, selection, order, and framing; attribution is adequate. |
| 2 | Mainly necessary terminology or conventional organization; one minor source-shaped feature may remain. |
| 3 | Multiple source-shaped features remain alongside meaningful synthesis. |
| 4 | Several channels closely track the source; independent synthesis is limited. |
| 5 | The source dominates the passage's wording, syntax, sequence, details, or architecture. |

Score only against an available comparison source. Name the channels that drive the result.

## Voice profile

### Strengths — higher is better

Score **Specificity**, **Authorial voice**, and **Source independence** from 1 to 5.

- `1` means the quality is largely absent.
- `3` means it is mixed or uneven.
- `5` means it is consistently strong and purpose-fit.

Use `N/A` for source independence without a comparison source.

### Voice fidelity — optional and evidence-bound

Score **Voice fidelity** separately from Authorial voice and only when a defined target or authorized writing samples exist.

- `1`: the result conflicts with most target traits;
- `2`: scattered resemblance, with major mismatches;
- `3`: recognizable alignment, but uneven or overly generic;
- `4`: strong alignment across most task-relevant traits;
- `5`: unusually close alignment across representative evidence without copying sample language.

Report the evidence basis and Low, Moderate, or High confidence beside the score. Use `N/A` when no defensible target exists. A high score is not an authorship or identity claim.

### Risks — higher is worse

Score **Redundancy**, **Formulaicity**, and **Abstraction** from 1 to 5.

- `1` means little or no material risk.
- `3` means a noticeable pattern that weakens sections.
- `5` means a pervasive pattern that obscures the writing's substance or voice.

### Slop density

If requested, calculate the mean of Redundancy, Formulaicity, and Abstraction. Report one decimal place and the component scores.

- `1.0–1.7`: Low
- `1.8–2.5`: Mild
- `2.6–3.3`: Noticeable
- `3.4–4.1`: High
- `4.2–5.0`: Severe

Never describe slop density as the likelihood that text is AI-generated.

## Finding severity

- **Low:** local style, wording, or citation-placement issue
- **Moderate:** too-close paraphrase, persistent generic prose, style discontinuity, or weak attribution
- **High:** near-verbatim patchwriting, extended structural dependence, misleading citation, or substantial undisclosed self-reuse
- **Critical:** large unattributed copying, fabricated sources, invented evidence, or substantial appropriation presented as original

Assign severity to individual findings, not to the writer.
