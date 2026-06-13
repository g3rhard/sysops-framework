---
title: "Chapter 7: Metrics & Measurement"
linkTitle: "Chapter 07: Metrics"
weight: 700
description: >
  "What gets measured gets managed, but what gets measured wrong gets mismanaged."
---

## 🎯 Learning Objectives

By the end of this chapter, you will understand:

- The four categories of SysOps Framework metrics
- How to design effective dashboards for different audiences
- Key performance indicators that align with operational goals
- How to measure framework implementation success

> **Principles in play.** Metrics are how _Service Reliability First_ stops being a slogan and becomes a number, and how _Risk Management_ ([Chapter 2](chapter-02-principles.md)) turns into something you can see coming rather than explain afterward.

## 📊 The SysOps Metrics Framework

![SysOps Metrics Dashboard](../assets/sysops-dashboard.png)

Traditional agile metrics like velocity and story points don't capture the value that operations teams provide. The SysOps Framework requires different metrics that reflect operational realities and demonstrate business value. Our metrics framework organizes measurements into four key categories, each serving different stakeholders and decision-making needs.

A warning before you build a single dashboard: a metric is a streetlight, not the street. The moment a number becomes a target, people optimize the number — sometimes at the expense of the thing it was supposed to represent. Measure MTTR badly and you'll teach your team to close incidents fast and fix them never. Reward "tickets closed" and watch one real problem get split into nine tickets. Every metric in this chapter comes with the same unwritten footnote: _measure it because it helps you decide something, not because it looks good on a slide._

### Who Needs Which Metric

Not every metric is for every person. Each role in the team cares about a different slice:

| Role | Primary Categories | What They Act On | When They Look |
|---|---|---|---|
| **On-Call Engineer** | Service Reliability, Operational Efficiency | Active alerts, error budget burn rate, incident status | Real-time / during shift |
| **Team Lead / Ops Manager** | Operational Efficiency, Team Performance | Change success rate, MTTR trends, cross-training coverage, tool effectiveness | Daily standup, weekly review |
| **Platform / Infra Manager** | Service Reliability, Business Value | SLO compliance, capacity utilization, cost per service unit, FinOps metrics | Weekly cycle, monthly report |
| **Executive Sponsor** | Business Value, Service Reliability (summary) | Availability trends, cost efficiency, risk mitigation, strategic initiative progress | Monthly review, quarterly business review |

These aren't hard boundaries — an on-call engineer might look at cost anomalies when debugging, and an executive sponsor might care about a specific incident's MTTR. But the table tells you what _default view_ each role needs on their dashboard. Build for that first; add secondary views later.

> **Rule of thumb.** If you can't name the person who will act on a metric within 24 hours of it turning red, that metric is noise. Remove it.

## 🛡️ Service Reliability Metrics

> **Linked practices ([Chapter 6](chapter-06-practices.md)):** these metrics are the scoreboard for _Service Level Management_ (Practice 1), _Incident and Problem Management_ (Practice 2), and _Backup & Recovery Operations_ (Practice 12). If a number here is unhealthy, the corresponding practice is where you go to fix it.

### Primary Indicators

