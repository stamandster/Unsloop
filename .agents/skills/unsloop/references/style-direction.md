# Style Direction and Evolution

Read this file when the user asks to select, design, imitate at a high level, preserve, evolve, review, or audit a literary, historical, rhetorical, or publication style. Examples include Early Modern English dramatic verse, epistolary prose, period-informed narration, a changing narrator across decades, or a house style that evolves by edition.

Style Direction is a specialization inside **Unsloop Write**, **Unsloop Review**, and **Unsloop Audit**, not a fourth mode and not a catalog of canned voices.

## Select the style path

Use an explicit style already supplied by the user without asking them to repeat it. When a consequential style direction is still open, offer only the relevant paths:

- **My evidenced voice:** derive task-relevant traits from authorized samples through [voice-fidelity.md](voice-fidelity.md).
- **Historical or literary tradition:** ground the design in a period, region, movement, form, and representative evidence.
- **Custom designed style:** combine user-selected traits without claiming a historical or authorial source.
- **Genre default:** follow appropriate current conventions without imposing a special profile.

Use a structured selector when the host provides one and the choice materially changes the artifact; otherwise ask conversationally. Do not add style intake to a simple task whose direction is already clear.

## Keep the style channels separate

Do not collapse these into one profile:

- **Author voice:** evidenced tendencies in the user's authorized writing.
- **Style direction:** the selected literary, historical, rhetorical, house, or custom design.
- **Narrative voice:** the designed narrator's register, distance, texture, rhythm, and reliability.
- **Viewpoint voice:** what a viewpoint character notices, understands, assumes, and can say.
- **Dialogue voice:** character-specific speech governed by the accepted character profile.
- **Form and delivery conventions:** constraints arising from verse, drama, correspondence, policy, speech, documentation, or another medium.

Current user directions and locked project decisions take precedence over an older style profile. Style must not import facts, autobiography, opinions, or distinctive wording from evidence samples.

## Build the `StyleBrief`

Capture only fields that affect the work:

- selected path and applicable manuscript or delivery scope;
- period or date range, region, tradition, movement, form, medium, and audience when relevant;
- target register, diction, syntax, sentence movement, imagery, rhetoric, rhythm, meter or prosody, punctuation, typography, and structural conventions;
- relationship to author, narrative, viewpoint, dialogue, and delivery voices;
- authenticity stance and modernization policy;
- intentional anachronisms, deviations, mixed influences, and prohibited caricatures;
- research corpus, evidence boundary, disputed features, confidence, and unresolved questions;
- stable, gradual, or phase-based evolution; and
- decision owner, profile state, version, and applicable chronology or manuscript range for persistent work.

Do not require every field. A short experiment may need only a one-sentence style target. A sustained or historically sensitive project benefits from a confirmed brief.

## Set historical and literary evidence boundaries

A period label is a research direction, not proof of authenticity. Distinguish:

- documented conventions in the inspected corpus;
- broad traits supported across representative sources;
- contested or source-limited interpretations;
- deliberate modernization or synthesis; and
- model-proposed invention.

When authenticity matters, identify the relevant date range, geography, literary tradition, social register, genre, performance or publication medium, and corpus scope. Use [source-acquisition.md](source-acquisition.md) and [research-provenance.md](research-provenance.md) when external evidence is gathered or persisted. Do not generalize one writer, elite register, printed edition, surviving sample, or modern adaptation to an entire period.

Convert a request for another identifiable author's style into broad, non-exclusive traits. Even when the source is public domain, prefer a tradition-level profile or a multi-source corpus over signature phrases, distinctive characters or worlds, recognizable rhetorical sequences, or passage-level imitation.

## Choose authenticity and readability

When the balance materially affects the result, offer:

- **Period-forward:** stronger documented period texture with higher reader burden.
- **Balanced (Recommended):** historically informed patterns with controlled modernization and clear disclosure.
- **Modern-reader-forward:** modern clarity and accessibility with selected period signals.

