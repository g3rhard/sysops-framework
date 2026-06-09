---
title: "Chapter 6: Management Practices"
linkTitle: "Chapter 06: Practices"
weight: 600
description: >
  "Good practices are the difference between chaos and control in operations."
---

## 🎯 Learning Objectives

By the end of this chapter, you will understand:

- The twelve core management practices that support the SysOps Framework
- How to implement each practice effectively
- Integration points between practices and operational cycles
- Maturity models for continuous practice improvement

## 🎯 The Twelve Core Management Practices

The SysOps Framework incorporates twelve essential management practices tailored specifically for operations teams. Unlike generic IT management approaches, these practices acknowledge the unique constraints and requirements of system administration work.

### 1. 📊 Service Level Management

**Purpose**: Establish clear service level objectives (SLOs) and service level indicators (SLIs) for all critical services, implementing error budgets to balance reliability with the pace of change.

#### Key Components

**Service Level Indicators (SLIs)**:

- Availability: Percentage of time service is operational
- Latency: Response time for user requests
- Throughput: Volume of successful requests processed
- Quality: Percentage of requests served without errors

**Service Level Objectives (SLOs)**:

- Target values for each SLI (e.g., 99.9% availability)
- Time windows for measurement (e.g., monthly, quarterly)
- Business justification for each target level
- Clear consequences for missing objectives

**Error Budgets**:

- Allowable amount of unreliability (100% - SLO)
- Tracking of budget consumption over time
- Policies for when error budget is exhausted
- Balance between reliability and feature velocity

#### Implementation Steps

1. **Service Inventory**: Catalog all services and their criticality levels
2. **SLI Selection**: Choose measurable indicators that matter to users
3. **SLO Definition**: Set realistic but challenging targets based on business needs
4. **Monitoring Setup**: Implement automated tracking and alerting
5. **Error Budget Management**: Create policies for budget consumption and replenishment

#### Example Service Level Management

**Service**: Customer Authentication API

- **Availability SLI**: Successful login attempts / Total login attempts
- **Availability SLO**: 99.95% measured monthly
- **Latency SLI**: 95th percentile response time
- **Latency SLO**: < 200ms for 95% of requests
- **Error Budget**: 0.05% = ~22 minutes downtime per month

### 2. 🚨 Incident and Problem Management

**Purpose**: Develop comprehensive incident response procedures with clear escalation paths and communication protocols. Implement blameless post-incident reviews to capture lessons learned and prevent recurrence.

#### Incident Management Process

**1. Detection and Alert**:

- Automated monitoring and alerting systems
- Clear alert severity classification
- On-call rotation and escalation procedures
- Initial response time targets based on severity

**2. Response and Triage**:

- Immediate response protocols
- Severity assessment and classification
- Resource allocation and team coordination
- Stakeholder communication procedures

**3. Resolution and Recovery**:

- Systematic troubleshooting approaches
- Escalation procedures for complex issues
- Service restoration verification
- Communication of resolution to stakeholders

**4. Post-Incident Review**:

- Blameless timeline reconstruction
- Root cause analysis techniques
- Action item identification and assignment
- Knowledge base and runbook updates

#### Blameless Post-Incident Review Process

A core principle of modern incident management is conducting **blameless post-incident reviews** (sometimes called post-mortems). This removes the fear that drives people to hide errors and enables genuine learning.

**The Five-Phase Blameless Post-Incident Process:**

**Phase 1: Timeline Reconstruction (Day 1-2)**

1. Gather all participants (on-call responder, escalation teams, management observer)
2. Create a detailed incident timeline:
   - When was the issue first detected?
   - What actions were taken and by whom?
   - What information was available at each decision point?
   - When was the service restored?
3. Document all communications and decisions made
4. Avoid assigning blame - focus on understanding the sequence of events

**Phase 2: Impact Analysis (Day 2-3)**

- How long was the service unavailable?
- How many users were affected?
- What was the business impact (revenue lost, data affected, customer trust)?
- How much error budget was consumed?
- What escalations were triggered?

**Phase 3: Root Cause Analysis (Day 3-5)**

Use the "5 Whys" technique or Fishbone diagram:

```text
Why did customers experience an outage?
→ The database server ran out of disk space

Why did the server run out of disk space?
→ Log files grew unexpectedly large

Why did log files grow large?
→ A new application deployed yesterday increased logging volume by 10x

Why wasn't this caught?
→ Load testing didn't include realistic logging configuration

Why wasn't load testing updated?
→ The application team wasn't aware of logging configuration requirements
```

**Phase 4: Action Item Generation (During review)**

- **Process improvements**: How can we prevent this exact incident?
  - Example: "Implement log rotation policy with size limits"
- **Detection improvements**: How can we detect this earlier?
  - Example: "Add monitoring for disk usage threshold at 80%"
- **Response improvements**: How can we respond faster?
  - Example: "Create runbook for disk space emergency procedure"
- **One-time actions**: What immediate fixes are needed?
  - Example: "Clean up old logs from this server"

**Phase 5: Communication & Follow-up**

- Share findings with broader team (not just responders)
- Assign clear ownership for action items
- Set target dates for resolution (usually 1-2 weeks for critical items)
- Follow up on action items until completed
- Celebrate what the team did well during response

