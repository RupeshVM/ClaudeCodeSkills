---
name: incident-response
description: "Investigate a production incident, outage, error spike, or service degradation and prepare mitigation, recovery, and timeline evidence. Use for operational diagnosis or incident coordination; actions remain read-only unless the user authorizes a specific change."
argument-hint: "<symptoms or incident reference> [service] [time window]"
disable-model-invocation: true
---

# Incident response

Prioritize user impact, evidence preservation, and the smallest safe path to
recovery. Interpret `$ARGUMENTS` as the symptoms, affected service, or time range.
Return findings and proposed actions in chat unless an artifact is requested.

## Establish the operating boundary

1. Read applicable incident runbooks, repository instructions, service topology,
   and available monitoring or operations tool descriptions.
2. Identify the affected environment and what the user has authorized. Start
   with bounded read-only diagnosis. Access to a production tool does not itself
   authorize configuration changes or mitigation commands.
3. Identify the incident lead and action owner if supplied; use unassigned roles
   if unknown. Do not appoint people, page responders, or send messages unless
   the user explicitly asks for those communications.
4. Set the observation window and timezone; use exact timestamps with offsets.
   Preserve reported times separately from inferred times and clock assumptions.
5. Capture user impact, affected paths/cohorts, start time, current symptoms,
   and last known healthy state. Mark unknowns instead of inventing blast radius.

Read [the incident template](references/incident-template.md) when organizing
findings or maintaining a requested incident document.

## Gather bounded evidence

- Check health indicators and representative user behavior before relying on a
  single dashboard metric. A live process or open port is not proof of service.
- Inspect relevant errors, latency, traffic, saturation, dependency health,
  recent deployments, configuration changes, and data/schema events.
- Narrow log and trace queries by service, time, and identifiers. Limit result
  volume and cost; avoid broad queries that worsen an overloaded system.
- Compare affected and healthy cohorts or instances when available. Correlation
  with a release is a hypothesis until supported by further evidence.
- Record sources, timestamps, observations, and confidence. Separate evidence,
  hypotheses, and actions taken.
- Redact credentials, authorization headers, personal data, and sensitive payloads
  from summaries. Do not dump environment values or full credential files.

Use existing authorized integrations. If required telemetry is inaccessible,
report the exact source or permission gap and continue with other evidence.
Never claim unavailable metrics, logs, or production behavior were inspected.

## Diagnose and propose mitigation

1. List the leading hypotheses and the observation that would support or
   disprove each. Prefer short checks that distinguish competing explanations.
2. Identify a mitigation that reduces current impact even if root cause remains
   uncertain. Evaluate scope, reversibility, dependencies, and data consequences.
3. Prefer the established runbook when it fits the observed failure; do not
   blindly execute a runbook for a different service or version.
4. Present concrete options, expected effects, risks, prerequisites, and a success
   check. Distinguish a temporary mitigation from a permanent fix.
5. For production writes, restarts, failovers, flags, destructive rollback, data
   changes, or access changes, verify explicit user authorization covers the
   exact target and action. If scope is missing, finish independent diagnosis
   and request that specific authority with the proposed action ready to assess.

Do not run production load tests, destructive experiments, or speculative fixes.
Do not treat urgency as permission to bypass security, verification, or access
controls. Do not repeatedly retry an expensive failing action unchanged.

## Execute only within authorized scope

When execution is explicitly authorized and supported by available tools:

1. Reconfirm target state with a read-only check and note the pre-action evidence.
2. Apply the narrowest supported action, using an existing runbook where possible.
3. Record the actual action, timestamp, result, and any unexpected behavior.
4. Verify representative user functionality and relevant health indicators over
   an appropriate observation window. Check for shifted impact or new failures.
5. Stop or recover according to the agreed criterion if the action worsens impact.
   Do not extend authorization to unrelated systems or escalating changes.

A successful command or rollback request does not prove recovery. If verification
is unavailable, report the action as completed with recovery still unconfirmed.

## Maintain a factual timeline and handoff

Record impact, detections, hypotheses, decisions, actual actions, and measured
outcomes with timestamps. Draft status updates only when requested; sending them
requires an explicit communication request and destination.

Finish with current impact, verified findings, remaining uncertainty, actions
actually taken, recovery evidence, next diagnostic or mitigation step, and owner
roles. Recommend follow-up for detection, prevention, or runbook gaps without
claiming a root cause that has not been established.
