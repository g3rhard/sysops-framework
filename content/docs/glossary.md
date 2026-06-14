---
title: "Glossary - SysOps Framework Terms"
linkTitle: "Glossary"
weight: 1300
description: >
  "A comprehensive reference for SysOps Framework terminology and acronyms."
---

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

> **See also**: Toil | **Related principle**: Automation and Efficiency (Ch2) | **Chapter**: 7 (Metrics)

**Availability**
The percentage of time a service is operational and accessible to users. Measured as uptime percentage (e.g., 99.9% availability means 43 minutes of downtime per month).

> **See also**: SLA, SLO, SLI | **Related practice**: Service Level Management | **Chapter**: 7 (Metrics)

---

### B

**Blameless Post-Incident Review (PIR)**
A structured learning process following an incident that focuses on understanding what happened rather than assigning blame. Goals include identifying root causes, capturing lessons learned, and preventing recurrence.

> **See also**: Incident, Problem Management | **Related practice**: Incident and Problem Management | **Chapter**: 6 (Practices)

**Blue-Green Deployment**
A deployment strategy where two identical production environments (blue and green) are maintained. New changes are deployed to the inactive environment, tested, then traffic is switched to make it live, enabling quick rollback if needed.

> **See also**: Staged Rollout, Canary Deployment | **Related practice**: Release Management | **Chapter**: 8 (Tools)

---

### C

**Canary Deployment**
A deployment strategy where a new version is rolled out to a small subset of users or servers first. If the canary performs well, the rollout continues to a larger percentage; if issues appear, the canary is rolled back and the blast radius is contained.

> **See also**: Blue-Green Deployment, Staged Rollout | **Related practice**: Release Management | **Chapter**: 8 (Tools)

**Capacity Planning**
The process of forecasting future resource needs (compute, storage, network) based on current utilization trends and business growth projections, ensuring systems have adequate resources while optimising costs.

> **Related practice**: Capacity and Performance Management | **Chapter**: 6 (Practices)

**Change Advisory Board (CAB)**
A group of stakeholders responsible for reviewing and approving changes to production systems. Composition typically includes IT leadership, business representatives, and technical specialists.

> **Related practice**: Change and Configuration Management | **Chapter**: 6 (Practices)

**Change and Configuration Management**
One of the twelve core management practices in the SysOps Framework, focused on planning, implementing, and tracking changes to IT systems in a controlled manner while maintaining an accurate CMDB.

> **See also**: CMDB | **Related metrics**: Operational Efficiency | **Chapter**: 6 (Practices)

**CMDB (Configuration Management Database)**
A centralized repository storing information about IT infrastructure components (servers, applications, databases), their relationships, dependencies, and configuration details.

> **See also**: Asset Management | **Related practice**: Change and Configuration Management | **Chapter**: 6 (Practices)

**Continuous Availability**
One of the six core principles of the SysOps Framework, acknowledging that operations work never stops and the framework must accommodate 24/7 responsibilities sustainably.

> **Chapter**: 2 (Principles)

**Cycle (Daily/Weekly/Monthly)**
The three overlapping operational cycles that form the foundation of the SysOps Framework structure, each with distinct purposes and activity types.

> **Chapter**: 3 (Structure)

---

### D

**Daily Operations Cycle**
The 24-hour cycle focused on reactive work: incident response, urgent maintenance, service monitoring, and team coordination. The primary domain for handling unplanned work.

> **See also**: Weekly Improvement Cycle, Monthly Strategy Cycle | **Chapter**: 3 (Structure)

**DORA Metrics**
DevOps Research and Assessment metrics that measure deployment frequency, lead time for changes, change failure rate, and mean time to recovery. Industry-standard for measuring operational performance.

> **Related practice**: Release Management | **Chapter**: 7 (Metrics)

---

### E

**Error Budget**
The allowable amount of unreliability for a service (100% - SLO target). For example, a 99.9% SLO allows approximately 43 minutes of downtime per month. Used to balance reliability with pace of change.

> **See also**: SLO, SLI | **Related practice**: Service Level Management | **Chapter**: 7 (Metrics)

