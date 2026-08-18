# Work Intake and Triage Template

> **Why this exists.** Chapter 3 — Framework Structure names the taxonomy (incidents, service requests, standard/normal/emergency changes, improvement work, strategic work, interruptions) and the routing rules that decide which cycle owns a piece of work. This template is the day-to-day artifact for applying those rules: one log to capture everything that arrives, one form to record the triage decision on anything that isn't immediately obvious. Severity uses Chapter 6's canonical SEV1-SEV4 scale (Incident Severity Classification) so intake records, paging, and reporting all key off the same four levels — don't let a second numbering scheme compete with it.

## Minimum Intake Fields

Capture at least these fields for every item, whatever ticketing system or spreadsheet is behind it:

| Field                | Required      | Notes                                                                                                                                                                                                                    |
| -------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                 | Yes           | Ticket number or link                                                                                                                                                                                                    |
| `title`              | Yes           | One line                                                                                                                                                                                                                 |
| `requester`          | Yes           | Who raised it                                                                                                                                                                                                            |
| `date_raised`        | Yes           | `YYYY-MM-DD HH:MM`                                                                                                                                                                                                       |
| `affected_service`   | If known      | System or service touched                                                                                                                                                                                                |
| `initial_type_guess` | Yes           | `incident` / `service_request` / `standard_change` / `normal_change` / `emergency_change` / `improvement` / `strategic` / `unclassified`                                                                                 |
| `severity`           | For incidents | `SEV1` / `SEV2` / `SEV3` / `SEV4` per Chapter 6's Incident Severity Classification — the canonical scale, not a local invention. Blank/`N/A` for non-incident items until (if ever) they're reclassified to an incident. |
| `impact_note`        | Yes           | Free-text detail beyond the severity rating — which service, which customers, what's actually broken. Supplements `severity`, doesn't replace it                                                                         |
| `confirmed_type`     | At triage     | Filled in once classified; may differ from the initial guess                                                                                                                                                             |
| `queue`              | At triage     | `daily` / `weekly` / `monthly`                                                                                                                                                                                           |
| `owner`              | At triage     | Person or role accountable for the next step                                                                                                                                                                             |
| `status`             | Yes           | `open` / `in_progress` / `blocked` / `done`                                                                                                                                                                              |
| `related_items`      | If any        | Linked incident, change, or improvement record                                                                                                                                                                           |

## Routing Quick-Reference

Ask, in order, and stop at the first "yes" (full rationale in Chapter 3, "Work Intake and Triage"):

1. Live service down, degraded, or at risk right now, or must happen today regardless of type? → **Daily queue**.
2. Can be scoped, executed, and measured inside roughly one week, no architecture decision, no multi-team coordination? → **Weekly queue**.
3. Spans multiple weeks, needs a capacity/architecture decision, or touches more than one team? → **Monthly queue**.
4. None of the above obviously true yet? → **Daily intake queue by default**; reclassify within one daily cycle.

An item stuck as `unclassified` past one daily cycle escalates to the team lead — that delay is itself a signal, not a paperwork gap.

## Copy-Ready Template

### Intake log (`work-intake-log.csv`)

```csv
id,title,requester,date_raised,affected_service,initial_type_guess,severity,impact_note,confirmed_type,queue,owner,status,related_items
INC-1042,Payment API returning 500s,monitoring-alert,2025-01-06 09:14,payment-api,incident,SEV1,Payments fully down for all customers,incident,daily,jane,in_progress,
REQ-338,New VPN access for contractor,sam,2025-01-06 10:02,vpn,service_request,N/A,No live impact; standard access request,service_request,daily,helpdesk,open,
CHG-221,Add index to orders table,priya,2025-01-06 11:30,orders-db,normal_change,N/A,No live impact planned,normal_change,weekly,priya,open,
IMP-58,Automate weekly cert renewal check,jane,2025-01-06 13:15,,improvement,N/A,No live impact,improvement,weekly,jane,open,INC-1042
STR-12,Evaluate managed database migration,team-lead,2025-01-06 15:00,orders-db,strategic,N/A,No live impact,strategic,monthly,team-lead,open,
```

### Triage and reclassification decision (one per item that needs a call)

```text
TRIAGE DECISION

Item:                 <id / link>
Raised by:             <requester>            Date/time: <YYYY-MM-DD HH:MM>
Initial type guess:    <incident / service_request / standard_change / normal_change / emergency_change / improvement / strategic / unclassified>

CLASSIFICATION
  Confirmed type:      <type>
  Severity (if incident): [ ] SEV1  [ ] SEV2  [ ] SEV3  [ ] SEV4  [ ] N/A (not an incident)
  Impact note:         <free text — which service, which customers, what's actually broken>
  Queue assigned:      [ ] Daily  [ ] Weekly  [ ] Monthly
  Classified by:       <name/role>            Date/time: <YYYY-MM-DD HH:MM>
  Reasoning (one line):

WIP CHECK (does this queue have room, given who's actually resourced to it this cycle?)
  Queue owner:         <name/role>
  Room to accept?      [ ] Yes  [ ] No — parked until: <date/condition>

RECLASSIFICATION (fill in only if this item is moving from its original queue)
  Previous type/queue:
  New type/queue:
  Reason for change:
  Accepted by (receiving owner):

ESCALATION (fill in only if a trigger below applies)
  [ ] Service request breached SLA or revealed live impact -> Incident, Daily, assign SEV1-SEV4
  [ ] Normal change needed to stop an active incident -> Emergency change, Daily
  [ ] Weekly improvement grew beyond one week / needs an architecture call / spans teams -> Strategic, Monthly
  [ ] Monthly initiative turned out to be a same-day fix once scoped -> Standard/Normal change or Improvement, hand down a cycle
  Notes:
```

Store both files next to the team's incident log and ticketing system so the intake log and triage decisions stay linked to the work they describe.
