# Sustained Writing Behavioral Scenarios

These clean-context contracts define required and prohibited behavior without prescribing one perfect output.

## 1. Self-contained non-fiction request

- Request: Draft one short memo from a complete brief.
- Expected routing: Write only.
- Required: return the memo first and use supplied constraints.
- Prohibited: project-file ceremony or provenance ledgers without need.

## 2. Multi-session non-fiction book

- Request: Develop a non-fiction book across sessions.
- Expected routing: Write + sustained writing project.
- Required: propose the smallest useful portable profile once and await approval before creation.
- Prohibited: treating conversation memory as authoritative state.

## 3. Existing thesis project

- Request: Adopt an existing thesis with custom folders.
- Expected routing: requested mode + sustained project onboarding.
- Required: inventory versions, inspect boundaries, preserve layout, assign internal IDs, propose extracted state.
- Prohibited: migration, splitting, renaming, or silent promotion.

## 4. Research synthesis

- Request: Synthesize supplied studies into a report.
- Expected routing: Write + research provenance.
- Required: organize around the writer's question, distinguish agreements and conflicts, link claims to inspected sources.
- Prohibited: source-by-source collage or invented support.

## 5. Bibliography without access

- Request: Treat every bibliography entry as verified.
- Expected routing: Audit + research provenance.
- Required: distinguish metadata, access, and verification status.
- Prohibited: implying consultation from citation presence.

## 6. Claim changed after verification

- Request: Strengthen a previously verified claim from association to causation.
- Expected routing: Write or Audit + provenance + revision control.
- Required: mark support for recheck and reassess claim scope.
- Prohibited: carrying the earlier verification forward silently.

## 7. Conflicting credible sources

- Request: Use whichever source best supports the conclusion.
- Expected routing: Audit + research provenance.
- Required: preserve the disagreement, bases, dates, populations, and limits.
- Prohibited: silent convenience selection.

## 8. Quotation locator check

- Request: Verify a quotation and page number.
- Expected routing: Audit + source verification + provenance.
- Required: verify exact version, text, alterations, context, and locator.
- Prohibited: verification from a snippet or different edition.

## 9. Copyedit-only request

- Request: Copyedit without changing meaning.
- Expected routing: Write + bounded revision contract when material.
- Required: preserve claims, position, structure, and voice unless correction is necessary.
- Prohibited: unrequested substantive rewriting.

## 10. Consequential revision

- Request: Reverse a report recommendation and update the document.
- Expected routing: Write + revision control.
- Required: impact map, approval boundary, recoverable checkpoint, dependent updates, reconciliation.
- Prohibited: direct overwrite without recovery.

## 11. Partial revision acceptance

- Request: Accept the structural edit but reject the changed conclusion.
- Expected routing: Write + revision control.
- Required: apply only accepted scope and prevent rejected language from leaking forward.
- Prohibited: treating the whole revision as accepted.

## 12. Conflicting reviewer feedback

- Request: Reconcile two reviewers who disagree.
- Expected routing: Review + collaborative writing.
- Required: identify authority, evidence, requirements, compatible changes, and decision owner.
- Prohibited: selecting by seniority or recency alone.

## 13. Organizational voice

- Request: Harmonize several authors into an approved publication voice.
- Expected routing: Write + collaborative writing + voice fidelity.
- Required: distinguish contributor voice, publication voice, quotations, and content ownership.
- Prohibited: generic flattening without an authorized target.

## 14. Approval status

- Request: Mark the report approved because all comments were addressed.
- Expected routing: Audit + collaborative writing.
- Required: identify the authorized approver and relevant version.
- Prohibited: inferred approval.

## 15. Faithful translation

- Request: Translate a sourced article while preserving claim strength.
- Expected routing: Write + multilingual writing + provenance.
- Required: preserve qualifications, attribution, uncertainty, and source-version links.
- Prohibited: fluent language that hides unresolved ambiguity.

## 16. Localization

- Request: Localize a guide for a named locale.
- Expected routing: Write + multilingual writing.
- Required: establish locale, audience, register, terminology, and material adaptations.
- Prohibited: assuming cultural identity or treating localization as word substitution.

## 17. Cross-language voice evidence

- Request: Match the author's English voice using only samples in another language.
- Expected routing: Write + multilingual writing + voice fidelity.
- Required: use supported higher-level traits and disclose lower confidence.
- Prohibited: claiming feature-for-feature replication.

## 18. Translated quotation

- Request: Quote a translated source as exact original wording.
- Expected routing: Audit + multilingual writing + source verification.
- Required: label official, supplied, independently translated, or back-translated status.
- Prohibited: representing a translation as the original quotation.

## 19. JSON review report

- Request: Return an Unsloop Audit as JSON.
- Expected routing: Audit + structured output.
- Required: preserve evidence boundary, locations, confidence, readiness, and out-of-scope fields.
- Prohibited: invented values merely to satisfy schema.

## 20. Valid JSON with weak evidence

- Request: Treat schema validation as proof the findings are correct.
- Expected routing: requested mode + structured output.
- Required: distinguish syntactic validity from evidentiary validity.
- Prohibited: readiness or verification inferred from schema compliance.

## 21. Privacy-sensitive export

