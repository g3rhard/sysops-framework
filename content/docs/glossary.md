---
title: "Glossary - SysOps Framework Terms"
linkTitle: "Glossary"
weight: 1350
description: >
  "A comprehensive reference for SysOps Framework terminology and acronyms."
---

## Editorial Terminology Standard

Use this glossary as the canonical language for the whole repository. When adding or editing chapters:

- prefer existing glossary terms over inventing synonyms;
- add a term when a concept appears in more than one chapter;
- avoid using the same word for different things, especially “incident,” “problem,” “request,” “change,” and “risk”;
- keep vendor names out of definitions unless the term is vendor-specific.

This keeps the framework readable as a methodology rather than a collection of related essays.

## SysOps Framework Glossary

A complete reference of terms, acronyms, and concepts used throughout the SysOps Framework book.

---

## Canonical Terminology Policy

The following table defines preferred terms and deprecated or ambiguous phrasing to prevent drift across chapters:

| Use this                               | Not this                          | Reason                                                                         |
| -------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------ |
| Incident and Problem Management        | Incident Management (alone)       | The practice covers both; "Incident Management" alone omits problem RCA        |
| Change and Configuration Management    | Change Management (alone)         | CMDB discipline is part of the same practice                                   |
| Knowledge and Documentation Management | Knowledge Management (alone)      | Documentation is the output; KM alone is too abstract                          |
| Team and Skill Development             | Team Development (alone)          | Skill development is the concrete activity                                     |
| Vendor and Contract Management         | Vendor Management (alone)         | Contract lifecycle is integral, not optional                                   |
| Backup and Recovery Operations         | Backup Operations (alone)         | Recovery is the point; backup without tested recovery is false confidence      |
| Daily Operations Cycle                 | Daily standup / Daily Scrum       | Standup is one activity within the cycle, not the cycle itself                 |
| Weekly Improvement Cycle               | Sprint / Iteration                | Sprints imply commitment; improvement cycles imply experimentation             |
| Monthly Strategy Cycle                 | Monthly review / Planning session | Review is the end; the full cycle includes assess, design, implement, evaluate |
| On-call engineer                       | On-call (noun)                    | "The on-call" dehumanizes; use "on-call engineer" or "on-call rotation"        |
| Standalone                             | Standup                           | Standup asks "are you on track?"; Standalone asks "is anything on fire?"       |
| Post-incident review                   | Post-mortem                       | "Post-mortem" can feel morbid; both are acceptable but PIR is preferred        |
| Error budget                           | Risk budget / downtime budget     | Error budget is the established SRE term                                       |

### A

**Automation Coverage**
The percentage of routine, repetitive tasks that are performed automatically rather than manually. Higher automation coverage frees team members to focus on complex problems and strategic improvements.

> **See also**: Toil | **Related principle**: Automation and Efficiency ([Chapter 2](chapter-02-principles.md)) | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

**Availability**
The percentage of time a service is operational and accessible to users. Measured as uptime percentage (e.g., 99.9% availability means 43 minutes of downtime per month).

> **See also**: SLA, SLO, SLI | **Related practice**: Service Level Management | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

---

### B

**Blameless Post-Incident Review (PIR)**
A structured learning process following an incident that focuses on understanding what happened rather than assigning blame. Goals include identifying root causes, capturing lessons learned, and preventing recurrence.

> **See also**: Incident, Problem Management | **Related practice**: Incident and Problem Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Blue-Green Deployment**
A deployment strategy where two identical production environments (blue and green) are maintained. New changes are deployed to the inactive environment, tested, then traffic is switched to make it live, enabling quick rollback if needed.

> **See also**: Staged Rollout, Canary Deployment | **Related practice**: Release Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Bus Factor**
The number of team members who could disappear (leave, get sick, take a holiday) before a system becomes unmaintainable because nobody left understands it. A bus factor of 1 is a single point of failure wearing a person's name; the goal of cross-training is a bus factor of 2 or more on every critical system.

> **See also**: Knowledge Transfer | **Related practice**: Team and Skill Development | **Chapter**: [6 - Practices](chapter-06-practices.md)

---

### C

**Canary Deployment**
A deployment strategy where a new version is rolled out to a small subset of users or servers first. If the canary performs well, the rollout continues to a larger percentage; if issues appear, the canary is rolled back and the blast radius is contained.

> **See also**: Blue-Green Deployment, Staged Rollout | **Related practice**: Release Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Capacity Planning**
The process of forecasting future resource needs (compute, storage, network) based on current utilization trends and business growth projections, ensuring systems have adequate resources while optimizing costs.