#### Incident Command System (ICS) Roles

For significant incidents, establish clear role assignments:

| Role                        | Responsibility                                                                                                               |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Incident Commander (IC)** | Overall coordination, decision authority, stakeholder communication. Single point of coordination for all incident response. |
| **Deputy IC**               | Supports IC, takes over if IC needs relief during long incidents. Maintains handoff log.                                     |
| **Scribe**                  | Documents timeline, decisions, commands given. Maintains incident narrative for post-incident review.                        |
| **Technical Lead**          | Coordinates technical troubleshooting, oversees system specialists, proposes solutions.                                      |
| **Communications Lead**     | Manages stakeholder updates, customer communications, internal status channel. Prevents communication chaos.                 |
| **System Specialists**      | Database, network, application, security experts investigating their domain. Report findings to Technical Lead.              |

**Why ICS Matters**: Prevents confusion, ensures one voice to customers, captures information for post-incident review, scales well for complex incidents.

---

#### Problem Management Process

**Distinction from Incident Management**:

- **Incident Management**: Restore service quickly
- **Problem Management**: Prevent incidents through root cause elimination

**Problem Identification**:

- Patterns in incident data
- Proactive monitoring and trending
- Stakeholder feedback and requests
- Known error database maintenance

**Problem Resolution**:

- Root cause analysis methodologies
- Change request generation for fixes
- Workaround documentation and communication
- Resolution verification and testing

#### 🎮 Interactive Scenario: Incident Response

**Scenario**: At 2:30 AM, monitoring alerts indicate that the customer database is responding slowly. Login times have increased from 200ms to 3000ms. Customer support is starting to receive complaints.

**Exercise**: Apply the incident management process:

1. **Detection**: What information do you need immediately?
2. **Response**: Who should be contacted and in what order?
3. **Triage**: What's the likely severity level?
4. **Resolution**: What are your first three diagnostic steps?
5. **Communication**: What should you tell stakeholders and when?

**Framework Response**:

1. **Detection**: Check database performance metrics, server resources, network connectivity
2. **Response**: Page database specialist, notify team lead, prepare stakeholder communication
3. **Triage**: Severity 2 (significant impact but service functional)
4. **Resolution**: Check query performance, examine server resources, review recent changes
5. **Communication**: Notify stakeholders of investigation within 15 minutes, provide updates every 30 minutes

### 3. 🔄 Change and Configuration Management

**Purpose**: Establish risk-assessed change management processes that can accommodate both routine changes and emergency fixes while maintaining accurate configuration management databases (CMDBs).

#### Change Management Categories

**Standard Changes**:

- Pre-approved, low-risk changes
- Automated or well-documented procedures
- Regular security patches and updates
- Routine maintenance activities

**Normal Changes**:

- Medium-risk changes requiring approval
- New software deployments
- Configuration modifications
- Infrastructure upgrades

**Emergency Changes**:

- High-urgency changes to restore service
- Security vulnerability fixes
- Critical system repairs
- Accelerated approval processes

#### Configuration Management

**Configuration Items (CIs)**:

- Servers, network devices, software applications
- Relationships and dependencies between CIs
- Change history and version control
- Baseline configurations and standards

**CMDB Maintenance**:

- Automated discovery and inventory tools
- Regular audits and reconciliation
- Change impact assessment capabilities
- Integration with monitoring and incident systems

#### Risk Assessment Framework

**Change Risk Factors**:

- **Complexity**: How many components are affected?
- **Testing**: How thoroughly has the change been tested?
- **Timing**: When will the change be implemented?
- **Rollback**: How easily can the change be reversed?
- **Dependencies**: What other systems might be affected?

**Risk Mitigation Strategies**:

- Staged rollouts and blue-green deployments
- Comprehensive testing in staging environments
- Automated rollback procedures
- Change windows during low-usage periods

### 4. 📈 Capacity and Performance Management

**Purpose**: Proactive monitoring and planning for system capacity needs, including predictive analytics to forecast resource requirements and regular performance tuning.

#### Capacity Planning Process

**Current State Analysis**:

- Resource utilization trends and patterns
- Peak usage periods and seasonal variations
- Performance bottlenecks and constraints
- Growth projections based on business plans

**Future State Modeling**:

- Predictive analytics and forecasting models
- Scenario planning for different growth rates
- Technology refresh and upgrade planning
- Cost optimization opportunities

**Capacity Implementation**:

- Procurement and deployment planning
- Scaling procedures and automation
- Performance testing and validation
- Monitoring and adjustment processes

#### Performance Management

**Performance Monitoring**:

- Key performance indicators (KPIs) for all systems
- Real-time dashboards and trending analysis
- Automated alerting for performance degradation
- User experience monitoring and feedback

**Performance Optimization**:

- Regular performance tuning activities
- Database query optimization
- Network and storage optimization
- Application and system configuration tuning

### 5. 📚 Knowledge and Documentation Management

**Purpose**: Systematic approach to capturing and sharing operational knowledge through runbooks, troubleshooting guides, and system documentation.

