# Scoring Rubric

## Purpose and limits

The v0.1 scales make judgment explicit and comparable. They are interpretive rubrics, not validated psychometric instruments, detector probabilities, or misconduct verdicts.

Score only when useful. Always pair a score with passage-level evidence and a short rationale.

## Source-dependence score

Use this scale only when the relevant comparison source is available.

| Score | Label | Observable relationship |
|---:|---|---|
| 1 | Independent | The draft expresses the idea through independent wording, syntax, selection, order, and framing; attribution is adequate where needed. |
| 2 | Light | The shared content is mainly necessary terminology or conventional organization; one minor source-shaped feature may remain. |
| 3 | Moderate | Multiple source-shaped features remain, such as similar sentence movement, idea order, or detail selection, but the passage contains meaningful synthesis. |
| 4 | Strong | The draft closely tracks the source through several channels despite surface rewriting; independent synthesis is limited. |
| 5 | Dominant | The source supplies most of the passage's wording, syntax, sequence, details, or rhetorical architecture; quotation or substantial redevelopment is required. |

### Comparison channels

Assess and cite the channels that drive the score:

- **Wording:** distinctive phrases, uncommon collocations, or terminology beyond what the topic requires
- **Syntax:** retained sentence skeletons, clause order, or grammatical movement
- **Idea order:** the same non-obvious conceptual sequence
- **Detail selection:** the same incidental examples, qualifications, or omissions
- **Rhetorical architecture:** the same setup, contrast, concession, illustration, and conclusion pattern

Do not average the five channels mechanically. A single dominant channel can be decisive, and ordinary terminology may deserve little weight.

## Human-voice profile

The profile contains two score families. Do not add all six numbers into one total.

### Strength dimensions — higher is better

| Score | Specificity | Authorial voice | Source independence |
|---:|---|---|---|
| 1 | Mostly generic; actors, actions, evidence, or consequences are unclear | No discernible judgment or priorities; prose feels interchangeable | Source-shaped wording or structure dominates the compared material |
| 2 | Occasional concrete detail, but broad claims dominate | Sparse signs of an author; emphasis feels conventional | Several material source-shaped features remain |
| 3 | Mixed; key claims are concrete but some generic padding remains | A position is visible, though uneven or muted | Meaningful synthesis coexists with noticeable source influence |
| 4 | Most claims name the relevant actors, actions, limits, and consequences | Clear judgment, selective detail, and natural emphasis | Sources are integrated through mostly independent language and structure |
| 5 | Precise throughout without unnecessary detail | Distinctive, credible, purpose-fit voice; polish does not erase personality | Fully independent synthesis with clear attribution |

Use **N/A** for source independence when no comparison source is available.

### Optional voice-fidelity score

Voice fidelity is different from Authorial voice. Authorial voice asks whether the writing has a credible point of view; Voice fidelity asks whether it aligns with a defined target evidenced by the user's instructions or authorized samples.

| Score | Observable alignment |
|---:|---|
| 1 | Conflicts with most task-relevant target traits |
| 2 | Shows scattered resemblance but major mismatches |
| 3 | Is recognizably aligned but uneven or overly generic |
| 4 | Aligns strongly across most task-relevant traits |
| 5 | Aligns unusually closely across representative evidence without copying sample language |

Use **N/A** without a defensible target. Report the evidence basis and a separate confidence label:

- **Low:** mainly a short conversation, generic preferences, or conflicting samples
- **Moderate:** one adequate sample or a strong current draft
- **High:** multiple representative samples agree with current instructions

Voice fidelity is not an identity or authorship probability.

### Risk dimensions — higher is worse

| Score | Redundancy | Formulaicity | Abstraction |
|---:|---|---|---|
| 1 | Each sentence adds material information | Structure follows the argument naturally | Concrete nouns and verbs dominate |
| 2 | Minor restatement that rarely slows the piece | A few conventional phrases, used appropriately | Occasional broad phrasing with enough context |
| 3 | Repeated ideas noticeably dilute some sections | Recurring templates or transitions flatten parts of the prose | Several claims hide behind abstract nouns or unspecified importance |
| 4 | Repetition is persistent and materially obscures the point | Paragraphs repeatedly use canned shapes, balance, or signposting | Abstract phrasing routinely replaces actors, actions, and evidence |
| 5 | Much of the document restates rather than develops | The document reads as an interchangeable template | The prose is so abstract that central claims are difficult to identify |

### Slop density

If a compact summary is requested, calculate:

```text
Slop density = mean(Redundancy, Formulaicity, Abstraction)
```

Report one decimal place and the three component scores. Do not label the result as an AI probability.

Suggested interpretation:

| Mean | Description |
|---:|---|
| 1.0–1.7 | Low |
| 1.8–2.5 | Mild |
| 2.6–3.3 | Noticeable |
| 3.4–4.1 | High |
| 4.2–5.0 | Severe |

## Finding severity

Severity ranks the consequence and urgency of a specific finding. It is separate from the profile scores.

| Severity | Use for |
|---|---|
| Low | Minor generic wording, local repetition, citation placement, or common phrasing |
| Moderate | Too-close paraphrase, persistent generic prose, style discontinuity, or weak evidence attribution |
| High | Near-verbatim patchwriting, extended structural dependence, misleading citation, or substantial undisclosed self-reuse |
| Critical | Large unattributed verbatim copying, fabricated sources, invented evidence, or substantial appropriation presented as original |

Escalate severity only when the available evidence supports it. If source access is incomplete, state what must be checked rather than assigning a definitive integrity label.