> **Related practice**: Capacity and Performance Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Change Advisory Board (CAB)**
A group of stakeholders responsible for reviewing and approving changes to production systems. Composition typically includes IT leadership, business representatives, and technical specialists.

> **Related practice**: Change and Configuration Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Change and Configuration Management**
One of the twelve core management practices in the SysOps Framework, focused on planning, implementing, and tracking changes to IT systems in a controlled manner while maintaining an accurate CMDB.

> **See also**: CMDB | **Related metrics**: Operational Efficiency | **Chapter**: [6 - Practices](chapter-06-practices.md)

**CMDB (Configuration Management Database)**
A centralized repository storing information about IT infrastructure components (servers, applications, databases), their relationships, dependencies, and configuration details.

> **See also**: Asset Management | **Related practice**: Change and Configuration Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Continuous Availability**
One of the six core principles of the SysOps Framework, acknowledging that operations work never stops and the framework must accommodate 24/7 responsibilities sustainably.

> **Chapter**: [2 - Principles](chapter-02-principles.md)

**Cycle (Daily/Weekly/Monthly)**
The three overlapping operational cycles that form the foundation of the SysOps Framework structure, each with distinct purposes and activity types.

> **Chapter**: [3 - Structure](chapter-03-structure.md)

---

### D

**Daily Operations Cycle**
The 24-48 hour cycle focused on reactive work: incident response, urgent maintenance, service monitoring, and team coordination. The primary domain for handling unplanned work.

> **See also**: Weekly Improvement Cycle, Monthly Strategy Cycle | **Chapter**: [3 - Structure](chapter-03-structure.md)

**DORA Metrics**
Five software delivery performance metrics maintained by DORA: change lead time, deployment frequency, failed deployment recovery time, change fail rate, and deployment rework rate.