> This practice is the canonical home for the **runbook** concept — what a runbook is and what it must contain. Tooling that stores and executes runbooks (Rundeck, StackStorm, Ansible Tower, wikis) is catalogued in [Chapter 8](chapter-08-tools.md); runbooks are _used_ in the daily cycle ([Chapter 3](chapter-03-structure.md)) and on-call handoffs ([Chapter 9](chapter-09-culture.md)).

#### Documentation Categories

**Runbooks**:

- Step-by-step procedures for routine operations
- Emergency response procedures
- System startup and shutdown procedures
- Troubleshooting guides and decision trees

**System Documentation**:

- Architecture diagrams and system overviews
- Configuration standards and baselines
- Integration points and dependencies
- Security and compliance requirements

**Process Documentation**:

- Standard operating procedures
- Change management procedures
- Incident response workflows
- Training and onboarding materials

#### Knowledge Management Practices

**Documentation Standards**:

- Consistent templates and formats
- Version control and review processes
- Regular updates and maintenance schedules
- Searchability and accessibility requirements

**Knowledge Sharing**:

- Regular knowledge transfer sessions
- Cross-training programs and job shadowing
- Communities of practice and expert networks
- Mentoring and coaching programs

### 6. 👥 Team and Skill Development

**Purpose**: Focus on cross-training team members across multiple systems and technologies to reduce single points of failure and establish career development paths.

#### Skill Development Framework

**Technical Skills**:

- System administration and troubleshooting
- Automation and scripting capabilities
- Monitoring and performance analysis
- Security and compliance knowledge

**Operational Skills**:

- Incident response and problem-solving
- Communication and collaboration
- Process improvement and optimization
- Project management and planning

**Leadership Skills**:

- Team coordination and mentoring
- Stakeholder communication and management
- Strategic thinking and decision-making
- Change management and cultural development

#### Cross-Training Program

**Skill Matrix Development**:

- Inventory of required skills and current capabilities
- Identification of skill gaps and single points of failure
- Training priorities based on business criticality
- Individual development planning and tracking

**Training Methods**:

- Hands-on system training and job shadowing
- Formal education and certification programs
- Internal knowledge sharing and peer teaching
- External training and conference attendance

**Career Development Paths**:

- Technical specialist tracks (deep expertise)
- Technical generalist tracks (broad knowledge)
- Team leadership and management tracks
- Cross-functional collaboration opportunities

### 7. 🤝 Vendor and Contract Management

**Purpose**: Manage relationships with external vendors, ensure service level agreements (SLAs) are met, and optimize vendor partnerships to support operational objectives.

#### Vendor Management Components

**Vendor Inventory and Categorization**:

- Critical vendors (infrastructure providers, security vendors, support services)
- Strategic vendors (long-term partnerships, significant investment)
- Tactical vendors (specific tools, point solutions)
- Risk assessment for each vendor (concentration risk, viability, security posture)

**Service Level Agreement (SLA) Management**:

- Define clear SLAs aligned with your internal SLOs
- SLA terms: availability, response time, resolution time by severity
- Penalties for non-compliance and credit mechanisms
- Escalation procedures and dispute resolution
- Regular SLA review and adjustment

**Contract Management**:

- Documented terms, conditions, and renewal dates
- Pricing structure and cost optimization opportunities
- Licensing compliance and audit procedures
- Security and compliance requirements (SOC 2, ISO certification)
- Data handling and confidentiality agreements

**Vendor Performance Monitoring**:

- Track SLA compliance metrics month-over-month
- Monitor incident response quality and timeliness
- Assess support quality and ticket resolution rates
- Regular business reviews with vendor contacts
- Risk indicators (financial health, technical changes, staff turnover)

**Vendor Risk Management**:

- Identify single points of failure and concentration risk
- Develop contingency plans for vendor failure
- Ensure contracts include exit clauses and data return procedures
- Monitor industry news and vendor viability
- Conduct periodic security audits of vendor practices

#### Example: Cloud Infrastructure Vendor SLA

**Service**: Cloud Compute Instances

- **Availability SLA**: 99.95% monthly availability
- **Response Time**: Critical issues <15 minutes, Urgent <1 hour
- **Resolution Time**: Critical within 4 hours, Urgent within 8 hours
- **Credits**: 10% of monthly fees for each 0.1% below SLA (maximum 30%)
- **Escalation**: Support Team → Account Manager → VP if unresolved within 24 hours
- **Review Schedule**: Monthly SLA compliance review with account team

---

### 8. 🚀 Release Management

**Purpose**: Govern the end-to-end lifecycle of software and infrastructure releases — from build through deployment to production — using CI/CD pipelines, deployment gates, and well-defined rollback criteria to reduce release risk and increase delivery velocity.

#### Release Management Components

**CI/CD Pipeline Governance**:

- Define pipeline stages: build → test → security scan → staging deploy → production deploy
- Enforce mandatory quality gates (unit tests, integration tests, static analysis, SAST/DAST)
- Require peer review and approval for all production deployments
- Publish pipeline health dashboards; track build success rate, pipeline duration, and flaky-test rate
- Store pipeline-as-code in version control alongside application source

**Deployment Gates**:

