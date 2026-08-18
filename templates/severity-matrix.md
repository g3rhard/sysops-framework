# Severity Matrix Template

> **Why this exists.** Severity gets defined once in Chapter 6 - Incident and Problem Management, but it gets _used_ everywhere: paging tools, the post-incident review template, the SLA template, the monthly ops report, and Chapter 10's security incident classification. This is the one copy-ready lookup card so every tool and template keys off the same four levels instead of quietly drifting into its own numbering.

## Severity Levels (Impact x Urgency)

| Severity            | Impact                                                                                           | Urgency               | Typical Trigger                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------ | --------------------- | ------------------------------------------------------------------------ |
| **SEV1 - Critical** | Total loss of a critical service; widespread customer impact; safety, legal, or revenue exposure | Immediate             | Payment processing down; confirmed data breach; full regional outage     |
| **SEV2 - High**     | Major functionality degraded for a large customer segment; no practical workaround               | Immediate or elevated | Login failing for a third of users; primary database unreachable         |
| **SEV3 - Moderate** | Limited functionality impaired for a small segment; workaround available                         | Elevated or standard  | Non-critical report delayed; degraded performance on a secondary feature |
| **SEV4 - Low**      | Minimal or no customer-facing impact                                                             | Standard              | Internal dashboard slow to load; a single noisy alert                    |

## Response, Paging, Communication, and PIR Expectations

| Severity | Initial Response  | Paging                                                              | Stakeholder Communication                              | Post-Incident Review                 |
| -------- | ----------------- | ------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------ |
| SEV1     | ≤ 5 min, 24/7     | Page primary immediately; page secondary if unacknowledged in 5 min | Update within 15 min, then every 30 min until resolved | Mandatory within 5 business days     |
| SEV2     | ≤ 15 min, 24/7    | Page primary on-call                                                | Update within 30 min, then hourly                      | Mandatory                            |
| SEV3     | Same business day | Ticket queue, no page                                               | Update on request or daily digest                      | Recommended, especially if recurring |
| SEV4     | Next business day | Logged only, no page                                                | Not required                                           | Not required                         |

## Copy-Ready Quick Reference

```text
SEV1 - Critical   | Page immediately  | Update every 30 min | PIR mandatory (5 business days)
SEV2 - High       | Page primary      | Update hourly        | PIR mandatory
SEV3 - Moderate   | Ticket queue       | Update on request    | PIR recommended
SEV4 - Low        | Log only           | No update required   | PIR not required
```

## Mapping Notes

- **P1-P4 paging shorthand**: some paging tools label these levels P1-P4 instead of SEV1-SEV4. The levels are identical - P1 = SEV1, P2 = SEV2, P3 = SEV3, P4 = SEV4. Pick one notation per team and use it consistently; don't run both at once.
- **Security incident type is a separate axis** (Chapter 10 - Risk & Compliance): Type 1 (confirmed breach/compromise), Type 2 (suspected incident), Type 3 (policy violation/drift), and Type 4 (monitoring alert) typically map to SEV1-SEV4 respectively, but type describes _what_ happened while severity drives _how urgently_ the team responds. Assess both.

## Notes on Filling This In

- **The first responder assigns severity; the Incident Commander owns changes to it.** Severity should be revised as facts change, not fixed at declaration time.
- **When in doubt, start one level more severe and downgrade.** The cost of an unnecessary page is minutes; the cost of a missed SEV1 is hours.
- **Don't average or split the difference between two levels.** If a call is genuinely between SEV2 and SEV3, pick SEV2 - urgency erring high is cheaper than urgency erring low.
