---
title: "Appendices: Templates & Checklists"
linkTitle: "Appendices"
weight: 1300
description: >
  "The boring pages you'll actually photocopy - readiness checklists, a milestone tracker, and the templates every operations team ends up rewriting at 2 a.m."
---

## What's In Here

The chapters make the argument. The appendices give you the paperwork.

Everything here is meant to be copied, pasted, butchered, and made your own. Nothing in this section is sacred - if a field doesn't apply to your team, delete it; if you need three more, add them. These are starting points, not commandments. The fastest way to ruin a good template is to treat it as a form to be _completed_ rather than a tool for _thinking_.

> **Downloadable versions:** Maintained, copy-ready templates live in the [`templates/`](https://github.com/g3rhard/sysops-framework/tree/main/templates) directory.

A note on placement: detailed, tick-box-heavy material lives here on purpose. The chapters keep the narrative and the key decisions; the appendices hold the granular checklists so the story stays readable and the reference material stays findable. When a chapter says "see the appendix," this is where it's pointing.

- **Appendix A** - Implementation Readiness Checklists (referenced from [Chapter 5](chapter-05-implementation.md))
- **Appendix B** - Six-Month Milestone Tracker (referenced from [Chapter 5](chapter-05-implementation.md))
- **Operational Templates** - links to the maintained files used throughout the book

---

## Appendix A: Implementation Readiness Checklists

Before you change a single process, find out where you actually stand. Be ruthlessly honest here - a readiness assessment that flatters you is worse than no assessment at all, because it sells you confidence you haven't earned. Work through all three lists with the whole team in the room.

### A.1 Technical Readiness

- [ ] Existing monitoring and alerting systems in place and trusted
- [ ] Documentation and knowledge management practices established
- [ ] Automation tools and capabilities available
- [ ] Incident response procedures defined
- [ ] Change management processes exist (even if informal)

### A.2 Cultural Readiness

- [ ] Team is open to new approaches
- [ ] Leadership actively supports change
- [ ] Stakeholders understand operational challenges
- [ ] Healthy collaboration and communication patterns already exist
- [ ] Team is willing to invest time in improvement

### A.3 Organizational Readiness

- [ ] Clear service definitions and ownership
- [ ] Defined service level expectations
- [ ] Existing metrics and measurement practices
- [ ] Resource availability for implementation
- [ ] Integration with other teams and processes is workable

> **Scoring rule of thumb:** if more than a third of any single list is unchecked, fix those gaps before starting the roadmap rather than during it. Trying to pour a new process onto missing foundations is how transformations quietly die in month two.

---

## Appendix B: Six-Month Milestone Tracker

This is the detailed companion to the implementation roadmap in [Chapter 5](chapter-05-implementation.md). The chapter explains the _why_ and the general plan; this tracker is the tick-box version you print out and pin to the wall. Each milestone maps to the corresponding maturity expectations in [Chapter 6](chapter-06-practices.md).

### Month 1 - Foundation and Assessment

- [ ] Current state fully assessed and documented
- [ ] Implementation plan approved by leadership
- [ ] Team trained on framework basics
- [ ] Baseline metrics established
- [ ] Initial stakeholder communications completed

_Maturity target: priority practices identified at Level 1 (Initial), with repeatable work beginning. See [Chapter 6](chapter-06-practices.md)._

### Month 2 - Daily Operations Foundation

- [ ] Daily operations cycle implemented
- [ ] Basic monitoring and alerting operational
- [ ] Incident response procedures defined
- [ ] Knowledge management system deployed
- [ ] Daily review meetings established

_Maturity target: incident and monitoring practices reaching Level 2 (Repeatable)._

### Month 3 - Weekly Improvement Integration

- [ ] Weekly improvement cycle integrated
- [ ] First improvement projects completed
- [ ] Cross-training program initiated
- [ ] Improvement effectiveness measurement active
- [ ] Team showing adoption of new practices

_Maturity target: core practices consistently at Level 2 (Repeatable), with evidence for selected Level 3 behaviors._

### Month 4 - Strategic Integration

- [ ] Monthly strategy cycle introduced
- [ ] All cycles running in parallel
- [ ] Advanced automation capabilities deployed
- [ ] Strategic planning processes established
- [ ] Stakeholder satisfaction improving

_Maturity target: priority practices moving toward Level 3 (Defined); other practices may remain at Level 1–2._

### Month 5 - Advanced Capabilities

- [ ] Advanced capabilities operational
- [ ] Predictive analytics providing value
- [ ] Team expertise development visible
- [ ] Process optimization showing results
- [ ] Cultural transformation evident

_Maturity target: priority practices producing consistent evidence; Level 4 is not required during rollout._

### Month 6 - Review and Stabilization

- [ ] All three cycles have named owners and produce decisions or evidence
- [ ] Priority practices operate without constant prompting
- [ ] Business and team outcomes have been compared with the baseline
- [ ] Remaining maturity gaps have owners and next-quarter actions
- [ ] Go / Adapt / Stop decision recorded for continued rollout

_Maturity target: priority practices at Level 3 (Defined). Level 4 (Managed) requires sustained measurement beyond the rollout._

---

## Operational Templates

The maintained, copy-ready templates live in the [`templates/`](https://github.com/g3rhard/sysops-framework/tree/main/templates) directory:

| Need                                            | Template                                                                        |
| ----------------------------------------------- | ------------------------------------------------------------------------------- |
| Review an incident without blaming responders   | [Post-incident review](../../templates/post-incident-review.md)                 |
| Coordinate a major incident                     | [Incident commander checklist](../../templates/incident-commander-checklist.md) |
| Plan, approve, validate, and roll back a change | [Change control form](../../templates/change-control-form.md)                   |
| Define service expectations                     | [SLA template](../../templates/sla-template.md)                                 |
| Define a sustainable rotation                   | [On-call policy template](../../templates/on-call-policy-template.md)           |
| Report service health and improvement work      | [Reporting template](../../templates/reporting-template.md)                     |
| Classify and route incoming work                | [Work-intake triage](../../templates/work-intake-triage.md)                     |
| Establish a pilot baseline                      | [Baseline metrics](../../templates/baseline-metrics.md)                         |
| Make the pilot Go / Adapt / Stop decision       | [Pilot retrospective](../../templates/pilot-retrospective.md)                   |
| Record services, ownership, and dependencies    | [Service inventory](../../templates/service-inventory.md)                       |
| Apply the canonical incident scale              | [Severity matrix](../../templates/severity-matrix.md)                           |
| Track operational risks and treatment decisions | [Risk register](../../templates/risk-register.md)                               |
| Hand work and risk to the next shift            | [Shift handoff](../../templates/shift-handoff.md)                               |

Keep one maintained copy of each template. The chapters explain when and why to use them; the template files contain the fields and checklists.

## Where to Go Next

These templates are deliberately generic so they survive contact with your reality. As your team matures, fold your hard-won specifics back into them - the best version of every template in this book is the one your team has already broken and rebuilt twice.

All templates live in the [`templates/`](https://github.com/g3rhard/sysops-framework/tree/main/templates) directory. Copy what you need, adapt, and version-control alongside your operational docs.

For the reasoning behind each artifact, follow the cross-references back into the chapters. For terminology, see the [Glossary](glossary.md). For how cycles, practices, and metrics interconnect, see the [Framework Data Relationships](data-relationships.md) page.

---

_[← Previous: Chapter 12 - Future Evolution](chapter-12-future.md) | [Next: Glossary →](glossary.md)_