| Gate                   | Criteria                             | Action on Failure |
| ---------------------- | ------------------------------------ | ----------------- |
| Test coverage          | ≥ 80% line coverage                  | Block merge       |
| Security scan          | Zero critical CVEs                   | Block deploy      |
| Performance regression | p95 latency < baseline × 1.10        | Block deploy      |
| Error rate baseline    | Error rate < SLO threshold for 5 min | Block promote     |
| Smoke test             | All smoke tests green                | Block promote     |
| Approval               | ≥ 1 designated approver sign-off     | Block promote     |

**Rollback Criteria and Procedures**:

- **Automatic rollback triggers**: error rate exceeds SLO threshold for > 2 minutes after deploy; health-check failures on ≥ 20% of instances
- **Manual rollback triggers**: customer-impact report confirmed by on-call engineer; critical bug identified post-deploy
- **Rollback runbook**: standardised steps documented in the knowledge base; target rollback completion < 10 minutes
- **Blue/green and canary strategies**: route a small traffic percentage to the new version before full promotion; automate promotion or rollback based on SLO signals

**Release Cadence and Planning**:

- Define release trains (e.g., weekly, bi-weekly, on-demand for hotfixes)
- Maintain a release calendar visible to all stakeholders
- Coordinate freeze windows with the Change Management practice (Practice 3)
- Track release frequency, change failure rate, and mean time to restore (MTTR) per the [DORA four-key metrics](https://dora.dev/research/2023/dora-report/)

**Environment Management**:

- Maintain parity between development, staging, and production environments using infrastructure-as-code
- Automate environment provisioning and teardown; avoid long-lived manual snowflake environments
- Gate production access: changes must pass staging validation before promotion

#### DORA Metrics Integration

The four DORA (DevOps Research and Assessment) key metrics directly measure Release Management effectiveness ([DORA State of DevOps Report](https://dora.dev/research/2023/dora-report/)):

| Metric                | Definition                                    | Elite Threshold          |
| --------------------- | --------------------------------------------- | ------------------------ |
| Deployment frequency  | How often code is deployed to production      | On-demand (multiple/day) |
| Lead time for changes | Time from commit to running in production     | < 1 hour                 |
| Change failure rate   | % of deployments causing a production failure | < 5%                     |
| Mean time to restore  | Time to recover from a production failure     | < 1 hour                 |

Track these metrics per team and review during the Weekly Improvement Cycle.

#### Example Release Gate Configuration

**Service**: Payment Processing API — Release v2.4.1

- **Gate 1 (Build)**: Compiled successfully, all 847 unit tests passed (98.6% coverage) ✅
- **Gate 2 (Security)**: SAST scan — 0 critical, 2 medium (accepted with risk sign-off) ✅
- **Gate 3 (Performance)**: Load test — p95 latency 142 ms vs. baseline 148 ms ✅
- **Gate 4 (Staging smoke)**: 12/12 smoke tests passed ✅
- **Gate 5 (Approval)**: Sign-off from Payment Platform lead ✅
- **Deployment strategy**: 10% canary → 100% over 30 minutes, automatic rollback if error rate > 0.5%

---

### 9. 🗄️ Asset Management

**Purpose**: Maintain an accurate, up-to-date inventory of all infrastructure assets — hardware, software, and cloud resources — throughout their entire lifecycle, and ensure license compliance to control risk and cost.

#### Asset Management Components

**Configuration Management Database (CMDB)**:

- Central authoritative record of all Configuration Items (CIs): servers, VMs, containers, network devices, storage, software, certificates, and their relationships
- Populate automatically via discovery tools (Ansible inventory, AWS Config, Azure Resource Graph, Terraform state) to avoid manual drift
- Link CIs to services, environments, and owners so that any Change or Incident record immediately shows the affected asset context
- Audit the CMDB monthly: compare discovered assets against records and reconcile discrepancies

**Asset Lifecycle Management**:

| Stage                    | Key Activities                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Procurement**          | Record asset in CMDB on purchase order; assign owner, cost centre, and depreciation schedule                                                                             |
| **Deployment**           | Tag with environment, team, and application; record in CMDB; link to service catalog                                                                                     |
| **In-service**           | Track change history, patch level, and capacity utilisation; review annually                                                                                             |
| **End-of-life planning** | Identify assets approaching hardware/software EOL; plan replacement or migration                                                                                         |
| **Decommission**         | Revoke access, sanitise data ([NIST SP 800-88 Rev. 1](https://doi.org/10.6028/NIST.SP.800-88r1)), update CMDB; reclaim licenses; dispose via certified e-waste programme |

**Software License Management**:

- Maintain a license register: product, edition, quantity purchased, quantity deployed, expiry dates
- Automate deployment discovery (Microsoft SCCM/Intune, Flexera, Snow Software, or cloud-native inventories)
- Run a **license reconciliation** monthly: compare entitlements against deployed instances; remediate over-deployment before vendor audits
- Track **SaaS subscriptions** separately: map seats to active users; deactivate leavers within 24 hours of offboarding
- Flag software with upcoming EOL/EOS dates at least 6 months in advance to allow migration planning

**Cloud Asset Management**:

- Use cloud-native tagging policies (enforced via Policy-as-Code, Practice 8) to attribute every cloud resource to a team, cost centre, and environment
- Schedule automated reports: untagged resources, unused Elastic IPs, idle instances, orphaned storage volumes
- Set budget alerts per account/project to catch runaway provisioning early (connects to Financial Management, Practice 11)

#### Example: CMDB Record — Production Web Server

| Attribute    | Value                               |
| ------------ | ----------------------------------- |
| CI Name      | prod-web-01                         |
| Type         | Virtual Machine                     |
| Environment  | Production                          |
| Owner        | Platform Team                       |
| Service      | Customer Portal                     |
| OS           | Ubuntu 24.04 LTS (EOL: 2029)        |
| Last patched | 2026-05-28                          |
| Related CIs  | prod-db-01, prod-lb-01, prod-web-02 |
| Last change  | CHG-2341 — kernel update 2026-05-28 |

---

### 10. 🎫 Service Request Management

**Purpose**: Provide a standardised, user-friendly channel through which staff and customers can request pre-approved IT services — keeping request fulfillment separate from incident response and enabling consistent, measurable delivery.

#### Service Request vs. Incident

| Aspect   | Service Request                                       | Incident                         |
| -------- | ----------------------------------------------------- | -------------------------------- |
| Nature   | Planned, expected, pre-approved                       | Unplanned, unexpected disruption |
| Urgency  | Normal (days) or expedited (same-day)                 | High — restore service ASAP      |
| Process  | Fulfillment workflow                                  | Incident response process        |
| Examples | New user access, hardware provision, SSL cert renewal | Database outage, network failure |

#### Service Catalog Design

A **service catalog** lists all requestable services with defined scope, fulfillment steps, SLA, and cost:

- **Standard requests** (pre-approved, automated or near-automated): new user account, VPN access, software installation, password reset
- **Normal requests** (require approval, manual fulfillment): new server/VM provisioning, firewall rule change, bulk license purchase
- **Complex requests** (project-like, multi-team): new environment build, network segment creation, third-party integration

For each catalog item document:

1. Description and eligibility (who can request it)
2. Required input information
3. Approval chain
4. Fulfillment SLA (e.g., standard: 2 business days; expedited: 4 hours)
5. Cost to the requesting team (chargeback, if applicable)
6. Automated fulfillment runbook or manual procedure link

#### Self-Service Portal

- Provide a self-service interface (ServiceNow, Jira Service Management, or an Internal Developer Platform portal like Backstage) so requesters can submit, track status, and receive fulfilment notifications without emailing the ops team
- Aim for **> 70% of standard requests fulfilled with zero ops-team touch** through automation (e.g., Ansible/Terraform triggered by approved request)
- Publish live queue metrics on a team dashboard to create accountability and visibility

#### Request Fulfillment Metrics

| Metric                          | Definition                                          | Target                    |
| ------------------------------- | --------------------------------------------------- | ------------------------- |
| Request fulfillment rate        | % of requests completed within SLA                  | ≥ 95%                     |
| Mean time to fulfillment (MTTF) | Avg time from submission to completion              | ≤ SLA per tier            |
| Automation rate                 | % of requests fulfilled without manual intervention | ≥ 70% (standard requests) |
| Request backlog age             | Oldest unresolved request in queue                  | < 5 business days         |
| Abandon rate                    | % of requests withdrawn before fulfillment          | < 5%                      |

---

### 11. 💰 Financial Management

**Purpose**: Give the operations team full visibility of its costs, link every spending decision to business value, and provide stakeholders with transparent, accurate forecasts — moving ops from an opaque cost centre to an accountable business partner.

#### Budget Planning and Forecasting

**Annual budgeting cycle**:

1. **Baseline**: Pull actuals for the past 12 months by category (people, infrastructure, software licenses, vendor services, training)
2. **Growth model**: Adjust for expected workload growth, new projects, and contract renewals
3. **Initiative funding**: Add budget for planned improvement projects (tool migrations, automation investments, resilience upgrades)
4. **Contingency reserve**: Allocate 5–10% for unplanned incidents, emergency hardware, and urgent security patches
5. **Stakeholder review**: Present to leadership with clear value narrative (cost per service, cost vs. downtime avoided)

**In-year forecasting**:

- Reforecast quarterly using actuals-to-date; flag variances > 10% of budget for management review
- Maintain a rolling 3-month forecast for cloud and variable-cost items updated monthly

#### Cost Accountability Models

| Model            | Description                                                      | When to Use                                         |
| ---------------- | ---------------------------------------------------------------- | --------------------------------------------------- |
| **Cost centre**  | Ops costs pooled centrally; no allocation to consumers           | Small organisations, shared services                |
| **Showback**     | Costs calculated per team/service and reported but not charged   | Building cost awareness without billing friction    |
| **Chargeback**   | Costs billed directly to consuming teams or cost centres         | Mature orgs; drives efficient consumption behaviour |
| **Unit pricing** | Internal rate card: fixed price per VM, per GB, per CI/CD minute | Platform teams with internal customers              |

**Chargeback implementation steps**:

1. Define the cost allocation unit (per service, per environment, per business unit)
2. Instrument cost attribution: cloud tags, CMDB ownership fields, FinOps tooling (Kubecost, Apptio)
3. Publish monthly cost reports to consuming team leads
4. Create an anomaly alert process: notify team lead when their allocated spend exceeds budget + 15% in a given month
5. Review rate card annually; adjust for actual cost changes

#### FinOps Integration

Financial Management is the governance layer; FinOps (Chapter 12) provides the technical tooling and discipline:

- **Inform phase**: CMDB + tagging → cost dashboards → showback reports
- **Optimize phase**: Rightsizing recommendations → commitment purchases → idle resource removal
- **Operate phase**: FinOps OKRs → chargeback accuracy → cost per unit economics

#### Financial Metrics

| Metric              | Definition                                         | Target                                   |
| ------------------- | -------------------------------------------------- | ---------------------------------------- |
| Budget variance     | Actual vs. budgeted spend                          | ≤ ±10% annually                          |
| Cost per service    | Monthly ops cost attributed to each service        | Trending down YoY                        |
| Unattributed spend  | Cloud/SaaS cost without owner tag                  | < 2% of total                            |
| License utilisation | Used seats / licensed seats                        | 80–95% (avoid waste and over-deployment) |
| ROI on automation   | Toil hours eliminated × fully-loaded engineer cost | Document annually                        |

---

### 12. 🔒 Backup & Recovery Operations

**Purpose**: Ensure that every critical system and data asset can be restored within defined Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) through regular, tested backup procedures and documented recovery runbooks.

#### RTO and RPO Definitions

- **Recovery Point Objective (RPO)**: Maximum acceptable data loss, expressed as time (e.g., RPO = 1 hour means backups must be taken at least hourly; data loss since the last backup is acceptable)
- **Recovery Time Objective (RTO)**: Maximum acceptable time to restore a service after a failure (e.g., RTO = 4 hours means the service must be back online within 4 hours of a declared disaster)

**Tiering assets by criticality**:

| Tier                       | Example Systems                                | RPO      | RTO     | Backup Frequency       |
| -------------------------- | ---------------------------------------------- | -------- | ------- | ---------------------- |
| Tier 1 — Mission Critical  | Payment API, auth service, core DB             | ≤ 15 min | ≤ 1 hr  | Continuous replication |
| Tier 2 — Business Critical | CRM, internal portals, monitoring stack        | ≤ 1 hr   | ≤ 4 hr  | Hourly incremental     |
| Tier 3 — Important         | Dev/staging environments, reporting DBs        | ≤ 4 hr   | ≤ 8 hr  | Every 4 hours          |
| Tier 4 — Standard          | Logs archive, internal wikis, low-traffic apps | ≤ 24 hr  | ≤ 24 hr | Daily full             |

#### Backup Strategy — The 3-2-1-1 Rule

> The 3-2-1-1 rule extends the classic 3-2-1 strategy with an additional offline or immutable copy, a practice widely adopted to defend against ransomware. See [CISA Ransomware Guide](https://www.cisa.gov/topics/cyber-threats-and-advisories/ransomware) for backup guidance and the immutable-copy requirement.

- **3** copies of data
- **2** different storage media/types (e.g., disk + object storage)
- **1** copy offsite or in a different cloud region
- **1** copy offline or immutable (protects against ransomware; use object-lock / WORM storage)

#### Testing Cadence

Backups that are never tested are not backups — they are hopes.

| Test Type                          | Frequency                         | What It Validates                                         |
| ---------------------------------- | --------------------------------- | --------------------------------------------------------- |
| **Automated restore verification** | Every backup cycle                | Backup file is readable and not corrupt; checksum matches |
| **Partial restore test**           | Monthly (automated)               | Specific files or tables can be recovered from backup     |
| **Full service restore test**      | Quarterly (planned)               | Full system can be rebuilt from backup within RTO         |
| **Disaster recovery simulation**   | Annually (or post-major-incident) | Cross-team failover to secondary site/region end-to-end   |

Log all test outcomes; treat a failed restore test as a Severity 2 incident requiring immediate root cause analysis and remediation.

#### Recovery Procedures

Every Tier 1 and Tier 2 system must have a documented recovery runbook containing:

1. **Prerequisites**: Access credentials, tool requirements, environment variables
2. **Identify the failure scope**: What data or system is affected; determine the restore point to use
3. **Initiate restore**: Step-by-step commands or automated runbook reference
4. **Validate restore**: Functional smoke tests to confirm data integrity and service health
5. **Notify stakeholders**: Update incident record; communicate restoration status
6. **Post-recovery review**: Update runbook with any steps that differed from documented procedure

**Recovery runbook review cadence**: Review and test runbooks annually, and immediately after any infrastructure change that affects the backup target (storage migration, database upgrade, credential rotation).

#### Monitoring Backup Health

- Alert on backup job failures within 15 minutes of the scheduled completion time
- Track **backup success rate** (target: 100% for Tier 1/2; ≥ 99% for Tier 3/4)
- Monitor **backup storage growth**: alert when projected full-capacity date is < 60 days away
- Audit **offsite/immutable copy confirmation** daily for Tier 1 systems
- Include backup health in the daily operations dashboard alongside service health metrics

---

## 🔗 Practice Integration with Operational Cycles

### Daily Operations Cycle Integration

- **Service Level Management**: Daily SLO monitoring and error budget tracking
- **Incident Management**: Real-time incident response and resolution
- **Change Management**: Implementation of approved standard changes
- **Performance Management**: Daily performance monitoring and alerts
- **Knowledge Management**: Real-time documentation updates during incidents
- **Team Development**: On-the-job learning and skill application
- **Vendor Management**: Escalation of vendor-related incidents, SLA impact tracking
- **Release Management**: Monitoring post-deployment health; triggering automatic rollbacks on SLO breach
- **Asset Management**: Verifying CI accuracy after incidents; updating CMDB when assets are modified
- **Service Request Management**: Fulfilling standard requests; monitoring request queue for same-day SLA items
- **Financial Management**: Monitoring daily cloud spend; flagging cost anomalies
- **Backup & Recovery Operations**: Verifying overnight backup job success; responding to backup failure alerts

### Weekly Improvement Cycle Integration

- **Service Level Management**: SLO review and adjustment recommendations
- **Problem Management**: Root cause analysis and prevention planning
- **Change Management**: Normal change planning and risk assessment
- **Capacity Management**: Weekly capacity trend analysis and planning
- **Knowledge Management**: Documentation updates and knowledge sharing sessions
- **Team Development**: Skill development planning and cross-training activities
- **Vendor Management**: Weekly SLA compliance monitoring, vendor performance review
- **Release Management**: Weekly DORA metrics review; release retrospectives; pipeline health review
- **Asset Management**: Weekly CMDB reconciliation; review of EOL asset alerts; license utilisation report
- **Service Request Management**: Request queue review; SLA compliance check; automation opportunity identification
- **Financial Management**: Weekly cloud spend vs. budget review; rightsizing recommendations actioning
- **Backup & Recovery Operations**: Weekly review of backup success rates; partial restore test results; storage growth trend

### Monthly Strategy Cycle Integration

- **Service Level Management**: Strategic SLO planning and business alignment
- **Change Management**: Major change planning and coordination
- **Capacity Management**: Long-term capacity planning and architecture decisions
- **Performance Management**: Strategic performance optimization initiatives
- **Knowledge Management**: Knowledge management strategy and tool improvements
- **Team Development**: Career development planning and strategic skill building
- **Vendor Management**: Vendor business reviews, contract renewals, strategic vendor assessments
- **Release Management**: Monthly trend analysis of DORA metrics; pipeline investment decisions; release strategy review
- **Asset Management**: Full CMDB audit; EOL planning and procurement requests; software license reconciliation and compliance reporting
- **Service Request Management**: Service catalog review; SLA target review; automation roadmap update; fulfillment metrics to stakeholders
- **Financial Management**: Monthly cost report to stakeholders; budget vs. actuals variance analysis; quarterly reforecast; chargeback invoicing
- **Backup & Recovery Operations**: Monthly full restore test review; quarterly DR simulation planning; RTO/RPO target review vs. actuals

## 📊 Practice Maturity Assessment

### Maturity Levels

- **Level 1 - Initial**: Practices are ad hoc and reactive
- **Level 2 - Repeatable**: Basic practices are defined and followed
- **Level 3 - Defined**: Practices are standardized and integrated
- **Level 4 - Managed**: Practices are measured and continuously improved
- **Level 5 - Optimizing**: Practices are continuously evolving and innovative

### Assessment Questions by Practice

#### Service Level Management Maturity

- Level 1: Do you have any defined service levels?
- Level 2: Are service levels documented and monitored?
- Level 3: Are SLOs integrated with business objectives and error budgets used?
- Level 4: Are SLOs continuously optimized based on data and feedback?
- Level 5: Are SLOs driving innovation and strategic decision-making?

#### Incident Management Maturity

- Level 1: Are incidents handled when they occur?
- Level 2: Are there defined incident response procedures?
- Level 3: Are post-incident reviews conducted and lessons captured?
- Level 4: Are incident metrics used to drive continuous improvement?
- Level 5: Are incidents prevented through proactive management?

#### Change Management Maturity

- Level 1: Are changes tracked in any form?
- Level 2: Are standard changes pre-approved and documented?
- Level 3: Are all changes categorized (standard/normal/emergency) with appropriate approval processes?
- Level 4: Are change success metrics tracked and used to refine processes?
- Level 5: Are changes fully automated with self-healing rollback and zero-downtime deployment?

#### Capacity and Performance Management Maturity

- Level 1: Is capacity managed reactively (buying more storage when it runs out)?
- Level 2: Are capacity trends monitored and basic forecasting performed?
- Level 3: Is capacity planning integrated with business plans and formal requests submitted?
- Level 4: Are predictive models used and capacity decisions tracked with actual outcomes?
- Level 5: Is capacity optimization continuous with automated scaling and cost optimization?

#### Knowledge and Documentation Management Maturity

- Level 1: Documentation exists but is outdated and inconsistent.
- Level 2: Documentation standards exist and most runbooks are documented.
- Level 3: Documentation is version-controlled and regularly reviewed for accuracy.
- Level 4: Documentation is integrated with incident response and automatically updated from configuration changes.
- Level 5: Knowledge is continuously synthesized from operational data, with intelligent documentation generation and AI-assisted search.

#### Team and Skill Development Maturity

- Level 1: Training happens informally when someone has time.
- Level 2: Are there documented skill requirements and a cross-training plan?
- Level 3: Are cross-training activities scheduled and tracked with documented skill matrices?
- Level 4: Are individual development plans in place aligned with team and organizational goals?
- Level 5: Are career development paths clear with advancement opportunities and continuous learning programs?

#### Vendor and Contract Management Maturity

- Level 1: Vendors are managed ad hoc with minimal documentation or formal agreements.
- Level 2: SLAs are documented and vendor inventory is maintained with basic contact information.
- Level 3: SLAs are actively monitored, performance metrics tracked, and formal vendor reviews conducted quarterly.
- Level 4: Vendor risk assessments are completed, contingency plans maintained, and contracts aligned with business requirements.
- Level 5: Vendors are strategically managed as partners with continuous optimization, proactive risk management, and integrated into strategic planning.

#### Release Management Maturity

- Level 1: Deployments are manual and undocumented; rollbacks require significant effort.
- Level 2: A basic CI pipeline exists; deployments follow an informal checklist; rollback procedures are documented.
- Level 3: All releases go through a defined CI/CD pipeline with automated test gates and documented rollback runbooks; DORA metrics are collected.
- Level 4: Deployment gates are enforced automatically; canary/blue-green strategies are standard; DORA metrics drive continuous improvement.
- Level 5: Deployments are fully automated with zero-touch production promotion; release frequency and lead time are continuously optimized; progressive delivery and feature flags enable safe experimentation.

#### Asset Management Maturity

- Level 1: No formal asset inventory; assets tracked in spreadsheets or not at all; license compliance unknown.
- Level 2: A basic asset register exists and is updated manually; software licenses are documented.
- Level 3: CMDB is populated via automated discovery; assets linked to services and owners; license reconciliation runs monthly.
- Level 4: CMDB is the authoritative source used by Change and Incident processes; EOL tracking and chargeback attribution are automated.
- Level 5: Asset intelligence drives proactive capacity and financial decisions; automated decommissioning workflows; continuous compliance posture visibility.

#### Service Request Management Maturity

- Level 1: Requests arrive via email or chat with no tracking, no SLA, and no consistent fulfillment process.
- Level 2: A basic ticketing system captures requests; common requests have documented procedures; informal SLAs exist.
- Level 3: A service catalog is published; requests are triaged to defined fulfillment workflows; SLAs are measured and reported.
- Level 4: Self-service portal in place; majority of standard requests fulfilled automatically; fulfillment metrics reviewed weekly.
- Level 5: Catalog is continuously optimized; near-zero-touch fulfillment for standard requests; request patterns feed into capacity and financial planning.

#### Financial Management Maturity

- Level 1: No formal IT budget tracking; costs are managed reactively; no cost attribution to services or teams.
- Level 2: An annual IT budget exists; actual vs. budget reviewed quarterly; high-level cost categories tracked.
- Level 3: Costs attributed to services and teams via showback; monthly financial reporting to stakeholders; budget variances investigated.
- Level 4: Chargeback model in place; FinOps tooling provides per-resource cost visibility; ROI tracked for automation investments.
- Level 5: Unit economics (cost per transaction, cost per user) drive continuous optimization; financial data integrated into capacity and release decisions; ops is seen as a value generator, not a cost centre.

#### Backup & Recovery Operations Maturity

- Level 1: Backups exist but are untested; no documented RTO/RPO; recovery is ad hoc and undocumented.
- Level 2: Backup schedules are defined and monitored; RTO/RPO targets documented for critical systems; basic recovery runbooks exist.
- Level 3: 3-2-1-1 backup strategy implemented for all tiers; monthly restore tests conducted; backup health reported in daily ops dashboard.
- Level 4: Recovery runbooks are automated or semi-automated; quarterly DR simulations completed; actual RTO/RPO consistently meets targets.
- Level 5: Continuous replication for Tier 1 assets; fully automated failover with zero-touch recovery tested and proven; RTO/RPO continuously improved through lessons learned.

## 🎯 Chapter Summary

The twelve core management practices provide the operational foundation that makes the SysOps Framework effective. Unlike generic IT management approaches, these practices are specifically designed for the interrupt-driven, high-availability world of operations teams.

Success with the SysOps Framework depends on implementing these practices consistently and improving them continuously. They work together to create a comprehensive operational capability that supports all three operational cycles while building team resilience and capability.

The practices should be implemented gradually, starting with basic capabilities and evolving toward more advanced maturity levels as the team develops experience and confidence with the framework.

## 🔮 Looking Ahead

In the next chapter, we'll explore the metrics and measurement approaches that help operations teams track their success and demonstrate value to stakeholders using the SysOps Framework.

## 💭 Reflection Questions

1. **Current Practices**: Which of these practices does your team already have in place?
2. **Practice Gaps**: Where are the biggest opportunities for improvement in your management practices?
3. **Integration Opportunities**: How could these practices be better integrated with your current operational cycles?

---

**🎮 Gamification Element - Chapter 6 Badge**
_Assess your team's maturity level for each practice and create an improvement plan to earn the "Practice Master" badge._

---

_[← Previous: Chapter 5 - Implementation Strategy](chapter-05-implementation.md) | [Next: Chapter 7 - Metrics & Measurement →](chapter-07-metrics.md)_
