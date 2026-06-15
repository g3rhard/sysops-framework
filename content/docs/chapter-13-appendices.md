---
title: "Appendices: Templates & Checklists"
linkTitle: "Appendices"
weight: 1300
description: >
  "The boring pages you'll actually photocopy - readiness checklists, a milestone tracker, and the templates every operations team ends up rewriting at 2 a.m."
---

## 🎯 What's In Here

The chapters make the argument. The appendices give you the paperwork.

Everything here is meant to be copied, pasted, butchered, and made your own. Nothing in this section is sacred - if a field doesn't apply to your team, delete it; if you need three more, add them. These are starting points, not commandments. The fastest way to ruin a good template is to treat it as a form to be _completed_ rather than a tool for _thinking_.

> **📥 Downloadable versions**: All templates below are available as separate Markdown files in the [`templates/`](https://github.com/g3rhard/sysops-framework/tree/main/templates) directory.

A note on placement: detailed, tick-box-heavy material lives here on purpose. The chapters keep the narrative and the key decisions; the appendices hold the granular checklists so the story stays readable and the reference material stays findable. When a chapter says "see the appendix," this is where it's pointing.

- **Appendix A** - Implementation Readiness Checklists (referenced from [Chapter 5](chapter-05-implementation.md))
- **Appendix B** - Six-Month Milestone Tracker (referenced from [Chapter 5](chapter-05-implementation.md))
- **Appendix C** - Post-Incident Review (Post-Mortem) Template (referenced from [Chapter 6](chapter-06-practices.md))
- **Appendix D** - Incident Commander Checklist (referenced from [Chapter 6](chapter-06-practices.md))
- **Appendix E** - Change Control Form (referenced from [Chapter 6](chapter-06-practices.md))
- **Appendix F** - Service Level Agreement (SLA) Template (referenced from [Chapter 6](chapter-06-practices.md) and [Chapter 7](chapter-07-metrics.md))

---

## 📋 Appendix A: Implementation Readiness Checklists

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

## 🗓️ Appendix B: Six-Month Milestone Tracker

This is the detailed companion to the implementation roadmap in [Chapter 5](chapter-05-implementation.md). The chapter explains the _why_ and the general plan; this tracker is the tick-box version you print out and pin to the wall. Each milestone maps to the corresponding maturity expectations in [Chapter 6](chapter-06-practices.md).

### Month 1 - Foundation and Assessment

- [ ] Current state fully assessed and documented
- [ ] Implementation plan approved by leadership
- [ ] Team trained on framework basics
- [ ] Baseline metrics established
- [ ] Initial stakeholder communications completed

_Maturity target: practices at Level 1–2 (Initial/Reactive → Developing). See [Chapter 6](chapter-06-practices.md)._

### Month 2 - Daily Operations Foundation

- [ ] Daily operations cycle implemented
- [ ] Basic monitoring and alerting operational
- [ ] Incident response procedures defined
- [ ] Knowledge management system deployed
- [ ] Daily review meetings established

_Maturity target: incident & monitoring practices reaching Level 2 (Developing)._

### Month 3 - Weekly Improvement Integration

- [ ] Weekly improvement cycle integrated
- [ ] First improvement projects completed
- [ ] Cross-training program initiated
- [ ] Improvement effectiveness measurement active
- [ ] Team showing adoption of new practices

_Maturity target: core practices at Level 2–3 (Developing → Defined)._

### Month 4 - Strategic Integration

- [ ] Monthly strategy cycle introduced
- [ ] All cycles running in parallel
- [ ] Advanced automation capabilities deployed
- [ ] Strategic planning processes established
- [ ] Stakeholder satisfaction improving

_Maturity target: most practices at Level 3 (Defined)._

### Month 5 - Advanced Capabilities

- [ ] Advanced capabilities operational
- [ ] Predictive analytics providing value
- [ ] Team expertise development visible
- [ ] Process optimization showing results
- [ ] Cultural transformation evident

_Maturity target: leading practices reaching Level 4 (Managed/Measured)._

### Month 6 - Full Framework Adoption

- [ ] Full framework adoption achieved
- [ ] Business value clearly demonstrated
- [ ] Team autonomy and expertise established
- [ ] Continuous improvement culture embedded
- [ ] Framework ready for scaling or replication

_Maturity target: practices stabilising at Level 4 with a credible path to Level 5 (Optimizing)._

---

## 🔬 Appendix C: Post-Incident Review (Post-Mortem) Template

Use this after any incident worth learning from. The first rule, repeated until it sticks: **this document is blameless.** It examines systems and decisions made with the information available at the time - never the character of the human who clicked the button. (For the philosophy behind that, see [Chapter 6](chapter-06-practices.md).)

```text
POST-INCIDENT REVIEW

Title:               <short, human-readable summary>
Incident ID:         <tracker reference>
Severity:            <SEV1 / SEV2 / SEV3>
Date of incident:    <YYYY-MM-DD>
Authors:             <names>
Status:              <Draft / In review / Final>

1. SUMMARY
   Two or three sentences a non-engineer could understand. What broke,
   who was affected, for how long.

2. IMPACT
   - Users/customers affected:
   - Duration (detection → full recovery):
   - SLO/error-budget impact:
   - Revenue / contractual / reputational impact:

3. TIMELINE (in the team's timezone, 24h clock)
   HH:MM  Event (detection, escalation, key decisions, mitigation, recovery)
   ...

4. ROOT CAUSE(S)
   The contributing factors - usually plural. Use "5 Whys" or a causal
   chain. Resist the urge to stop at the first technical trigger.

5. DETECTION
   - How did we find out? (alert / customer report / luck)
   - Time to detect:
   - Could we have detected it sooner?

6. RESPONSE
   - What went well:
   - What was difficult or slowed us down:
   - Were the right people reachable?

7. ACTION ITEMS
   | # | Action | Type (prevent/detect/mitigate) | Owner | Due | Ticket |
   |---|--------|--------------------------------|-------|-----|--------|
   |   |        |                                |       |     |        |
   (Every action item has a single owner and a date, or it is not an action item.)

8. LESSONS LEARNED
   - What we got lucky on:
   - What we want to remember:
```

---

## 🎟️ Appendix D: Incident Commander Checklist

A pocket card for whoever is holding the wheel during a major incident. The Incident Commander's job is to **coordinate, not to fix** - the moment the IC's head is buried in a terminal, nobody is flying the plane. (Roles are defined in the Incident Command System section of [Chapter 6](chapter-06-practices.md).)

**On taking command:**

- [ ] Declare yourself IC out loud / in the incident channel ("I am IC for this incident")
- [ ] Confirm the severity level and adjust as facts change
- [ ] Open the incident channel / bridge and pin the key facts
- [ ] Assign a Scribe (someone who is _not_ also debugging)
- [ ] Assign a Communications Lead for stakeholder/customer updates
- [ ] Identify the Technical Lead(s) actually working the problem

**During the incident:**

- [ ] Keep a running summary updated: current status, what we're trying, next checkpoint time
- [ ] Set and announce the next update time (e.g., "next update in 15 minutes")
- [ ] Protect responders from interruptions and status-chasers
- [ ] Make the call on risky mitigations - document who decided and why
- [ ] Escalate / pull in additional help early rather than late
- [ ] Watch for responder fatigue; rotate people on long incidents

**On recovery:**

- [ ] Confirm full recovery with the Technical Lead (not just "the graph looks better")
- [ ] Announce all-clear and stand down the response
- [ ] Schedule the post-incident review (Appendix C) while memories are fresh
- [ ] Ensure the timeline and decisions were captured by the Scribe

---

## 📝 Appendix E: Change Control Form

For any change significant enough that "we'll just remember what we did" is a lie. Routine, pre-approved standard changes don't need this; normal and high-risk changes do.

```text
CHANGE REQUEST

Change ID:           <tracker reference>
Title:               <short description>
Requested by:        <name>           Date raised: <YYYY-MM-DD>
Change type:         [ ] Standard (pre-approved)  [ ] Normal  [ ] Emergency
Risk level:          [ ] Low  [ ] Medium  [ ] High

DESCRIPTION
  What is changing and why (the business or operational reason):

SYSTEMS / SERVICES AFFECTED
  - Primary:
  - Downstream dependencies:

IMPLEMENTATION PLAN
  Step-by-step actions, including who does what:

VALIDATION PLAN
  How we will confirm the change worked:

ROLLBACK PLAN
  Exact steps to undo this change, and the point of no return:
  Estimated rollback time:

SCHEDULING
  Proposed window:                 Expected duration:
  Maintenance/notification needed? [ ] Yes  [ ] No

APPROVALS
  | Role | Name | Decision (approve/reject) | Date |
  |------|------|---------------------------|------|
  | Change owner          |  |  |  |
  | Technical reviewer    |  |  |  |
  | Service/business owner|  |  |  |

POST-IMPLEMENTATION
  Outcome:        [ ] Success  [ ] Success with issues  [ ] Rolled back
  Notes / follow-up actions:
```

> A change without a rollback plan isn't a change - it's a bet. Write the rollback plan first; if you can't, that tells you something important about the risk.

---

## 📑 Appendix F: Service Level Agreement (SLA) Template

A starting skeleton for an SLA between an operations team and the business or an external customer. Keep the targets _achievable_ - an SLA you routinely miss is worse than an honest, lower number you can defend. The relationship between SLA, SLO, and SLI is explained in [Chapter 7](chapter-07-metrics.md).

```text
SERVICE LEVEL AGREEMENT

Service name:        <service this SLA covers>
Provider:            <team>
Consumer:            <business unit / customer>
Effective date:      <YYYY-MM-DD>     Review cadence: <e.g., every 6 months>

1. SERVICE DESCRIPTION
   What the service does and what is explicitly OUT of scope.

2. SERVICE HOURS
   - Supported hours (e.g., 24/7, or Mon–Fri 08:00–18:00):
   - Planned maintenance windows (excluded from availability calc):

3. AVAILABILITY TARGET (SLA)
   - Target: <e.g., 99.9% monthly>
   - Measurement method (the SLI): <how uptime is actually measured>
   - Exclusions: <planned maintenance, force majeure, consumer-side faults>

4. PERFORMANCE TARGETS
   - <e.g., p95 latency < 300 ms>
   - <e.g., batch job completes by 06:00>

5. SUPPORT & RESPONSE TARGETS
   | Severity | Definition | Response target | Resolution target |
   |----------|-----------|-----------------|-------------------|
   | SEV1     |           |                 |                   |
   | SEV2     |           |                 |                   |
   | SEV3     |           |                 |                   |

6. REPORTING
   - What is reported, how often, and to whom:

7. REMEDIES / CONSEQUENCES
   - What happens if targets are missed (service credits, review, escalation):

8. RESPONSIBILITIES OF THE CONSUMER
   - What the consumer must do for the SLA to hold (e.g., supported clients,
     change notice, valid contact details):

9. SIGN-OFF
   | Role | Name | Signature | Date |
   |------|------|-----------|------|
```

---

## 🧪 Completed Example Artifacts

Blank templates are useful, but examples help teams understand the expected level of detail. Add completed examples over time for:

| Artifact             | Example scenario                                         | Why it helps                                                   |
| -------------------- | -------------------------------------------------------- | -------------------------------------------------------------- |
| Post-incident review | Failed database failover during business hours           | Shows blameless analysis and action tracking                   |
| Change control form  | Firewall rule change for production service              | Shows risk classification and rollback planning                |
| SLA template         | Internal identity service                                | Shows how service levels connect to support expectations       |
| On-call policy       | Small platform team with business-hours primary coverage | Shows sustainable rotation boundaries                          |
| Reporting template   | Monthly operations review                                | Shows service health, toil, risk, and improvements in one view |

Completed examples should be realistic but fictional. Avoid customer names, production IPs, or tool-specific screenshots that age quickly.

## 🔗 Where to Go Next

These templates are deliberately generic so they survive contact with your reality. As your team matures, fold your hard-won specifics back into them - the best version of every template in this book is the one your team has already broken and rebuilt twice.

All templates live in the [`templates/`](https://github.com/g3rhard/sysops-framework/tree/main/templates) directory. Copy what you need, adapt, and version-control alongside your operational docs.

For the reasoning behind each artifact, follow the cross-references back into the chapters. For terminology, see the [Glossary](glossary.md). For how cycles, practices, and metrics interconnect, see the [Framework Data Relationships](data-relationships.md) page.
