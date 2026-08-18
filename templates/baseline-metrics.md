# Baseline Metrics Template

> **Why this exists.** Chapter 7 — Metrics is clear that a stale or fabricated baseline is worse than no baseline at all — you cannot tell if the framework is working if you never honestly measured where you started. An honest "we don't know yet, here's our best estimate ± range" beats a precise-looking number nobody can defend. This is the artifact referenced as `baseline-metrics.csv` in Getting Started — Week 1, and compared against in Week 4.

## What to Measure

Log every incident, interrupt, and unit of planned work during the observation window. For each entry, record the **minimum fields** below — skip anything you can't fill in rather than guessing.

**Minimum fields (one row per event):**

| Field                   | Required | Notes                                                                                                                         |
| ----------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `date`                  | Yes      | `YYYY-MM-DD`                                                                                                                  |
| `time_detected`         | If known | 24h clock; leave blank if the team doesn't track this yet                                                                     |
| `time_resolved`         | If known | 24h clock; leave blank rather than estimate a fake number                                                                     |
| `category`              | Yes      | `incident`, `interrupt`, `planned_change`, `improvement`                                                                      |
| `reactive_or_proactive` | Yes      | See classification rule below                                                                                                 |
| `severity`              | If known | `SEV1`–`SEV4` per Chapter 6's Incident Severity Classification (use `unclassified` if the team hasn't triaged a severity yet) |
| `duration_minutes`      | If known | `time_resolved - time_detected`; leave blank if timestamps are missing                                                        |
| `confidence`            | Yes      | `measured`, `estimated`, or `unknown` — see uncertainty section below                                                         |
| `description`           | Yes      | One line, plain language                                                                                                      |

From this log you roll up the **three baseline metrics** named in Getting Started: incident frequency, MTTR (if calculable), and a team satisfaction score (1–10 survey, taken once at the start of the window).

## Observation Window

**Default: 5 consecutive working days** (Getting Started Week 1). This is short on purpose — the pilot needs a baseline fast, not a statistically perfect one.

**If your team already has incident/ticket history:** pull the last 4 calendar weeks (roughly 20 working days) from your existing tracker to compute a sturdier baseline frequency and MTTR, and use the 5-day log to calibrate reactive/proactive classification and collect the satisfaction score prospectively. Note both sample sizes in the summary.

**Fallback for teams with no historical data and no time to wait:** run the 5-day log as-is. Mark every rolled-up number `confidence: low, n=5 days` in the summary rather than presenting it as a stable baseline. Re-baseline with a rolling 4-week window at Day 30 and again at Day 90 once real data accumulates — the Day 30 and Day 90 numbers, not the Day 5 number, are what should carry weight in a Go/Adapt/Stop decision.

## Reactive vs. Proactive: How to Tell Them Apart

Use one question to classify each entry: **would this work have happened today without an external trigger?**

|              | Reactive                                                                                          | Proactive                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Trigger**  | An alert, monitor, customer report, escalation, or someone flagging a problem right now           | Chosen in advance from a backlog or plan                                                          |
| **Timing**   | Interrupts whatever was already planned                                                           | Scheduled and protected (e.g., the Week 3 improvement block)                                      |
| **Examples** | Incident response, on-call pages, ad-hoc requests that break into planned work, emergency changes | Automation work, documentation, capacity planning, risk mitigation, training, planned maintenance |

**Borderline case:** a change made _during_ an incident's timeline to stop or work around it is reactive. The same fix, scheduled and executed later as a backlog item once the incident is closed, is proactive — record it under `improvement` and reference the incident it came from. If you genuinely cannot tell which side an entry falls on, mark it `reactive_or_proactive: unclear` rather than forcing a guess — that's a data quality signal, not a failure.

## Recording Uncertainty (Don't Fabricate Precision)

Most teams starting a pilot do not have clean historical data. That is expected — the framework does not require it. What it requires is honesty about what you actually know:

- Use the `confidence` field on every rolled-up number: `measured` (from timestamps or a system of record), `estimated` (recalled from memory or partial records), or `unknown` (don't have it — say so).
- Prefer a range over a false-precision point estimate: `MTTR ~45–90 min (estimated, n=3 incidents)` is more honest and more useful than `MTTR: 62 min`.
- If a number can't be produced at all, write `unknown` in the summary. Do not backfill a plausible-sounding figure to make a report or trend line look complete — that's the fabrication this template exists to prevent.
- Carry the sample size (`n=`) alongside every rate or average. A 95% success rate on 3 events and a 95% success rate on 300 events are not the same claim.

## Copy-Ready Template

### Event log (`baseline-metrics.csv`)

```csv
date,time_detected,time_resolved,category,reactive_or_proactive,severity,duration_minutes,confidence,description
2025-01-06,09:14,09:52,incident,reactive,SEV1,38,measured,Payment API returned 500s after a deploy; rolled back
2025-01-06,,,improvement,proactive,,,estimated,Started writing runbook for the deploy rollback procedure
2025-01-07,14:02,,interrupt,reactive,SEV4,,unknown,Ad-hoc request from support to reset a stuck job; resolution time not logged
2025-01-08,,,planned_change,proactive,,,measured,"Scheduled DB index maintenance, no incident"
```

### Baseline summary (fill in once the log is complete)

```yaml
baseline_summary:
  observation_window:
    start: "<YYYY-MM-DD>"
    end: "<YYYY-MM-DD>"
    type: "5-day prospective | 4-week retroactive | 5-day fallback (low confidence)"

  incident_frequency:
    value: "<count per week, or 'unknown'>"
    confidence: "measured | estimated | unknown"
    n: "<number of days/weeks the count is based on>"

  mttr:
    value: "<e.g., '~45-90 min' or 'unknown'>"
    confidence: "measured | estimated | unknown"
    n: "<number of incidents with usable timestamps>"

  reactive_proactive_split:
    reactive_pct: "<% of logged time/events, or 'unknown'>"
    proactive_pct: "<% of logged time/events, or 'unknown'>"
    unclear_pct: "<% that couldn't be classified>"

  team_satisfaction_score:
    value: "<1-10>"
    n: "<number of respondents>"
    survey_date: "<YYYY-MM-DD>"

  notes: >
    <Anything that makes these numbers less solid than they look: short
    window, missing timestamps, one loud incident skewing the average,
    etc. This field exists so the Week 4 comparison doesn't compare a
    fuzzy number against a fuzzy number as if both were exact.>
```

Store both files next to your incident log and reuse the same format at Day 30 and Day 90 so comparisons stay apples-to-apples.
