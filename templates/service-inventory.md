# Service Inventory Template

> **Why this exists.** Chapter 6 - Service Level Management starts with "catalog all services and their criticality levels" as Implementation Step 1, and Asset Management, Incident & Problem Management, and Backup & Recovery Operations all assume that catalog already exists. A CMDB with no owner field and a wiki page nobody updates are both worse than one boring, current table. Start here, keep it current, and let a full CMDB grow around it once tooling justifies the investment.

## Minimum Fields (one row per service)

| Field                 | Required      | Notes                                                                                                                                                             |
| --------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service`             | Yes           | Name used consistently everywhere - incidents, SLAs, dashboards                                                                                                   |
| `owner`               | Yes           | Team or named individual accountable; not a distribution list                                                                                                     |
| `tier`                | Yes           | Criticality tier, aligned to the RTO/RPO tiers in Chapter 6, Practice 12: Tier 1 Mission Critical / Tier 2 Business Critical / Tier 3 Important / Tier 4 Standard |
| `slo`                 | Yes           | Availability/latency target, or a link to the full SLA                                                                                                            |
| `dependencies`        | Yes           | Upstream and downstream services, shared infrastructure, and third-party dependencies                                                                             |
| `runbook`             | Yes           | Link to the runbook(s) covering this service's operation and failure modes                                                                                        |
| `on_call_route`       | Yes           | Paging service/escalation policy name that reaches the right responder                                                                                            |
| `rto`                 | If applicable | Recovery Time Objective                                                                                                                                           |
| `rpo`                 | If applicable | Recovery Point Objective                                                                                                                                          |
| `data_classification` | Yes           | Public / Internal / Confidential / Restricted (Chapter 10 - Risk & Compliance)                                                                                    |
| `vendor`              | If applicable | Third-party provider this service depends on, if any                                                                                                              |
| `lifecycle_stage`     | Yes           | Active / Deprecated / Sunset planned / Decommissioned                                                                                                             |

Add fields your team actually uses (cost center, compliance scope, region); resist adding fields nobody will keep updated.

## Copy-Ready Template

```csv
service,owner,tier,slo,dependencies,runbook,on_call_route,rto,rpo,data_classification,vendor,lifecycle_stage
Customer Authentication API,Platform Team,Tier 1 - Mission Critical,99.95% monthly / <200ms p95,"prod-db-01, prod-lb-01",https://wiki.internal/runbooks/auth-api,pagerduty:auth-api-primary,1 hr,15 min,Restricted,AWS RDS,Active
Internal Reporting Dashboard,Data Team,Tier 3 - Important,99.0% monthly,"prod-db-01, warehouse-etl",https://wiki.internal/runbooks/reporting,pagerduty:data-team,8 hr,4 hr,Internal,,Active
Legacy Billing Batch Job,Finance Systems Team,Tier 4 - Standard,best effort,prod-db-01,https://wiki.internal/runbooks/billing-batch,pagerduty:finance-systems,24 hr,24 hr,Confidential,,Deprecated
```

## Notes on Filling This In

- **One row, one owner.** If two teams think they own a service, that is the exact ambiguity this inventory exists to remove - resolve it before adding the row, not after the next incident.
- **`tier` drives everything else.** Response times, backup frequency, and on-call urgency elsewhere in the framework are keyed off this field; get it right before optimizing the others.
- **Link, don't duplicate.** `runbook` and `slo` should link to the maintained documents (post-incident review, SLA template, knowledge base), not restate their contents here.
- **Review quarterly at minimum.** An inventory that isn't reconciled against what's actually deployed rots as fast as an unmaintained CMDB - fold this into the CMDB audit cadence from Chapter 6, Practice 9.
