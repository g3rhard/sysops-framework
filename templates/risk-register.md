# Risk Register Template

> **Why this exists.** Chapter 10 - Risk & Compliance references "the risk register" repeatedly - pentest findings feed it, audits expect it, maturity reviews check whether it's actually kept up to date - but a register that only exists as a mention is not a register. This is the copy-ready version: one row per risk, one owner, one treatment decision, reviewed on a cadence instead of after the incident that proves it was needed.

## Minimum Fields (one row per risk)

| Field         | Required      | Notes                                                                                                        |
| ------------- | ------------- | ------------------------------------------------------------------------------------------------------------ |
| `risk_id`     | Yes           | Stable identifier (e.g., `RISK-2026-014`) so it can be referenced from incidents, audits, and change tickets |
| `description` | Yes           | One or two sentences: what could go wrong and to what                                                        |
| `risk_type`   | Yes           | Availability / Security / Compliance / Capacity / Process / Technology (Chapter 10 risk types)               |
| `impact`      | Yes           | 1-5 (Chapter 10 Risk Assessment Framework); coarse prioritization, not a precise measurement                 |
| `probability` | Yes           | 1-5                                                                                                          |
| `score`       | Yes           | `impact x probability`; used to rank, not to prove precision                                                 |
| `owner`       | Yes           | Named individual accountable for the treatment decision and its follow-through                               |
| `treatment`   | Yes           | Accept / Mitigate / Transfer / Avoid                                                                         |
| `mitigation`  | If mitigating | The specific action(s) being taken, each with its own due date                                               |
| `status`      | Yes           | Open / In progress / Mitigated / Accepted / Closed                                                           |
| `next_review` | Yes           | Date this risk is next reassessed                                                                            |

## Copy-Ready Template

```csv
risk_id,description,risk_type,impact,probability,score,owner,treatment,mitigation,status,next_review
RISK-2026-014,"Production database runs on 5-year-old hardware with no redundancy",Availability,5,4,20,Platform Team Lead,Mitigate,"Implement hardware redundancy and refresh plan; target 2026-Q3",In progress,2026-09-01
RISK-2026-015,"Single vendor provides authentication with no documented failover",Technology,5,3,15,Security Lead,Mitigate,"Evaluate secondary IdP; document manual failover runbook",Open,2026-07-15
RISK-2026-016,"Quarterly access review is manual and frequently slips",Process,3,3,9,Compliance Owner,Accept,"Accepted for this fiscal year; revisit if audit finding recurs",Accepted,2027-01-01
```

## Review Cadence

- **Weekly Improvement Cycle**: review open, high-score risks and confirm mitigation actions are progressing.
- **Monthly Strategy Cycle**: review the full register - new risks, closed risks, and any risk whose `next_review` date has passed.
- **After every incident or near-miss**: check whether it maps to an existing risk (update score/status) or represents a new one (add a row).

## Notes on Filling This In

- **A risk without an owner is a complaint, not a risk.** Every row needs a name, not a team alias.
- **Treat scores as a ranking tool, not a scientific measurement.** A 20 and a 19 are both "urgent" - don't spend time arguing over which is technically higher.
- **`Accept` is a valid, documented decision.** Recording "we accepted this and here's why" is more defensible in an audit than silence.
- **Keep this register separate from the incident log.** Incidents are things that already happened; this register is things that have not happened yet.