**Error Budget Burn Rate**
The rate at which a service is consuming its error budget. High burn rates indicate either reliability issues or excessive changes.

> **See also**: Error Budget | **Related practice**: Service Level Management | **Chapter**: 7 (Metrics)

---

### F

**FinOps (Financial Operations)**
The discipline of managing cloud costs and optimising cloud infrastructure spending, including cost allocation, waste identification, and unit economics.

> **Related practice**: Financial Management | **Chapters**: 7 (Metrics), 12 (Future)

**Five Whys**
A root cause analysis technique that involves asking "why" five times to drill down from symptoms to root causes.

> **Related practice**: Incident and Problem Management | **Chapter**: 6 (Practices)

---

### I

**ICS (Incident Command System)**
An organizational structure for incident response that defines clear roles (Incident Commander, Deputy, Scribe, Technical Lead, Communications Lead) to ensure coordinated response at scale.

> **Related practice**: Incident and Problem Management | **Chapter**: 6 (Practices)

**Incident**
An unplanned interruption or degradation of a service requiring immediate response.

> **See also**: Problem | **Related practice**: Incident and Problem Management | **Chapter**: 6 (Practices)

**Incident Commander (IC)**
The single point of authority during incident response, responsible for overall coordination and decision-making. The IC ensures clear communication and prevents conflicting actions.

> **See also**: ICS | **Related practice**: Incident and Problem Management | **Chapter**: 6 (Practices)

**Incident and Problem Management**
One of the twelve core management practices in the SysOps Framework. Encompasses both real-time incident response and systematic root cause analysis to prevent recurrence.

> **See also**: Blameless PIR, Five Whys | **Related metrics**: Service Reliability | **Chapter**: 6 (Practices)

