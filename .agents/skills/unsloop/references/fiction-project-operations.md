# Fiction Project Operations

Read this file for existing-manuscript onboarding, persistent project state, acceptance and rejection, alternate branches, retcons, consequential revision, checkpoints, recovery, or manuscript-ledger reconciliation.

## Contents

- [Preserve authority and layout](#preserve-authority-and-layout)
- [Choose persistent write policy](#choose-persistent-write-policy)
- [Use the portable project contract](#use-the-portable-project-contract)
- [Onboard an existing manuscript](#onboard-an-existing-manuscript)
- [Apply state lifecycles](#apply-state-lifecycles)
- [Process a batch disposition](#process-a-batch-disposition)
- [Manage alternate branches](#manage-alternate-branches)
- [Analyze and apply retcons](#analyze-and-apply-retcons)
- [Protect revision recovery](#protect-revision-recovery)
- [Maintain and reconcile state](#maintain-and-reconcile-state)
- [Use optional project tooling](#use-optional-project-tooling)

## Preserve authority and layout

Treat accepted manuscript prose as the primary evidence for what appears in the story. Treat the user's current explicit directions and accepted decisions as authority for what should govern future work. Project ledgers summarize and connect that authority; they do not silently overrule it.

Before changing a persistent project:

1. inspect the manuscript, notes, records, and relevant version-control state;
2. identify the exact files and manuscript range in scope;
3. determine which version is authoritative from user direction, project records, accepted status, and content—not timestamps alone;
4. surface conflicts that cannot be resolved safely;
5. preserve a coherent existing layout and naming scheme; and
6. obtain approval before creating, moving, renaming, or replacing project files.

Never migrate a custom project merely to match Unsloop's default layout.

## Choose persistent write policy

Before creating or changing project files, resolve **Immutable versions** or **Overwrite current** through [write-history.md](write-history.md) unless the project already records the choice. Store the confirmed policy in `BRIEF.md` or `STATUS.md`. Under Immutable versions, archive one append-only response batch containing every manuscript and story record written in that response; keep `unsloop-history/` beside `story/` and `manuscript/` unless an accepted native system provides equivalent response-level history. Under Overwrite current, retain all retcon, canon, branch, and consequential-revision checkpoints.

## Use the portable project contract

Use visible Markdown with relative paths. Propose the smallest useful profile once and create it only after approval.

### Compact

```text
story/
  BRIEF.md
  STATUS.md
  SCENES.md
manuscript/
  001-title.md
```

### Full

```text
story/
  BRIEF.md
  STATUS.md
  SCENES.md
  CANON.md
  STYLE.md
  CHARACTERS.md
  CHARACTER-VOICES.md
  TIMELINE.md
  ARCS.md
  RESEARCH.md
  DECISIONS.md
manuscript/
  001-title.md
```

### Series

```text
story/
  SERIES.md
  STATUS.md
  CANON.md
  STYLE.md
  CHARACTERS.md
  CHARACTER-VOICES.md
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

Add optional ledgers only when they earn their maintenance cost:

- `WORLD.md` for places, organizations, systems, objects, technology, or magic rules;
- `GLOSSARY.md` for invented terms, spellings, capitalization, pronunciation, and naming rules;
- `KNOWLEDGE.md` for secrets, misconceptions, reveals, and who knows what when;
- `BRANCHES.md` for alternate paths and merge disposition; and
- `VOICE.md` only for an explicitly authorized distilled profile, never source samples.
- `STYLE.md` for a confirmed or evolving Style Direction whose constraints must survive batches or sessions.

`CHARACTER-VOICES.md` is not an author voice-sample store. It records approved fictional characterization and speech constraints. Use it for sustained projects with multiple recurring speakers; retain compact in-context cards for one-off work.

Use the templates under `assets/fiction-project/` when creating new records. Do not copy unused templates into the user's project.

## Onboard an existing manuscript

Use this procedure for a manuscript that predates Unsloop state:

1. **Inventory:** list supplied manuscript files, notes, outlines, project records, formats, and plausible versions without changing them.
2. **Bound inspection:** record which files and ranges were inspected, inaccessible, duplicated, or incomplete.
3. **Resolve authority:** identify the working manuscript version; ask only if authority remains materially ambiguous.
4. **Map units:** identify books, parts, chapters, installments, and scenes. Assign stable internal scene IDs without renaming files automatically.
5. **Extract tentative state:** identify characters, relationships, chronology, setting rules, arcs, reveals, setups, payoffs, terminology, research questions, apparent locked decisions, and observable personality and speech traits for recurring characters.
6. **Cite basis:** attach manuscript locations and confidence to extracted state.
7. **Mark Proposed:** treat every inference as Proposed, including apparently obvious canon and extracted character voice traits, until the author accepts it or clearly accepted manuscript text establishes it.
8. **Surface conflicts:** list contradictions, competing versions, unclear status, missing units, and manuscript-ledger disagreements.
9. **Propose state:** show the smallest useful project profile and the proposed records without reorganizing the manuscript.
10. **Confirm:** obtain the author's approval of the authority boundary, layout, and consequential extracted state.
11. **Create safely:** create only approved missing records; never overwrite an existing file.
12. **Promote selectively:** make author-accepted or clearly established manuscript facts Confirmed; leave uncertain extractions Proposed.
13. **Resume:** produce `STATUS.md` with current phase, last accepted unit, open decisions, risks, next approved action, and files required to continue.

For a monolithic manuscript, keep the original file unless the user explicitly authorizes splitting. For non-Markdown documents, use available document extraction without representing formatting or uninspected content as verified.

## Apply state lifecycles

### Project phase

- **Discovery**
- **Contract**
- **Foundation**
- **Architecture**
- **Drafting**
- **Revision**
- **Complete**
- **Archived**

### Manuscript-unit state

- **Planned:** intended but not drafted.
- **Drafted:** prose exists but has not completed requested revision or acceptance.
- **Revised:** a requested revision exists and awaits disposition.
- **Accepted:** the author accepted this version into the active manuscript.
- **Cut:** intentionally removed from the active manuscript but retained recoverably when material.
- **Archived:** no longer active and retained only for history or reference.

### Canon state

- **Proposed:** introduced by planning, extraction, a branch, or an unaccepted batch.
- **Confirmed:** explicitly accepted or established in accepted manuscript prose.
- **Superseded:** replaced through an approved retcon; retain the old entry and decision reference.

### Batch disposition

- **Accepted**
- **Partially accepted**
- **Rejected**
- **Revision requested**

Do not infer acceptance from silence, continuation, or polished presentation when the selected cadence requires a checkpoint.

## Process a batch disposition

At a checkpoint, identify manuscript units, new story facts, decisions, and ledger changes separately.

- **Accepted:** promote accepted facts to Confirmed, mark accepted units Accepted, and update affected state.
- **Partially accepted:** record exactly which prose, units, decisions, and facts were accepted. Promote only those items; keep the rest Proposed or mark their disposition.
- **Rejected:** do not promote its details, do not use them in later drafting, and remove them from active status. Record the rejection only when it prevents recurrence or explains a retained decision.
- **Revision requested:** mark the affected unit Revised only after producing the revision; keep new facts Proposed until acceptance.

Prevent rejected or unaccepted details from leaking into `CANON.md`, character knowledge, future scene plans, `STATUS.md` as accepted state, or assembled manuscript output.

## Manage alternate branches

Use a branch only when the user wants to explore a materially different direction without changing active canon.

```text
story/branches/<branch-slug>/
manuscript/branches/<branch-slug>/
```

Record the branch slug, parent checkpoint, purpose, affected scope, status, proposed decisions, and merge or abandonment disposition in `BRANCHES.md`. Branch state is Proposed by default and cannot modify main Confirmed canon.

To merge a branch:

1. compare it with the current main checkpoint;
2. identify conflicts and downstream effects;
3. obtain explicit acceptance of the merge scope;
4. create a recoverable checkpoint;
5. merge accepted prose and decisions only;
6. promote accepted branch facts; and
7. reconcile all affected records.

Abandoned branches remain outside the active manuscript and resume state.

## Analyze and apply retcons

Before changing Confirmed canon or accepted prose that establishes it:

1. state the proposed change and rationale;
2. locate the existing canon entry, accepted prose, and decision basis;
3. identify every affected scene or chapter;
4. map effects on character knowledge, motivation, relationships, chronology, ages, setting or world rules, arcs, subplots, setups, reveals, payoffs, research, dialogue, and description;
5. distinguish required changes, optional improvements, and unresolved effects;
6. offer narrower alternatives when useful;
7. obtain explicit approval of the retcon and affected scope;
8. create a recoverable checkpoint;
9. record the decision and mark the prior canon Superseded rather than deleting it;
10. revise in dependency order;
11. update affected records and resume state; and
12. report unresolved downstream effects.

Use the same impact-map discipline for a large structural revision even when it is not formally a retcon.

## Protect revision recovery

Before a consequential or bulk revision:

- resolve the exact affected files and paths;
- inspect current version-control or document state;
- avoid overwriting unrelated user changes;
- prefer a user-authorized version-control branch or commit when available;
- otherwise create a versioned project-local checkpoint containing only affected files plus a manifest and hashes;
- never overwrite an existing checkpoint;
- work in bounded batches and validate after each batch;
- keep Cut, rejected, or superseded prose outside the active manuscript when retention is useful; and
- verify that recovery can restore the prior accepted state.

Do not require Git. Do not commit, branch, copy, or checkpoint without authority implied by the user's requested workflow or explicit approval where consequential.

## Maintain and reconcile state

After an accepted batch, update only affected records:

- `BRIEF.md`: creative contract, authority, cadence, constraints, and locked decisions;
- `STYLE.md`: StyleBrief, channel boundaries, authenticity stance, evolution model, confirmed phases, and approved deviations;
- `STATUS.md`: phase, cadence, last accepted unit, immediate state, open decisions, Proposed details, risks, next action, batch limit, required context, persistent write policy, and latest completed immutable response batch when applicable;
- `SCENES.md`: stable ID, manuscript location, unit state, POV, time, place, purpose, pressure, turn, consequence, knowledge, setup/payoff, research, and continuity;
- `CANON.md`: scoped fact, state, basis, and retcon reference;
- `CHARACTERS.md`: goals, pressures, capabilities, limitations, relationships, knowledge, arc state, and speech tendencies;
- `TIMELINE.md`: events, order, duration, ages, travel, deadlines, dependencies, and uncertainty;
- `ARCS.md`: setup, development, turn, payoff, and status;
- `RESEARCH.md`: question, source, access, verification, decision, and affected story locations; and
- `DECISIONS.md`: authority, rationale, affected artifacts, checkpoint, and canon-lock effect.

Reconcile ledger claims with accepted prose. Surface rather than silently resolve discrepancies. Keep `STATUS.md` compact enough to resume, and never use it as a substitute for the authoritative manuscript.

## Use optional project tooling

When executable access and Python are available, the bundled `scripts/fiction_project.py` may initialize approved templates, check state, create checkpoints, or assemble accepted Markdown units. Read its help before use.

- Run mutation-capable commands in dry-run mode first.
- Require the user's approved destination and profile before initialization.
- Use `--apply` for creation or assembly.
- Never overwrite an existing file or destination.
- Treat tool output as structural evidence, not a creative or continuity verdict.

When the script is unavailable, follow the same contracts manually with the templates. The script is optional; the Markdown workflow remains authoritative.

The separate `scripts/write_history.py` helper may preserve baseline and response batches for either fiction or non-fiction projects. It does not decide which prose is authoritative or accepted.
