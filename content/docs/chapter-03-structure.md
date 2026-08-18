---
title: "Chapter 3: Framework Structure"
linkTitle: "Chapter 03: Structure"
weight: 300
description: >
  "Operations teams don't need sprints; they need cycles that match the rhythm of their work."
---

> **Principles in play.** The multi-cycle structure exists to honor three principles from [Chapter 2](chapter-02-principles.md) at once: _Continuous Availability_ (the daily cycle never stops), _Rapid Response_ (interrupts are designed in, not apologized for), and _Automation and Efficiency_ (the weekly cycle is where toil goes to die).

## The Multi-Cycle Approach

Traditional agile frameworks use a single cycle (sprint) to organize all work. This creates artificial constraints for operations teams who handle different types of work with different time horizons and urgency levels. The SysOps Framework uses three interconnected cycles that run simultaneously:

| Cycle                    | Cadence     | Focus                                      |
| ------------------------ | ----------- | ------------------------------------------ |
| Daily Operations Cycle   | 24–48 hours | Immediate operational needs                |
| Weekly Improvement Cycle | 7 days      | Process improvements and systematic issues |
| Monthly Strategy Cycle   | 4 weeks     | Strategic initiatives and major projects   |

> **Diagram:** Daily work produces patterns for weekly improvement; weekly evidence informs monthly strategy; monthly priorities and capacity decisions flow back into daily operations.

![Three-cycle operating model showing cadence, ownership, phases, outcomes, and feedback](../../assets/sysops-framework-diagram.png)

This multi-cycle approach acknowledges that operations teams simultaneously:

- Respond to immediate issues (daily)
- Improve systems and processes (weekly)
- Plan and execute strategic changes (monthly)

Think of it less like a sprint and more like a hospital. The emergency room (daily) never closes and can't schedule its patients. The ward rounds (weekly) review what keeps coming through the door and adjust treatment. And the board (monthly) decides whether to build a new wing. Nobody sane asks the ER to stop accepting patients because it's "mid-sprint" — yet that is precisely what we ask of operations teams every time we hand them a single cadence and wish them luck.

### Cycle Ownership and Handoffs

| Cycle   | Primary Owner                          | Accountable For                                                                                      |
| ------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Daily   | On-call engineer (rotating)            | Keeping services running, incident response, shift handoff                                           |
| Weekly  | Team lead or rotating improvement lead | Delivering at least one verifiable improvement per week                                              |
| Monthly | Team lead or manager                   | Delivering at least one strategic initiative per month or a clear explanation of why it was deferred |

**Handoff rule**: No output from a faster cycle disappears into a slower one without explicit acceptance. If the daily cycle identifies a recurring pattern that merits a weekly improvement, the daily owner must write it up just well enough for the weekly owner to pick up. One paragraph, one link to the incident log. Done is better than perfect.

## Work Intake and Triage

Before any of the three cycles can run smoothly, work has to get into the right one. This section names what typically arrives, how it gets routed, and who is allowed to say "actually, that's not what this is."

### A Taxonomy for What Arrives

| Work type            | What it is                                                                                       | Default cycle                                  | Full definition                                   |
| -------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------- | ------------------------------------------------- |
| **Incident**         | Unplanned disruption or degradation to a live service                                            | Daily                                          | [Chapter 6, Practice 2](chapter-06-practices.md)  |
| **Service request**  | Pre-approved, catalog-eligible ask (access, provisioning, standard support)                      | Daily (fulfillment queue)                      | [Chapter 6, Practice 10](chapter-06-practices.md) |
| **Standard change**  | Pre-approved, low-risk, repeatable change                                                        | Daily                                          | [Chapter 6, Practice 3](chapter-06-practices.md)  |
| **Normal change**    | Medium-risk change requiring review and a scheduled window                                       | Weekly (Monthly if it needs multi-week design) | [Chapter 6, Practice 3](chapter-06-practices.md)  |
| **Emergency change** | Urgent change made to restore or protect a live service                                          | Daily                                          | [Chapter 6, Practice 3](chapter-06-practices.md)  |
| **Improvement work** | Automation, documentation, or process fixes that remove recurring toil                           | Weekly                                         | This chapter                                      |
| **Strategic work**   | Multi-week initiatives: architecture, capacity, tooling, major migrations                        | Monthly                                        | This chapter                                      |
| **Interruption**     | Anything ad hoc that hasn't been classified yet — a ping, a hallway question, an unscheduled ask | Daily (triage first)                           | See "In-Flight and Unclassified Work" below       |