The stance governs degree, not factual verification. Record how it affects vocabulary, syntax, orthography, punctuation, annotation, meter, cultural reference, and reader support. Do not simulate age merely through random archaic words, obsolete spellings, apostrophes, or `thee` and `thou` decoration.

## Apply a style direction

Draft from the functional profile rather than sprinkling surface markers. For each material trait, know what it contributes to meaning, character, pacing, argument, performance, atmosphere, or reader orientation.

For **Early Modern English dramatic verse**, for example, resolve the dramatic form, verse or prose use, blank verse or rhyme policy, metrical flexibility, enjambment, caesura, rhetorical movement, social register, stage delivery, and modernization stance. Treat Elizabethan and Jacobean traditions as useful but internally varied contexts, not one interchangeable preset. Do not claim period authenticity beyond the inspected evidence.

Review style at the passage and whole-work levels. A locally plausible line can still violate the project's form, social register, narrative channel, chronology, or evolution phase.

## Govern stylistic evolution

Select the evolution model only when change is intended:

- **Stable:** one confirmed profile applies throughout the stated scope.
- **Gradual:** named traits change along an approved trajectory with bounded transition markers.
- **Phase-based:** discrete `StylePhase` records apply to defined eras, volumes, editions, narrators, character ages, or manuscript ranges.

Each material `StylePhase` records an ID, Proposed/Confirmed/Superseded state, scope or chronology, applicable profile version, changes and rationale, observable linguistic markers, continuity requirements, intentional deviations, evidence basis, confidence, and approval decision.

Do not infer that a historical tradition, real author's style, narrator, or character naturally evolved in a particular way without evidence or an explicit creative decision. For creative projects, new phases remain Proposed until the author accepts them. Confirmed style state is locked within its scope; a prospective evolution or retroactive override requires an impact-aware decision and, for consequential revision, a recoverable checkpoint.

Review boundaries between phases as transitions. The change may be gradual, abrupt, concealed, cyclical, or deliberately inconsistent, but its relationship to chronology, character, form, and reader experience must remain intelligible.

## Use the existing modes

- **Write:** select or design the style, draft within the accepted profile, propose evolution, and update only accepted state.
- **Review:** assess fit, consistency, effectiveness, drift, reader burden, and whether deviations appear purposeful; preserve effective departures.
- **Audit:** leave the artifact unchanged while comparing it with the confirmed profile, declared phase, supplied corpus, historical evidence, or house requirements. Report anachronism, unsupported authenticity, corpus limits, and proposed corrections separately.

Do not score historical authenticity from surface archaism. When evidence is incomplete, report supported features, plausible adaptations, unverified features, and out-of-scope expert judgments separately.

## Persist only when useful

Use no project file for a self-contained style experiment. For multi-session work, propose `story/STYLE.md` or `writing/STYLE.md` once and create it only after approval. Respect an existing coherent layout.

Store the distilled profile, evidence citations or basis, confidence, decisions, phases, and intentional deviations—not copied source passages or personal voice samples. If the profile derives from the user's samples, keep those samples task-local unless separately authorized under the voice-storage rules.

For a series, `story/STYLE.md` holds series-wide direction; a book-specific override may live under `story/books/<book-slug>/STYLE.md`. For other sustained writing, `writing/STYLE.md` records the applicable artifact and version scope. Another model or session should be able to resume from the confirmed profile and current phase without guessing from prior prose alone.

## Protect integrity

- Do not market a generated style as authenticated historical language without adequate evidence.
- Do not convert demographic, regional, disability, class, or second-language stereotypes into style markers.
- Do not force archaic vocabulary, dialect spelling, metrical regularity, or ornamental rhetoric when it does not serve the approved design.
- Do not let style weaken factual support, quotation accuracy, accessibility requirements, legal meaning, procedural safety, or the author's explicit intent.
- Do not flatten purposeful variation merely to improve surface consistency.
- Do not claim exact author imitation, identity replication, or community authority.
