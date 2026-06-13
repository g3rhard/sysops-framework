# SysOps Framework — Development TODO

> **LLM/Agent Instructions**: Use `- [x]` = verified complete, `- [ ]` = not yet done, `- [~]` = partial/needs improvement. Check file content before marking anything complete — do not infer from headings alone. Priority tiers: **P1** = must-have, **P2** = important, **P3** = nice-to-have.

> **Editorial conventions** (keep these in mind for every edit):
>
> - **Audience** is defined up front (README, `_index.md` "Who This Book Is For", and a Chapter 1 callout): teams of highly skilled individuals each running separate projects/systems/pagers under one team name, whose work is a mix of operational + R&D + only some development, where agile/scrum doesn't fit and they want _order_. The book is intentionally opinionated about bringing that shared work together without a lockstep cadence.
> - **Readability**: chapters deliberately mix the necessary dense reference material with jokes, short stories, and wry asides so the book reads as human-written, not AI-generated. Preserve this voice when editing.
> - **Appendix rule**: detailed tick-box checklists and milestone trackers live in `content/docs/chapter-13-appendices.md`. Chapters keep the narrative, key points, and general plan, then point to the appendix.

---

## Status Summary (as of 2026-06-12)

| Area                            | Done | Partial | Remaining |
| ------------------------------- | ---- | ------- | --------- |
| Chapter content gaps            | 14   | 0       | 0         |
| Missing practices               | 5    | 0       | 0         |
| Cross-references & data         | 6    | 0       | 0         |
| Appendices & glossary           | 2    | 0       | 0         |
| Medium-priority content         | 6    | 0       | 1         |
| Diagrams (matplotlib PNGs)      | 4    | 0       | 0         |
| Mermaid conversion for PDF/EPUB | 0    | 0       | all       |
| Foundation & consistency (P0)   | 0    | 0       | 11        |
| Quality & infrastructure (P1)   | 0    | 0       | 4         |
| Product & repo (P1/P2)          | 0    | 0       | 5         |
| Gamification elements           | 0    | 0       | all       |

---

## 🏗️ P0 — Foundation & Consistency

> **Status**: None started. These are the most critical items from the editorial audit — they fix the book's entry funnel, resolve internal contradictions, and establish the operating model.

### Entry Funnel Rewrites

- [ ] **`_index.md`: Clarify promise, audience, and outcomes** — Add a one-liner at the top ("What this framework fixes"), followed by explicit "Who this is for" / "Who should not use this" / "Outcome at 30/90/180 days". Collapse the benefits block and move community/support to the bottom. Add a compact Mermaid narrative-arc diagram and a "Team profile → Should you read this?" table. Remove or clearly mark commercial/training offers that aren't live yet.
- [ ] **`getting-started/_index.md`: Restructure as pilot guide** — Rebuild as a decision-based entry point with two explicit tracks: "Pilot in one team" (30-day) and "Full rollout" (180-day). Replace abstract prerequisites with observable signals. Link success indicators to concrete artifacts. Add a clear exit to either "ready for pilot" or "close readiness gaps first".
- [ ] **Chapter 1: Add formal Problem Statement and Design Requirements** — After the research block, add a formal 5–7 sentence "Problem Statement" section that closes the argument. After "Key Insights", add "Design Requirements for a Better Ops Methodology" so Chapter 2 reads as the answer, not a philosophical leap. Add small-team and regulated-environment examples to broaden relevance.
- [ ] **Chapter 2: Add principle precedence rules and anti-patterns** — For each principle, add a consistent micro-structure: "what it protects / what it costs / common misuse / proxy metrics / failure mode". Add a precedence-rules table for conflicts (e.g. reliability vs speed). Strengthen the bridge to Chapter 3 so the three-cycle model follows naturally.
- [ ] **Chapter 3: Add one-page operating model and concrete calendars** — Lead with a single-page "operating model" visual showing which work type lives in which cycle, outputs that flow between cycles, and cycle owners. Add two concrete schedule examples: one for a small ops team, one for a platform/SRE team. Clarify that the 60–70 / 20–30 / 10–20 split is a hypothesis, not a KPI.

### Consistency Fixes

- [ ] **Fix practice count everywhere (6/7/12 → 12)** — Audit and correct every mention of the practice count across all files: `chapter-04-comparison.md` (says "six"), `data-relationships.md` (says "seven"), `glossary.md` (says "seven"), `_index.md` and `chapter-01-challenge.md` and any other page that references the count. The canonical number is **12 core management practices** as defined in Chapter 6.
- [ ] **Create `data/framework.yaml` as single source of truth** — A canonical YAML file describing cycles, principles, practices, metric categories, and their relationships. Use it to generate glossary clusters, data-relationship diagrams, practice-index tables, and home-page summaries so drift can never recur.
- [ ] **Convert ASCII / list schemas to Mermaid diagrams** — Replace all ASCII-art diagrams and verbose list-based schemas in `content/docs/` with proper Mermaid ````mermaid` code blocks. Add captions and meaningful alt-text to every diagram. Key targets: `data-relationships.md` (heavy ASCII), `chapter-03-structure.md` (cycle flow), `chapter-06-practices.md` (practice maps), and any remaining list-as-diagram patterns.
- [ ] **Fix `baseURL` in `hugo.yaml`** — Change `baseURL: https://g3rhard.github.io/sysops-framework` to `https://g3rhard.cc/sysops-framework/` to match the live site and repo metadata.
- [ ] **Update `data-relationships.md` to 12-practice model + Mermaid** — Rewrite the entire page to reflect the current 12-practice model, convert its ASCII diagrams into Mermaid, and make it a generated-from-source page (tied to `data/framework.yaml`).
- [ ] **Update `glossary.md` to 12-practice model** — Fix all references to "seven management practices". Add per-term cross-references ("see also", "related practice", "related metric", "related chapter"). Add canonical terminology policy to prevent future drift.

