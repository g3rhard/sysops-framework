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

### A

**Automation Coverage**
The percentage of routine, repetitive tasks that are performed automatically rather than manually. Higher automation coverage frees team members to focus on complex problems and strategic improvements.

**Availability**
The percentage of time a service is operational and accessible to users. Measured as uptime percentage (e.g., 99.9% availability means 43 minutes of downtime per month).

---

### B

**Blameless Post-Incident Review (Post-Mortem)**
A structured learning process following an incident that focuses on understanding what happened rather than assigning blame. Goals include identifying root causes, capturing lessons learned, and preventing recurrence.

**Blue-Green Deployment**
A deployment strategy where two identical production environments (blue and green) are maintained. New changes are deployed to the inactive environment, tested, then traffic is switched to make it live, enabling quick rollback if needed.

---

### C

**Capacity Planning**
The process of forecasting future resource needs (compute, storage, network) based on current utilization trends and business growth projections, ensuring systems have adequate resources while optimizing costs.

**Change Advisory Board (CAB)**
A group of stakeholders responsible for reviewing and approving changes to production systems. Composition typically includes IT leadership, business representatives, and technical specialists.

**Change Management**
The discipline of planning, implementing, and tracking changes to IT systems in a controlled manner to minimize risk and disruption.

**CMDB (Configuration Management Database)**
A centralized repository storing information about IT infrastructure components (servers, applications, databases), their relationships, dependencies, and configuration details.

**Continuous Availability**
One of the six core principles of the SysOps Framework, acknowledging that operations work never stops and the framework must accommodate 24/7 responsibilities sustainably.

**Cycle (Daily/Weekly/Monthly)**
The three overlapping operational cycles that form the foundation of the SysOps Framework structure, each with distinct purposes and activity types.

---

### D

**Daily Operations Cycle**
The 24-hour cycle focused on reactive work: incident response, urgent maintenance, service monitoring, and team coordination. The primary domain for handling unplanned work.

**DORA Metrics**
DevOps Research and Assessment metrics that measure deployment frequency, lead time for changes, change failure rate, and mean time to recovery. Industry-standard for measuring operational performance.

---

### E

**Error Budget**
The allowable amount of unreliability for a service (100% - SLO target). For example, a 99.9% SLO allows approximately 43 minutes of downtime per month. Used to balance reliability with pace of change.

**Error Budget Burn Rate**
The rate at which a service is consuming its error budget. High burn rates indicate either reliability issues or excessive changes.

---

### F

**FinOps (Financial Operations)**
The discipline of managing cloud costs and optimizing cloud infrastructure spending, including cost allocation, waste identification, and unit economics.

**Five Whys**
A root cause analysis technique that involves asking "why" five times to drill down from symptoms to root causes. Example: Why did the server crash? → Why did it run out of memory? → Why wasn't it right-sized?

---

### H

**Hybrid Deployment**
An approach combining multiple operational frameworks. Example: Using Kanban for daily operations work and SysOps weekly cycles for planned improvements.

---

### I

**ICS (Incident Command System)**
An organizational structure for incident response that defines clear roles (Incident Commander, Deputy, Scribe, Technical Lead, Communications Lead) to ensure coordinated response at scale.

**Incident**
An unplanned interruption or degradation of a service requiring immediate response.

**Incident Commander (IC)**
The single point of authority during incident response, responsible for overall coordination and decision-making. The IC ensures clear communication and prevents conflicting actions.

**Incident Management**
The practice and process for responding to incidents quickly to restore service and minimize business impact.

