# Pilot Retrospective Template

> **One page. Honest, not flattering.** The point of this document is to drive a **Go / Adapt / Stop** decision at the end of the 30-day pilot (Getting Started — Week 4), using the same criteria the pilot was scored against at the start. If the honest answer is "Stop," writing that down is a successful use of this template, not a failed pilot.

```text
PILOT RETROSPECTIVE

Team:                  <team name>
Pilot dates:           <start YYYY-MM-DD> to <end YYYY-MM-DD>  (30 days)
Prepared by:           <name>
Baseline reference:    baseline-metrics.csv (Week 1)

1. BASELINE VS. WEEK 4 COMPARISON
   Pull these from the Week 1 baseline summary and a fresh Week 4 count.
   Carry the confidence field forward -- do not upgrade an "estimated"
   Week 1 number to "measured" just because it's now being compared.

   | Metric                          | Week 1 baseline | Week 4 | Change | Confidence |
   |----------------------------------|-----------------|--------|--------|------------|
   | Incident frequency (per week)    |                 |        |        |            |
   | MTTR                             |                 |        |        |            |
   | Reactive vs. proactive time split |                |        |        |            |
   | Team satisfaction (1-10)         |                 |        |        |            |

2. WHAT WORKED
   -
   -

3. WHAT DIDN'T
   -
   -

4. WHAT WE WOULD CHANGE
   -
   -

5. READINESS SIGNALS REVISITED
   Re-score the Quick Assessment from Getting Started. A signal flipping
   from "No" to "Yes" is pilot evidence; use it in the decision below.

   | Signal                                                              | Week 1 | Week 4 |
   |------------------------------------------------------------------------|--------|--------|
   | Team spends more time firefighting than improving                    |        |        |
   | Sprint commitments disrupted by operational emergencies monthly+      |        |        |
   | Basic monitoring and incident tracking in place                      |        |        |
   | At least one person willing to try a different approach              |        |        |
   | Manager knows operations work doesn't fit sprints                    |        |        |
   | Team can protect the team-agreed weekly improvement allocation       |        |        |

6. STOP CONDITIONS CHECK (Getting Started -- Stop Conditions)
   Check any that occurred during the pilot. Any checked box needs a
   documented mitigation before a Go decision.

   [ ] Daily cycle became a second status meeting
   [ ] Weekly improvement work was never actually protected
   [ ] Stakeholders still demand sprint-style commitments for reactive work
   [ ] Metrics were used to blame individuals

7. DECISION: GO / ADAPT / STOP

   GO -- all of the following are true:
     - At least one improvement was completed and documented (Week 3 artifact)
     - Team reports the daily cycle helps more than it costs
     - No unresolved stop conditions from section 6
     - Manager still agrees to protect improvement time going forward
   -> Proceed to Track B (Full Rollout), Month 1 Foundation and Assessment.

   ADAPT -- one or more of the following:
     - Cycle mechanics need adjustment, but the team wants to continue
     - A stop condition was triggered but has a clear, agreed fix
     - Baseline data was too thin (low confidence) to decide confidently
   -> Adjust scope or cadence and re-run the 30-day pilot.

   STOP -- one or more of the following:
     - Team reports the cycle adds ceremony without reducing confusion
     - No management support materialized despite the pilot's evidence
     - A stop condition recurred after an attempted fix
   -> Document why. Revisit Chapters 1-2 before considering another attempt.

   Decision made:        <Go / Adapt / Stop>
   Rationale (2-3 sentences):

```

## Notes on Filling This In

- **Don't smooth the baseline comparison.** If Week 1 MTTR was `estimated, n=3`, say so again in row 1 of the Week 4 table — don't present it as if both numbers are equally solid.
- **A single "Adapt" is not a failure to report upward.** It means the team learned something specific enough to name; that is the pilot working as intended.
- **The rationale line is mandatory.** A Go/Adapt/Stop decision without a written reason is exactly the kind of unmeasured judgment call this framework exists to replace.
