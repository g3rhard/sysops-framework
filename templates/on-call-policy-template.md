# On-Call Policy Template

> An on-call policy nobody reads because it's 12 pages of legal language is an on-call policy that doesn't exist.

```yaml
policy_name: "On-Call Operations Policy"
version: 1.0
owner: "<Engineering Manager>"
review_cadence: "quarterly"

purpose: >
  Define the principles, expectations, and compensation for on-call
  rotations so that service reliability is maintained without burning
  out the engineers who maintain it.

scope:
  applies_to: "All platform and service engineers above L3"
  excludes: "Interns, probationary hires (first 3 months), known medical exceptions"
  coverage_hours: "24/7 for P1/P2; business hours only for P3/P4"

rotation:
  pattern: "Primary + secondary"
  shift_length: "7 days (Monday 09:00 -> next Monday 09:00)"
  min_rest_between_shifts: "One full rotation off (7 days) after any on-call week"
  max_frequency: "One week in five (aiming for one in six)"
  handoff_time: "Monday 09:00, 30 min overlap required"

compensation:
  base: "Flat weekly on-call allowance: $X per shift week"
  incident_premium: "Additional $Y per P1 confirmed outside business hours"
  time_off_in_lieu: "Day off after any shift where > 3 pages interrupted sleep"
  alternative: "Non-monetary: one 'on-call recovery' day after shift week"

escalation:
  tier_1: "Primary on-call (0-5 min)"
  tier_2: "Secondary on-call (5-15 min no ack)"
  tier_3: "Team lead (15-30 min unresolved)"
  tier_4: "Engineering director (30+ min, customer-impacting)"
  override: "Any responder may invoke escalation at any time if out of their depth"

alert_quality:
  pager_threshold: "Only P1 and P2 page. P3 -> ticket queue. P4 -> log."
  max_pages_per_shift: "5 actionable pages before post-shift review required"
  runbook_requirement: "Every alerting rule MUST link to a runbook in its annotation"
  quarterly_review: "Alert inventory reviewed every quarter; silence or retire stale rules"

failure_modes:
  - scenario: "Primary misses 2 pages in one shift"
    action: "Review with manager; check for burnout, alert fatigue, or personal circumstances"
  - scenario: "Shift > 6 hours without a break during active incident"
    action: "Incident Commander MUST rotate responder out; mandatory handoff"
  - scenario: "Engineer on-call more than 1 week in 4 for 2 consecutive quarters"
    action: "Team composition review -- team is understaffed for its reliability targets"
```
