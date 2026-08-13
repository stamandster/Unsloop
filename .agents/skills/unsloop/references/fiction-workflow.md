# Fiction Workflow

Read this file for any fiction request: an isolated scene, flash fiction, short story, novella, novel, serial, or multi-book series. Apply it within **Unsloop Write**; fiction is not a fourth mode.

Treat every subject and genre as available unless a governing safety rule or the user's boundary excludes it. Do not assume a religious, biblical, literary, commercial, or other subject context. Use **story canon** for facts established within the fiction; do not call the project record a “story bible.”

## Contents

- [Scale the workflow](#scale-the-workflow)
- [Establish the fiction brief](#establish-the-fiction-brief)
- [Choose the collaboration cadence](#choose-the-collaboration-cadence)
- [Create a portable project only when useful](#create-a-portable-project-only-when-useful)
- [Manage story state](#manage-story-state)
- [Develop the story](#develop-the-story)
- [Plan chapters and scenes](#plan-chapters-and-scenes)
- [Run the drafting loop](#run-the-drafting-loop)
- [Revise at the right scale](#revise-at-the-right-scale)
- [Protect voice and integrity](#protect-voice-and-integrity)
- [Handle conflicts and limits](#handle-conflicts-and-limits)
- [Complete and hand off](#complete-and-hand-off)

## Scale the workflow

Match the controls to the work instead of forcing every fiction request through novel-scale preparation.

| Request scale | Default handling | Persistent files |
|---|---|---|
| Isolated scene, flash fiction, or exploratory passage | Build only the brief needed to write the requested unit. | None unless requested. |
| Short story or multi-scene work expected to continue | Establish a compact story contract and scene sequence. | Propose the compact project after continuity across sessions becomes useful. |
| Novella, novel, or serial | Establish the creative contract, architecture, scene ledger, and resumable state before sustained drafting. | Propose the full project once, then create it only after approval. |
| Series or shared-world project | Separate series-wide canon from book-specific arcs and manuscripts. | Use the series extension after approval. |

Do not ask a user requesting one clear scene to select a file layout, story framework, or long-term workflow. Do not start a full novel from a one-line premise without resolving the decisions that would materially shape the manuscript.

Inspect any existing manuscript, outline, or project files before proposing changes. Adopt a coherent existing layout. Never overwrite, rename, relocate, or normalize existing fiction files without explicit authorization.

## Establish the fiction brief

Apply the topic-path procedure from [writing-brief.md](writing-brief.md). In fiction, **topic** may be a premise, subject, image, conflict, character, setting, genre idea, or story question.

If the user wants to brainstorm, generate genuinely distinct story directions. For each useful option, state the premise or narrative engine, likely genre and scale, intended reader experience, central pressure, and material research needs. Do not offer superficial variations of one plot.

Extract what the user has already supplied before asking. Capture only fields that affect the current stage:

1. **Form and scale:** scene, short story, novella, novel, serial, or series; exploratory or committed.
2. **Premise:** the situation, destabilizing pressure, and source of sustained change or conflict.
3. **Creative goal:** what the work should accomplish and what experience, question, tension, or emotional movement it should leave with the reader.
4. **Audience and positioning:** intended readership, genre expectations, accessibility, age range when material, and publication or personal-use context.
5. **Genre and tonal range:** genre, subgenre, atmosphere, humor, darkness, realism, and boundaries.
6. **Narration:** point-of-view system, person, tense, narrative distance, narrator reliability, and any switching rules.
7. **Voice:** the author's evidenced tendencies when requested, the designed narrative voice, viewpoint-character voice, and dialogue distinctions.
8. **Story elements:** characters, relationships, setting, conflict, stakes, chronology, themes or questions, ending direction, and known scenes.
9. **Research boundary:** real-world facts that require support, invented rules, supplied sources, inaccessible sources, and facts intentionally left unresolved.
10. **Constraints:** target length, chapter or installment size, content limits, deadlines, format, continuity obligations, and series commitments.
11. **Collaboration cadence:** Guided, Adaptive, or Autonomous, including the maximum drafting batch before review.
12. **Starting state:** idea only, notes, outline, partial draft, complete draft, revision, or continuation of an existing project.

Treat the intended reader experience as a fiction-specific form of the writing goal. Do not force the user to state a moral, lesson, theme, or market category. Treat theme as a question or pattern to develop unless the user explicitly wants a proposition.

For sustained work, summarize a compact creative contract before architecture or drafting. Include the premise, narrative promise, form and scope, central character pressure, intended reader experience, narration, voice direction, boundaries, research needs, and collaboration cadence. Mark consequential elements as Known, Inferred, or Unknown.

## Choose the collaboration cadence

For a sustained fiction project, determine the cadence when it is not already clear. Use a structured choice control when available and suitable; otherwise present the same choices in concise plain text.

- **Guided:** approve every major development phase and each requested drafting unit.
- **Adaptive (Recommended):** approve the creative contract, story architecture, and drafting batches; pause again only when a consequential deviation or unresolved choice appears.
- **Autonomous:** approve the creative contract and maximum batch size, then plan, draft, and update project state through that checkpoint.

When using a structured control, use this compact contract:

- **Header:** `Cadence`
- **Question:** `How should we collaborate on this fiction project?`
- **Option 1:** `Adaptive (Recommended)` — Confirm the creative contract, architecture, and drafting batches, then pause for consequential changes.
- **Option 2:** `Guided` — Confirm every major development phase and each drafting unit.
- **Option 3:** `Autonomous` — After the creative contract and batch limit are approved, work through the checkpoint and report decisions.

Wait for the choice before sustained planning or drafting. If the control is unavailable, ask the same three-way question conversationally. Do not change the host's collaboration or execution mode merely to obtain the control.

The cadence controls when to pause, not who owns the story. In every cadence:

- preserve the user's explicit premise, purpose, boundaries, and accepted decisions;
- do not change confirmed canon, the ending direction, the POV system, real-person treatment, or other locked decisions without approval;
- distinguish low-risk connective invention from decisions that redirect the work;
- keep details introduced during an unaccepted drafting batch **Proposed** until the user accepts the batch; and
- let the user change cadence at any time.

In Autonomous cadence, pause before crossing a content boundary, making a consequential real-world claim without support, retconning confirmed material, changing the intended reader experience, or expanding beyond the approved batch. Report material decisions at the checkpoint instead of hiding them inside polished prose.

## Create a portable project only when useful

Use visible, plain Markdown so the author can inspect, edit, version, and move the project without Unsloop or a particular model. Use relative links and paths. Do not require a database, memory service, vendor format, or hidden agent state.

For a new persistent project, propose the smallest useful layout once and obtain approval before creating it.

### Compact project

```text
story/
  BRIEF.md
  STATUS.md
  SCENES.md
manuscript/
  001-title.md
```

Use the compact project for a short story or another multi-scene work that benefits from cross-session continuity.

### Full project

```text
story/
  BRIEF.md
  STATUS.md
  SCENES.md
  CANON.md
  CHARACTERS.md
  TIMELINE.md
  ARCS.md
  RESEARCH.md
  DECISIONS.md
manuscript/
  001-title.md
```

Create only the files the project needs. For example, omit `RESEARCH.md` when no material real-world research exists. Use stable, zero-padded manuscript filenames and descriptive slugs. Preserve the user's preferred division into scenes, chapters, or installments.

### Series extension

```text
story/
  SERIES.md
  CANON.md
  CHARACTERS.md
  TIMELINE.md
  books/
    book-slug/
      BRIEF.md
      STATUS.md
      ARCS.md
      SCENES.md
manuscript/
  book-slug/
    001-title.md
```

Keep shared-world rules and cross-book facts at series level. Keep a book's promise, arcs, scene ledger, and status in its book folder. Record the scope of a fact when it applies only to one book, timeline, viewpoint, or version.

Do not create `VOICE.md` by default. Create a distilled `story/VOICE.md` only after the user explicitly authorizes persistence. Never copy the source writing samples into it; store only the approved, task-relevant traits, basis, confidence, and limits.

## Manage story state

Treat project Markdown as an author-editable continuity system, not an unquestionable database. Reconcile it with the accepted manuscript and the user's current directions.

### `BRIEF.md`

Record the creative contract: working title, form, premise, narrative promise, intended reader experience, audience, genre, tonal range, POV, tense, narrative distance, boundaries, target scale, research boundary, cadence, and locked decisions.

### `STATUS.md`

Maintain a concise, model-agnostic resume packet containing:

- current project phase and selected cadence;
- last accepted manuscript unit and last completed checkpoint;
- immediate character, place, time, and plot state;
- proposed details awaiting acceptance;
- open decisions, continuity risks, and blocked research;
- the next approved action and maximum batch; and
- the project files needed to resume that action.

Keep `STATUS.md` compact enough to load at the beginning of a new session. It summarizes state but does not replace the authoritative manuscript or ledgers.

Use `story/STATUS.md` as the portable default path for a single sustained work. Series book status may live at the corresponding `story/books/<book-slug>/STATUS.md` path.

### `CANON.md`

Record story-world facts, rules, relationships, and irrevocable events with one of these states:

- **Proposed:** introduced in planning or an unaccepted draft; usable within the current batch but not locked.
- **Confirmed:** explicitly accepted by the user or established in accepted manuscript text.
- **Superseded:** intentionally replaced through an approved retcon; retain the old entry and link it to the decision.

Do not silently resolve contradictions by editing the older entry. Identify the conflict and request or record an explicit retcon decision.

### Other ledgers

- `CHARACTERS.md`: identity, goals, pressures, relationships, capabilities, limitations, knowledge by point in time, arc state, speech tendencies, and confirmed physical details.
- `TIMELINE.md`: ordered events, durations, ages, travel, deadlines, causal dependencies, and uncertainty.
- `ARCS.md`: plot, character, relationship, thematic, mystery, and subplot trajectories; setup, development, turn, payoff, and current status.
- `SCENES.md`: stable scene ID, manuscript location, POV, time and place, purpose, character objective, obstacle, turn, consequence, knowledge or reveal, setup/payoff effects, status, and continuity notes.
- `RESEARCH.md`: factual question, source or lead, access level, verification status, decision, and affected scene or canon entry.
- `DECISIONS.md`: consequential choice, user or governing authority, rationale, affected artifacts, date or sequence, and whether it locks canon.

Treat accepted manuscript text as the primary evidence for what actually appears in the story. When a ledger and accepted prose conflict, surface the discrepancy instead of silently choosing whichever is convenient.

## Develop the story

Move through these phases only to the degree the work requires:

1. **Discover:** establish or brainstorm the topic, story seed, premise, and intended reader experience.
2. **Contract:** confirm form, scope, narration, voice direction, boundaries, research boundary, cadence, and locked decisions.
3. **Foundation:** develop characters, relationships, setting, world rules, chronology, and the central source of pressure.
4. **Architecture:** shape the plot spine, character and relationship arcs, subplots, reveals, setups, payoffs, escalation, and ending direction.
5. **Scene design:** map the causal sequence into chapters, scenes, or installments.
6. **Draft:** write in approved batches and update story state.
7. **Revise:** run structural, continuity, character, voice, integrity, and prose passes separately enough to diagnose causes.
8. **Complete:** reconcile the manuscript and ledgers, disclose unresolved matters, and prepare the requested handoff.

Do not treat a phase order as a demand for exhaustive outlining. Discovery writers may use lightweight scene intentions and update architecture after accepted discoveries. Outline-driven writers may lock more decisions before prose. Preserve either method while keeping consequential decisions visible.

## Plan chapters and scenes

Give each planned unit a reason to exist. For a scene, normally establish:

- stable identifier and provisional placement;
- POV character, time, location, and entry state;
- immediate objective or pressure;
- obstacle, uncertainty, or competing desire;
- meaningful turn, discovery, choice, escalation, or failure;
- consequence and changed exit state;
- information known, concealed, misunderstood, or revealed;
- setup, callback, motif, subplot, or payoff affected; and
- continuity dependencies and research still needed.

Use this as a diagnostic, not a formula. Quiet scenes, atmosphere, reflection, humor, and relationship texture may be the scene's real work. Do not add artificial conflict or force every unit into identical beats.

Check causal movement between units. A later event should arise from prior choices, pressures, information, or credible coincidence rather than merely following it in the outline. Track chapter-to-chapter state changes so characters do not reset emotionally or informationally.

## Run the drafting loop

For each approved unit or batch:

1. Load the creative contract, `STATUS.md`, relevant scene records, affected canon, character states, timeline segment, arc entries, research, and only the manuscript context needed for continuity.
2. State or internally resolve the scene's purpose, entry state, turn, consequence, POV limits, and open risks.
3. Draft the requested prose without adding process notes ahead of the artifact.
4. Check POV access, tense, narrative distance, character knowledge, spatial and temporal continuity, motivation, dialogue distinction, and causal consequence.
5. Check the prose for specificity, useful irregularity, formulaic transitions, redundant explanation, generic emotional labeling, and manufactured intensity.
6. Check real-world claims and source-shaped material within the available evidence boundary.
7. Update the scene ledger, status, and affected project records. Mark new details Proposed until the batch is accepted.
8. At the cadence checkpoint, present the manuscript first, then only material decisions, deviations, continuity concerns, research limits, and the next eligible action.
9. After acceptance, promote accepted story facts to Confirmed and update the resume state.

Do not let project-record maintenance replace prose quality. Do not hide weak motivation, missing causality, or unresolved continuity behind a complete-looking ledger.

## Revise at the right scale

Separate revision passes when combining them would obscure causes or produce unnecessary rewriting:

1. **Story contract:** premise, narrative promise, intended reader experience, scope, and ending alignment.
2. **Structure and pacing:** causality, escalation, reversals, quiet space, subplot integration, chapter function, and setup/payoff.
3. **Character and relationship:** motivation, agency, knowledge, capability, change, emotional continuity, and distinct dialogue.
4. **Canon and chronology:** facts, rules, ages, distances, timing, injuries, objects, names, and information flow.
5. **POV and narration:** access, person, tense, narrative distance, reliability, switching rules, and viewpoint discipline.
6. **Theme and motif:** earned recurrence and implication without converting the story into a lecture.
7. **Research and integrity:** supported real-world detail, attribution when needed, source independence, adaptation risk, and unresolved verification.
8. **Human voice and prose:** specificity, rhythm, image choice, sentence movement, redundancy, formulaicity, abstraction, cliché, and over-polishing.
9. **Line and copy edit:** clarity, grammar, punctuation, formatting, and house style after structural decisions are stable.

Preserve purposeful repetition, motifs, character-specific diction, genre conventions, and deliberate roughness. Do not flatten every narrator or character into one polished house voice.

## Protect voice and integrity

Keep four channels distinct:

- **Author voice evidence:** authorized samples showing the user's observable language tendencies.
- **Narrative design:** the voice, distance, texture, and constraints chosen for this particular story.
- **Character expression:** viewpoint filters and dialogue patterns derived from the user's characters and accepted canon.
- **Factual research:** evidence about the real world, not evidence about how the prose should sound.

Distinguish the author's evidenced personal voice, the designed narrative voice, viewpoint-character voice, and character-specific dialogue. Keep real-world research evidence separate from fictional canon and from every voice channel.

The project voice may intentionally differ from the author's ordinary nonfiction or conversational voice. Prefer same-form fiction samples when close fidelity matters. Do not import the samples' facts, autobiographical experiences, characters, settings, opinions, or memorable wording.

When the user requests the style of another identifiable author, translate the request into broad traits such as pacing, formality, narrative distance, density, humor, imagery, or sentence movement. Do not promise exact imitation or reproduce signature phrases, protected characters, distinctive settings, or a recognizable rhetorical sequence.

Do not claim a manuscript is original against all fiction when the comparison corpus is incomplete. When adaptation, homage, fan work, or close inspiration is involved, identify source dependence only from available evidence and distinguish creative influence from textual or structural copying. Flag publication, licensing, platform, or disclosure questions as unresolved policy matters rather than offering a legal verdict.

Fiction may invent people, events, dialogue, worlds, and emotions when the work is clearly presented as fiction. Do not present an invented scene as proof of a factual claim, a fabricated personal experience, an authentic quotation, or a verified event. Use additional care when fiction depicts real people or makes allegations that readers could mistake for fact.

## Handle conflicts and limits

- **Existing files disagree:** identify which manuscript and records were inspected; ask which is authoritative when acceptance state cannot be inferred.
- **Confirmed canon conflicts with the requested draft:** propose options and require an explicit retcon or scope decision.
- **Context cannot hold the project:** load `STATUS.md` and only the relevant ledgers and manuscript range; state the inspected boundary and avoid global claims.
- **Research is unavailable:** mark the detail unresolved, use a clearly labeled placeholder, or draft around it without inventing verification.
- **The user declines project files:** work conversationally, warn when context limits continuity, and provide a compact resume packet on request.
- **The user changes cadence:** record the new cadence and checkpoint without retroactively treating proposed material as accepted.
- **The project changes genre, POV, premise, or ending:** treat it as a consequential decision and update the creative contract only after approval.
- **The draft discovers a better direction:** preserve the discovery as a proposal; do not erase the prior plan until the user accepts the change.
- **A one-off request grows:** propose the compact or full project at the point persistence becomes materially useful, not before.

## Complete and hand off

For a small request, return the fiction first and add only material assumptions or limitations.

At a sustained-project checkpoint, return:

1. the requested scene, chapter, outline, or revision;
2. material decisions or deviations introduced;
3. continuity or research concerns that affect the next work;
4. proposed details awaiting acceptance;
5. the current checkpoint and next approved action.

At manuscript completion:

- confirm that accepted prose and story records agree or list unresolved discrepancies;
- identify incomplete scenes, arcs, setups, payoffs, research, and decisions;
- distinguish creative completion from copyediting, formatting, submission, publication, legal, or policy readiness;
- apply an honest readiness label only when it helps the author decide the next step; and
- leave `STATUS.md` usable as a final handoff or revision starting point.

Never represent a fluent draft as finished merely because the requested word count was reached.