---

## 📚 Content Gaps

### P1 — Chapter Enhancements (existing — verified complete)

### P1 — Chapter Restructuring & Depth (new — from editorial audit)

- [ ] **Chapter 4: Restructure as buyer's guide** — Rebuild from "framework debate" into "when to use SysOps vs Scrum vs Kanban vs hybrid". Fix the practice-count inconsistency inside the comparison table (P0 cross-reference). Add middle-market and small-team examples. Add a "Quick selection guide" table at the top, "Hybrid operating model patterns" section, and "Stakeholder translation kit".
- [ ] **Chapter 5: Add pilot/full-rollout tracks** — Add two explicit adoption trajectories: a 30-day pilot track and a 180-day full rollout. Give each phase named owners (team lead, on-call owner, manager, sponsor) and required artifacts. Add go/no-go criteria per month and a rollback plan for the rollout itself.
- [ ] **Chapter 6: Add per-practice executive summary block** — For each of the 12 practices, add a consistent top block: "why it exists / minimal version / mature version / key metrics / dependencies / typical anti-patterns". Add a one-page practice index table at the chapter top with columns: criticality, effort, best-first-signal. Medium-term: consider splitting into child pages.
- [ ] **Chapter 7: Add audience-based metric views** — Tie each metric category to a specific audience (on-call, team lead, platform manager, exec sponsor). Add a KPI specification template (definition, owner, cadence, data source, RAG thresholds, action-on-breach). Expand "what not to measure" and "how metrics can be gamed".
- [ ] **Chapter 8: Add minimum viable stacks by team size** — Add three pre-configured stacks at the chapter top: minimum for small team, balanced for mid-size, regulated for enterprise. Separate capability discussion from vendor examples (capability first, then tool choices). Add "what not to buy yet" guidance. Medium-term: split into subpages by tool category.
- [ ] **Chapter 9: Add manager's playbook** — Add concrete manager-oriented content: performance-review signals, career-ladder examples, on-call policy blueprint, stakeholder-expectation reset guidance. Strengthen the "anti-hero culture without anti-expertise" narrative.
- [ ] **Chapter 10: Add control-mapping layer** — Add a control-mapping table showing which practices map to SOC 2 / ISO 27001 / GDPR / internal audit requirements. Distinguish policy, procedure, and evidence more clearly. Add policy-as-code examples (OPA/Rego) and DR-exercise-by-maturity-level guidance.
- [ ] **Chapter 11: Restructure as symptom-driven troubleshooting** — Rebuild around "what you see → probable cause → corrective action" pattern. Add decision trees, rescue playbooks, and false-adoption-signals section.
- [ ] **Chapter 12: Separate near-term/mid-term/horizon** — Split trends into "do now", "watch", and "long-term adapt". Tie each trend back to specific existing chapters (what changes, what stays invariant).
- [ ] **Chapter 13: Export templates as downloadable files** — Add real version-controlled template files in a `templates/` directory: incident, change, SLO, on-call, reporting. Create a `team-starter-pack.zip` that bundles the core templates. Update appendix pages to link to the downloadable versions.

