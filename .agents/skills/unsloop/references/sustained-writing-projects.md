# Sustained Writing Projects

Read this file for multi-session or multi-artifact non-fiction such as a book, thesis, report, course, documentation set, research synthesis, policy, or substantial professional deliverable.

## Contents

- [Scale the project](#scale-the-project)
- [Choose collaboration cadence](#choose-collaboration-cadence)
- [Choose persistent write policy](#choose-persistent-write-policy)
- [Preserve authority and layout](#preserve-authority-and-layout)
- [Use portable project state](#use-portable-project-state)
- [Onboard existing work](#onboard-existing-work)
- [Draft and resume](#draft-and-resume)
- [Complete and hand off](#complete-and-hand-off)

## Scale the project

Do not create project files for a self-contained request by default. For work likely to span sessions, models, sources, or reviewers, propose the smallest useful Markdown profile once and create it only after approval.

- **Compact:** brief, status, outline, section ledger, and manuscript units.
- **Research:** add claims, sources, quotations, requirements, and decisions; also add a source policy and research log when evidence is gathered beyond supplied material.
- **Collaborative:** add stakeholders, changes, requirements, and decisions.
- **Full:** combine the relevant ledgers; add terminology only when controlled language or cross-document consistency matters.

Use `assets/writing-project/` as optional templates. Manual Markdown remains the baseline.

## Choose collaboration cadence

For persistent work, offer the same portable cadence choices without changing the public mode:

- **Guided:** approve the brief, architecture, research boundary, each major unit, and each revision batch.
- **Adaptive (Recommended):** approve the brief, architecture, and work batches; pause for consequential deviations or conflicts.
- **Autonomous:** approve the project contract and batch limit, then work through that batch while maintaining Proposed, Not checked, and unaccepted state until the checkpoint.

Even in Autonomous cadence, pause before changing the author's position, evidence conclusion, governing requirement, privacy boundary, external commitment, approved terminology, translation policy, stakeholder authority, or accepted manuscript state. Do not promote claims, decisions, changes, or approval from silence.

## Choose persistent write policy

Before creating or changing project files, resolve **Immutable versions** or **Overwrite current** through [write-history.md](write-history.md) unless the project already records the choice. Store the confirmed policy in `BRIEF.md` or `STATUS.md`. Under Immutable versions, use one append-only response batch for all writing files changed together and keep `unsloop-history/` beside `writing/` and `manuscript/` unless an existing coherent version system is accepted. Under Overwrite current, retain the ordinary checkpoint rules for consequential changes.

## Preserve authority and layout

Treat the user's current directions and accepted decisions as authority for intended content. Treat accepted manuscript text as evidence of what the current artifact says. Ledgers summarize those authorities; they do not silently overrule them.

Before persistent changes:

1. inventory artifacts, versions, notes, requirements, sources, and existing records;
2. state the exact files and ranges inspected;
3. resolve the authoritative working version from explicit direction and accepted state, not timestamps alone;
4. preserve a coherent existing layout;
5. assign stable internal section IDs without renaming files automatically; and
6. obtain approval before creating, moving, splitting, or replacing files.

Extracted claims, requirements, decisions, and terminology remain Proposed or Unverified until their basis supports promotion.

## Use portable project state

```text
writing/
  BRIEF.md
  STATUS.md
  OUTLINE.md
  STYLE.md
  SECTIONS.md
  CLAIMS.md
  SOURCES.md
  SOURCE-POLICY.md
  RESEARCH-LOG.md
  QUOTATIONS.md
  REQUIREMENTS.md
  DECISIONS.md
  CHANGES.md
  STAKEHOLDERS.md
  TERMINOLOGY.md
  CHRONOLOGY.md
  VALIDATION.md
  DATA.md
  INTERVIEWS.md
  MEDIA.md
  CONTENT-MAP.md
  MAINTENANCE.md
  USABILITY.md
manuscript/
  001-title.md
```

Create only the files the project needs. Use relative paths and stable IDs:

- `SEC-*` for manuscript units;
- `SRC-*` for sources;
- `CLM-*` for claims;
- `QTE-*` for quotations;
- `REQ-*` for requirements;
- `DEC-*` for decisions; and
- `CHG-*` for proposed or applied changes.

Add `STYLE.md` only when a selected Style Direction or planned stylistic evolution must remain stable across sections, sessions, models, or collaborators. Keep author voice, document voice, quoted-source voice, and form-specific conventions distinct. Style phases use stable `STP-*` identifiers and Proposed, Confirmed, or Superseded state; a confirmed phase cannot change silently.

Add `CHRONOLOGY.md` for evidence-led narrative or biography and `VALIDATION.md` for procedures, policies, plans, or technical documents only when those records improve control. Read [documentary-documentation.md](documentary-documentation.md) for form-specific contracts and [source-acquisition.md](source-acquisition.md) for supplied, scoped-web, broad-web, or hybrid research.

Add `DATA.md` for material quantitative claims, `INTERVIEWS.md` for oral evidence, `MEDIA.md` for transformed multimodal evidence, `CONTENT-MAP.md` for an interconnected documentation set, `MAINTENANCE.md` for publication lifecycle, and `USABILITY.md` for reader or task validation. Create only records the project will maintain.

Use these project phases: **Discovery**, **Briefing**, **Research**, **Architecture**, **Drafting**, **Revision**, **Approval**, **Complete**, or **Archived**.

`STATUS.md` is the resume packet. Record the phase, authoritative version, last accepted unit, checkpoint, evidence boundary, immediate context, open decisions, stale or disputed support, next approved action, and files needed to resume. It does not replace the manuscript or source records.

Also record the confirmed persistent write policy and, when Immutable versions applies, the latest completed response batch. Do not infer authority from batch recency alone.

## Onboard existing work

1. Inventory every supplied version and format without mutation.
2. Record inspected and inaccessible ranges.
3. Resolve authority or surface the ambiguity.
4. Map units and assign stable internal IDs.
5. Extract tentative claims, sources, requirements, decisions, terminology, and change requests with locations and confidence.
6. Mark extracted state Proposed, Not checked, or Unverified as appropriate.
7. Present conflicts and the smallest useful project profile.
8. Obtain approval before creating records or promoting state.
9. Create only missing approved files and refuse overwrite.
10. Produce a compact resume state.

Keep monolithic documents intact unless the user authorizes splitting. For non-Markdown formats, use the host's document tools and disclose any formatting or content boundary not inspected.

## Draft and resume

Use manuscript-unit states **Planned**, **Drafted**, **Revised**, **Accepted**, **Cut**, and **Archived**. Assembly includes Accepted units by default.

At each meaningful checkpoint:

- identify the unit and manuscript version;
- update requirements and provenance affected by the work;
- record new decisions and unresolved questions;
- keep unsupported or disputed claims visible;
- apply accepted changes only;
- update `STATUS.md`; and
- load only the records and manuscript range needed for the next action.

Do not infer approval from silence when the workflow requires disposition.

## Complete and hand off

Distinguish content completion, evidence verification, substantive revision, line editing, copyediting, assembly, approval, and delivery. A complete-looking project ledger does not prove factual support, policy compliance, or professional approval.

At handoff, state the authoritative version, included and excluded units, governing requirements, evidence boundary, unresolved claims or decisions, applied changes, assembly manifest when present, and next action.
