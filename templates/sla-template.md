# Service Level Agreement (SLA) Template

> An SLA you routinely miss is worse than an honest, lower number you can defend.

```text
SERVICE LEVEL AGREEMENT

Service name:        <service this SLA covers>
Provider:            <team>
Consumer:            <business unit / customer>
Effective date:      <YYYY-MM-DD>     Review cadence: <e.g., every 6 months>

1. SERVICE DESCRIPTION
   What the service does and what is explicitly OUT of scope.

2. SERVICE HOURS
   - Supported hours (e.g., 24/7, or Mon-Fri 08:00-18:00):
   - Planned maintenance windows (excluded from availability calc):

3. AVAILABILITY TARGET (SLA)
   - Target: <e.g., 99.9% monthly>
   - Measurement method (the SLI): <how uptime is actually measured>
   - Exclusions: <planned maintenance, force majeure, consumer-side faults>

4. PERFORMANCE TARGETS
   - <e.g., p95 latency < 300 ms>
   - <e.g., batch job completes by 06:00>

5. SUPPORT & RESPONSE TARGETS
   | Severity | Definition | Response target | Resolution target |
   |----------|-----------|-----------------|-------------------|
   | SEV1     |           |                 |                   |
   | SEV2     |           |                 |                   |
   | SEV3     |           |                 |                   |

6. REPORTING
   - What is reported, how often, and to whom:

7. REMEDIES / CONSEQUENCES
   - What happens if targets are missed (service credits, review, escalation):

8. RESPONSIBILITIES OF THE CONSUMER
   - What the consumer must do for the SLA to hold (e.g., supported clients,
     change notice, valid contact details):

9. SIGN-OFF
   | Role | Name | Signature | Date |
   |------|------|-----------|------|
```