- [x] **Chapter 1: Add source citations** — Converted statistics to "preliminary research" caveat in `chapter-01-challenge.md` (line 37). _Verified._
- [x] **Chapter 2: Acknowledge ITIL/ITSM** — "Note on ITIL and Service Management" section added in `chapter-02-principles.md` (lines 22–35), mapping all 6 principles to ITIL domains. _Verified._
- [x] **Chapter 4: Add Kanban/Lean comparison** — Dedicated "Kanban vs SysOps Framework" section with comparison table and "When Kanban Works Well" / "When SysOps Adds Value" sub-sections added in `chapter-04-comparison.md` (lines 66–115). _Verified._
- [x] **Chapter 4: Add SRE comparison** — "Site Reliability Engineering (SRE) vs SysOps Framework" section with integration table added in `chapter-04-comparison.md` (lines 116–154). _Verified._
- [x] **Chapter 6: Add blameless post-mortem process** — "Blameless Post-Incident Reviews" section added in `chapter-06-practices.md` (lines 103+). _Verified._
- [x] **Chapter 6: Add Incident Command System (ICS) roles** — Full ICS role table (Incident Commander, Scribe, Communications Lead, Technical Lead) added in `chapter-06-practices.md` (lines 166–179). _Verified._
- [x] **Chapter 6: Add Vendor & Contract Management as 7th practice** — Complete section with SLA negotiation, vendor categories, performance monitoring, and risk management added in `chapter-06-practices.md` (lines 420+). _Verified._
- [x] **Chapter 6: Complete maturity model for all practices** — All 7 practices have 5-level maturity assessment in `chapter-06-practices.md` (lines 510–576). _Verified._
- [x] **Chapter 7: Add FinOps metrics** — "FinOps (Financial Operations) Metrics" section with cost per transaction, cloud cost optimization, unit economics added in `chapter-07-metrics.md` (lines 225+). _Verified._
- [x] **Chapter 6: Add Release Management as distinct practice** — Practice 8 added in `chapter-06-practices.md`: CI/CD pipeline governance, deployment gates table, rollback criteria (auto + manual), DORA metrics integration, canary/blue-green example, maturity model level 1–5, and cycle integration entries for all three cycles. _Verified._
- [x] **Chapter 8: Modernize tools section** — Added OpenTelemetry subsection (OTel Collector, OTLP, vendor-neutral observability), GitOps section (ArgoCD + Flux with feature comparison), Service Mesh section (Istio/Linkerd/Cilium comparison table), ChatOps section (example workflow + governance note), and "Modern Platform Engineering Patterns" top-level section covering IDP/Backstage, Policy-as-Code (OPA, Kyverno, Conftest with example), and GitOps multi-environment repo structure. Tool categories updated from 6 to 9. Chapter summary updated. _Verified._
- [x] **Chapter 10: Expand Security & Compliance** — Three new subsections added under Security Integration: "Supply Chain Security" (SBOM formats CycloneDX/SPDX, Syft/Grype tooling, SLSA levels 1–4 table, Sigstore/Cosign, regulatory context); "Breach Response Timelines" (0–30 day timeline table, regulatory clock rules, GDPR Art. 33/34 obligations, tabletop rehearsal); "Penetration Testing Frequency and Scope" (frequency table by asset type, engagement process, remediation tracking). Learning objectives and chapter summary updated. _Verified._
- [x] **Chapter 12: Add modern emerging topics** — Added "FinOps as a Discipline" section (three phases: Inform/Optimize/Operate, tagging enforcement, FinOps tooling, SysOps cycle integration), "Multi-Cloud Operations Strategy" section (pattern table, tooling/observability/identity/cost mitigations, quarterly strategy review), and "Carbon-Aware and Sustainable Infrastructure" section (temporal/spatial shifting, WattTime/Electricity Maps APIs, PUE, SCI score, SysOps integration with Chapter 6/7 practices). Learning objectives and chapter summary updated. _Verified._
- [x] **All chapters: Align ITIL references to ITIL 4 / watch for ITIL 5** — All ITIL references updated to explicitly say "ITIL 4" in `chapter-02-principles.md` (Note on ITIL section fully rewritten: SVS model, 34 practices, 7 guiding principles, per-principle ITIL 4 practice mapping) and `glossary.md` (entry updated; framework comparison list updated). ITIL 5 awareness note added in chapter-02 with a monitor note. No other ITIL references found in remaining chapters. _Verified._

### P1 — Missing Practices (add to Chapter 6 or as standalone pages)

- [x] **Vendor & Contract Management** — Added as Practice 7 in `chapter-06-practices.md`. _Verified._
- [x] **Asset Management** — Practice 9 added in `chapter-06-practices.md`: CMDB design (CI attributes, discovery-driven population, monthly audit), asset lifecycle table (procurement → decommission), software license management (register, reconciliation, SaaS seat tracking, EOL alerting), cloud asset tagging, example CMDB record, maturity levels 1–5. _Verified._
- [x] **Service Request Management** — Practice 10 added in `chapter-06-practices.md`: request vs. incident distinction table, service catalog design (standard/normal/complex tiers), self-service portal guidance (≥70% automation target), five fulfillment metrics with targets, maturity levels 1–5. _Verified._
- [x] **Financial Management** — Practice 11 added in `chapter-06-practices.md`: annual budget cycle (5-step), in-year forecasting, cost accountability models table (cost centre/showback/chargeback/unit pricing), chargeback implementation steps, FinOps integration alignment to Chapter 12, five financial metrics with targets, maturity levels 1–5. _Verified._
- [x] **Backup & Recovery Operations** — Practice 12 added in `chapter-06-practices.md`: RTO/RPO definitions, four-tier asset criticality table with backup frequency, 3-2-1-1 backup rule, restore testing cadence table (automated → partial → full → DR sim), recovery runbook template (6 steps), backup health monitoring, maturity levels 1–5. _Verified._

### P2 — Cross-References & Data Relationships

