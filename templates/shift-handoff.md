# Shift Handoff Template

> **Why this exists.** Chapter 9 - Culture & Organization requires a handoff document at the start of every on-call shift so the incoming responder isn't reconstructing context from memory or Slack scrollback. An unwritten handoff is a bet that nothing important happened last shift - a bet the team eventually loses at 3 a.m.

```text
SHIFT HANDOFF

Outgoing responder:     <name>
Incoming responder:     <name>
Shift end / start:      <YYYY-MM-DD HH:MM> (timezone)
Overlap window:         <e.g., 30 min, 09:00-09:30>

1. ACTIVE INCIDENTS OR KNOWN ISSUES
   Anything unresolved that the incoming responder needs to be aware of.
   Include current status, severity (SEV1-SEV4), and next expected action.
   -
   -

2. SCHEDULED MAINTENANCE WINDOWS
   Anything planned during the upcoming shift period.
   -
   -

3. RECENT DEPLOYMENTS
   Anything deployed in the last 24-48 hours that may still be unstable.
   Link the change record.
   -
   -

4. KNOWN NOISY ALERTS
   Alerts expected to fire that are not actionable, and how to handle them
   (silence, acknowledge and ignore, escalate anyway).
   -
   -

5. ESCALATION CONTACTS FOR THIS SHIFT
   Any changes to the standard escalation path (see on-call policy) --
   vacations, backup coverage, vendor support windows.
   -
   -

6. EMERGENCY ACCESS
   Secrets manager path or access procedure location -- not the
   credentials themselves.
   -

7. ANYTHING ELSE THE NEXT RESPONDER SHOULD KNOW
   Gut feelings count. "Database has felt slow all shift but nothing
   alerted" is exactly the kind of thing this section exists for.
   -

Handoff acknowledged by incoming responder:  [ ] Yes, read and understood
```

## Notes on Filling This In

- **Write it at the end of the shift, not from memory the next morning.** Update it as things happen; don't reconstruct it in the last five minutes.
- **A blank section is a claim, not an omission.** "No active incidents" is useful information; an empty box with no explanation is not.
- **The incoming responder should read this before the overlap window ends**, not discover it mid-incident.
- **Keep handoffs in the same place every time** (pinned incident channel message, shared doc, or wiki page) so nobody has to go looking for the last one.