| Metric | Definition | Target Range | Measurement | Business Value |
| ------ | ---------- | ------------ | ----------- | -------------- |
| Uptime and Availability | Percentage of time services are operational and accessible | 99.9%+ for critical services, 99.5%+ for important services | Automated monitoring with synthetic transactions | Direct correlation to revenue and customer satisfaction |
| Mean Time to Recovery (MTTR) | Average time from incident detection to service restoration | <30 min for critical services, <2 hr for standard services | Incident tracking from alert to resolution confirmation | Minimizes business impact of service disruptions |
| Mean Time Between Failures (MTBF) | Average operational time between service failures | >720 hours for critical systems | Time tracking between incident occurrences | Indicates system stability and reliability investment effectiveness |
| SLO Compliance ([Google SRE Book — Ch. 4](https://sre.google/sre-book/service-level-objectives/)) | Percentage of time meeting defined service level targets | 95%+ compliance across all defined SLOs | Automated calculation based on SLI data | Demonstrates commitment to service quality standards |
| Error Budget Burn Rate | Rate at which reliability budget is being consumed | <50% of monthly budget consumed | Real-time tracking of error budget consumption | Balances reliability with innovation and change velocity |

### Implementation Example

**Service**: Customer Payment Processing System

```yaml
SLOs:
  availability:
    target: 99.95%
    measurement_window: monthly
    current: 99.97%
  latency:
    target: 95th percentile < 500ms
    measurement_window: daily
    current: 320ms
  error_rate:
    target: < 0.1%
    measurement_window: hourly
    current: 0.03%

Error Budget:
  monthly_allowance: 22_minutes
  consumed_this_month: 8_minutes
  remaining: 14_minutes
  burn_rate: healthy
```

> **Audience**: On-call engineers watch burn rate and MTTR in real time. Team leads review SLO attainment weekly. Executives see only the monthly summary — unless a service is burning its error budget faster than planned, in which case everyone sees it.

## ⚡ Operational Efficiency Metrics

> **Linked practices ([Chapter 6](chapter-06-practices.md)):** these track the health of _Change and Configuration Management_ (Practice 3), _Capacity and Performance Management_ (Practice 4), _Release Management_ (Practice 8), and _Service Request Management_ (Practice 10).

### Automation and Process Metrics

| Metric | Definition | Target Range | Measurement | Business Value |
| ------ | ---------- | ------------ | ----------- | -------------- |
| Automation Coverage | Percentage of routine tasks performed automatically | 70%+ of repetitive tasks automated | Task inventory with automation status tracking | Reduces manual effort and increases consistency |
| Incident Response Time | Time from alert generation to initial human response | <15 min for critical alerts, <60 min for warnings | Timestamp analysis from monitoring to acknowledgment | Demonstrates operational readiness and responsiveness |
| Change Success Rate | Percentage of changes implemented without causing incidents | 95%+ success rate for normal changes | Change tracking with incident correlation analysis | Shows process maturity and risk management effectiveness |
| Capacity Utilization | Optimal resource usage without performance degradation | 60–80% utilization for most resources | Resource monitoring with performance correlation | Maximizes infrastructure investment while maintaining performance |
| Tool Effectiveness Score | Team satisfaction and productivity with operational tools | 8/10 average satisfaction score | Regular surveys and productivity analysis | Ensures tool investments support team effectiveness |

### 🎮 Interactive Exercise: Efficiency Optimization

**Scenario**: Your team currently handles 200 tasks per month. Analysis shows:

- 80 tasks are fully manual (40%)
- 60 tasks are partially automated (30%)
- 40 tasks are fully automated (20%)
- 20 tasks are ad-hoc/undefined (10%)

**Challenge Questions**:

1. What's your current automation coverage percentage?
2. Which task category should you prioritize for automation?
3. What would be a realistic 6-month automation target?
4. How would you measure the business value of automation improvements?

**Framework Approach**:

1. **Current Coverage**: 20% fully automated + 15% (half of partial) = 35%
2. **Priority**: Standardize ad-hoc tasks first, then automate high-frequency manual tasks
3. **Target**: 60% automation coverage (realistic 25% improvement)
4. **Value Measurement**: Time savings × hourly cost + error reduction + capacity for strategic work

> **Audience**: Team leads own these metrics — they're the operational health scorecard. Platform managers watch change success rate and capacity utilization as proxy measures for process maturity. On-call engineers contribute data but shouldn't need to track the aggregate numbers.

## 👥 Team Performance Metrics

> **Linked practices ([Chapter 6](chapter-06-practices.md)):** these measure the payoff from _Knowledge and Documentation Management_ (Practice 5) and _Team and Skill Development_ (Practice 6) — the practices that decide whether your team is resilient or just a bus-factor of one.

### Knowledge and Capability Indicators

| Metric | Definition | Target Range | Measurement | Business Value |
| ------ | ---------- | ------------ | ----------- | -------------- |
| Knowledge Transfer Rate | Effectiveness of knowledge sharing and documentation practices | 90%+ of critical knowledge documented and accessible | Knowledge audits and accessibility testing | Reduces single points of failure and improves team resilience |
| Cross-Training Completion | Percentage of team members trained on multiple critical systems | 80%+ of team cross-trained on critical systems | Skills matrix tracking and competency assessments | Improves team flexibility and reduces knowledge silos |
| On-Call Rotation Health | Sustainability and fairness of on-call responsibilities | "Green" status with balanced load distribution | Rotation analysis, workload distribution, team feedback | Maintains team morale and prevents burnout |
| Problem Resolution Time | Average time to resolve complex problems (not incidents) | <2 hr for standard problems, <8 hr for complex issues | Problem tracking from identification to permanent resolution | Demonstrates team capability and process maturity |
| Documentation Coverage | Percentage of systems and processes with current documentation | 85%+ coverage with quarterly update verification | Documentation inventory with currency tracking | Enables effective knowledge transfer and faster onboarding |

### Team Health Assessment

**Monthly Team Health Indicators**:

- Workload balance and stress levels
- Skill development progress and satisfaction
- Collaboration effectiveness and communication
- Innovation time and continuous improvement engagement
- Career development and growth opportunities

> **Audience**: Team leads review cross-training coverage and skill development monthly. Managers watch documentation coverage and problem resolution time as indicators of team maturity. Individual team members see only their own development progress — comparing cross-training stats across the team undermines the practice.

## 💰 Business Value Metrics

> **Linked practices ([Chapter 6](chapter-06-practices.md)):** these connect operations to the balance sheet, drawing on _Vendor and Contract Management_ (Practice 7), _Asset Management_ (Practice 9), and _Financial Management_ (Practice 11). The FinOps metrics below are the operational expression of Practice 11.

### Strategic Impact Measurements

| Metric | Definition | Target Range | Measurement | Business Value |
| ------ | ---------- | ------------ | ----------- | -------------- |
| Customer Satisfaction Score | Internal customer satisfaction with IT services and support | 4.5/5 average satisfaction rating | Regular surveys and feedback collection | Demonstrates service quality and stakeholder alignment |
| Business Service Availability | Uptime of business-critical services during business hours | 99.5%+ availability during business hours | Business-hour focused availability tracking | Direct impact on business operations and revenue |
| Cost Per Service Unit | Total cost of operations divided by service units delivered | Decreasing trend year-over-year | Financial analysis with service volume correlation | Demonstrates operational efficiency and cost optimization |

### FinOps (Financial Operations) Metrics ([FinOps Foundation](https://www.finops.org/introduction/what-is-finops/))

| Metric | Definition | Target Range | Measurement | Business Value |
| ------ | ---------- | ------------ | ----------- | -------------- |
| Cloud Cost Allocation | Accurate attribution of cloud costs to services, teams, or departments | 100% allocation with <5% unallocated "shared" costs | Cloud billing analysis with tagging compliance tracking | Enables cost accountability and chargeback models |
| Cloud Waste Ratio | Percentage of cloud spending on idle or underutilized resources | <15% waste (industry average is 30%) | Instance utilization analysis, reserved instance coverage, storage audits | Direct opportunity for cost reduction |
| Unit Economics | Cost per key business metric (e.g., per transaction, per user, per GB processed) | Decreasing trend month-over-month | Cloud costs divided by application metrics | Demonstrates how cost relates to business outcomes |
| Reserved Instance and Commitment Coverage | Percentage of workloads using reserved capacity vs. on-demand pricing | 60%+ for predictable workloads, 20%+ for variable workloads | Commitment utilization tracking and forecast comparison | Demonstrates cost optimization through commitment planning |
| Right-Sizing Efficiency | Percentage of instances operating within optimal sizing parameters | 85%+ of instances properly sized (not over- or under-provisioned) | CPU/memory utilization analysis with instance type cost efficiency | Identifies quick wins for cost reduction |
| Cost Anomaly Detection | Ability to identify unusual spending patterns quickly | Detect anomalies within 24–48 hours of occurrence | Automated cost trending and deviation analysis | Prevents runaway costs and identifies infrastructure issues |

#### Example: Cloud Cost Management Dashboard

```yaml
Cloud Cost Metrics:
  Monthly_Spend: $50,000 (↑ 2% from last month)
  Projected_Annual: $600,000
  Cost_per_Transaction: $0.0025 (↓ 0.0003 from last month)

  FinOps_Metrics:
    Waste_Ratio: 12% ($6,000 monthly opportunity)
    Reserved_Instance_Coverage: 65%
    Unallocated_Costs: 3.5%
    Right_Sizing_Efficiency: 87%

  Optimization_Opportunities:
    Idle_Instances: $2,100/month
    Oversized_Instances: $1,800/month
    Unused_Storage: $950/month
    Commitment_Gaps: $1,150/month
```

> **Audience**: Platform managers and FinOps practitioners track cost allocation and waste ratio weekly. Executives see the unit economics trend and budget variance monthly — not the raw numbers. Showing an executive a dashboard full of FinOps line items is how you get eye contact with their coffee mug. Show them cost per transaction and whether it's going down.

---

| Metric | Definition | Target Range | Measurement | Business Value |
| ------ | ---------- | ------------ | ----------- | -------------- |
| Innovation Time Percentage | Time spent on improvements and innovation vs. maintenance | 20%+ of time dedicated to improvements and innovation | Time tracking with activity categorization | Shows focus on continuous improvement and strategic value |
| Risk Mitigation Effectiveness | Success rate in identifying and preventing operational risks | "High" effectiveness with proactive issue prevention | Risk assessment tracking with outcome analysis | Demonstrates proactive management and business protection |

## 📈 Dashboard Design and Implementation

> **Reality check.** A dashboard nobody opens is just an expensive screensaver. Before adding a metric, ask who will act on it and what decision it changes — if the honest answer is "it's nice to see," it belongs in a report, not on the wall. The best operational dashboards are slightly boring and frequently glanced at; the worst are beautiful, comprehensive, and ignored.

### Multi-Level Dashboard Strategy

#### Executive Dashboard (Strategic View)

**Update Frequency**: Monthly

**Key Metrics**:

- Overall service availability trends
- Business impact of IT services
- Cost efficiency and optimization
- Strategic initiative progress
- Risk mitigation summary

**Example Layout**:

```yaml
Executive Dashboard:
  Service Health: 99.7% (↑ 0.2% from last month)
  Business Impact: $12K revenue protected through uptime
  Cost Efficiency: 8% reduction in cost per service unit
  Strategic Projects: 3/4 on track, 1 delayed
  Risk Status: 2 high risks mitigated, 1 medium under review
```

#### Management Dashboard (Tactical View)

**Update Frequency**: Weekly

**Key Metrics**:

- Service level objective compliance
- Incident trends and resolution effectiveness
- Team performance and capacity
- Process improvement progress
- Resource utilization optimization

#### Operational Dashboard (Real-Time View)

**Update Frequency**: Real-time

**Key Metrics**:

- Current service status and alerts
- Active incidents and response progress
- System performance and capacity
- On-call status and escalation queues
- Change implementation status

### Dashboard Implementation Guidelines

**Design Principles**:

- **Clarity**: Information should be immediately understandable
- **Relevance**: Show metrics that matter to the specific audience
- **Actionability**: Enable quick decision-making and response
- **Context**: Provide historical trends and comparative data
- **Accessibility**: Available on multiple devices and platforms

**Technical Requirements**:

- Real-time data integration from multiple sources
- Automated alerting for threshold violations
- Historical data retention and trending analysis
- Role-based access and customization options
- Mobile-friendly responsive design

### KPI Specification Template

Before you add a single metric to any dashboard, write its specification. This template forces you to answer the hard questions upfront — so you don't discover six months later that nobody knows what "green" means or who was supposed to fix a red number.

```yaml
metric_name: "<human-readable name>"
category: "<one of: service_reliability, operational_efficiency, team_performance, business_value>"
definition: "<precise formula or measurement method>"
unit: "<ms, %, count, $, ratio>"

owner:
  role: "<on-call_engineer | team_lead | platform_manager | executive_sponsor>"
  review_cadence: "<daily | weekly | monthly | quarterly>"

thresholds:
  green: "<healthy range or condition>"
  amber: "<warning range — investigate soon>"
  red: "<breach — immediate action required>"
  action_on_red: "<what happens when red: page, create ticket, escalate>"

data_source: "<which tool or system provides this metric>"
measurement_window: "<rolling_hour | rolling_day | calendar_month | trailing_28d>"

gaming_risk: "<how someone could cheat this metric>"
mitigation: "<how to detect or prevent the gaming>"
```

**Example — filled template**:

```yaml
metric_name: "Error Budget Burn Rate"
category: "service_reliability"
definition: "(error budget consumed this month) / (total monthly error budget)"
unit: "%"

owner:
  role: "on-call_engineer"
  review_cadence: "daily"

thresholds:
  green: "< 50% consumed"
  amber: "50–80% consumed"
  red: "> 80% consumed — freeze feature deployments until next month"
  action_on_red: "Slack alert to #release-coordination; change approval requires director sign-off"

data_source: "Prometheus SLO recording rules + Grafana dashboard"
measurement_window: "calendar_month"

gaming_risk: "Artificially inflate error budget by extending the SLO target (e.g., 99.9% → 99.0% makes more budget)"
mitigation: "SLO targets locked behind change management; quarterly SLO review requires team lead approval"
```

Apply this template to every metric on your dashboard. The `gaming_risk` field is the most important — if you can't think of how someone might game it, you haven't thought hard enough.

## 🔄 Continuous Improvement Through Metrics

### Metrics-Driven Improvement Process

**1. Baseline Establishment**

- Document current performance levels across all metric categories
- Identify areas of strength and improvement opportunities
- Set realistic but challenging improvement targets
- Establish measurement methodologies and data collection processes

**2. Regular Review Cycles**

- Daily: Operational metrics review and incident response
- Weekly: Process effectiveness and team performance analysis
- Monthly: Strategic metrics evaluation and trend analysis
- Quarterly: Comprehensive metrics review and target adjustment

**3. Improvement Planning**

- Use metrics data to prioritize improvement initiatives
- Connect improvement efforts to business value demonstration
- Track improvement implementation effectiveness
- Adjust targets based on capability maturity and business needs

**4. Stakeholder Communication**

- Translate technical metrics into business language
- Provide regular updates on performance and improvement trends
- Demonstrate value delivery through metric improvements
- Build confidence through consistent performance reporting

## 🎯 Measuring Framework Implementation Success

### Implementation Maturity Indicators

**Month 1-2: Foundation Metrics**

- Baseline establishment completion: 100%
- Team training and buy-in: >90% participation
- Initial dashboard deployment: Basic operational view
- Stakeholder communication: Regular update cadence established

**Month 3-4: Process Integration Metrics**

- Operational cycle adherence: >80% consistency
- Incident response improvement: 20% reduction in MTTR
- Documentation coverage increase: +15% from baseline
- Team satisfaction with new processes: >7/10

**Month 5-6: Value Demonstration Metrics**

- Service reliability improvement: Measurable SLO improvements
- Operational efficiency gains: >25% automation coverage increase
- Team capability development: Cross-training targets met
- Business stakeholder satisfaction: >4/5 rating improvement

### Long-Term Success Indicators

**Year 1 Targets**:

- Sustained service reliability improvements
- Demonstrable cost efficiency gains
- Team expertise and satisfaction growth
- Framework adoption becoming organizational standard

**Ongoing Evolution**:

- Continuous metric refinement and improvement
- Integration with broader organizational metrics
- Influence on other team methodology adoption
- Innovation and best practice sharing

## 🛠️ Tools and Technologies for Metrics

### Monitoring and Data Collection

- **Infrastructure Monitoring**: Prometheus, Grafana, Datadog, New Relic
- **Application Performance**: APM tools with business transaction monitoring
- **Synthetic Monitoring**: Uptime robots and user experience simulation
- **Log Aggregation**: ELK Stack, Splunk, Fluentd for centralized logging

### Dashboard and Visualization

- **Real-Time Dashboards**: Grafana, Tableau, Power BI for live visualization
- **Executive Reporting**: Automated report generation and distribution
- **Mobile Accessibility**: Responsive dashboards and mobile applications
- **Custom Visualizations**: Tailored charts and graphs for specific audiences

### Analytics and Intelligence

- **Predictive Analytics**: Machine learning for capacity and failure prediction
- **Trend Analysis**: Statistical analysis for performance trending
- **Correlation Analysis**: Identifying relationships between metrics and outcomes
- **Anomaly Detection**: Automated identification of unusual patterns

## 💡 Common Metrics Pitfalls and Solutions

### The Big Four

| Pitfall | How It Shows Up | Why It Happens | How to Fix It |
|---|---|---|---|
| **Vanity Metrics** | Dashboard looks great, nobody acts on it | Metric measures activity, not outcome | Before adding a metric, write down exactly what decision it will change and who makes it |
| **Metric Overload** | 47 metrics on one screen, all "important" | No clear owner per metric; fear of missing something | Max 7 metrics per dashboard. If you need more, you need more audiences, not more numbers |
| **Stale Baselines** | Comparing this month's performance against a pre-migration baseline from 18 months ago | Baselines set once and forgotten | Schedule baseline reviews alongside quarterly business reviews; update after any major infrastructure change |
| **Goodhart's Law** | MTTR drops to 8 minutes but incidents recur because nobody fixes root causes | Metric is optimized, the underlying outcome is not | Every metric needs a counter-metric (e.g., MTTR + recurrence rate). Balanced scorecards catch gaming |

### What Not to Measure

Some things look measurable but aren't worth the cost of collection, or actively cause harm when measured.

**Avoid measuring**:

- **Individual incident response time** — it teaches people to delay declaring an incident (the clock only starts when they acknowledge). Measure team-level MTTR instead.
- **Uptime percent to two decimal places for low-criticality systems** — 99.73% vs 99.74% for an internal wiki is noise. Binary (green/red) is enough for Tier 3 and below.
- **Number of runbooks written** — a terrible runbook that nobody uses counts as "written." Measure runbook usage and accuracy instead.
- **Hours worked / overtime** — this metric inevitably becomes a target, and the target is always "work more." Measure sustainable on-call load, not hours.
- **Velocity / story points** — these measure agile software delivery, not operations. They actively misrepresent ops work, where value is in prevention and stability, not feature output.

**What to measure instead**:

| Instead of | Measure |
|---|---|
| Uptime to 5 nines for everything | SLO attainment per criticality tier |
| Individual response time | Team MTTR + recurrence rate |
| Runbooks written | Runbook usage during incidents + accuracy score (post-incident review question: "did the runbook help?") |
| Hours worked | On-call health score (interruptions slept through, pages per shift, time to decompress) |

### How Metrics Can Be Gamed

Every metric worth tracking can be manipulated. The trick is knowing how so you can build safeguards.

**Common gaming patterns**:

1. **MTTR gaming**: Close the incident ticket without fixing the root cause. MTTR drops, but the same incident happens next week. *Defense:* Track recurrence rate alongside MTTR. Any incident that reoccurs within 30 days counts as a failure.

2. **SLO attainment gaming**: Set SLO targets so low they're never breached. 99.9% attainment on a 99.0% SLO is not an achievement. *Defense:* Lock SLO targets in change management. Require team lead approval to relax a target. Track SLO target hardening (are SLOs getting tighter over time?).

3. **Automation coverage gaming**: Count every tiny script as "automation" to inflate the percentage. *Defense:* Define "automation" as "eliminates a manual step that previously required a human decision." A cron job that existed before the metrics started doesn't count as new automation.

4. **Cost per service unit gaming**: Include only direct infrastructure costs and exclude the labor, support, and overhead that make up 60% of the real cost. *Defense:* Use total cost of ownership (TCO) as the denominator. If a cost can't be attributed, publish it as "unattributed" rather than hiding it.

5. **Ticket closure gaming**: Split a single problem into five tickets to show five "resolved" items. *Defense:* Require problem-to-ticket linkage. If five tickets share the same root cause, they count as one.

> **Litmus test.** Ask yourself: "If this metric was the only thing my bonus depended on, what would I do differently?" If the honest answer is something that makes the system worse, you need to redesign the metric — or add a counter-metric that catches the bad behavior.

## 🎯 Chapter Summary

Effective measurement is crucial for demonstrating the value of the SysOps Framework and driving continuous improvement. The four-category metrics approach ensures comprehensive coverage of service reliability, operational efficiency, team performance, and business value.

Success depends on choosing the right metrics for each audience, implementing effective dashboards and reporting, and using metrics data to drive decision-making and improvement efforts. The key is balancing comprehensive measurement with actionable insights that support both operational excellence and strategic business objectives.

## 🔮 Looking Ahead

In the next chapter, we'll explore the tools and technologies that support effective implementation of the SysOps Framework, including automation platforms, monitoring systems, and collaboration tools that enable the metrics and practices we've discussed.

## 💭 Reflection Questions

1. **Current Metrics**: What metrics does your team currently track, and how well do they align with the SysOps categories?
2. **Value Demonstration**: How could better metrics help you demonstrate your team's value to stakeholders?
3. **Improvement Focus**: Which metric category would provide the most immediate benefit for your team?

---

**🎮 Gamification Element - Chapter 7 Badge**
_Design a comprehensive metrics dashboard for your team including all four categories and earn the "Metrics Master" badge._

---

_[← Previous: Chapter 6 - Management Practices](chapter-06-practices.md) | [Next: Chapter 8 - Tools & Technology →](chapter-08-tools.md)_
