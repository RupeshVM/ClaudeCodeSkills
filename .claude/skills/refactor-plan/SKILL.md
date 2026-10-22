---
name: refactor-plan
description: Plan a behavior-preserving refactor with explicit invariants, dependency-aware steps, regression checks, and rollback points. Use before restructuring code or replacing an internal abstraction.
argument-hint: "<component or refactor goal> [constraints]"
---

# Plan a refactor

Create a sequence of reviewable changes that improves structure while preserving agreed behavior. Default to a plan in chat. Do not edit application code unless the user also requests implementation.

## Establish the reason and boundaries

1. Read `$ARGUMENTS`, the user's objective, applicable repository instructions, component documentation, and recent relevant changes when available.
2. Identify the concrete problem: repeated change cost, unsafe coupling, difficult testing, duplicated logic, an unsupported abstraction, or a specific maintenance risk.
3. Locate the component, callers, public interfaces, persisted representations, configuration, and tests.
4. Inspect current working tree changes and account for active work that the plan must preserve.
5. State the smallest scope that achieves the objective. Keep unrelated formatting, dependency upgrades, and product changes outside that scope.

Distinguish a behavior-preserving refactor from a feature change or bug fix. If existing behavior is undesirable but must change, name that change separately and give it its own acceptance criteria.

## Define invariants

Describe the behavior that each step must preserve, using evidence from current code, tests, contracts, and documented requirements:

- Public function, API, command, and event contracts.
- Inputs, outputs, error behavior, and supported edge cases.
- Authorization, tenant boundaries, privacy, and logging constraints.
- Persisted data format, schema compatibility, and migration expectations.
- Ordering, retries, idempotency, transactions, and concurrency guarantees.
- Performance and resource characteristics when relevant to the goal.
- Supported runtime versions, platforms, configuration, and extension points.

Mark uncertain behavior as an investigation item. Do not silently promote an implementation accident into a permanent contract or assume an undocumented caller does not exist.

## Assess current evidence

1. Map the dependency direction between the component and its callers. A small table or diagram is useful when it reveals sequencing constraints.
2. Identify existing tests that protect the invariants and important coverage gaps.
3. Propose characterization tests for uncertain behavior before structural changes. Tests should assert externally relevant behavior rather than freeze private implementation details.
4. Identify generated code and the source definitions that own it. Plan to use existing generation commands instead of editing generated outputs directly.
5. Check whether dependency cycles, shared state, global initialization, or data migration constrain the refactor.

If the repository lacks evidence for a critical invariant, start with a discovery or test step. Do not call a large mechanical rewrite safe merely because it is easy to script.

## Compare approaches

Present a small number of feasible alternatives when the tradeoff is material. Compare:

| Criterion | What to evaluate |
| --- | --- |
| Change size | Files, consumers, and migration effort affected |
| Behavior risk | Invariants exposed and how they can fail |
| Maintainability | How the approach addresses the stated problem |
| Compatibility | Existing callers and persisted data |
| Validation | Tests and observations that can detect regressions |
| Reversibility | Ability to roll back each stage safely |

Recommend one approach based on the repository's constraints. Avoid abstractions that only support speculative future use cases.

## Sequence the plan

For every step, provide:

1. **Purpose:** the specific structural improvement or prerequisite.
2. **Affected code:** verified file paths, symbols, and callers; mark candidate paths that do not yet exist.
3. **Change:** a clear description of the edit and its boundary.
4. **Dependencies:** earlier steps, compatibility adapters, or required decisions.
5. **Verification:** relevant tests, type checks, builds, contract checks, or representative calls.
6. **Completion criterion:** evidence that makes the next step safe.
7. **Rollback:** the recovery path and any state that makes reversal difficult.

Prefer steps that keep the tree runnable and the tests meaningful. Where needed, introduce an adapter, move callers incrementally, then remove the obsolete path after confirming it is unused.

Do not prescribe deleting or replacing user changes. Do not add broad dependency upgrades to make the plan appear simpler.

## Account for rollout

For an internal refactor with no deployment implications, say so briefly. For a change crossing process, release, or data boundaries, explain compatibility windows, staged rollout, monitoring, and rollback constraints.

Distinguish reversing source changes from reversing persisted state. A schema or data migration may need a separately reviewed migration plan even when code changes are reversible.

## Deliver

Present the objective, invariants, selected approach, ordered steps, validation strategy, and unresolved risks. Give rough complexity only when useful and label estimates as uncertain.

Keep the final plan actionable for another developer without the conversation history. If implementation was also requested, use the plan to continue into the authorized changes and verification rather than stopping at the plan.