- [x] **Create data relationships page** — `content/docs/data-relationships.md` created (365 lines) with practice-to-cycle mappings and metric linkages. _Verified._
- [x] **Map Chapter 6 practices to Chapter 3 cycles** — Covered in `data-relationships.md`. _Verified._
- [x] **Link Chapter 7 metrics to Chapter 6 practices** — Per-category cross-reference callouts added inline in `chapter-07-metrics.md` under all four metric categories (Service Reliability → practices 1/2/12; Operational Efficiency → 3/4/8/10; Team Performance → 5/6; Business Value → 7/9/11). _Verified._
- [x] **Cross-reference Chapter 2 principles throughout chapters** — "Principles in play" callout added near the top of every chapter 3–12, each naming the specific Chapter 2 principle(s) the chapter operationalises and linking back to `chapter-02-principles.md`. _Verified._
- [x] **Link Chapter 5 milestones to Chapter 6 maturity levels** — Phase-to-maturity mapping added in `chapter-05-implementation.md` (Month 1 → Level 1–2, Month 4 → Level 3, Month 6 → Level 4 with path to 5) and per-month maturity targets added in the milestone tracker (`chapter-13-appendices.md`, Appendix B). _Verified._
- [x] **Map Chapter 8 tools to Chapter 6 practices** — "Mapping Tools to Practices" table added in `chapter-08-tools.md` linking all nine tool categories (plus Networking/Infra Ops) to their primary Chapter 6 practices. _Verified._

### P1 — Glossary & Appendices

- [x] **Create comprehensive glossary** — `content/docs/glossary.md` created (292 lines) with SLI, SLO, MTTR, MTBF, error budget, toil, on-call, etc. _Verified._
- [x] **Add appendices with templates** — P1. New `content/docs/chapter-13-appendices.md` created with Appendix A (implementation readiness checklists, moved from ch5), Appendix B (six-month milestone tracker with maturity targets, moved from ch5), Appendix C (blameless post-incident review template), Appendix D (incident commander checklist), Appendix E (change control form), and Appendix F (SLA template). Cross-linked from chapters 5/6/7. _Verified._
- [ ] **Per-chapter companion resources** — P3. The fabricated "📚 Additional Resources" bullet lists (dangling text pointing to non-existent workshops/templates/calculators/assessments/case studies/community pages) were **removed from all chapters** (2–12) because they linked to nothing and misled readers. If these companion artifacts are desired, create them as real, linkable assets and re-add the sections. Candidate artifacts referenced by the old lists: decision-making framework template, multi-cycle planning worksheets, resource allocation calculator, framework-fit assessment, implementation planning workbook, readiness evaluation, runbook/documentation standards template, metrics dashboard design kit, tool selection/evaluation framework, culture readiness assessment, operational risk assessment template, implementation health-check diagnostic, practitioners network/community page, enhancement roadmap. Overlaps with **Add appendices with templates** (above) and **Multi-Platform Considerations → Downloadable worksheets**. _Removed; not yet created._

---

## 📝 Medium Priority Content