**ITIL (Information Technology Infrastructure Library)**
A comprehensive framework describing IT service management best practices. **[ITIL 4](https://www.axelos.com/certifications/itil-service-management)** (released February 2019) is the current stable standard, introducing the Service Value System (SVS), 34 management practices, and 7 guiding principles. **[ITIL 5](https://www.peoplecert.org/itil-5)** was announced by PeopleCert in January 2026; its Foundation certification is available but the full practice library is not yet widely published. The SysOps Framework operationalises many ITIL 4 concepts with specific cycles and practices, and will be updated to align with ITIL 5 once its content is stable.

---

### K

**Kanban**
An agile methodology using continuous flow and work-in-progress (WIP) limits to manage work. Unlike sprint-based approaches, Kanban pulls new work when capacity becomes available. Particularly effective for operations teams with interrupt-driven work.

**Knowledge Transfer**
The process of sharing operational knowledge, procedures, and expertise from experienced team members to others, typically through documentation, training, and job shadowing.

---

### L

**Lean**
A management philosophy focused on eliminating waste and optimizing processes. Originally from manufacturing, Lean principles emphasize flow, value, and continuous improvement.

---

### M

**Management Practice**
One of the seven core operational practices in the SysOps Framework: Service Level Management, Incident Management, Change Management, Capacity & Performance Management, Knowledge & Documentation Management, Team & Skill Development, and Vendor Management.

**Mean Time Between Failures (MTBF)**
The average operational time between service failures. Indicates system stability and the effectiveness of reliability investments.

**Mean Time to Recovery (MTTR)**
The average time from incident detection to service restoration. Critical for minimizing business impact of outages.

**Monthly Strategy Cycle**
The 30-day cycle focused on strategic and architectural decisions: capacity planning, architecture reviews, performance analysis, and goal setting.

**MTBF**
See Mean Time Between Failures.

**MTTR**
See Mean Time to Recovery.

---

### O

**On-Call**
The practice of assigning team members to be available and responsive outside normal business hours to handle critical incidents.

**On-Call Rotation**
The schedule determining which team member is on-call during specific periods, typically designed to distribute workload fairly and prevent burnout.

**Operations Cycle**
See Daily/Weekly/Monthly Cycle.

---

### P

**Post-Incident Review**
See Blameless Post-Incident Review.

**Problem Management**
The practice of identifying root causes of recurring incidents and implementing permanent fixes to prevent recurrence.

**Production Readiness Review (PRR)**
A review process before deploying systems to production to ensure they meet operational standards for monitoring, documentation, runbooks, and failover capabilities.

---

### R

**Rapid Response**
One of the six core principles of the SysOps Framework, emphasizing built-in protocols for immediate response to critical issues without bureaucratic delays.

**Right-Sizing**
Ensuring infrastructure components (compute instances, storage, memory) are appropriately sized for the workload, avoiding both over-provisioning (waste) and under-provisioning (performance issues).

**Risk Management**
One of the six core principles of the SysOps Framework, emphasizing proactive identification and mitigation of operational risks.

**Runbook**
A documented, step-by-step procedure for performing routine operations tasks or responding to specific incidents. Examples: "Database Failover Runbook," "Production Emergency Access Procedure."

---

### S

**SLA (Service Level Agreement)**
A formal agreement between operations and customers/stakeholders defining the expected level of service, including availability targets, response times, and remedies for non-compliance.

**SLI (Service Level Indicator)**
A measurable metric that reflects the service user’s experience. Common SLIs include availability, latency, throughput, and error rate. See [Google SRE Book — Ch. 4](https://sre.google/sre-book/service-level-objectives/) for the canonical definitions of SLI, SLO, and error budget.

**SLO (Service Level Objective)**
A target value for an SLI, typically defined in business terms (e.g., 99.95% availability, <200ms latency for 95% of requests).

**Service Reliability First**
One of the six core principles of the SysOps Framework, emphasizing that every decision must prioritize system reliability and availability above other considerations.

**SRE (Site Reliability Engineering)**
A discipline [developed at Google](https://sre.google/sre-book/table-of-contents/) for managing large-scale systems, emphasizing error budgets, toil reduction, and production readiness. SRE practices naturally integrate into the SysOps Framework.

**Staged Rollout**
A deployment strategy where changes are deployed to a subset of systems first (e.g., 10%, then 25%, then 100%) to identify issues at scale before full deployment.

---

### T

**Team Development**
One of the seven core management practices in the SysOps Framework, focused on cross-training, skill development, and career development paths.

**Toil**
Manual, repetitive work that doesn't provide long-term value and can be automated. Managing toil is a key focus of operations teams.

---

### U

**Unit Economics**
A metric showing cost relative to business outcomes (e.g., cost per transaction, cost per user, cost per GB processed). Used to demonstrate how infrastructure costs relate to business value.

---

### V

**Vendor Management**
One of the seven core management practices in the SysOps Framework, focused on managing vendor relationships, ensuring SLA compliance, and optimizing vendor partnerships.

---

### W

**Weekly Improvement Cycle**
The 7-day cycle focused on planned improvements: process improvements, automation projects, knowledge sharing, and root cause analysis.

---

### Z

**Zero Trust**
A security principle that assumes no system is inherently trustworthy, requiring verification and authentication for all access regardless of source or network location.

---

## Framework Components

### The Three Operational Cycles

| Cycle   | Duration | Primary Focus        | Example Activities                                   |
| ------- | -------- | -------------------- | ---------------------------------------------------- |
| Daily   | 24 hours | Reactive work        | Incident response, urgent maintenance, monitoring    |
| Weekly  | 7 days   | Planned improvements | Automation, root cause analysis, process improvement |
| Monthly | ~30 days | Strategic decisions  | Capacity planning, architecture review, goal setting |

### The Seven Management Practices

1. **Service Level Management** - Define and monitor SLOs, manage error budgets
2. **Incident Management** - Respond to incidents, conduct blameless post-mortems
3. **Change Management** - Plan and implement changes, manage risk
4. **Capacity & Performance Management** - Forecast needs, optimize utilization
5. **Knowledge & Documentation Management** - Create and maintain documentation, facilitate knowledge transfer
6. **Team & Skill Development** - Cross-training, career development, skill building
7. **Vendor Management** - Manage vendor relationships and SLA compliance

### The Six Core Principles

1. **Service Reliability First** - Prioritize reliability and availability
2. **Continuous Availability** - Support 24/7 operations sustainably
3. **Rapid Response** - Enable quick emergency response
4. **Automation and Efficiency** - Systematically automate routine work
5. **Knowledge Sharing** - Document and transfer operational knowledge
6. **Risk Management** - Proactively identify and mitigate risks

---

## Related Framework Comparisons

- **Kanban** - Continuous flow methodology, effective for interrupt-driven work
- **Scrum** - Sprint-based development framework, not optimized for operations
- **SAFe** - Large-scale agile framework for multi-team coordination
- **ITIL 4** - Current (2019–) IT service management standard with 34 practices and a Service Value System model; ITIL 5 announced January 2026 — monitor for updates
- **SRE** - Site reliability engineering practices that integrate naturally with SysOps cycles
- **Lean** - Management philosophy emphasizing waste elimination and continuous improvement
