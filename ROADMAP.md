# Roadmap

> **Document role:** Delivery sequence for the baselines in [`BRD.md`](BRD.md), [`PRD.md`](PRD.md), and [`FSD.md`](FSD.md). Checked items indicate implemented documentation or controls, not empirical validation unless stated.

## v0.1 — Foundation

**Goal:** Turn the project vision into a coherent method and usable core skill.

- [x] Define Unsloop, Review, Write, and Audit
- [x] Separate integrity and human-voice lenses
- [x] Define source-dependence scoring
- [x] Define directional voice-profile scores
- [x] Define consent-aware voice sampling and evidence hierarchy
- [x] Define optional voice-fidelity scoring and confidence labels
- [x] Define the progressive writing brief and proportional intake rules
- [x] Add existing-topic, topic-refinement, and topic-brainstorming entry paths
- [x] Add capability-aware structured questions with a conversational fallback
- [x] Add governing-direction hierarchy and explicit content roles
- [x] Add hard-constraint, allocation, and safety-buffer handling
- [x] Add requirement-coverage and readiness contracts
- [x] Add functional-example and emotional-integrity review
- [x] Establish output, evidence, and ethics contracts
- [x] Create and validate the repo-local core skill under `.agents/skills`
- [x] Add dependency-free project-local validation
- [x] Initialize portable Git metadata and line-ending rules
- [x] Add optional global discovery through a link to the authoritative project skill
- [x] Establish BRD, PRD, and FSD baselines with requirement traceability
- [x] Align all project and operational Markdown with the specification hierarchy
- [x] Define a model- and harness-agnostic Agent Skills core
- [x] Preserve Codex support while documenting Claude, Pi, and generic harness adapters
- [x] Add capability negotiation and fallbacks for harness and model differences
- [x] Add a topic-neutral fiction workflow within Unsloop Write for scenes through series
- [x] Add Guided, Adaptive, and Autonomous fiction collaboration cadences
- [x] Add author-approved portable fiction state with resumable status and classified canon
- [x] Separate author, narrative, viewpoint, and dialogue voice targets
- [x] Add manuscript-scale context, continuity, research, retcon, and handoff controls
- [x] Route fiction through Write, Review, and Audit without adding a fourth mode
- [x] Add existing-manuscript onboarding with Proposed extraction and authority confirmation
- [x] Add manuscript-unit, batch, branch, partial-acceptance, and rejection lifecycles
- [x] Add retcon impact maps and recoverable consequential revision
- [x] Add portable fiction templates and optional fail-closed project tooling
- [x] Add focused fiction-review and bounded publication-handoff workflows
- [x] Add deterministic tests for project initialization, validation, checkpointing, assembly, overwrite refusal, authorization, and path safety
- [x] Add 30 clean-context behavioral fixture contracts covering critical fiction operations and boundaries
- [x] Add proportionate sustained non-fiction project state, onboarding, resumption, assembly, and handoff
- [x] Add claim, source, quotation, conflict, manuscript-location, and verification-freshness provenance
- [x] Add general revision classification, partial disposition, impact analysis, checkpoints, and reconciliation
- [x] Add stakeholder authority, feedback consolidation, and version-specific approval boundaries
- [x] Add multilingual, localization, translated-quotation, and cross-language voice workflows
- [x] Add an optional machine-readable Unsloop report schema and portable JSON project-state export
- [x] Add sustained-writing templates and fail-closed standard-library project tooling
- [x] Add Guided, Adaptive, and Autonomous sustained non-fiction collaboration cadences
- [x] Add deterministic sustained-project tests and 27 clean-context behavioral scenario contracts
- [x] Add author-controlled, versioned character personality and dialogue profiles with drift and override controls
- [x] Add documentary, biography, procedure, policy, plan, direction, instruction, and technical-documentation form contracts
- [x] Add user-only, scoped-web, broad-web, and hybrid source acquisition with claim-specific suitability and non-upgrading overrides
- [x] Add documentary chronology and validation ledgers plus 24 clean-context behavioral scenario contracts
- [x] Add cross-skill responsibility, authority, conflict, and unified-handoff composition
- [x] Add untrusted-source instruction isolation, active-content boundaries, and sensitive-data safeguards
- [x] Add quantitative, interview/oral-history, and multimodal evidence workflows and portable ledgers
- [x] Add documentation-system architecture, dependency, maintenance, correction, deprecation, withdrawal, and archival controls
- [x] Add reader, task, accessibility, plain-language, and localization validation evidence states
- [x] Add 24 clean-context operational extension scenarios and deterministic ledger checks

## v0.2 — Examples and calibration

**Goal:** Test whether different reviewers apply the method consistently.

