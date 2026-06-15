---
title: "Chapter 10: Risk & Compliance"
linkTitle: "Chapter 10: Risk"
weight: 1000
description: >
  "In operations, every decision is a risk decision, whether you realize it or not."
---

## 🎯 Learning Objectives

By the end of this chapter, you will understand:

- How to integrate risk management into operational cycles
- Compliance requirements and their impact on operations frameworks
- Risk assessment methodologies for operational decisions
- Building security and compliance into the SysOps Framework
- Supply chain security using SBOMs, provenance, and current SLSA guidance
- Breach response timelines and regulatory notification obligations
- Penetration testing frequency, scope, and integration into the risk lifecycle

> **Principles in play.** This whole chapter is _Risk Management_ ([Chapter 2](chapter-02-principles.md)) given room to breathe, in constant tension with _Service Reliability First_ - because the riskiest control of all is the one so heavy that nobody actually follows it.

## ⚖️ Risk Management in Operations

### Understanding Operational Risk

Risk management has an image problem. Say the words out loud and half the room pictures a binder nobody has opened since the audit, full of heat maps in three shades of traffic-light. Real operational risk management is the opposite of a binder: it's the quiet voice that asks "what happens if _this_ disappears at the worst possible moment?" - and then does something cheap about it today instead of something expensive about it during the outage. The goal of this chapter is the voice, not the binder.

**Types of Operational Risk**:

| Risk Type         | What It Covers                                            |
| ----------------- | --------------------------------------------------------- |
| Availability risk | Service outages and performance degradation               |
| Security risk     | Data breaches, unauthorized access, and cyber attacks     |
| Compliance risk   | Regulatory violations and audit failures                  |
| Capacity risk     | Resource exhaustion and performance bottlenecks           |
| Process risk      | Human error and procedural failures                       |
| Technology risk   | Hardware failures, software bugs, and vendor dependencies |

**Risk Management Principles**:

- **Continuous Assessment**: Risk evaluation integrated into all operational cycles
- **Proactive Mitigation**: Address risks before they become incidents
- **Balanced Decisions**: Consider risk alongside business value and operational needs
- **Documented Rationale**: Clear reasoning for risk-related decisions
- **Learning Culture**: Use incidents and near-misses to improve risk understanding

### Risk Assessment Framework

**Risk Identification Process**:

- **System Dependencies**: Map all critical system relationships and dependencies
- **Failure Mode Analysis**: Identify potential failure points and their impacts
- **Threat Modeling**: Analyze security threats and attack vectors
- **Historical Analysis**: Learn from past incidents and industry events
- **Environmental Scanning**: Monitor for emerging risks and threat landscapes

**Risk Evaluation Criteria**:

- **Impact Severity**: Business and customer impact of risk realization
- **Probability**: Likelihood of risk occurring within a given timeframe
- **Detection Capability**: Ability to identify and respond to risk events
- **Recovery Complexity**: Difficulty and time required to recover from risk events
- **Cascading Effects**: Potential for risks to trigger additional problems

> **Note.** Impact × probability scoring is a _prioritisation_ tool, not a measurement. The numbers are deliberately coarse - their job is to force a conversation about which risks to fund first, not to pretend three-times-four is a scientifically precise 12. Treat a 20 and a 19 as "both urgent," not as a ranking.

### 🎮 Interactive Risk Assessment Exercise

**Scenario**: Your team manages a critical customer database with the following characteristics:

- Contains personal and financial information for 100,000 customers
- Required for all customer transactions and support operations
- Currently running on 5-year-old hardware with limited redundancy
- Backed up daily to offsite storage
- Accessed by 50 internal users and 3 external applications

**Risk Assessment Challenge**:

1. Identify the top 5 operational risks for this system
2. Evaluate each risk using Impact (1-5) and Probability (1-5) scales
3. Calculate risk scores (Impact × Probability) to prioritize mitigation efforts
4. Propose specific mitigation strategies for the highest-priority risks

**Sample Framework Response**:

```yaml
Risk Assessment Results:
  Hardware Failure:
    Impact: 5 (complete system unavailability)
    Probability: 4 (aging hardware, no redundancy)
    Score: 20 (Critical)
    Mitigation: Implement hardware redundancy and refresh plan

  Data Breach:
    Impact: 5 (regulatory fines, customer trust loss)
    Probability: 3 (external threats, internal access)
    Score: 15 (High)
    Mitigation: Enhanced access controls and monitoring

  Backup Failure:
    Impact: 4 (data loss during hardware failure)
    Probability: 2 (tested backup processes)
    Score: 8 (Medium)
    Mitigation: Automated backup testing and verification
```