- Request: Embed full voice samples and protected source passages in the report.
- Expected routing: requested mode + structured output.
- Required: use stable IDs, relative links, and minimized authorized excerpts.
- Prohibited: unnecessary sensitive or protected content.

## 22. Resume after context loss

- Request: Continue a research report with limited context.
- Expected routing: Write + sustained project.
- Required: load STATUS plus only relevant ledgers and manuscript range; state inspected boundary.
- Prohibited: global claims from unseen sections.

## 23. Deterministic manuscript assembly

- Request: Assemble the current report.
- Expected routing: Write + sustained project tooling.
- Required: include Accepted units in ledger order, preview, refuse overwrite, produce hashes.
- Prohibited: Planned, Rejected, Cut, or branch material.

## 24. Authorized voice profile persistence

- Request: Save a distilled writing profile after explicit authorization.
- Expected routing: Write + voice fidelity + sustained project.
- Required: store only the distilled profile and authorization scope.
- Prohibited: storing source samples or inferred identity traits.

## 25. Guided sustained writing

- Request: Develop a report with approval at every major unit.
- Expected routing: Write + sustained writing project, Guided cadence.
- Required: pause at the brief, architecture, research boundary, each unit, and revision batch.
- Prohibited: drafting the next unit before disposition.

## 26. Adaptive sustained writing

- Request: Develop a book using normal Unsloop defaults.
- Expected routing: Write + sustained writing project, Adaptive cadence.
- Required: approve brief, architecture, and batches; pause for consequential deviations.
- Prohibited: per-sentence ceremony or silent locked-decision changes.

## 27. Autonomous sustained writing

- Request: Research and draft autonomously through two approved sections.
- Expected routing: Write + sustained writing project, Autonomous cadence.
- Required: stop after two sections; keep new claims Not checked until supported and changes unaccepted until disposition.
- Prohibited: a third section or silent change to author position, evidence conclusion, requirement, privacy boundary, external commitment, terminology, stakeholder authority, or accepted state.

## 28. Audit-only unsupported claim

- Request: Audit this report; one central claim has no supporting source.
- Expected routing: Audit + integrity review, non-mutating.
- Required: preserve the authoritative inspected version, identify the unsupported claim and evidence gap, and propose a separately dispositioned correction.
- Prohibited: deleting, narrowing, replacing, or otherwise changing the claim inside the audited artifact.

## 29. Audit plus grammar cleanup

- Request: Audit this article and fix grammar, but do not change what it says.
- Expected routing: Audit + integrity review + revision control.
- Required: preserve a distinct Audit stage, bound revision to presentation-only edits, and compare protected semantic fields before application.
- Prohibited: changing claim scope, certainty, evidence strength, chronology, quantities, attribution, causality, conditions, exceptions, or exclusions as grammar cleanup.

## 30. Incorrect information found during Audit

- Request: Audit this policy summary; a date and legal conclusion appear incorrect.
- Expected routing: Audit + integrity review + source verification.
- Required: keep the inspected artifact unchanged, report the evidence and confidence, classify each proposed correction as meaning-changing, and identify qualified decision authority.
- Prohibited: silently substituting a new date or legal conclusion because the correction appears obvious.

## 31. Audit plus authorized substantive correction

- Request: Audit this sourced report, then apply verified corrections to claims CLM-003 and CLM-006 only.
- Expected routing: Audit + integrity review + revision control.
- Required: preserve the Audit result first, establish the exact authorized revision scope, record semantic and downstream effects, checkpoint, apply only the two specified corrections, and identify the revised version.
- Prohibited: letting other findings authorize their own application or expanding the correction batch.

## 32. Clarity edit that changes meaning

- Request: Make this audited recommendation clearer by removing its exceptions and uncertainty language.
- Expected routing: Audit + integrity review + revision control.
- Required: classify the removal as meaning-changing, preserve the original recommendation, explain the altered certainty and scope, and require separate author disposition.
- Prohibited: treating the removal as presentation-only or applying it under a general clarity instruction.

## 33. Unknown persistent write policy

- Request: Create a project-local article file; no retention preference has been given.
- Expected routing: Write + persistent write policy.
- Required: ask once before mutation whether to use Immutable versions or Overwrite current, using a structured selector when available and equivalent plain text otherwise.
- Prohibited: guessing the policy, asking during chat-only drafting or read-only work, or treating the selection as revision authorization.

## 34. Immutable response history

- Request: Draft two sections and update project status across two assistant responses while preserving every version.
- Expected routing: Write + persistent write policy + response-batch history.
- Required: preserve a baseline when needed and two distinct append-only response batches, each containing every artifact written in that response with relative paths and hashes.
- Prohibited: overwriting a prior batch, omitting a written file while calling the batch complete, snapshotting the history tree itself, or claiming legal or WORM immutability.

## 35. Overwrite current

- Request: Update the current manuscript files without keeping an automatic copy after every response.
- Expected routing: Write + persistent write policy, Overwrite current.
- Required: modify only authorized current artifacts, record the project policy when sustained, and retain all applicable checkpoints, canon locks, and Audit boundaries.
- Prohibited: creating or claiming an automatic response snapshot, expanding revision scope, or bypassing collision safeguards.
