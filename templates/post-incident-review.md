# Post-Incident Review Template

> **Blameless by design.** This document examines systems and decisions made with the information available at the time — never the character of the human who clicked the button.

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
   - Duration (detection -> full recovery):
   - SLO/error-budget impact:
   - Revenue / contractual / reputational impact:

3. TIMELINE (in the team's timezone, 24h clock)
   HH:MM  Event (detection, escalation, key decisions, mitigation, recovery)
   ...

4. ROOT CAUSE(S)
   The contributing factors -- usually plural. Use "5 Whys" or a causal
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