**ITIL (Information Technology Infrastructure Library)**
A comprehensive framework describing IT service management best practices. **ITIL 4** ([Axelos](https://www.axelos.com/certifications/itil-service-management), February 2019) is the current stable standard with 34 practices and the Service Value System. **ITIL 5** ([PeopleCert](https://www.peoplecert.org/news-and-announcements/itil-version-5-explained), announced January 2026) Foundation is available; full practice library pending. The SysOps Framework operationalises many ITIL 4 concepts.

> **Chapter**: 2 (Principles)

---

### K

**Kanban**
An agile methodology using continuous flow and work-in-progress (WIP) limits to manage work. Particularly effective for operations teams with interrupt-driven work, but lacks the multi-cycle strategic structure of SysOps.

> **Chapter**: 4 (Comparison)

**Knowledge and Documentation Management**
One of the twelve core management practices in the SysOps Framework, focused on capturing and sharing operational knowledge through runbooks, troubleshooting guides, and system documentation.

> **See also**: Runbook | **Related metrics**: Team Performance | **Chapter**: 6 (Practices)

**Knowledge Transfer**
The process of sharing operational knowledge, procedures, and expertise from experienced team members to others, typically through documentation, training, and job shadowing.

> **Related practice**: Knowledge and Documentation Management | **Chapter**: 6 (Practices)

---

### L

**Lean**
A management philosophy focused on eliminating waste and optimising processes. Originally from manufacturing, Lean principles influence SysOps via automation and efficiency.

> **Chapter**: 4 (Comparison)

---

### M

**Management Practice**
One of the twelve core operational practices that define the work performed within the SysOps Framework cycles.

> **Chapter**: 6 (Practices)

**Mean Time Between Failures (MTBF)**
The average operational time between service failures. Indicates system stability and the effectiveness of reliability investments.

> **Related practice**: Service Level Management | **Related metrics**: Service Reliability | **Chapter**: 7 (Metrics)

**Mean Time to Recovery (MTTR)**
The average time from incident detection to service restoration. Critical for minimising business impact of outages.

> **Related practice**: Incident and Problem Management | **Related metrics**: Service Reliability | **Chapter**: 7 (Metrics)

**Monthly Strategy Cycle**
The 4-week cycle focused on strategic and architectural decisions: capacity planning, architecture reviews, performance analysis, and goal setting.

> **See also**: Daily Operations Cycle, Weekly Improvement Cycle | **Chapter**: 3 (Structure)

---

### O

**On-Call Rotation**
The schedule determining which team member is on-call during specific periods, typically designed to distribute workload fairly and prevent burnout.

> **Related practice**: Team and Skill Development | **Chapter**: 9 (Culture)

**Operations Cycle**
See Daily Operations Cycle, Weekly Improvement Cycle, or Monthly Strategy Cycle.

---

### P

**Post-Incident Review (PIR)**
See Blameless Post-Incident Review.

**Problem**
The underlying root cause of one or more incidents. Problems are identified through post-incident reviews and trend analysis, then addressed through problem management.

> **See also**: Incident | **Related practice**: Incident and Problem Management | **Chapter**: 6 (Practices)

**Problem Management**
The practice of identifying root causes of recurring incidents and implementing permanent fixes to prevent recurrence.

> **See also**: Five Whys, Blameless PIR | **Related practice**: Incident and Problem Management | **Chapter**: 6 (Practices)

**Production Readiness Review (PRR)**
A review process before deploying systems to production to ensure they meet operational standards for monitoring, documentation, runbooks, and failover capabilities.

> **Related practice**: Release Management | **Chapter**: 8 (Tools)

---

### R

**Rapid Response**
One of the six core principles of the SysOps Framework, emphasising built-in protocols for immediate response to critical issues without bureaucratic delays.

> **Chapter**: 2 (Principles)

**Risk Management**
One of the six core principles of the SysOps Framework, emphasising proactive identification and mitigation of operational risks.

> **See also**: Disaster Recovery | **Chapters**: 2 (Principles), 10 (Risk & Compliance)

**Runbook**
A documented, step-by-step procedure for performing routine operations tasks or responding to specific incidents. Examples: "Database Failover Runbook," "Production Emergency Access Procedure."

> **Related practice**: Knowledge and Documentation Management | **Chapter**: 6 (Practices)

---

### S

**Service Level Agreement (SLA)**
A formal agreement between operations and customers/stakeholders defining the expected level of service, including availability targets, response times, and remedies for non-compliance.

> **See also**: SLO, SLI | **Related practice**: Service Level Management, Vendor and Contract Management | **Chapter**: 7 (Metrics)

**Service Level Indicator (SLI)**
A measurable metric that reflects the service user's experience. Common SLIs include availability, latency, throughput, and error rate.

> **See also**: SLO, Error Budget | **Related practice**: Service Level Management | **Chapter**: 7 (Metrics) — see [Google SRE Book Ch.4](https://sre.google/sre-book/service-level-objectives/) for canonical definitions

**Service Level Management**
One of the twelve core management practices in the SysOps Framework. Establishes SLOs and SLIs, implements error budgets, and drives reliability accountability.

> **See also**: SLO, SLI, Error Budget | **Related metrics**: Service Reliability | **Chapter**: 6 (Practices)

**Service Level Objective (SLO)**
A target value for an SLI, typically defined in business terms (e.g., 99.95% availability, <200ms latency for 95% of requests).

> **See also**: SLI, Error Budget | **Related practice**: Service Level Management | **Chapter**: 7 (Metrics)

**Service Reliability First**
One of the six core principles of the SysOps Framework, emphasising that every decision must prioritise system reliability and availability above other considerations.

> **Chapter**: 2 (Principles)

**SRE (Site Reliability Engineering)**
A discipline developed at Google for managing large-scale systems, emphasising error budgets, toil reduction, and production readiness. SRE practices integrate naturally into the SysOps Framework.

> **See also**: Error Budget, Toil | **Chapter**: 4 (Comparison)

**Staged Rollout**
A deployment strategy where changes are deployed to a subset of systems first (e.g., 10%, then 25%, then 100%) to identify issues at scale before full deployment.

> **See also**: Canary Deployment, Blue-Green Deployment | **Related practice**: Release Management | **Chapter**: 8 (Tools)

---

### T

**Team and Skill Development**
One of the twelve core management practices in the SysOps Framework, focused on cross-training, career development, and reducing single points of failure through team capability growth.

> **Related metrics**: Team Performance | **Chapter**: 6 (Practices)

**Toil**
Manual, repetitive work that doesn't provide long-term value and can be automated. Managing toil is a key focus of operations teams; Google SRE caps toil at 50% of an SRE's time.

> **See also**: Automation Coverage | **Related principle**: Automation and Efficiency (Ch2) | **Chapter**: 7 (Metrics)

---

### U

**Unit Economics**
A metric showing cost relative to business outcomes (e.g., cost per transaction, cost per user, cost per GB processed). Used to demonstrate how infrastructure costs relate to business value.

> **Related practice**: Financial Management | **Related metrics**: Business Value | **Chapter**: 7 (Metrics)

---

### V

**Vendor and Contract Management**
One of the twelve core management practices in the SysOps Framework, focused on managing vendor relationships, ensuring SLA compliance, and optimising vendor partnerships.

> **Related metrics**: Business Value | **Chapter**: 6 (Practices)

---

### W

**Weekly Improvement Cycle**
The 7-day cycle focused on planned improvements: process improvements, automation projects, knowledge sharing, and root cause analysis.

> **See also**: Daily Operations Cycle, Monthly Strategy Cycle | **Chapter**: 3 (Structure)

---

### Z

**Zero Trust**
A security principle that assumes no system is inherently trustworthy, requiring verification and authentication for all access regardless of source or network location.

> **Chapter**: 10 (Risk & Compliance)

---

## Framework Components

### The Three Operational Cycles

| Cycle   | Duration | Primary Focus        | Example Activities                                   |
| ------- | -------- | -------------------- | ---------------------------------------------------- |
| Daily   | 24 hours | Reactive work        | Incident response, urgent maintenance, monitoring    |
| Weekly  | 7 days   | Planned improvements | Automation, root cause analysis, process improvement |
| Monthly | ~30 days | Strategic decisions  | Capacity planning, architecture review, goal setting |

### The Twelve Management Practices

1. **Service Level Management** — Define and monitor SLOs, manage error budgets
2. **Incident and Problem Management** — Respond to incidents, conduct blameless post-mortems, perform root cause analysis
3. **Change and Configuration Management** — Plan and implement changes, manage risk, maintain CMDB
4. **Capacity and Performance Management** — Forecast needs, optimise utilization
5. **Knowledge and Documentation Management** — Create and maintain documentation, facilitate knowledge transfer
6. **Team and Skill Development** — Cross-training, career development, skill building
7. **Vendor and Contract Management** — Manage vendor relationships, SLA compliance, contract lifecycle
8. **Release Management** — Govern CI/CD pipelines, manage deployment gates, coordinate rollouts
9. **Asset Management** — Track hardware/software assets, manage licensing, cloud resource tagging
10. **Service Request Management** — Handle standardized requests via service catalog, automate fulfillment
11. **Financial Management** — Budget planning, cost allocation, chargeback/showback models
12. **Backup and Recovery Operations** — Define RTO/RPO, manage backup schedules, conduct restore tests

### The Six Core Principles

1. **Service Reliability First** — Prioritise reliability and availability
2. **Continuous Availability** — Support 24/7 operations sustainably
3. **Rapid Response** — Enable quick emergency response
4. **Automation and Efficiency** — Systematically automate routine work
5. **Knowledge Sharing** — Document and transfer operational knowledge
6. **Risk Management** — Proactively identify and mitigate risks

---

## Related Framework Comparisons

- **Kanban** — Continuous flow methodology, effective for interrupt-driven work (see Ch4)
- **Scrum** — Sprint-based development framework, not optimized for operations (see Ch4)
- **SAFe** — Large-scale agile framework for multi-team coordination (see Ch4)
- **ITIL 4** — Current (2019–) IT service management standard with 34 practices and a Service Value System model; ITIL 5 announced January 2026 — monitor for updates (see Ch2)
- **SRE** — Site reliability engineering practices that integrate naturally with SysOps cycles (see Ch4)
- **Lean** — Management philosophy emphasising waste elimination and continuous improvement (see Ch4)