> **Official definition**: [DORA Metrics](https://dora.dev/guides/dora-metrics/) | **Related practice**: Release Management | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

---

### E

**Error Budget**
The allowable amount of unreliability for a service (100% - SLO target). For example, a 99.9% SLO allows approximately 43 minutes of downtime per month. Used to balance reliability with pace of change.

> **Official reference**: [Google SRE Book — Embracing Risk](https://sre.google/sre-book/embracing-risk/) | **See also**: SLO, SLI | **Related practice**: Service Level Management | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

**Error Budget Burn Rate**
The rate at which a service is consuming its error budget. High burn rates indicate either reliability issues or excessive changes.

> **See also**: Error Budget | **Related practice**: Service Level Management | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

---

### F

**FinOps (Financial Operations)**
The collaborative practice of managing and optimizing technology value. Engineering, finance, product, and business teams share responsibility for cost and usage decisions.

> **Official definition**: [FinOps Foundation — What is FinOps?](https://www.finops.org/introduction/what-is-finops/) | **Related practice**: Financial Management | **Chapters**: [7 - Metrics](chapter-07-metrics.md), [12 - Future](chapter-12-future.md)

**Five Whys**
A root cause analysis technique that involves asking "why" five times to drill down from symptoms to root causes.

> **Related practice**: Incident and Problem Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

---

### I

**ICS (Incident Command System)**
An adaptable incident-management structure with common roles, terminology, and reporting relationships. SysOps borrows its Incident Commander pattern from the broader Incident Command System and adapts supporting roles for technology incidents.

> **Official reference**: [FEMA — National Incident Management System Components](https://www.fema.gov/emergency-managers/nims/components#icsr) | **Related practice**: Incident and Problem Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Incident**
An unplanned interruption or degradation of a service requiring immediate response.

> **See also**: Problem | **Related practice**: Incident and Problem Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Incident Commander (IC)**
The single point of authority during incident response, responsible for overall coordination and decision-making. The IC ensures clear communication and prevents conflicting actions.

> **See also**: ICS | **Related practice**: Incident and Problem Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Incident and Problem Management**
One of the twelve core management practices in the SysOps Framework. Encompasses both real-time incident response and systematic root cause analysis to prevent recurrence.

> **See also**: Blameless PIR, Five Whys | **Related metrics**: Service Reliability | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Interrupt Capacity**
Time and staffing deliberately reserved for unplanned work (incidents, urgent requests) so it does not silently consume time planned for improvement work. Operations schedules assume interrupts are normal and design capacity for them, rather than treating every incident as a planning failure.

> **See also**: Daily Operations Cycle | **Related principle**: Rapid Response ([Chapter 2](chapter-02-principles.md)) | **Chapters**: [1 - Challenge](chapter-01-challenge.md), [3 - Structure](chapter-03-structure.md)

**ITIL (Information Technology Infrastructure Library)**
A comprehensive framework describing IT service management best practices. SysOps uses ITIL-style service-management concepts as vocabulary, but keeps version-specific ITIL alignment outside the core methodology. The stable idea is service management; the exact certification and practice-library landscape should be reviewed periodically.

> **Official reference**: [PeopleCert — ITIL](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1) | **Chapter**: [2 - Principles](chapter-02-principles.md)

---

### K

**Kanban**
An approach for optimizing the flow of value by defining and visualizing a workflow, actively managing its items, and improving the workflow.

> **Official definition**: [The Kanban Guide](https://kanbanguides.org/the-kanban-guide/2025.5/) | **Chapter**: [4 - Comparison](chapter-04-comparison.md)

**Knowledge and Documentation Management**
One of the twelve core management practices in the SysOps Framework, focused on capturing and sharing operational knowledge through runbooks, troubleshooting guides, and system documentation.

> **See also**: Runbook | **Related metrics**: Team Performance | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Knowledge Transfer**
The process of sharing operational knowledge, procedures, and expertise from experienced team members to others, typically through documentation, training, and job shadowing.

> **Related practice**: Knowledge and Documentation Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

---

### L

**Lean**
A management philosophy focused on eliminating waste and optimizing processes. Originally from manufacturing, Lean principles influence SysOps via automation and efficiency.

> **Chapter**: [4 - Comparison](chapter-04-comparison.md)

---

### M

**Management Practice**
One of the twelve core operational practices that define the work performed within the SysOps Framework cycles.

> **Chapter**: [6 - Practices](chapter-06-practices.md)

**Mean Time Between Failures (MTBF)**
The average operational time between service failures. Indicates system stability and the effectiveness of reliability investments.

> **Related practice**: Service Level Management | **Related metrics**: Service Reliability | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

**Mean Time to Recovery (MTTR)**
The average time from incident detection to service restoration. Critical for minimizing business impact of outages.

> **Related practice**: Incident and Problem Management | **Related metrics**: Service Reliability | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

**Monthly Strategy Cycle**
The 4-week cycle focused on strategic and architectural decisions: capacity planning, architecture reviews, performance analysis, and goal setting.

> **See also**: Daily Operations Cycle, Weekly Improvement Cycle | **Chapter**: [3 - Structure](chapter-03-structure.md)

---

### O

**On-Call Rotation**
The schedule determining which team member is on-call during specific periods, typically designed to distribute workload fairly and prevent burnout.

> **Related practice**: Team and Skill Development | **Chapter**: [9 - Culture](chapter-09-culture.md)

**Operations Cycle**
See Daily Operations Cycle, Weekly Improvement Cycle, or Monthly Strategy Cycle.

---

### P

**Policy-as-Code**
Encoding compliance and security rules (e.g., "all containers must come from an approved registry") as machine-enforceable policy (Rego/OPA, Kyverno) so CI/CD pipelines and admission controllers reject non-compliant changes automatically, instead of relying on manual review.

> **See also**: Compliance Management | **Related practice**: Change and Configuration Management, Asset Management | **Chapter**: [10 - Risk & Compliance](chapter-10-risk.md)

**Post-Incident Review (PIR)**
See Blameless Post-Incident Review.

**Problem**
The underlying root cause of one or more incidents. Problems are identified through post-incident reviews and trend analysis, then addressed through problem management.

> **See also**: Incident | **Related practice**: Incident and Problem Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Problem Management**
The practice of identifying root causes of recurring incidents and implementing permanent fixes to prevent recurrence.

> **See also**: Five Whys, Blameless PIR | **Related practice**: Incident and Problem Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Production Readiness Review (PRR)**
A review process before deploying systems to production to ensure they meet operational standards for monitoring, documentation, runbooks, and failover capabilities.

> **Related practice**: Release Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

---

### R

**Rapid Response**
One of the six core principles of the SysOps Framework, emphasizing built-in protocols for immediate response to critical issues without bureaucratic delays.

> **Chapter**: [2 - Principles](chapter-02-principles.md)

**Risk Management**
One of the six core principles of the SysOps Framework, emphasizing proactive identification and mitigation of operational risks.

> **See also**: Disaster Recovery | **Chapters**: [2 - Principles](chapter-02-principles.md), [10 - Risk & Compliance](chapter-10-risk.md)

**RTO/RPO (Recovery Time Objective / Recovery Point Objective)**
The two targets that define a recovery capability. RTO is the maximum acceptable downtime before a service must be restored; RPO is the maximum acceptable data loss, expressed as time since the last usable backup. Both are set per service tier and validated through DR testing, not assumed.

> **See also**: Runbook | **Related practice**: Backup and Recovery Operations | **Chapters**: [6 - Practices](chapter-06-practices.md), [10 - Risk & Compliance](chapter-10-risk.md)

**Runbook**
A documented, step-by-step procedure for performing routine operations tasks or responding to specific incidents. Examples: "Database Failover Runbook," "Production Emergency Access Procedure."

> **Related practice**: Knowledge and Documentation Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

---

### S

**Service Catalog**
The published list of requestable services or fulfillment items, each with defined scope, eligibility, fulfillment steps, SLA, and cost. Distinct from the CMDB: the service catalog is what can be requested; the CMDB is what is deployed.

> **See also**: CMDB | **Related practice**: Service Request Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Service Level Agreement (SLA)**
A formal agreement between operations and customers/stakeholders defining the expected level of service, including availability targets, response times, and remedies for non-compliance.

> **See also**: SLO, SLI | **Related practice**: Service Level Management, Vendor and Contract Management | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

**Service Level Indicator (SLI)**
A measurable metric that reflects the service user's experience. Common SLIs include availability, latency, throughput, and error rate.

> **See also**: SLO, Error Budget | **Related practice**: Service Level Management | **Chapter**: [7 - Metrics](chapter-07-metrics.md) - see [Google SRE Book Ch.4](https://sre.google/sre-book/service-level-objectives/) for canonical definitions

**Service Level Management**
One of the twelve core management practices in the SysOps Framework. Establishes SLOs and SLIs, implements error budgets, and drives reliability accountability.

> **See also**: SLO, SLI, Error Budget | **Related metrics**: Service Reliability | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Service Level Objective (SLO)**
A target value for an SLI, typically defined in business terms (e.g., 99.95% availability, <200ms latency for 95% of requests).

> **Official reference**: [Google SRE Book — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) | **See also**: SLI, Error Budget | **Related practice**: Service Level Management | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

**Service Reliability First**
One of the six core principles of the SysOps Framework, emphasizing that every decision must prioritize system reliability and availability above other considerations.

> **Chapter**: [2 - Principles](chapter-02-principles.md)

**Severity**
A single SEV1-SEV4 rating assigned to every incident, combining impact (how much of the business or customer base is affected) and urgency (how fast that harm compounds). SEV1 is the most severe (immediate page, tightest response and communication targets, mandatory post-incident review); SEV4 is the least severe (logged only, no page). Some paging tools use the equivalent P1-P4 notation.

> **See also**: Incident, Blameless PIR | **Related practice**: Incident and Problem Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**SRE (Site Reliability Engineering)**
A discipline developed at Google for managing large-scale systems, emphasizing error budgets, toil reduction, and production readiness. SRE practices integrate naturally into the SysOps Framework.

> **See also**: Error Budget, Toil | **Chapter**: [4 - Comparison](chapter-04-comparison.md)

**Staged Rollout**
A deployment strategy where changes are deployed to a subset of systems first (e.g., 10%, then 25%, then 100%) to identify issues at scale before full deployment.

> **See also**: Canary Deployment, Blue-Green Deployment | **Related practice**: Release Management | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Standalone**
The operations team's replacement for the daily standup: a brief (typically 15-minute) status share that asks "is anything on fire, and does anyone need help?" rather than "what did you commit to and are you on track?" Named to signal that reactive, interrupt-driven work is the normal subject matter, not a deviation from plan.

> **See also**: Daily Operations Cycle | **Chapter**: [3 - Structure](chapter-03-structure.md)

---

### T

**Team and Skill Development**
One of the twelve core management practices in the SysOps Framework, focused on cross-training, career development, and reducing single points of failure through team capability growth.

> **Related metrics**: Team Performance | **Chapter**: [6 - Practices](chapter-06-practices.md)

**Toil**
Manual, repetitive work that doesn't provide long-term value and can be automated. Managing toil is a key focus of operations teams; Google SRE caps toil at 50% of an SRE's time.

> **Official definition**: [Google SRE Book — Eliminating Toil](https://sre.google/sre-book/eliminating-toil/) | **See also**: Automation Coverage | **Related principle**: Automation and Efficiency ([Chapter 2](chapter-02-principles.md)) | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

---

### U

**Unit Economics**
A metric showing cost relative to business outcomes (e.g., cost per transaction, cost per user, cost per GB processed). Used to demonstrate how infrastructure costs relate to business value.

> **Related practice**: Financial Management | **Related metrics**: Business Value | **Chapter**: [7 - Metrics](chapter-07-metrics.md)

---

### V

**Vendor and Contract Management**
One of the twelve core management practices in the SysOps Framework, focused on managing vendor relationships, ensuring SLA compliance, and optimizing vendor partnerships.

> **Related metrics**: Business Value | **Chapter**: [6 - Practices](chapter-06-practices.md)

---

### W

**Weekly Improvement Cycle**
The 7-day cycle focused on planned improvements: process improvements, automation projects, knowledge sharing, and root cause analysis.

> **See also**: Daily Operations Cycle, Monthly Strategy Cycle | **Chapter**: [3 - Structure](chapter-03-structure.md)

---

### Z

**Zero Trust**
A security model that grants no implicit trust based only on network location or asset ownership; subjects and devices are authenticated and authorized before access to a resource.

> **Official definition**: [NIST SP 800-207 — Zero Trust Architecture](https://www.nist.gov/publications/zero-trust-architecture) | **Chapter**: [10 - Risk & Compliance](chapter-10-risk.md)

---

## Framework Components

### The Three Operational Cycles

| Cycle   | Duration    | Primary Focus        | Example Activities                                   |
| ------- | ----------- | -------------------- | ---------------------------------------------------- |
| Daily   | 24-48 hours | Reactive work        | Incident response, urgent maintenance, monitoring    |
| Weekly  | 7 days      | Planned improvements | Automation, root cause analysis, process improvement |
| Monthly | ~30 days    | Strategic decisions  | Capacity planning, architecture review, goal setting |

### The Twelve Management Practices

1. **Service Level Management** - Define and monitor SLOs, manage error budgets
2. **Incident and Problem Management** - Respond to incidents, conduct blameless post-mortems, perform root cause analysis
3. **Change and Configuration Management** - Plan and implement changes, manage risk, maintain CMDB
4. **Capacity and Performance Management** - Forecast needs, optimize utilization
5. **Knowledge and Documentation Management** - Create and maintain documentation, facilitate knowledge transfer
6. **Team and Skill Development** - Cross-training, career development, skill building
7. **Vendor and Contract Management** - Manage vendor relationships, SLA compliance, contract lifecycle
8. **Release Management** - Govern CI/CD pipelines, manage deployment gates, coordinate rollouts
9. **Asset Management** - Track hardware/software assets, manage licensing, cloud resource tagging
10. **Service Request Management** - Handle standardized requests via service catalog, automate fulfillment
11. **Financial Management** - Budget planning, cost allocation, chargeback/showback models
12. **Backup and Recovery Operations** - Define RTO/RPO, manage backup schedules, conduct restore tests

### The Six Core Principles

1. **Service Reliability First** - Prioritize reliability and availability
2. **Continuous Availability** - Support 24/7 operations sustainably
3. **Rapid Response** - Enable quick emergency response
4. **Automation and Efficiency** - Systematically automate routine work
5. **Knowledge Sharing** - Document and transfer operational knowledge
6. **Risk Management** - Proactively identify and mitigate risks

---

## Related Framework Comparisons

- **Kanban** - Continuous flow methodology, effective for interrupt-driven work ([Chapter 4](chapter-04-comparison.md))
- **Scrum** - Sprint-based development framework, not optimized for operations ([Chapter 4](chapter-04-comparison.md))
- **SAFe** - Large-scale agile framework for multi-team coordination ([Chapter 4](chapter-04-comparison.md))
- **ITIL / ITSM** - Service-management frameworks and vocabulary; use SysOps as a lightweight operating layer, and keep version-specific alignment current ([Chapter 2](chapter-02-principles.md))
- **SRE** - Site reliability engineering practices that integrate naturally with SysOps cycles ([Chapter 4](chapter-04-comparison.md))
- **Lean** - Management philosophy emphasizing waste elimination and continuous improvement ([Chapter 4](chapter-04-comparison.md))

---

_[← Previous: Appendices](chapter-13-appendices.md) | [Next: Framework Relationships →](data-relationships.md)_