## 🛡️ Security Integration

### Security as Code in Operations

**Security-First Design**:

- **Default Deny**: Start with minimal access and add permissions as needed
- **Defense in Depth**: Multiple layers of security controls and monitoring
- **Zero Trust Architecture**: Verify all access requests regardless of source
- **Continuous Monitoring**: Real-time security monitoring and incident response

**Automated Security Controls**:

- **Configuration Management**: Enforce security baselines through automation
- **Vulnerability Management**: Automated scanning and patch deployment
- **Access Management**: Automated provisioning and deprovisioning
- **Compliance Checking**: Continuous compliance monitoring and reporting

> **In practice.** "Default deny" reads beautifully on a slide and ruins your week the first time you turn it on. Roll it out in audit-only mode first, watch what legitimate traffic it _would_ have blocked for a couple of weeks, then enforce. Flipping straight to enforce is how you discover which critical batch job nobody documented - at 3 a.m., during the run that matters.

**Security Integration with Operational Cycles**:

**Daily Operations Cycle**:

- Security monitoring and alert triage
- Security incident response and containment
- Vulnerability assessment and emergency patching
- Security baseline verification and enforcement

**Weekly Improvement Cycle**:

- Security process improvements and automation
- Security training and awareness activities
- Security tool evaluation and implementation
- Security metrics analysis and reporting

**Monthly Strategy Cycle**:

- Security architecture planning and review
- Security risk assessment and mitigation planning
- Security compliance planning and audit preparation
- Security technology strategy and roadmap development

### Incident Response and Security

**Security Incident Classification**:

| Category   | Definition                                          |
| ---------- | --------------------------------------------------- |
| Category 1 | Confirmed data breach or system compromise          |
| Category 2 | Suspected security incident requiring investigation |
| Category 3 | Security policy violation or configuration drift    |
| Category 4 | Security monitoring alert requiring review          |

**Integrated Response Process**:

1. **Detection**: Security monitoring integrated with operational monitoring
2. **Assessment**: Joint evaluation of security and operational impact
3. **Response**: Coordinated containment and recovery procedures
4. **Recovery**: Secure restoration of services and data
5. **Analysis**: Combined security and operational lessons learned

### Supply Chain Security

Modern software delivery depends on hundreds of open-source packages, container base images, and third-party services. A compromise anywhere in that chain can reach production. Two complementary standards address this risk:

**Software Bill of Materials (SBOM)**:

- An SBOM is a machine-readable inventory of every component in a software artifact (libraries, versions, licenses, checksums).
- Formats: **[SPDX](https://spdx.dev/specifications/)** (ISO/IEC 5962:2021) and **[CycloneDX](https://cyclonedx.org/specification/overview/)** (OWASP standard) are the two dominant formats; prefer CycloneDX for container and application SBOMs.
- **Generate SBOMs at build time** using tools like Syft, Trivy, or Microsoft SBOM Tool; attach them to container image attestations or release artefacts.
- **Consume SBOMs** in CI with tools like Grype, OWASP Dependency-Check, or Snyk to detect CVEs before deployment.
- **Regulatory context**: [US Executive Order 14028 (2021)](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) and [EU Cyber Resilience Act (2024)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847) mandate SBOM provision for software sold to government and critical infrastructure sectors.

**[SLSA](https://slsa.dev/) (Supply-chain Levels for Software Artifacts)**:

- A security framework by Google/OpenSSF that defines build integrity requirements across four levels.

SLSA evolves, so avoid pinning policy to a retired version of the specification. Use the current SLSA documentation for exact requirements and keep your internal control text focused on durable outcomes:

| Control outcome                        | Practical implementation                                      | What it prevents                      |
| -------------------------------------- | ------------------------------------------------------------- | ------------------------------------- |
| Build process is documented            | CI configuration and build scripts are versioned              | Accidental or unexplained build drift |
| Provenance is generated                | Build metadata records source, builder, and artifact identity | Unknown artifact origin               |
| Provenance is protected and verifiable | Signed provenance or trusted build attestations               | Tampering with build outputs          |
| Critical builds use hardened builders  | Isolated runners, controlled dependencies, reviewed pipelines | Build infrastructure compromise       |

- **Implementation path**: start by generating SBOMs and provenance for critical services; then move toward verified provenance and hardened build environments for high-risk systems.
- Use **[Sigstore](https://docs.sigstore.dev/)** (Cosign, Rekor) to sign and verify container images and build provenance; integrate verification into OPA/Kyverno admission policies so only signed, policy-compliant images can deploy.

> **In practice.** Don't gate deployments on _every_ CVE the scanner reports - you'll train the team to click "override" on reflex within a week. Gate on critical/high severity with a known fix available, and route the rest to the backlog. A policy nobody can satisfy is a policy everybody learns to bypass.

**SysOps Integration**: Embed SBOM generation into the CI/CD pipeline (Release Management, Practice 8); block deployment on critical CVEs via Policy-as-Code gates; store SBOMs in an artifact repository (e.g., OCI-attached attestation) for audit evidence in Compliance Management.

### Regulatory Context Without Overclaiming

Regulatory language must be precise. SBOMs and provenance are increasingly important in procurement, secure development, and product cybersecurity discussions, but requirements differ by jurisdiction, sector, and product type.

Use this wording in policies:

> We maintain component inventory and build provenance for critical services to improve vulnerability response, software supply-chain transparency, and audit readiness. Where specific regulation or customer contracts require stronger evidence, those requirements are mapped to concrete build, release, and asset-management controls.

This keeps the framework useful without pretending that one global SBOM rule applies to every team.

### Breach Response Timelines

A well-defined breach response timeline prevents ad-hoc decisions under pressure and ensures regulatory obligations are met. The following timelines should be documented in the incident response runbook:

| Window          | Action                                                                                                                                                                                                                                                  | Owner                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| 0–15 min        | Detect and classify: confirm breach vs. false positive; escalate to Incident Commander                                                                                                                                                                  | On-call engineer       |
| 0–1 hr          | Contain: isolate affected systems; revoke compromised credentials; block exfiltration paths                                                                                                                                                             | IC + Security lead     |
| 1–4 hr          | Assess scope: identify affected data, systems, and users; preserve forensic evidence (memory dumps, logs)                                                                                                                                               | Security + Ops         |
| 4–24 hr         | Notify internally: executive team, legal, DPO; begin regulatory clock assessment                                                                                                                                                                        | CISO / DPO             |
| 24–72 hr        | **Regulatory notification**: [GDPR Art. 33](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) requires supervisory authority notification within 72 hours of becoming aware; US state breach laws vary (24–72 hr for some states) | Legal / DPO            |
| 72 hr – 30 days | Notify affected individuals ([GDPR Art. 34](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) if high risk); coordinate with law enforcement if required                                                                          | Legal / Communications |
| Ongoing         | Root cause analysis; control remediation; post-breach audit; lessons learned                                                                                                                                                                            | All teams              |

> **Warning.** The regulatory clock starts on _awareness_, not on discovery. If an automated alert fires at 02:00 but nobody reviews it until 08:00, you have already burned six hours of your 72-hour GDPR window - and "we hadn't looked yet" is not a defence a regulator accepts.

**Key principles**:

- **Preserve evidence before containment actions change system state** where operationally safe to do so.
- **Rehearse annually**: run a tabletop breach simulation to validate timeline adherence and update runbooks with findings.

### Penetration Testing Frequency and Scope

Penetration testing proactively identifies exploitable vulnerabilities before attackers do. Frequency depends on risk profile and regulatory requirements:

| Environment / Change                  | Recommended Frequency                   | Test Type                                                                                       |
| ------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Internet-facing applications          | Annually (minimum); after major changes | External web application pentest ([OWASP Top 10](https://owasp.org/www-project-top-ten/) scope) |
| Internal network                      | Annually                                | Internal network / lateral movement                                                             |
| Cloud infrastructure                  | Annually + after architectural changes  | Cloud configuration review + privilege escalation                                               |
| APIs (public or partner)              | Every 6 months or after API changes     | API security test ([OWASP API Top 10](https://owasp.org/www-project-api-security/))             |
| After significant breach or near-miss | Immediately after remediation           | Targeted retest                                                                                 |
| Pre-production for critical services  | Before first production launch          | Pre-launch assessment                                                                           |

**Pentest engagement process**:

1. **Scoping**: Define in-scope systems, test types (black/grey/white box), rules of engagement, and emergency stop conditions.
2. **Authorization**: Obtain written sign-off from system owner, legal, and cloud provider (AWS/GCP/Azure each have pentest policies; notify before testing cloud assets).
3. **Execution**: Use certified testers (OSCP, CHECK, CREST); require daily finding briefs for critical issues found mid-test.
4. **Remediation tracking**: All critical and high findings must have remediation due dates; retest critical findings within 30 days.
5. **Evidence retention**: Retain pentest reports for 3 years minimum for compliance purposes.

> **Warning.** Never point a pentest at cloud-hosted assets without checking your provider's rules of engagement first. AWS, GCP, and Azure each publish what's allowed and what needs prior notice; unauthorized testing can trip abuse detection, get your account suspended, and - depending on jurisdiction - cross the line into an actual offence.

**SysOps Integration**: Pentest findings feed directly into the risk register; critical findings trigger an emergency change (Practice 3, emergency change category); remediated controls are validated through Policy-as-Code and SBOM scanning to confirm fix persistence.

## 📋 Compliance Management

### Policy, Procedure, and Evidence - The Three Layers

Before mapping controls, it's essential to distinguish the three layers of compliance. Mixing them up is the most common source of audit findings.

| Layer         | Definition                       | Example                                                                                                  | Who Owns It                   |
| ------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **Policy**    | What must be done (the rule)     | "All production changes must be approved before deployment"                                              | Security / Compliance officer |
| **Procedure** | How it's done (the steps)        | "Submit a change request in Jira → Team lead reviews → Deploy via CI/CD → Verify health"                 | Team lead / Process owner     |
| **Evidence**  | Proof it was done (the artifact) | Change request ticket, approval timestamp, CI/CD pipeline log with green build, post-deploy health check | Engineer / Automation         |

> **Common failure mode.** Teams document a policy without a procedure (it says what but not how), or a procedure without evidence collection (everyone follows the steps but nothing proves it after the fact). An auditor needs all three: "show me your policy" → "show me your procedure" → "show me evidence it was followed." If any link is missing, the control is not operating effectively.

### Control-Mapping Table: Practices to Frameworks

The SysOps Framework is not a compliance framework - but its practices implement controls that satisfy compliance requirements. Use this table to map which SysOps practice produces the evidence for which control in SOC 2, ISO 27001, and GDPR. This is your audit readiness blueprint: for every control, you can point to a practice, the procedure under that practice, and the evidence it generates.

| SysOps Practice                             | SOC 2 (Trust Services Criteria)              | ISO 27001 (Annex A)                                                  | GDPR (Articles)                  | Evidence Produced                                           |
| ------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------- | -------------------------------- | ----------------------------------------------------------- |
| **1. Service Level Management**             | Availability (A1.1, A1.2)                    | A.12.1 (Operational planning)                                        | Art. 32 (Security of processing) | SLO attainment reports, error budget logs                   |
| **2. Incident & Problem Management**        | Security (CC7.3, CC7.4), Availability (A1.3) | A.16.1 (Incident management)                                         | Art. 33/34 (Breach notification) | Incident timeline, PIR, action items                        |
| **3. Change & Configuration Management**    | Change management (CC8.1)                    | A.12.1 (Change management), A.12.5 (Control of operational software) | Art. 32                          | Change tickets, approval records, CMDB audit trail          |
| **4. Capacity & Performance Management**    | Availability (A1.2)                          | A.12.1 (Capacity management)                                         | -                                | Capacity trend reports, performance baselines               |
| **5. Knowledge & Documentation Management** | -                                            | A.7.5 (Documentation)                                                | Art. 5 (Accountability)          | Runbooks, SOPs, system documentation                        |
| **6. Team & Skill Development**             | -                                            | A.7.2 (Competence)                                                   | -                                | Training records, skill matrix                              |
| **7. Vendor & Contract Management**         | Vendor management (CC9.1, CC9.2)             | A.15.1 (Supplier relationships)                                      | Art. 28 (Processor)              | SLA compliance reports, vendor risk assessments             |
| **8. Release Management**                   | Change management (CC8.1)                    | A.12.1, A.12.6 (Technical vulnerability management)                  | Art. 32                          | CI/CD pipeline logs, deployment approvals, rollback records |
| **9. Asset Management**                     | Physical security (A1.4 - if hardware)       | A.8.1 (Asset inventory)                                              | Art. 32                          | CMDB, asset register, license records                       |
| **10. Service Request Management**          | -                                            | A.12.1                                                               | -                                | Request tickets, fulfillment SLA reports                    |
| **11. Financial Management**                | -                                            | -                                                                    | -                                | Budget reports, cost allocation records                     |
| **12. Backup & Recovery Operations**        | Availability (A1.3)                          | A.12.3 (Backup), A.17.1 (Business continuity)                        | Art. 32                          | Backup success logs, restore test results, DR test reports  |

> **How to read this table.** If your SOC 2 auditor asks for change management evidence (CC8.1), point them to Practice 3 (Change & Configuration Management), whose procedure produces change tickets, approval records, and CMDB audit trails as evidence. If they find a gap in evidence collection, strengthen the procedure - not the tool.

### Policy-as-Code for Compliance

The bridge between "policy exists on paper" and "policy is enforced automatically" is Policy-as-Code. Instead of relying on manual compliance checks, encode the policy rules and let CI/CD and admission control enforce them.

**How Policy-as-Code serves each compliance layer**:

| Compliance Layer | Policy-as-Code Application                                                    | Example                                                                     |
| ---------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Policy**       | Policy written as Rego (OPA) or YAML (Kyverno) rules                          | "All containers must come from an approved registry"                        |
| **Procedure**    | Policy evaluated in CI/CD pipeline gates and Kubernetes admission webhooks    | OPA Gatekeeper rejects pods from unapproved registries at deploy time       |
| **Evidence**     | Admission decision logged with timestamp, request payload, and policy version | Audit log shows "Pod X was rejected by policy v1.3 at 2026-06-13T14:22:00Z" |

**Examples for compliance-relevant controls**:

```rego
# OPA Gatekeeper: Require encryption in transit (GDPR Art. 32, SOC 2 CC6.1)
package ingress_tls

violation[{"msg": msg}] {
  ingress := input.review.object
  not ingress.spec.tls
  msg := sprintf("Ingress %v must have TLS configured - encryption in transit is required", [ingress.metadata.name])
}
```

```yaml
# Kyverno: Require resource limits (ISO 27001 A.12.1 - capacity management)
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-resource-limits
spec:
  validationFailureAction: enforce
  rules:
    - name: check-containers
      match:
        any:
          - resources:
              kinds:
                - Pod
      validate:
        message: "All containers must specify resource requests and limits"
        pattern:
          spec:
            containers:
              - resources:
                  limits:
                    memory: "?*"
                    cpu: "?*"
```

> **Start with the highest-risk controls first.** Do not attempt to encode every policy before the audit - you never will. Instead, pick the three controls that scare you most (e.g., "no unapproved image registries," "TLS required on all ingress," "backup retention ≥ 30 days"), build policies for those, validate they work, and expand incrementally. Three enforced policies beat thirty written policies that nobody checks.

### Compliance Integration Strategies

- **Built-in Controls**: Embed compliance requirements into operational processes
- **Automated Evidence**: Generate compliance artifacts through normal operations
- **Continuous Monitoring**: Real-time compliance status tracking and alerting
- **Audit Readiness**: Maintain audit trails and documentation continuously

> **In practice.** The cheapest audit is the one you never prepared for - because the evidence collected itself all year. If you find the team doing a frantic "audit sprint" the month before the assessor arrives, that's a signal your controls produce paperwork on demand instead of as a by-product of normal work. Aim for the latter; the binder-stuffing season is a smell, not a tradition.

### Audit Trail and Documentation

**Audit Trail Requirements**:

- **Change Documentation**: Complete records of all system and process changes
- **Access Logging**: Comprehensive logs of system and data access
- **Incident Records**: Detailed documentation of all security and operational incidents
- **Process Evidence**: Documentation of adherence to defined procedures

**Documentation Standards**:

- **Completeness**: All required information captured and maintained
- **Accuracy**: Information is correct and up-to-date
- **Accessibility**: Easy to locate and retrieve for audit purposes
- **Retention**: Maintained for required retention periods
- **Security**: Protected from unauthorized modification or access

### 🎮 Compliance Scenario Challenge

**Scenario**: Your organization is implementing SOC 2 Type II compliance for your SaaS platform. The audit requirements include:

- Documented change management procedures
- Evidence of security monitoring and incident response
- Proof of data backup and recovery capabilities
- Access control management and review processes

**Challenge Questions**:

1. How would you integrate these requirements into the SysOps Framework cycles?
2. What automated evidence collection could you implement?
3. How would you prepare for the annual compliance audit?
4. What documentation standards would you establish?

**Framework Integration Approach**:

1. **Daily Cycle**: Automated logging and monitoring evidence collection
2. **Weekly Cycle**: Access reviews and security control validation
3. **Monthly Cycle**: Compliance status reporting and audit preparation
4. **Documentation**: Automated audit trail generation with manual review processes

## 🔒 Data Protection and Privacy

### Data Lifecycle Management

**Data Classification**:

| Classification | Description                                              |
| -------------- | -------------------------------------------------------- |
| Public         | Information intended for public consumption              |
| Internal       | Information for internal business use only               |
| Confidential   | Sensitive business information requiring protection      |
| Restricted     | Highly sensitive information with strict access controls |

**Data Handling Requirements**:

- **Collection**: Minimize data collection to business requirements
- **Storage**: Secure storage with appropriate access controls
- **Processing**: Authorized processing with audit trails
- **Transmission**: Encrypted transmission with secure protocols
- **Retention**: Defined retention periods with secure disposal
- **Deletion**: Secure deletion and disposal procedures

### Privacy by Design

**Core Principles**:

- **Proactive**: Anticipate and prevent privacy invasions
- **Default Protection**: Maximum privacy protection as the default setting
- **Privacy Embedded**: Privacy considerations integrated into system design
- **Full Functionality**: Accommodate privacy without sacrificing functionality
- **End-to-End Security**: Complete lifecycle data protection
- **Visibility**: Ensure transparency for all stakeholders
- **Respect**: Keep user privacy as the top priority

**Implementation in Operations**:

- **Data Minimization**: Collect and retain only necessary data
- **Access Controls**: Strict role-based access to personal data
- **Encryption**: Data encryption at rest and in transit
- **Monitoring**: Comprehensive audit trails for data access and processing
- **Breach Response**: Rapid detection and response to data breaches

## 🏗️ Business Continuity and Disaster Recovery

### Business Continuity Planning

**Key Components**:

- **Risk Assessment**: Identify threats to business operations
- **Business Impact Analysis**: Understand the consequences of service disruptions
- **Recovery Strategies**: Define approaches for maintaining or restoring operations
- **Plan Development**: Document procedures for business continuity responses
- **Testing and Maintenance**: Regular testing and updating of continuity plans

**Integration with SysOps Framework**:

- **Daily Operations**: Continuous monitoring for threats to business continuity
- **Weekly Improvements**: Regular testing and improvement of continuity procedures
- **Monthly Strategy**: Business continuity planning and capability development

> **Warning.** An untested backup is not a backup - it's a hope with a cron job. The only thing that proves you can recover is a restore you actually performed, end to end, into a usable state. Plenty of teams have discovered mid-incident that their backups were silently corrupt, missing a critical table, or encrypted with a key nobody still has. Test the restore, not the backup.

### Disaster Recovery Implementation

**Recovery Objectives**:

| Objective                      | Defines                                          |
| ------------------------------ | ------------------------------------------------ |
| Recovery Time Objective (RTO)  | Maximum acceptable downtime                      |
| Recovery Point Objective (RPO) | Maximum acceptable data loss                     |
| Recovery Level Objective (RLO) | Minimum acceptable service level during recovery |

**Recovery Strategies**:

| Strategy       | Description                                             | Trade-off                               |
| -------------- | ------------------------------------------------------- | --------------------------------------- |
| Hot site       | Fully equipped backup facility ready for immediate use  | Lowest RTO, highest cost                |
| Warm site      | Partially equipped facility requiring setup time        | Moderate RTO and cost                   |
| Cold site      | Basic facility requiring complete setup and restoration | Highest RTO, lowest cost                |
| Cloud recovery | Cloud-based backup and recovery capabilities            | Elastic cost; RTO depends on automation |

### Disaster Recovery Testing Methodology

A DR plan that has never been tested is a hypothesis, not a capability. Testing must be systematic, scheduled, and progressively more demanding as team maturity grows.

#### Testing Tiers

| Tier | Test Type                  | Description                                                                                                                   | Frequency                        | Disruption to Production         |
| ---- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | -------------------------------- |
| 1    | **Document review**        | Walk through the DR plan with the team; identify gaps, outdated steps, or missing contacts                                    | Quarterly                        | None                             |
| 2    | **Tabletop exercise**      | Facilitate a structured scenario discussion; responders describe what they would do step-by-step without executing            | Quarterly                        | None                             |
| 3    | **Component restore test** | Restore individual system components (a single database, a specific service) from backup to an isolated environment           | Monthly                          | None (isolated env)              |
| 4    | **Parallel failover test** | Activate the DR environment in parallel with production; validate that traffic _could_ be switched without actually switching | Semi-annually                    | Low                              |
| 5    | **Partial cut-over test**  | Route a subset of traffic (e.g., 5–10% canary or a non-critical tenant) to the DR environment; validate end-to-end            | Annually                         | Low                              |
| 6    | **Full failover test**     | Cut all traffic to the DR environment; run production from the DR site for a defined period; then fail back                   | Annually (or as maturity allows) | Medium - plan maintenance window |

Start at Tier 1–2 and progress upward annually. Do not attempt a full failover test without first passing Tiers 3–5.

#### DR Test Planning Process

1. **Define scope**: which systems, regions, and failure scenarios are in scope for this test
2. **Set success criteria before the test**: document expected RTO and RPO targets that must be met for the test to pass
3. **Notify stakeholders**: schedule at least 4 weeks in advance; communicate impact window and rollback plan
4. **Appoint a Test Director**: a named individual (typically the Incident Commander) who has authority to halt the test if real impact exceeds the agreed threshold
5. **Execute with real conditions**: avoid shortcuts (e.g., using pre-warmed caches or pre-loaded data) that would not exist in a real disaster
6. **Measure actual RTO and RPO**: record timestamps at each milestone; compare against targets
7. **Document findings immediately**: capture every deviation, workaround, and failed step during the test, not after
8. **Publish a DR test report** within 5 business days: findings, actual vs. target RTO/RPO, action items with owners and due dates

#### Failure Scenario Library

Rotate through different scenarios each test cycle to avoid building muscle memory for only one failure mode:

- **Single availability zone failure**: all resources in one AZ become unavailable; validate automatic failover to another AZ
- **Primary database failure**: primary DB becomes unresponsive; validate replica promotion and application reconnection
- **Region-level outage**: entire cloud region is unavailable; validate failover to secondary region
- **Ransomware / data corruption**: primary data is corrupted or encrypted; validate restore from immutable backup (3-2-1-1 rule, Practice 12)
- **DNS provider outage**: DNS resolution fails for primary domains; validate fallback DNS configuration
- **CI/CD pipeline failure**: deployment pipeline unavailable; validate ability to deploy manually from artefact repository
- **Third-party dependency outage**: a critical SaaS service (authentication, payment processing) is unavailable; validate graceful degradation or bypass

#### RTO / RPO Validation Recording

For each test, record the following in the DR test log:

```text
Test Date:          2026-Q2 Full Failover Test
Scenario:           Primary region (eu-west-1) total failure
Test Director:      [Name]
Test Start:         14:00 UTC
Failure declared:   14:05 UTC
First traffic on DR:14:22 UTC  → RTO so far: 17 min
Full traffic on DR: 14:31 UTC  → Actual RTO: 26 min  (Target: 30 min) ✅
Data validated:     14:38 UTC  → Actual RPO: 8 min   (Target: 15 min) ✅
Fail-back complete: 16:15 UTC
Issues found:       3 (see action log)
Test result:        PASS
```

Store all DR test logs in the knowledge management system (Chapter 6, Practice 5); retain for 3 years minimum for audit and compliance evidence.

#### DR Testing Integration with SysOps Cycles

- **Monthly Strategy Cycle**: schedule upcoming DR tests; review action items from previous tests
- **Weekly Improvement Cycle**: close DR test action items; update runbooks with findings
- **After every major infrastructure change**: re-validate DR assumptions that may have been invalidated by the change (new database, region expansion, service mesh addition)

## 📊 Risk Metrics and Reporting

### Risk Assessment Metrics

**Risk Exposure Indicators**:

- **Total Risk Score**: Sum of all identified risks weighted by impact and probability
- **Critical Risk Count**: Number of risks scored as critical priority
- **Risk Trend Analysis**: Changes in risk exposure over time
- **Mitigation Effectiveness**: Success rate of risk mitigation efforts

**Security Metrics**:

- **Vulnerability Metrics**: Count and severity of identified vulnerabilities
- **Incident Metrics**: Frequency and impact of security incidents
- **Compliance Metrics**: Percentage of compliance requirements met
- **Security Training Metrics**: Team security awareness and training completion

**Operational Risk Metrics**:

- **System Availability**: Uptime percentage for critical systems
- **Change Success Rate**: Percentage of changes implemented without incidents
- **Backup Success Rate**: Percentage of successful backup operations
- **Recovery Testing**: Frequency and success rate of disaster recovery tests

### Executive Risk Reporting

**Risk Dashboard Components**:

- **Risk Heat Map**: Visual representation of risks by impact and probability
- **Trend Analysis**: Changes in risk exposure over time
- **Mitigation Status**: Progress on risk mitigation initiatives
- **Compliance Status**: Current compliance posture and any deficiencies

> **Reality check.** A heat map glowing reassuringly green is the easiest artifact in this entire chapter to fake - just be optimistic about every probability. Executives trust the colours, so the colours have to be honest. If nothing on the board has been amber in six months, the question isn't "why are we so safe?" - it's "who's grading their own homework?"

**Reporting Frequency**:

- **Real-time**: Critical risk events and security incidents
- **Weekly**: Operational risk status and mitigation progress
- **Monthly**: Comprehensive risk assessment and compliance status
- **Quarterly**: Strategic risk review and annual planning updates

## 🔄 Continuous Risk Management

### Risk Management Maturity

| Level | Stage        | What It Looks Like                                                                                                                                      |
| ----- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Reactive     | Risk managed after incidents; limited documentation and tracking; manual assessment; inconsistent mitigation                                            |
| 2     | Managed      | Regular assessments and reviews; documented processes; basic tracking and reporting; some automated controls                                            |
| 3     | Defined      | Risk management integrated across operations; standardized methodologies; comprehensive monitoring and alerting; risk-based decisions                   |
| 4     | Quantitative | Quantitative assessment and modeling; predictive analytics and forecasting; cost-benefit analysis of mitigations; risk metrics tied to business metrics |
| 5     | Optimizing   | Continuous process optimization; ML-driven risk prediction; risk management drives strategy; industry leadership in practice                            |

> **Reality check.** Most teams don't need Level 5, and several reach for the machine-learning bullet long before they can reliably do the Level 2 basics. Be honestly Level 2 before you cosplay Level 5 - a tidy risk register that people actually keep up to date beats a predictive model nobody trusts.

### Continuous Improvement

**Risk Learning Process**:

1. **Incident Analysis**: Detailed analysis of all risk events and near-misses
2. **Pattern Recognition**: Identification of common risk factors and themes
3. **Process Improvement**: Updates to risk management processes based on learning
4. **Control Enhancement**: Strengthening of risk controls and mitigation strategies
5. **Culture Development**: Building risk awareness and management capabilities

**Risk Management Evolution**:

- **Baseline Establishment**: Initial risk assessment and control implementation
- **Process Maturation**: Refinement of risk management processes and capabilities
- **Integration**: Full integration of risk management with operational processes
- **Optimization**: Continuous optimization and improvement of risk management
- **Innovation**: Leading-edge risk management practices and technologies

## 🎯 Chapter Summary

Risk management and compliance are not separate activities from operations-they must be integrated into every aspect of the SysOps Framework. Success requires embedding risk considerations into all operational cycles, automating compliance evidence collection, and building a culture where risk awareness drives decision-making.

Modern operations teams must also address the expanding attack surface of the software supply chain: generating SBOMs at build time, enforcing SLSA build integrity, and validating provenance before every production deployment. Breach response timelines must be pre-agreed and rehearsed - regulatory clocks start on awareness, not on planned action. Penetration testing must be frequent, scoped correctly, and its findings tracked to confirmed remediation rather than filed and forgotten.

The key is to make risk management and compliance enablers of operational excellence rather than barriers to efficiency. This requires thoughtful integration of controls and processes, automation of routine compliance activities, and continuous improvement based on risk events and changing threat landscapes.

## 🔮 Looking Ahead

In the next chapter, we'll explore common challenges and limitations of the SysOps Framework, along with practical solutions and workarounds for difficult implementation scenarios.

## 💭 Reflection Questions

1. **Risk Assessment**: What are the top operational risks in your current environment?
2. **Compliance Integration**: How could you better integrate compliance requirements into your operational processes?
3. **Risk Culture**: How would you build a culture of risk awareness without creating analysis paralysis?

---

**🎮 Gamification Element - Chapter 10 Badge**
_Complete a comprehensive risk assessment for your environment and earn the "Risk Guardian" badge._

---

_[← Previous: Chapter 9 - Culture & Organization](chapter-09-culture.md) | [Next: Chapter 11 - Challenges & Solutions →](chapter-11-challenges.md)_