- [x] **Official citations & source links** — P2. All key claims, standards, metrics, and tool recommendations must be backed by a link to an authoritative primary source. See the **Citation Standards** section below for the approved source registry and per-chapter checklist. _Verified — inline citations added to chapters 2, 6, 7, 8, 10, 12, and the glossary._
- [x] **Real case studies** — P2. The four fictional case studies were replaced with documented, publicly verifiable industry cases, each carrying a primary-source citation and a note that they _illustrate_ (not endorse, and are not direct accounts of) the framework. `chapter-04-comparison.md`: Google SRE & error budgets ([SRE Book](https://sre.google/sre-book/embracing-risk/)) and Knight Capital's 2012 trading incident ([SEC order 34-70694](https://www.sec.gov/litigation/admin/2013/34-70694.pdf)). `chapter-09-culture.md`: the GitLab 2017 database outage ([GitLab postmortem](https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/)) and Netflix Chaos Engineering ([Principles of Chaos](https://principlesofchaos.org/)). _Verified._
- [x] **Deduplication pass** — P2. Canonical homes established and cross-linked instead of re-explaining: automation _principle_ → Ch.2 (added a "Where automation lives in this framework" reference map), cycle _activity_ → Ch.3, roadmap _milestones_ → Ch.5, runbook _concept_ → Ch.6, all _tooling_ → Ch.8 (marked as the canonical catalogue), _metrics_ → Ch.7, _future/self-healing_ → Ch.12. Thin restatements in Ch.3/5/6/8 converted to forward/backward cross-references. _Verified._
- [x] **On-call rotation design** — "On-Call Rotation Design" section added in `chapter-09-culture.md` (under Team Development): rotation principles, five rotation structure patterns (table), on-call handoff checklist (6 items), alert quality standards, five on-call health metrics with targets, escalation path diagram (0–60 min timeline). _Verified._
- [x] **Networking/infrastructure operations guidance** — New top-level "Networking & Infrastructure Operations" section added in `chapter-08-tools.md`: DNS management (record type table, DNS-as-code, TTL guidance, monitoring); Load Balancing (type comparison table, health check design, drain/TLS/timeout runbook items); CDN Operations (cache management, origin shield/failover, security at the edge, four CDN metrics with targets); Infrastructure Network Monitoring (flow analysis, BGP, topology-as-code, firewall auditing). _Verified._
- [x] **Disaster recovery testing methodology** — Existing thin Testing & Validation stub in `chapter-10-risk.md` replaced with full "Disaster Recovery Testing Methodology" section: six-tier test ladder (document review → full failover) with frequency and disruption level; 8-step DR test planning process; failure scenario library (7 scenarios); RTO/RPO validation recording template with example log; cycle integration guidance. _Verified._

---

## 🖼️ Diagrams

- [x] **Improve all diagrams** — P2. All four matplotlib scripts completely rewritten with a shared `scripts/diagrams/_design_system.py` design system providing a consistent colour palette, card/shadow helpers, and typography hierarchy. Each diagram now uses white card panels with coloured accent headers, status-coloured values, and proper data-coordinate layouts. `generate_diagrams.py` updated to inject the diagrams directory into `sys.path` so the design system module resolves correctly in CI. Output at 300 DPI, ~430–540 KB per PNG. _Verified — all 4 diagrams generate cleanly._

### PDF/EPUB Mermaid Conversion

> **Critical finding**: Hugo renders Mermaid via client-side JavaScript (browser only). The Pandoc + lualatex PDF/EPUB pipeline has **no Mermaid handling** — `mermaid` code blocks would appear as raw verbatim text in the printed output.

- [ ] **Add Mermaid CLI to CI pipeline** — P1. Install `@mermaid-js/mermaid-cli` (or equivalent headless renderer) in the PDF/EPUB workflow. Add a preprocessing step that finds all ````mermaid` blocks in the assembled Markdown, renders each to a PNG/SVG, and replaces the block with a standard `![diagram](...)` image reference before Pandoc runs.
- [ ] **Add Mermaid alt-text and caption standard** — P1. Every new Mermaid diagram block must include a caption comment and `![Alt text](...)` fallback so readers of the PDF/EPUB get the same information. Document this in the style guide (see **Quality & Infrastructure** below).
- [ ] **Vendor Mermaid JS for offline/reliable web rendering** — P3. Currently the Docsy theme fetches Mermaid JS from a CDN. For deterministic rendering (including offline use), vendor the JS bundle in `static/` or `assets/` and reference it locally.

---

## 🔧 Quality & Infrastructure

> **Status**: Not started. P1 (CI gates), P2 (style guide, accessibility).

- [ ] **Create `docs/style-guide.md`** — P2. Define editorial rules: preferred language variant, heading style, emoji policy (note: the PDF pipeline strips emoji — document which are safe and which are not), callout taxonomy (note, tip, warning, caution), table conventions, example formatting, citation style, file naming, and tone. This prevents register drift between opinionated prose and catalogue sections.
- [ ] **Add docs quality CI (`docs-quality.yml`)** — P1. Four mandatory jobs:
  - **Prose lint**: Vale with a custom style config to catch register drift, passive voice, weasel words, and inconsistent terminology.
  - **Markdown lint**: `markdownlint-cli2` with the existing `.markdownlint.json` config to enforce consistent Markdown style.
  - **Link check**: `lychee` to verify all internal and external links in Markdown files.
  - **Accessibility smoke test**: Pa11y CI against the built Hugo site (or a subset of key pages) to catch missing alt-text, heading-hierarchy issues, and contrast problems.
- [ ] **Adopt accessibility-by-default requirements** — P2. Document and enforce: descriptive headings with one meaningful hierarchy per page, alt text on every contentful image, correct data-table markup, and WCAG AA contrast. Reference W3C guidance. This is critical because new Mermaid diagrams and the existing matplotlib assets both need proper alt-text.
- [ ] **Add SEO and social-card metadata** — P2. Fix `baseURL` in `hugo.yaml` (already in **P0 — Foundation & Consistency**). Verify canonical URLs, sitemap behaviour, Open Graph titles/descriptions/images. Create a dedicated book cover/social share image (not just a repurposed asset screenshot).

## 📗 Product & Repo

> **Status**: Not started. P1 (README), P2 (CONTRIBUTING, positioning).

- [ ] **Update README** — P1. Make it more repo-oriented: what the project is, who it helps, how to browse docs locally, how releases work, what is auto-generated. Fix the "EPUB coming soon" claim (the workflow already generates EPUB). Extract shared intro blocks into a partial or data source so README and docs home don't diverge.
- [ ] **Update CONTRIBUTING.md** — P2. Add a clear contributor journey: local preview setup, branch naming, PR checklist, link to style guide, expected review norms, issue labels. Distinguish core-content contributions from translation/community contributions.
- [ ] **Clarify product positioning** — P2. The project currently speaks as open framework + practical book + proto-service (training, support, certification). Decide whether the commercial layer is "planned" or "active" and reflect that consistently on the home page, getting-started page, and README. Remove or clearly label any training/support sections that don't have live offerings.
- [ ] **Add Buy Me a Coffee placement** — P3. Add a soft support ask at the end of the appendices (after value is delivered) and in README after downloads.
- [ ] **Add LinkedIn announcement drafts** — P3. The `Analysis.md` contains ready-to-use announcement text in both English and Russian. Polish and publish when the P0/P1 work is complete.

## 📎 Citation Standards

> **Purpose**: Every factual claim, standard reference, metric threshold, and tool recommendation in the framework must be traceable to a primary authoritative source. This section defines the approved source registry and a per-chapter citation checklist so the work can be done incrementally and verified.

### Rules

1. **One link per claim, first occurrence only** — cite on first mention in each chapter; subsequent mentions in the same chapter may omit the link unless the claim is repeated in a different context.
2. **Approved sources only** — see the registry below. Do not cite blog posts, vendor marketing pages, Wikipedia, or unofficial tutorials as primary evidence.
3. **Link to the specific section, not just the homepage** — e.g., link to the DORA metrics definitions page, not `dora.dev` root.
4. **Version-pin where possible** — if a standard has a version (e.g., NIST SP 800-88 Rev. 1), include the revision in link text and URL.
5. **Format**: inline Markdown link immediately after the claim — `([source name](URL))`.

### Approved Source Registry

| Domain                                       | Trusted Source                           | Base URL                                                                                                                         |
| -------------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **ITIL 4**                                   | PeopleCert / Axelos official ITIL site   | https://www.axelos.com/certifications/itil-service-management                                                                    |
| **ITIL 5**                                   | PeopleCert ITIL 5 announcement           | https://www.peoplecert.org/news-and-announcements/itil-version-5-explained                                                                                                |
| **DORA metrics**                             | DORA (DevOps Research and Assessment)    | https://dora.dev/research/2023/dora-report/                                                                                      |
| **SLSA framework**                           | OpenSSF SLSA specification               | https://slsa.dev/spec/v1.0/                                                                                                      |
| **SBOM — CycloneDX**                         | OWASP CycloneDX specification            | https://cyclonedx.org/specification/overview/                                                                                    |
| **SBOM — SPDX**                              | Linux Foundation SPDX ISO standard       | https://spdx.dev/specifications/                                                                                                 |
| **OWASP Top 10**                             | OWASP Top 10                             | https://owasp.org/www-project-top-ten/                                                                                           |
| **OWASP API Top 10**                         | OWASP API Security Project               | https://owasp.org/www-project-api-security/                                                                                      |
| **NIST SP 800-88**                           | NIST Guidelines for Media Sanitization   | https://doi.org/10.6028/NIST.SP.800-88r1                                                                                         |
| **NIST Cybersecurity Framework**             | NIST CSF 2.0                             | https://www.nist.gov/cyberframework                                                                                              |
| **OpenTelemetry**                            | CNCF OpenTelemetry official docs         | https://opentelemetry.io/docs/                                                                                                   |
| **Sigstore / Cosign**                        | Sigstore project (OpenSSF)               | https://docs.sigstore.dev/                                                                                                       |
| **OPA (Open Policy Agent)**                  | CNCF OPA official docs                   | https://www.openpolicyagent.org/docs/latest/                                                                                     |
| **Kyverno**                                  | CNCF Kyverno official docs               | https://kyverno.io/docs/                                                                                                         |
| **ArgoCD**                                   | Argo Project official docs               | https://argo-cd.readthedocs.io/en/stable/                                                                                        |
| **Flux CD**                                  | CNCF Flux official docs                  | https://fluxcd.io/flux/                                                                                                          |
| **Terraform / OpenTofu**                     | HashiCorp Terraform docs                 | https://developer.hashicorp.com/terraform/docs                                                                                   |
| **Kubernetes**                               | CNCF Kubernetes official docs            | https://kubernetes.io/docs/                                                                                                      |
| **Prometheus**                               | CNCF Prometheus official docs            | https://prometheus.io/docs/                                                                                                      |
| **Ansible**                                  | Red Hat Ansible official docs            | https://docs.ansible.com/                                                                                                        |
| **Backstage (IDP)**                          | CNCF Backstage official docs             | https://backstage.io/docs/                                                                                                       |
| **FinOps Foundation**                        | FinOps Foundation (CNCF) official site   | https://www.finops.org/introduction/what-is-finops/                                                                              |
| **Green Software Foundation / SCI**          | GSF Software Carbon Intensity spec       | https://greensoftware.foundation/standards/sci/                                                              |
| **Carbon Aware SDK**                         | GSF Carbon Aware SDK GitHub              | https://github.com/Green-Software-Foundation/carbon-aware-sdk                                                                    |
| **GDPR Art. 33 / Art. 34**                   | EUR-Lex GDPR full text                   | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679                                                           |
| **EU Cyber Resilience Act**                  | EUR-Lex CRA                              | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847                                                             |
| **US EO 14028 (SBOM mandate)**               | Federal Register EO 14028                | https://www.govinfo.gov/content/pkg/FR-2021-05-17/html/2021-10460.htm |
| **SOC 2**                                    | AICPA Trust Services Criteria            | https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services                              |
| **ISO 27001**                                | ISO/IEC 27001:2022                       | https://www.iso.org/standard/27001                                                                                               |
| **SRE book (Google)**                        | Google SRE book (free online)            | https://sre.google/sre-book/table-of-contents/                                                                                   |
| **Case study — Knight Capital (2012)**       | SEC press release / administrative order | https://www.sec.gov/news/press-release/2013-222                                                                                  |
| **Case study — GitLab 2017 outage**          | GitLab official postmortem               | https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/                                            |
| **Case study — Chaos Engineering (Netflix)** | Principles of Chaos Engineering          | https://principlesofchaos.org/                                                                                                   |
| **CNCF landscape**                           | CNCF Cloud Native Landscape              | https://landscape.cncf.io/                                                                                                       |

### Per-Chapter Citation Checklist

Each item below lists the specific claims that need a source link added inline in the chapter file.

#### Chapter 2 — Principles (`chapter-02-principles.md`)

- [x] ITIL 4 release date (February 2019), 34 practices, 7 guiding principles, SVS model → [Axelos ITIL 4](https://www.axelos.com/certifications/itil-service-management)
- [x] ITIL 5 announcement (January 2026) → [PeopleCert ITIL 5](https://www.peoplecert.org/news-and-announcements/itil-version-5-explained)

#### Chapter 6 — Practices (`chapter-06-practices.md`)

- [x] DORA four-key metrics (deployment frequency, lead time, change failure rate, MTTR) → [dora.dev](https://dora.dev/research/2023/dora-report/)
- [x] DORA elite thresholds (deployment frequency on-demand, lead time < 1 hr, CFR < 5%, MTTR < 1 hr) → same DORA source
- [x] NIST SP 800-88 (media sanitisation at decommission) → [NIST 800-88r1](https://doi.org/10.6028/NIST.SP.800-88r1)
- [x] 3-2-1-1 backup rule (immutable/WORM copy) → [CISA Ransomware Guide](https://www.cisa.gov/resources-tools/resources/stopransomware-guide) (added explanatory callout)

#### Chapter 7 — Metrics (`chapter-07-metrics.md`)

- [x] Any specific SLI/SLO/error-budget references → [Google SRE book Ch. 4](https://sre.google/sre-book/service-level-objectives/)
- [x] FinOps metrics definitions → [FinOps Foundation](https://www.finops.org/introduction/what-is-finops/)

#### Chapter 8 — Tools (`chapter-08-tools.md`)

- [x] OpenTelemetry description (CNCF graduated, OTLP protocol) → [opentelemetry.io](https://opentelemetry.io/docs/)
- [x] ArgoCD (CNCF graduated) → [argo-cd.readthedocs.io](https://argo-cd.readthedocs.io/en/stable/)
- [x] Flux CD (CNCF graduated) → [fluxcd.io](https://fluxcd.io/flux/)
- [x] OPA / Gatekeeper (CNCF graduated) → [openpolicyagent.org](https://www.openpolicyagent.org/docs/latest/)
- [x] Kyverno (CNCF incubating) → [kyverno.io](https://kyverno.io/docs/)
- [x] Backstage (CNCF incubating) → [backstage.io](https://backstage.io/docs/)
- [x] Sigstore / Cosign → [docs.sigstore.dev](https://docs.sigstore.dev/) — cited in chapter-10-risk.md (supply chain security section)

#### Chapter 10 — Risk (`chapter-10-risk.md`)

- [x] SBOM CycloneDX format (OWASP standard) → [cyclonedx.org](https://cyclonedx.org/specification/overview/)
- [x] SBOM SPDX (ISO/IEC 5962:2021) → [spdx.dev](https://spdx.dev/specifications/)
- [x] SLSA levels 1–4 → [slsa.dev/spec/v1.0](https://slsa.dev/spec/v1.0/)
- [x] US EO 14028 SBOM mandate → [Federal Register EO 14028](https://www.govinfo.gov/content/pkg/FR-2021-05-17/html/2021-10460.htm)
- [x] EU Cyber Resilience Act (2024) → [EUR-Lex CRA](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847)
- [x] GDPR Art. 33 (72-hour notification) and Art. 34 (individual notification) → [EUR-Lex GDPR](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679)
- [x] NIST SP 800-88 at decommission step → [NIST 800-88r1](https://doi.org/10.6028/NIST.SP.800-88r1) — cited in chapter-06-practices.md; also present in chapter-10 context
- [x] OWASP Top 10 (pentest scope) → [owasp.org Top 10](https://owasp.org/www-project-top-ten/)
- [x] OWASP API Top 10 (API pentest scope) → [owasp.org API Security](https://owasp.org/www-project-api-security/)

#### Chapter 12 — Future (`chapter-12-future.md`)

- [x] FinOps Foundation definition and three phases → [finops.org](https://www.finops.org/introduction/what-is-finops/)
- [x] Software Carbon Intensity (SCI) score → [GSF SCI spec](https://greensoftware.foundation/standards/sci/)
- [x] Carbon Aware SDK → [GitHub GSF](https://github.com/Green-Software-Foundation/carbon-aware-sdk)
- [x] WattTime API → [watttime.org](https://www.watttime.org/api-documentation/)
- [x] Electricity Maps API → [electricitymaps.com](https://www.electricitymaps.com/free-tier-api)
- [x] EU CSRD (carbon disclosure) → [EUR-Lex CSRD](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2464)
- [x] SEC climate disclosure rule → [sec.gov](https://www.sec.gov/rules-regulations/2024/03/the-enhancement-and-standardization-of-climate-related-disclosures-for-investors)

#### Glossary (`glossary.md`)

- [x] ITIL 4 entry → [Axelos](https://www.axelos.com/certifications/itil-service-management)
- [x] SRE / error budget / SLI / SLO entries → [Google SRE book](https://sre.google/sre-book/table-of-contents/)

---

## 🎮 Gamification & Interactive Elements

> **Status**: None implemented. All P3 unless noted.

### Chapter-Specific Exercises

- [ ] **Chapter 1** — "Sprint Breaker" scenario simulation; "Agile vs Reality" quiz; "Challenge Identifier" badge
- [ ] **Chapter 2** — "Principle Navigator" decision tree; "Values Conflict Resolution" game; badge
- [ ] **Chapter 3** — "Cycle Master" planning game; "Multi-Cycle Juggling" simulation; badge
- [ ] **Chapter 4** — "Framework Detective" analysis; "Methodology Matcher" game; badge
- [ ] **Chapter 5** — "Implementation Architect" planning tool; "Change Champion" simulation; badge
- [ ] **Chapter 6** — "Practice Master" maturity assessment tool; "Process Integration" puzzle; badge

### Cross-Chapter Progress System

- [ ] Framework Mastery Path — visual progress indicator across all chapters
- [ ] Knowledge Points system — points for completing exercises, assessments, real-world implementations
- [ ] Skill Trees — unlock advanced topics based on foundational completion
- [ ] Team Challenges — group exercises for implementing framework concepts

### Scenario Libraries

- [ ] Crisis Simulation Bank — realistic operational crisis scenarios
- [ ] Decision Point Database — common decision points with principle-based guidance
- [ ] Success Story Collection — real implementation stories with lessons learned
- [ ] Failure Case Studies — post-mortems of bad implementations

### Virtual Labs (Future)

- [ ] SysOps Simulator — virtual environment for practicing framework implementation
- [ ] Incident Response Training — realistic incident scenarios with time pressure
- [ ] Tool Integration Playground — hands-on experience with framework tools
- [ ] Team Collaboration Exercises — multi-user scenarios

### Community Features (Future)

- [ ] Implementation Showcase — teams share framework adaptations
- [ ] Peer Mentoring Program — experienced implementers guide newcomers
- [ ] Best Practice Exchange — community-driven tips and techniques
- [ ] Regional Meetups — local in-person groups

### Assessment & Certification (Future)

- [ ] SysOps Framework Practitioner — basic certification for individual contributors
- [ ] SysOps Framework Leader — advanced certification for team leaders
- [ ] Organizational Assessment — framework maturity evaluation for entire orgs
- [ ] Continuous Learning Paths — ongoing development tracks

---

## 🏆 Achievement System

> **Status**: Design only — no implementation. P3.

- [ ] **Foundation badges**: Challenge Identifier, Principle Navigator, Cycle Master
- [ ] **Implementation badges**: Framework Analyst, Implementation Planner, Practice Master
- [ ] **Advanced badges**: Metrics Guru, Tool Integrator, Culture Champion
- [ ] **Master badges**: SysOps Architect, Framework Evangelist, Innovation Leader
- [ ] **Leaderboards**: Implementation Speed, Team Improvement, Community Contribution, Innovation Index

---

## 🎯 Learning Paths

> **Status**: Documented but not yet built as interactive content. P2.

### Individual Contributor Path

1. Foundation (Chapters 1–3)
2. Application (Chapters 4–6)
3. Mastery (Chapters 7–9)
4. Leadership (Chapters 10–12)

### Team Leader Path

1. Strategic Understanding (Chapters 4–5)
2. Implementation Leadership (Chapters 6–8)
3. Organizational Integration (Chapters 9–11)
4. Continuous Evolution (Chapter 12)

### Executive Sponsor Path

1. Business Case (Chapters 1, 4)
2. Investment Planning (Chapter 5)
3. Success Measurement (Chapter 7)
4. Strategic Alignment (Chapters 9, 12)

---

## 🎪 Personality & Memorability Elements

> **Status**: Not started. P3.

- [ ] **Mascots**: "Ops the Octopus" (juggling concerns), "Sprint the Rabbit" (agile), "Steady the Turtle" (sustainable improvement)
- [ ] **Memorable analogies**: Operations as Air Traffic Control, Three-Ring Circus, Operational Gardening
- [ ] **Story-based learning**: "The Tale of Two Teams", "Crisis at Fictional Corp", "The Transformation Journey"
- [ ] **Humor elements**: "Murphy's Law Moments", "The Sprint That Never Was", "Operational Poetry"

---

## 📱 Multi-Platform Considerations

> **Status**: Not started. P2.

- [ ] Mobile-friendly quick reference cards — key concepts accessible on mobile
- [ ] Pocket assessments — brief quizzes and self-evaluations
- [ ] Incident checklists — mobile-optimized response guides
- [ ] Drag-and-drop planning — visual web tools for cycle and resource planning
- [ ] Downloadable worksheets — PDF versions of exercises and templates
- [ ] Printable quick references — essential desk-reference cards

---

## 🌟 Community Engagement

> **Status**: Not started. P3.

- [ ] User-generated implementation stories and adaptation examples
- [ ] Guest chapter additions from industry experts
- [ ] Monthly implementation challenges
- [ ] Annual SysOps Conference (virtual/hybrid)
- [ ] Regional workshops and hackathons

---

_Last verified: 2026-06-13 (editorial audit incorporated). Re-verify completion status by grepping file content — do not infer from filenames or headings alone._