- [ ] Build anonymized fixtures for quotation, paraphrase, patchwriting, structural dependence, and secondary-source problems
- [ ] Build voice fixtures covering multiple genres and levels of formality
- [ ] Test sparse, conflicting, cross-genre, and multilingual voice samples
- [ ] Test sparse, conflicting, over-specified, and high-stakes writing briefs
- [ ] Test topic discovery with no seed, a rough direction, and an already explicit topic
- [ ] Test equivalent decisions through structured and plain-text question interfaces
- [ ] Test conflicting governing directions and hard-versus-working constraints
- [ ] Test requirement coverage independently from factual support
- [ ] Test readiness labels against unresolved choices, evidence, and authorization
- [ ] Test emotional-integrity findings across persuasive, pastoral, commercial, and personal genres
- [ ] Add expected evidence notes without prescribing a single perfect rewrite
- [ ] Forward-test brief, standard, and deep reviews in clean contexts
- [ ] Revise ambiguous scale anchors
- [ ] Record common false positives, especially for second-language and highly conventional writing
- [ ] Convert the FSD verification matrix into reusable fixtures with expected boundaries and outputs
- [ ] Trace fixture results back to `PR-*`, `NFR-*`, and `FS-*` requirements
- [ ] Forward-test the same Review, Write, and Audit fixtures in Codex, Claude, Pi, and at least one manual Agent Skills adapter
- [ ] Compare model families and context sizes without treating one model's output as the reference truth
- [ ] Test missing-tool fallbacks for structured input, browsing, file editing, memory, and length measurement
- [ ] Test minimal scene, short-story, novel, serial, and series workflow scaling
- [ ] Test Guided, Adaptive, and Autonomous checkpoint behavior with consequential deviations
- [ ] Test Proposed-to-Confirmed canon promotion, explicit retcons, and manuscript-ledger conflicts
- [ ] Test cross-session fiction resumption from `story/STATUS.md` with partial manuscript context
- [ ] Test author, narrative, viewpoint, and dialogue voice separation across fiction genres
- [ ] Test historical fiction, named-author adaptation, real-person depiction, and incomplete research boundaries
- [ ] Forward-test existing-manuscript onboarding across monolithic and multi-file projects
- [ ] Forward-test partial acceptance, rejection, branch merge, retcon, and recovery behavior
- [ ] Forward-test developmental, continuity, simulated-reader, and authenticity review boundaries
- [ ] Forward-test assembly and publication-support artifacts against supplied requirements
- [ ] Forward-test compact, research, collaborative, and full sustained-writing profiles
- [ ] Forward-test claim freshness, conflicting sources, quotation versions, and bibliography boundaries
- [ ] Forward-test partial non-fiction revision acceptance and multi-reviewer authority conflicts
- [ ] Forward-test translation, localization, cross-language voice, and structured-output equivalence
- [ ] Forward-test multi-character voice distinction, contextual variation, drift detection, prospective evolution, and retroactive override
- [ ] Forward-test biography reconstruction and living-person allegation boundaries
- [ ] Forward-test scoped-site stopping, broad-web counterevidence, weak-source overrides, and stale-source refresh
- [ ] Forward-test procedure, policy, plan, and technical-document validation states with qualified reviewers
- [ ] Forward-test cross-skill composition with domain, DOCX/PDF, spreadsheet, and coding skills
- [ ] Forward-test prompt injection, redirects, active downloads, credential requests, and hostile metadata in research corpora
- [ ] Forward-test numerical reproduction, interview permissions, OCR/transcript uncertainty, and visual-claim boundaries
- [ ] Forward-test content dependency propagation, correction, deprecation, withdrawal, archival, and reader-validation labeling

## v0.3 — Assisted audit tooling

**Goal:** Reduce mechanical comparison work while keeping findings inspectable.

- [ ] Prototype passage alignment across draft and supplied sources
- [ ] Surface shared wording, syntax, idea order, and detail selection separately
- [ ] Export a source map without assigning misconduct
- [ ] Add citation and locator verification hooks
- [ ] Define privacy expectations for local and external processing
- [ ] Add adapter fixtures that verify identical evidence and ethics boundaries across harnesses

## v0.4 — Mode specialization

**Goal:** Decide whether observed use justifies separate skills.

- [ ] Evaluate trigger precision for Review, Write, and Audit
- [ ] Split only the modes that meet the criteria in `docs/NAMING.md`
- [ ] Add user-approved persistent personal-voice and publication-style profiles
- [x] Support Markdown and machine-readable review reports

## v1.0 — Validated release

**Goal:** Publish a stable, documented method with known limits.

- [ ] Demonstrate acceptable inter-reviewer agreement on the core classifications
- [ ] Publish benchmark design and limitations
- [ ] Stabilize score anchors and output contracts
- [ ] Complete privacy, accessibility, and bias review
- [ ] Document installation and release packaging outside the skill bundle
- [ ] Publish a cross-harness compatibility matrix with tested versions and known limitations

## Open questions

- Should source dependence be reported per passage, per source, or both?
- Which genres need their own voice expectations?
- What minimum sample diversity supports High voice-fidelity confidence across genres?
- What minimum evidence should be required before assigning High or Critical severity?
- When does a separate mode skill improve reliability enough to justify maintenance cost?
- What evidence threshold should move the BRD/PRD/FSD baseline from documented to empirically validated?
