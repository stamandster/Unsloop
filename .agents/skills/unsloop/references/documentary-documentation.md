# Documentary and Documentation Writing

Read this file for long-form factual narrative or controlled documents, including biography, documentary narrative, case history, procedure, policy, plan, direction, instruction, manual, specification, runbook, reference, or technical documentation.

Load [interview-evidence.md](interview-evidence.md), [quantitative-evidence.md](quantitative-evidence.md), [multimodal-evidence.md](multimodal-evidence.md), [documentation-systems.md](documentation-systems.md), or [usability-validation.md](usability-validation.md) only when the artifact uses those evidence types or lifecycle needs.

## Contents

- [Select the artifact family](#select-the-artifact-family)
- [Build the document contract](#build-the-document-contract)
- [Set the evidence acquisition policy](#set-the-evidence-acquisition-policy)
- [Gather and reconcile material](#gather-and-reconcile-material)
- [Apply the form contract](#apply-the-form-contract)
- [Draft and validate](#draft-and-validate)
- [Revise and hand off](#revise-and-hand-off)

## Select the artifact family

Distinguish the requested form before research or architecture:

- **Documentary narrative or biography:** evidence-led account of people, events, institutions, places, or a question over time.
- **Procedure or instruction:** repeatable actions intended to produce a defined result safely and correctly.
- **Policy:** authorized rules, obligations, permissions, prohibitions, exceptions, and controls.
- **Plan or direction:** proposed objectives, sequence, owners, dependencies, decisions, risks, and measures.
- **Technical documentation:** versioned explanation or reference for a system, product, process, interface, environment, or implementation.

Use Write for research planning, architecture, drafting, requested revision, and handoff; Review for factual-form, clarity, usability, coherence, and voice diagnosis; and Audit for non-mutating evidence, provenance, currency, compliance, requirement, procedure-validation, or technical-accuracy comparison. Audit reports unsafe, unsupported, stale, or incorrect information without silently changing the controlled document. Do not create a fourth mode.

When the user says “documentary style,” confirm or infer whether they mean evidence-led narrative voice, a documentary script, or controlled documentation. Do not apply cinematic narration to a policy or operational procedure unless explicitly requested.

For documentary scripts, narrated explanations, timed training, guided demonstrations, or presentation-bound controlled documents, read [delivery-and-presentation.md](delivery-and-presentation.md).

## Build the document contract

Extract before asking:

1. artifact family, deliverable, format, length, and intended use;
2. topic, governing question, thesis or operational outcome;
3. audience, prior knowledge, decisions or actions expected;
4. authority, owner, approvers, applicable standards, templates, and non-waivable directions;
5. factual scope, jurisdictions, systems, people, dates, versions, and exclusions;
6. evidence acquisition mode and source scope;
7. voice, narrator stance, terminology, accessibility, localization, and quotation policy;
8. privacy, consent, confidentiality, safety, security, legal, reputational, and publication boundaries;
9. required validation, testing, review, and readiness stage; and
10. update owner, effective date, review cycle, and maintenance expectations when applicable.

Mark consequential fields Known, Inferred, or Unknown. Distinguish what **is**, what a source **claims**, what is **inferred**, what is **proposed**, and what an authority **requires**.

## Set the evidence acquisition policy

Use [source-acquisition.md](source-acquisition.md) when evidence may be gathered beyond the user's supplied materials. Select one mode:

- **User-provided only**;
- **Scoped web** limited to approved sites or domains;
- **Broad web** with an approved topical and privacy boundary; or
- **Hybrid** using supplied material plus scoped or broad research.

Do not browse merely to add volume. Research the decisions, claims, chronology, instructions, or versions that materially affect the artifact. For current, changing, disputed, high-stakes, or publication-bound claims, verify against appropriate sources rather than relying on model memory.

## Gather and reconcile material

1. Inventory user-supplied facts, testimony, notes, records, sources, requirements, and unresolved questions.
2. Separate voice or narrative examples from factual evidence.
3. Create a claim and source plan before broad collection.
4. Search within the approved scope and record what was actually inspected.
5. Prefer original, authoritative, primary, or technically controlling material when it fits the claim.
6. Seek independent corroboration for consequential claims, allegations, self-descriptions, promotional claims, and reconstructed events.
7. Preserve credible conflicts, missing records, and uncertainty.
8. Map each material claim, quotation, requirement, step, or technical assertion to its basis and manuscript location.
9. Stop when the stated coverage and confidence target is reached or remaining gaps are explicit.

User-provided information may be accepted as the user's direction, memory, testimony, or organizational authority where applicable. It is not automatically independent factual verification. Label the role it actually plays.

## Apply the form contract

### Documentary narrative and biography

Establish the central question, factual scope, chronology, subject and narrator relationship, point of view, narrative frame, evidence gaps, disputed accounts, reconstruction policy, quotation policy, and privacy or consent boundary.

- Distinguish documented fact, attributed recollection, supported inference, disputed account, and unknown.
- Never invent quotations, private thoughts, composite events, causal motives, or scene details and present them as fact.
- Label reconstruction, dramatization, composite treatment, or hypothetical illustration explicitly when authorized.
- Treat self-report, institutional records, journalism, archives, interviews, and later recollection according to their actual provenance and limitations.
- For interviews or oral history, preserve consent, attribution, transcript type, correction rights, corroboration, and subject-response status.
- Use heightened care for living people, minors, private persons, allegations, medical or sensitive information, and claims with legal or reputational stakes.
- Keep chronology and identity resolution explicit; do not merge people or events silently.
- Let narrative force come from evidence, selection, contrast, and consequence—not manufactured certainty or sentiment.

### Procedures and instructions

Define task outcome, audience, prerequisites, roles and permissions, tools, materials, environment and version, safety warnings, initial state, ordered steps, decision branches, expected result, verification, failure modes, recovery or rollback, escalation, and maintenance owner.

- Put prerequisites and irreversible warnings before the affected action.
- Use one actionable operation per step where practical.
- Identify exact inputs, outputs, locations, commands, and observable success criteria.
- Distinguish **Tested**, **Partially tested**, **Desk-checked**, **User-reported**, and **Untested** behavior.
- Do not claim a procedure works because it is plausible or well written.
- Preserve alternative paths only when the conditions are explicit.

### Policies

Define issuing authority, purpose, scope, audience, definitions, effective date, normative requirements, permissions, prohibitions, roles, controls, exceptions, evidence or recordkeeping, escalation or enforcement, review cycle, superseded versions, and approval state.

- Distinguish policy from procedure, guidance, law, regulation, contract, and recommendation.
- Use normative terms consistently and define their force for the document.
- Do not invent organizational authority, legal obligations, enforcement powers, approvals, or compliance claims.
- Make exceptions and decision ownership explicit.
- Separate current policy from proposed policy and implementation planning.

### Plans and direction

Define current baseline, desired outcome, scope, assumptions, dependencies, workstreams, owners, resources, sequence, milestones, decision gates, risks, mitigations, contingencies, measures, reporting cadence, change authority, and completion criteria.

- Distinguish commitments from proposals, estimates, options, and assumptions.
- Give every material action an owner or mark it unassigned.
- Expose critical dependencies and unresolved decisions before presenting dates as reliable.
- Do not convert a goal into a guarantee or a schedule into evidence of feasibility.
- Keep direction from authorized owners distinct from supporting rationale and external facts.

### Technical documentation

Define product or system, version, platform, environment, audience, prerequisites, security boundary, interfaces, schemas, configuration, commands, examples, expected outputs, errors, compatibility, limitations, rollback, tested status, and maintenance owner.

- Prefer exact identifiers and versioned authoritative sources.
- Verify material numerical claims, tables, charts, and examples through their source data and transformations when present.
- Mark generated examples, pseudocode, inferred behavior, unexecuted commands, and unverified compatibility.
- Never say code, commands, APIs, links, or procedures were tested unless they were actually run or verified in the stated environment.
- Keep conceptual explanation, tutorial, how-to, reference, troubleshooting, and release information distinct when combining them would confuse the reader.
- Avoid exposing credentials, secrets, private endpoints, exploit details, or unsafe instructions beyond the authorized need.

## Draft and validate

Structure around the user's outcome and the form contract, not the order sources were found. Attribute claims where they enter. Use `CLAIMS.md`, `SOURCES.md`, `QUOTATIONS.md`, `REQUIREMENTS.md`, `SOURCE-POLICY.md`, and `RESEARCH-LOG.md` when persistence improves traceability.

For chapters, headings, subheadings, phases, and other visible divisions, apply [section-flow.md](section-flow.md). Make each boundary express the actual narrative, argumentative, chronological, or operational relationship. Do not insert a generic bridge where hierarchy and sequence already orient the reader, and do not smooth away a necessary warning, exception, decision gate, or deliberate documentary cut.

Validate at the right level:

- documentary or biography: chronology, names, quotations, contested claims, inference labels, consent and privacy boundaries;
- procedure: prerequisites, step order, branches, safety, observable results, failure and recovery;
- policy: authority, scope, definitions, normative consistency, exceptions, controls, approval and version;
- plan: dependencies, owners, dates, resources, risks, gates, measures, and assumption status; and
- technical documentation: version, environment, commands, schemas, examples, outputs, errors, security, compatibility, and tested status.

For a documentation set, also validate content architecture, canonical ownership, cross-references, dependencies, supported versions, stale or deprecated units, corrections, and maintenance triggers. Use real reader or task testing when usability matters; keep simulated hypotheses separate from observed results.

Use human subject-matter, legal, safety, security, compliance, lived-experience, or technical review when the artifact's stakes require it. Unsloop does not certify those judgments.

## Revise and hand off

Use [revision-control.md](revision-control.md) for consequential changes. When revision follows Audit, preserve the unchanged audited version and audit result before creating the separately authorized revised version. At handoff, state the authoritative artifact version, form and audience, evidence acquisition mode, sites or corpora inspected, claim and quotation boundary, validation performed, tested or approval status, unresolved gaps, excluded material, maintenance owner, and next action.

Do not call an artifact factual, tested, compliant, approved, safe, complete, or current beyond the evidence, execution, authority, and date actually established.
