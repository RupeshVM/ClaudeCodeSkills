---
name: technical-design
description: Design a scoped feature or system change with repository-grounded options, interfaces, data flows, security, compatibility, validation, rollout, and rollback.
argument-hint: "<requirements, feature brief, or technical problem>"
---

# Technical design

Create an implementable design for the stated requirements. Ground it in the
existing system and keep code changes, infrastructure changes, and publication
outside this skill unless the user separately requests them. Default to a draft
in chat; write a design file only when asked.

## Inspect the system and constraints

1. Read `$ARGUMENTS`, applicable repository instructions, requirements, relevant
   architecture documentation, entry points, tests, and configuration examples.
2. Trace the existing request or event flow through the components that change.
   Identify current interfaces, data ownership, dependencies, and deployment
   boundaries. Cite actual file paths for material repository claims.
3. Record required behavior and quality constraints. Distinguish established
   requirements, inferred behavior, proposals, and unresolved decisions.
4. Identify compatibility commitments, platform limits, operational ownership,
   and resource constraints before choosing a new dependency or service.
5. Ask only for decisions that prevent useful design work. Analyze independent
   portions and mark assumptions rather than inventing missing approvals.

## Compare solutions

Present the simplest viable approach and any credible alternative that changes
an important tradeoff. Include leaving the current design in place when it could
meet the need. Evaluate complexity, user behavior, performance, operating cost,
delivery risk, testability, and reversibility.

Recommend an option and explain the deciding constraints. Prefer existing
conventions unless there is evidence they cannot satisfy the requirement. Do
not add queues, databases, services, or frameworks merely to fill out a diagram.

## Specify the chosen design

- Responsibilities and boundaries: what each component owns and how it
  communicates. Include a short flow diagram only when it clarifies the design.
- Interfaces: input/output contracts, validation, error semantics, versioning,
  idempotency, pagination, and timeouts where relevant. Mark proposed contracts.
- State and data: schema changes, ownership, invariants, transactions,
  concurrency, retention/deletion, and a compatible migration sequence.
- Security and privacy: trust boundaries, authentication, authorization,
  cross-tenant isolation, sensitive data handling, secret sources, and audit
  needs. Do not place credential values or real sensitive records in examples.
- Failure behavior: dependency outages, partial success, retries, duplicate
  work, recovery, and bounded resource use. Explain how consistency is restored.
- Observability: signals for successful behavior and failure, relevant logs,
  metrics, traces, alert owners if known, and sensitive-data redaction.
- Compatibility: old clients, stored records, mixed-version deployments,
  feature flags, and supported platform behavior as applicable.

Avoid false precision. State estimates and unmeasured performance expectations
as hypotheses, with a concrete measurement or discovery step.

## Validate and deliver safely

Map each important requirement and risk to a validation method. Distinguish
unit, integration, contract, migration, load, and manual checks; include only
those justified by the design. Use repository-supported commands when known,
and label commands that still need to be discovered.

Describe rollout sequencing, enablement conditions, expected signals, failure
thresholds where established, and rollback or roll-forward behavior. Address
irreversible data migrations explicitly rather than promising a simple revert.
Do not deploy or change production settings while drafting the design.

## Deliverable and completion

Read [the design template](references/design.md) when preparing the result.
Include the recommendation, alternatives, component and data flows, contracts,
risks, validation, rollout, and unresolved decisions. Scale detail to complexity.

A design is ready for implementation planning when the change boundaries,
contracts, data transitions, and major failure paths are sufficiently clear to
identify reviewable work. Label it provisional if a mandatory decision remains.
Recommend a small discovery spike when feasibility is still unknown; do not
present an unverified approach as production-ready.