> Chapter 6 owns the long-form definitions and maturity model for each practice. This chapter only answers one question for each type: which cycle does it belong to, right now? For incidents specifically, Chapter 6's [Incident Severity Classification](chapter-06-practices.md) (SEV1-SEV4) is the one severity vocabulary used everywhere in the framework — triage records here should carry that same SEV1-SEV4 rating rather than inventing a second scale.

### Routing: Which Cycle Does This Go To?

Ask, in order, and stop at the first "yes":

1. **Is a live service down, degraded, or at risk right now, or does it need to happen today regardless of type** (incident, emergency change, urgent service request)? → Daily queue.
2. **Can it be scoped, executed, and measured inside roughly one week without an architecture decision or multi-team coordination** (standard/normal change, automation, doc fix)? → Weekly queue.
3. **Does it span multiple weeks, require capacity/architecture decisions, or touch more than one team** (major migration, new platform, disaster-recovery build-out)? → Monthly queue.
4. **None of the above are obviously true yet?** → Daily intake queue by default, reclassify within one daily cycle (see below).

Interruptions are not a fourth cycle — they are unclassified work that must resolve to one of the three above before the current cycle's owner treats it as committed.

### Who Classifies, Who Owns the Queue

Classification authority follows the same ownership as the cycles themselves (see [Cycle Ownership and Handoffs](#cycle-ownership-and-handoffs) above):

| Queue   | Owner                                  | First classification                                       | Reclassification                                                   |
| ------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------ |
| Daily   | On-call engineer (rotating)            | Whoever receives the item first (on-call, helpdesk, alert) | Any team member can propose; the daily owner or team lead confirms |
| Weekly  | Team lead or rotating improvement lead | Weekly owner, during Plan                                  | Team lead                                                          |
| Monthly | Team lead or manager                   | Monthly owner, during Assess                               | Team lead or manager                                               |

Anyone can flag a misclassified item. Only the owner of the queue an item is moving into can accept it — the same handoff rule above applies to reclassification, not just to normal cycle-to-cycle flow.

### In-Flight and Unclassified Work

- Every item is classified within one daily cycle of arriving. If nobody has looked at it by the next daily review, it escalates to the team lead — being unclassified for more than a day is itself a signal something is broken.
- Work already in flight when new information arrives (for example, a normal change turns out to need emergency treatment) is not silently reassigned. The current owner logs a one-line handoff note and the receiving owner explicitly accepts before priority shifts.
- Nothing sits in a generic "misc" backlog. If it doesn't fit the taxonomy above, that gap is escalated to the team lead as a taxonomy problem, not parked indefinitely.

### WIP: Scale the Limit, Not the Rule

Don't copy a fixed number like "three items per queue" from a book that has never met your team. Instead, size WIP to who is actually resourced to the queue this cycle:

- **Daily queue**: WIP is roughly the number of people on shift, minus whoever is needed to hold on-call coverage. A one-person daily rotation runs one thing at a time by definition; a five-person team can run several incidents or requests in parallel because different people own them.
- **Weekly queue**: WIP is roughly the number of people the team lead has actually freed from daily duty this week, not the whole roster. Most teams under ten people should default to one improvement item in flight per rotating improvement lead — running more than that in parallel usually means nobody has clear ownership.
- **Monthly queue**: WIP is roughly one strategic initiative in active implementation per month, regardless of team size, because sustained multi-week focus is the scarce resource. Larger teams (6-10+ people) may run two only if they have different leads and neither lead is also carrying on-call load that month.

The rule, not the number, is what scales: **WIP per queue is bounded by the people who can work it without abandoning daily coverage** — recount it every time team size or on-call load changes.

### Escalation and Reclassification

| Trigger                                                                                            | Action                                                                                 |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Service request breaches its SLA or reveals live service impact                                    | Reclassify to Incident, move to Daily queue, assign a SEV1-SEV4 severity per Chapter 6 |
| Normal change is needed to stop an active incident                                                 | Reclassify to Emergency change, Daily queue, expedited approval                        |
| Weekly improvement grows beyond one week, needs an architecture decision, or spans teams           | Reclassify to Strategic work, Monthly queue                                            |
| Monthly initiative turns out to be a same-day fix once scoped                                      | Reclassify to Standard/Normal change or Improvement work, hand down a cycle            |
| Daily cycle consistently exceeds 80% capacity ([see below](#what-to-do-when-daily-work-dominates)) | Do not add new Weekly/Monthly commitments until it's addressed                         |

Reclassification is always logged: what changed, who accepted it, why. Not for process's own sake — "it got reclassified" is exactly the kind of thing a post-incident review needs to reconstruct later.

### Minimum Intake Fields

Whatever ticketing system or spreadsheet the team uses, capture at least:

1. **ID / reference** — ticket number or link
2. **Title** — one line
3. **Requester** — who raised it
4. **Date/time raised**
5. **Affected service or system**
6. **Initial type guess** — incident / service request / standard, normal, or emergency change / improvement / strategic / unclassified
7. **Severity (incidents)** — SEV1-SEV4 per Chapter 6's [Incident Severity Classification](chapter-06-practices.md); the canonical scale for every incident record, not a locally invented one. Non-incident items leave this blank or mark N/A.
8. **Impact note** — free-text detail beyond the severity rating (which service, which customers, what's actually broken); useful context for non-incident items too, but never a substitute for the SEV1-SEV4 field on an incident
9. **Confirmed classification and queue** — filled in at triage
10. **Owner** — the person or role accountable for the next step
11. **Status** — open / in progress / blocked / done
12. **Related items** — linked incident, change, or improvement record

> **Template:** a copy-ready intake and triage log covering these fields is provided in [`templates/work-intake-triage.md`](../../templates/work-intake-triage.md).

## Minimum Viable Adoption Modes

Do not start all three cycles on day one just to look mature. Match the adoption mode to the team’s current load.

| Mode                       | Use when                                                                        | What you run                                                      | What you explicitly postpone                                  |
| -------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------- |
| **Daily-only**             | Interrupt load consumes most capacity, incidents/support dominate, trust is low | Daily triage, incident visibility, basic documentation, one queue | Weekly improvement commitments and monthly strategy workshops |
| **Daily + Weekly**         | Daily work is visible and the team can protect 10–20% capacity                  | Daily response plus one weekly improvement target                 | Full strategic planning and broad practice rollout            |
| **Full three-cycle model** | Daily and weekly cycles are stable without constant rescue                      | Daily operations, weekly improvements, monthly strategy           | Nothing — but scope still stays limited by capacity           |

> **Adoption rule.** You do not earn maturity points for running more ceremonies. You earn them when the team can protect reliability, reduce toil, and explain trade-offs without hiding work.

### Entry Criteria by Team Context

| Team context                              | Recommended starting mode | First success signal                                          |
| ----------------------------------------- | ------------------------- | ------------------------------------------------------------- |
| 1–2 people, broad internal IT ownership   | Daily-only                | Work is visible and nothing critical is forgotten             |
| 3–5 person infrastructure / sysadmin team | Daily + Weekly            | At least one improvement ships every week or two              |
| 6–10 person platform/SRE team             | Full three-cycle model    | Daily interrupts no longer erase strategic work               |
| Regulated or audited environment          | Daily + Weekly, then full | Evidence is captured as work happens, not reconstructed later |

## Daily Operations Cycle (24-48 hours)

### Purpose

Handle immediate operational needs: system monitoring, incident response, routine maintenance, and urgent requests that cannot be deferred.

### The Cycle Flow: Monitor → Respond → Document → Review

#### 1. Monitor (Ongoing)

**Activities**:

- Continuous system monitoring and alerting
- Daily health checks and status reviews
- Early warning identification
- Trend analysis and pattern recognition

**Outputs**:

- System status dashboards
- Daily health reports
- Alert summaries and trends
- Early warning notifications

**Key Practices**:

- Automated monitoring with intelligent alerting
- Daily standalones (not standups) - brief status sharing
- Proactive monitoring that identifies issues before they become critical
- Clear escalation procedures for different alert types

> Yes, "standalones," not "standups" — and the distinction is deadly serious. A standup asks "what did you commit to and are you on track?" A standalone asks "is anything on fire, and does anyone need help?" One of those questions is useful to a person who spent last night babysitting a failing RAID array. The other invites them to apologize for it.

#### 2. Respond (As Needed)

**Activities**:

- Incident response and resolution
- Emergency fixes and patches
- Urgent stakeholder requests
- Critical maintenance activities

**Outputs**:

- Incident resolution
- System fixes and patches
- Stakeholder communication
- Service restoration

**Key Practices**:

- Pre-defined response procedures for common incidents
- Clear communication protocols during incidents
- Documented escalation paths
- Rapid resolution with safety guardrails

#### 3. Document (Immediate)

**Activities**:

- Incident documentation and post-mortems
- Change logging and configuration updates
- Knowledge base updates
- Lessons learned capture

**Outputs**:

- Incident reports and timelines
- Updated documentation and runbooks
- Change logs and configuration records
- Knowledge articles and troubleshooting guides

**Key Practices**:

- Automated documentation where possible
- Standardized incident report templates
- Real-time change tracking
- Searchable knowledge management systems

#### 4. Review (Daily)

**Activities**:

- Daily reflection on incidents and responses
- Identification of systemic issues
- Planning for next day's priorities
- Handoff preparation for shift changes

**Outputs**:

- Daily review summaries
- Issue escalation to weekly cycle
- Priority updates and adjustments
- Shift handoff documentation

**Key Practices**:

- Brief daily reviews (15-20 minutes maximum)
- Focus on patterns and systemic issues
- Clear handoff procedures
- Integration with weekly improvement planning

### Scenario: Daily Cycle Planning

**Scenario**: You're starting a Tuesday morning shift. Yesterday's handoff notes include:

- Database performance degradation (resolved, but needs monitoring)
- Scheduled maintenance window tonight (requires preparation)
- New application deployment pending (waiting for security approval)
- Monitoring alert false positives (need investigation)

**Exercise**: Plan your daily cycle activities:

1. **Monitor**: What should you watch carefully today?
2. **Respond**: What requires immediate action?
3. **Document**: What needs recording or updating?
4. **Review**: What patterns should you look for?

## Weekly Improvement Cycle (7 days)

### Purpose

Focus on process improvements, automation initiatives, and addressing systemic issues identified during daily operations that require more than immediate fixes.

> Automation is a primary driver of this cycle. For the underlying principle see [Chapter 2 — Automation and Efficiency](chapter-02-principles.md); for the tools deployed here (IaC, runbook automation, GitOps) see [Chapter 8](chapter-08-tools.md). This chapter focuses on _when_ automation work is planned and executed, not on re-explaining why or with which tools.

### The Cycle Flow: Plan → Execute → Measure → Improve

#### 1. Plan (Mondays or cycle start)

**Activities**:

- Review patterns and issues from daily operations
- Prioritize improvement opportunities
- Plan automation and process enhancement projects
- Allocate resources for improvement work

**Outputs**:

- Weekly improvement backlog
- Resource allocation plans
- Success criteria definitions
- Risk assessments for planned changes

**Key Practices**:

- Data-driven prioritization based on daily cycle insights
- Capacity allocation (typically 20-30% of team time)
- Risk assessment and mitigation planning

#### 2. Execute (Throughout the week)

**Activities**:

- Implement planned improvements
- Deploy automation tools and scripts
- Update processes and procedures
- Conduct training and knowledge sharing

**Outputs**:

- Improved processes and procedures
- Automation tools and scripts
- Updated documentation and training materials
- Enhanced monitoring and alerting

**Key Practices**:

- Small, incremental improvements over large projects
- Test improvements in safe environments first
- Maintain service availability during improvement work
- Document changes and their impacts

#### 3. Measure (Throughout and at end of week)

**Activities**:

- Track improvement effectiveness
- Measure impact on daily operations
- Collect feedback from team members
- Monitor system performance changes

**Outputs**:

- Improvement effectiveness metrics
- System performance comparisons
- Team feedback and satisfaction scores
- Identification of unintended consequences

**Key Practices**:

- Define measurable success criteria upfront
- Use before/after comparisons
- Collect both quantitative and qualitative feedback
- Monitor for negative impacts on other systems

#### 4. Improve (End of week)

**Activities**:

- Analyze improvement results
- Identify successful patterns and failed experiments
- Plan next week's improvement priorities
- Share learnings with other teams

**Outputs**:

- Improvement effectiveness analysis
- Lessons learned documentation
- Next week's improvement priorities
- Best practice sharing materials

**Key Practices**:

- Honest assessment of what worked and what didn't
- Celebration of successful improvements
- Planning for continuous improvement

### Example Weekly Improvements

- Automating manual server health checks
- Implementing new monitoring alerts for early problem detection
- Streamlining incident response procedures
- Creating or updating system documentation
- Cross-training team members on new technologies

## Monthly Strategy Cycle (4 weeks)

### Purpose

Handle larger projects, strategic initiatives, capacity planning, and technology evaluations that require sustained effort over multiple weeks.

### The Cycle Flow: Assess → Design → Implement → Evaluate

#### 1. Assess (Week 1)

**Activities**:

- Strategic planning and goal setting
- Technology evaluation and selection
- Capacity planning and resource assessment
- Risk analysis for major initiatives

**Outputs**:

- Strategic initiative roadmaps
- Technology evaluation reports
- Capacity planning analyses
- Risk assessment and mitigation plans

**Key Practices**:

- Alignment with business objectives
- Realistic resource allocation considering operational demands
- Stakeholder involvement and communication
- Clear success criteria and timelines

#### 2. Design (Week 2)

**Activities**:

- Detailed project planning and design
- Architecture and implementation planning
- Resource allocation and timeline development
- Communication and change management planning

**Outputs**:

- Detailed project plans and timelines
- Technical architecture and design documents
- Resource allocation and responsibility matrices
- Communication and training plans

**Key Practices**:

- Involve team members in design decisions
- Plan for operational continuity during implementation
- Consider integration with existing systems and processes
- Build in testing and rollback procedures

#### 3. Implement (Week 3)

**Activities**:

- Execute strategic projects and initiatives
- Deploy new technologies and systems
- Implement process changes and improvements
- Conduct training and knowledge transfer

**Outputs**:

- Implemented systems and technologies
- Process changes and improvements
- Training materials and documentation
- Project status reports and updates

**Key Practices**:

- Phased implementation with testing at each stage
- Continuous communication with stakeholders
- Monitoring for impacts on daily operations
- Documentation of changes and procedures

#### 4. Evaluate (Week 4)

**Activities**:

- Project evaluation and success measurement
- Lessons learned analysis and documentation
- Planning for next month's strategic initiatives
- Stakeholder feedback collection and analysis

**Outputs**:

- Project evaluation reports
- Lessons learned documentation
- Next month's strategic priorities
- Stakeholder feedback summaries

**Key Practices**:

- Honest evaluation of project success and failures
- Stakeholder communication about results and next steps
- Planning integration with ongoing operations

### Example Monthly Strategic Initiatives

- Major infrastructure upgrades or migrations
- Implementation of new monitoring or management platforms
- Disaster recovery planning and testing
- Security framework implementation
- Team skill development and certification programs

## How the Cycles Interact

The three cycles are designed to work together without conflict:

### Information Flow

- **Daily → Weekly**: Patterns and systemic issues identified in daily operations become improvement priorities
- **Weekly → Monthly**: Successful improvements inform strategic initiatives and technology choices
- **Monthly → Daily**: Strategic implementations create new monitoring needs and operational procedures

### Resource Allocation

| Cycle               | Planning Range | Notes                                |
| ------------------- | -------------- | ------------------------------------ |
| Daily Operations    | 60–70%         | Varies by team and environment       |
| Weekly Improvements | 20–30%         | The cycle where toil goes to die     |
| Monthly Strategy    | 10–20%         | Concentrated in implementation weeks |

> **These are ranges within one 100% pool, not three independent budgets.** The three ranges overlap on purpose — no team lands at the top of all three at once, because daily plus weekly plus monthly must add up to 100% of capacity, not up to 120%. Pick one point in each range that sums to 100% for your team: for example, 65% daily + 25% weekly + 10% monthly, or 70% daily + 20% weekly + 10% monthly. If daily work is running high, weekly and monthly have to come down to match; they are not separate pools someone can protect regardless of what daily is doing.

> **Reality check.** These percentages are a starting hypothesis, not a budget handed down from on high. If your daily operations are eating 90%, that's not a planning failure to paper over — it's the single most important number in this book telling you the team is underwater. Fix the drowning before you fret about hitting a tidy 20% improvement target.

### Sample Schedule: Small Ops Team (3-4 People)

| Time            | Mon                                          | Tue                            | Wed                                 | Thu                         | Fri                                                                                         |
| --------------- | -------------------------------------------- | ------------------------------ | ----------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------- |
| **Daily**       | Standalone (15min), review weekend incidents | Standalone, check alert health | Standalone, mid-week capacity check | Standalone, knowledge share | Standalone, weekly review prep                                                              |
| **On-call**     | Engineer A primary                           | Engineer A                     | Engineer B primary                  | Engineer B                  | Engineer A                                                                                  |
| **Improvement** | 2h — plan weekly improvement                 | —                              | 2h — execute improvement            | —                           | 1h — measure, document results                                                              |
| **Monthly**     | —                                            | —                              | —                                   | —                           | 1-2h — rotates across the 4-week cycle: Wk1 Assess, Wk2 Design, Wk3 Implement, Wk4 Evaluate |

**Key constraint**: With 3-4 people, the weekly improvement time is only 4-5 hours total. Pick one small improvement per week, not three. The Monthly Strategy Cycle is 4 weeks long, not 4 months — each week of the cycle maps to one phase (Assess → Design → Implement → Evaluate), and this Friday slot is where that week's phase gets its dedicated time.

### Sample Schedule: Platform/SRE Team (6-8 People)

| Time            | Mon                                           | Tue                         | Wed                            | Thu                         | Fri                                  |
| --------------- | --------------------------------------------- | --------------------------- | ------------------------------ | --------------------------- | ------------------------------------ |
| **Daily**       | Standalone (15min), rotate incident commander | Standalone, service review  | Standalone, error budget check | Standalone, knowledge share | Standalone, metrics review           |
| **On-call**     | Primary + secondary rotation (weekly swap)    |                             |                                |                             |                                      |
| **Improvement** | 4h — sprint-style improvement planning        | 2h — paired automation work | 4h — improvement execution     | 2h — paired work            | 2h — demo & retro                    |
| **Monthly**     | 2h — monthly initiative kickoff               | As needed                   | As needed                      | As needed                   | Monthly review + next month planning |

**Key advantage**: With 6+ people, a dedicated improvement lead can rotate weekly, and the team can run small paired sessions (automation, documentation, refactoring) without pulling everyone away from operational responsibilities.

### What to Do When Daily Work Dominates

If the daily cycle consistently consumes more than 80% of capacity:

1. Do not try to implement the weekly or monthly cycle yet. They will fail and create frustration.
2. Spend two weeks measuring _exactly_ what consumes the daily cycle — capture every interruption, its duration, and its source.
3. Identify the top three sources of daily work that are recurring, predictable, or automatable.
4. Negotiate with stakeholders for 10% protected improvement time. Show them the data: "These three things cost us X hours per week. With 4 hours of protected time, we can automate one of them this month."
5. Once daily work drops below 70%, introduce the weekly cycle. Once below 60%, introduce the monthly cycle.

This is not failure — it is honest capacity planning. The framework adapts to your reality, not the other way around.

### Priority Resolution

When cycles conflict (which should be rare with proper planning):

1. **Service-affecting issues**: Always take priority (Daily Operations)
2. **Improvement work**: Can be paused for significant operational needs
3. **Strategic projects**: Can be rescheduled if necessary

## Adapting Cycles to Your Environment

> **Note.** The cadences below are defaults, not commandments. The framework cares that you _have_ three distinct horizons of work, not that the daily cycle is exactly 24 hours. Adjust the numbers to your reality; keep the separation of concerns.

### High-Availability Environments

- Shorter daily cycles (12-24 hours) with more frequent reviews
- More frequent weekly cycles (every 3-5 days)
- Longer monthly cycles (6-8 weeks) to accommodate extensive testing

### Development-Heavy Environments

- Longer daily cycles (48-72 hours) to accommodate planned work
- Integration with development sprint cycles
- Quarterly strategic cycles aligned with product releases

### Small Teams

- Combined weekly/monthly cycles
- Longer cycle periods to accommodate capacity constraints
- More automation to reduce daily operational burden

### Large Organizations

- Multiple parallel cycles for different service areas
- Coordination mechanisms between cycle teams
- Standardized cycle templates and procedures

## Measuring Cycle Effectiveness

### Daily Operations Metrics

- Incident response time and resolution rate
- System availability and performance
- Alert accuracy and false positive rates
- Team sustainability and on-call health

### Weekly Improvement Metrics

- Number and impact of improvements implemented
- Process efficiency gains
- Automation coverage increases
- Team skill development progress

### Monthly Strategy Metrics

- Strategic project completion rate and success
- Technology evaluation and adoption effectiveness
- Capacity planning accuracy
- Stakeholder satisfaction with strategic initiatives

---

_[← Previous: Chapter 2 - Core Principles](chapter-02-principles.md) | [Next: Chapter 4 - Comparison →](chapter-04-comparison.md)_
