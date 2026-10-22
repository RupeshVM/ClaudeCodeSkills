---
name: acceptance-criteria
description: Turn a feature, story, or bug report into concrete acceptance scenarios covering normal behavior, failures, permissions, boundaries, and measurable quality requirements.
argument-hint: "<feature, story, bug report, or issue reference>"
---

# Acceptance criteria

Define the observable conditions under which a scoped change is acceptable.
Produce criteria in chat by default. Do not create tests, change implementation,
or publish criteria to a tracker unless the user requests that action.

## Understand the acceptance boundary

1. Read `$ARGUMENTS`, existing requirements, relevant repository documentation,
   and the current behavior in code or tests when available.
2. Identify the user or client, intended outcome, entry points, permissions,
   relevant states, and explicit exclusions. Preserve supplied requirement IDs.
3. Separate desired behavior from existing behavior. A current test can explain
   a contract; it does not by itself define the intended product change.
4. Flag ambiguity that affects expected results. Ask a focused question only
   when a concrete criterion cannot be written responsibly; otherwise use a
   labeled proposal. Never silently invent policy, numeric targets, or access
   rules.

## Select scenarios by risk

Cover the main successful path first, then choose relevant cases from:

- Empty, missing, invalid, maximum, and just-outside-boundary inputs.
- Anonymous, authorized, unauthorized, and cross-tenant access.
- Missing records, stale state, conflicting updates, and repeat submissions.
- Dependency failure, timeout, retry, cancellation, and recovery.
- Data consistency, persistence, deletion, and migration compatibility.
- Accessible interaction and errors for user-facing changes.
- Backwards compatibility for documented clients and stored data.
- Performance or reliability requirements that have measurable targets.

Do not add every category mechanically. State which important categories are
inapplicable and why when their absence could surprise a reviewer. Group
equivalent inputs into a boundary table instead of duplicating scenarios.

## Write testable criteria

1. Give each criterion a stable local ID, such as `AC-01`, and trace it to a
   requirement or user outcome. These are labels, not tracker issue keys.
2. Use Given/When/Then or an equally concrete input/action/result structure.
   State preconditions, the triggering action, and observable results. Specify
   the observation surface: UI, response, persisted state, event, or audit log.
3. Avoid combining unrelated outcomes in one scenario. Include related effects
   together when they form one atomic business operation.
4. Use deterministic fixtures and explicit boundary values when known. Mark
   placeholders that require a product decision instead of implying they are
   approved values. Do not put real customer data or credentials in examples.
5. Specify error behavior without exposing secrets or sensitive records. Define
   whether a failed operation leaves state unchanged when that matters.
6. For time-based or performance criteria, include population, measurement
   window, relevant workload, and pass condition. If no approved target exists,
   label it unresolved rather than using arbitrary thresholds.

## Separate acceptance from implementation checks

Acceptance criteria describe behavior a reviewer can observe. Unit-test names,
specific private methods, internal class structure, and build commands belong
in a test plan unless they are contractual requirements.

Include release acceptance conditions only when the feature requires them, such
as a migration reconciliation check or a rollback verification. Do not claim
that criteria have passed unless they were executed in the current work and
the result can be evidenced.

## Deliverable and completion

Read [the scenario template](references/scenarios.md) to structure the output.
Provide the scope, numbered scenarios, a compact boundary table where useful,
traceability, and unresolved decisions. Indicate proposed versus agreed
criteria when that distinction is known.

The criteria are ready for review when each has a clear pass/fail observation,
important failure and permission paths are represented, and assumptions cannot
be mistaken for established requirements. Report unresolved criteria explicitly;
do not manufacture agreement or test execution results.
