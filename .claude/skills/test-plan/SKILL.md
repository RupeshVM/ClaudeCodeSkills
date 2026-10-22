---
name: test-plan
description: Build a risk-based test strategy or feature test plan with concrete scenarios, coverage gaps, environments, and release criteria grounded in the repository.
argument-hint: "[feature, change, component, or release scope]"
---

# Test plan

Create an executable plan for checking behavior that matters to users and integrations.
Use `$ARGUMENTS`, the requested change, and the repository's existing tests as evidence.
A test plan describes checks; it does not imply that any of those checks have run.

## Discover scope and existing capabilities

1. Read repository instructions, the feature or issue, acceptance criteria, and relevant design.
2. Identify changed behavior, affected interfaces, persistence, dependencies, and consumers.
3. Inspect test configuration, representative existing tests, CI jobs, and supported commands.
4. Determine available unit, integration, contract, browser, and performance test capabilities.
   Reuse the established runner and fixtures rather than proposing a new framework by default.
5. Note required services, synthetic data, permissions, platforms, and configuration names.
   Check availability without printing secrets or assuming a configured integration works.

For vague requirements, list the specific ambiguity and a provisional behavior assumption.
Ask only questions whose answers materially change coverage or release risk.
Keep unrelated product areas outside the plan unless a shared dependency makes them relevant.

## Rank behavioral risks

Build a short risk inventory using impact and likelihood, with evidence behind each rating.
Consider data loss, authorization bypass, incorrect billing, availability, and user confusion.
Add likelihood signals such as changed branching logic, concurrency, migrations, or past failures.
Avoid fabricated incident history or precision unsupported by the available evidence.

Assign priority according to what must work before merge or release:

- **Critical:** failure could violate security, lose data, or break the primary workflow.
- **High:** likely regressions and meaningful failures in normal or important edge cases.
- **Supporting:** lower-impact variations that can follow the primary validation where justified.

Record which risks remain untested if time or environment limits the selected scope.
Do not downgrade a risk solely because its test is inconvenient to run.

## Design concrete coverage

For every acceptance criterion and important risk, specify an observable assertion.
Cover the successful path and relevant boundaries rather than duplicating implementation branches.

- Inputs: missing, empty, malformed, out of range, unicode, and large values where applicable.
- State: first use, repeated use, partial state, expired state, and migration compatibility.
- Permissions: anonymous, correct owner, other tenant or owner, and insufficient role.
- Failures: dependency timeout, rejected response, retry exhaustion, and partial success.
- Ordering: duplicate requests, idempotency, cancellation, and concurrency where relevant.
- Interfaces: backward compatibility, serialization, pagination, and error contracts.
- User experience: keyboard and screen-reader behavior, clear feedback, and recovery when relevant.

Use the cheapest test layer that proves the requirement with sufficient realism.
Unit tests suit deterministic logic; integration tests prove real boundaries such as storage;
contract tests prove consumer/provider assumptions; end-to-end tests cover selected user journeys.
Do not require every scenario at every layer. Explain intentional gaps and overlaps.

Read [the coverage matrix](references/coverage-matrix.md) before organizing the final plan.
Give each planned check a stable local scenario ID, setup, action, expected result, and layer.
Label invented scenario IDs as plan identifiers, not existing test or issue IDs.

## Make execution practical

1. List existing commands and working directories; distinguish verified commands from suggestions.
2. Specify synthetic fixtures, cleanup, isolation, clocks, seeds, and dependency substitutes.
3. Use supported local configuration and avoid shared production state.
4. Define what can run in parallel and what requires ordering or exclusive resources.
5. Include any necessary manual checks with exact observations and pass/fail criteria.
6. Define merge and release gates using required behavior and acceptable residual risk.
   A percentage coverage target alone does not establish correctness.

If execution is requested, run the available selected checks and preserve the runner's exit status.
Confirm the intended tests actually executed; separate a zero-test run from a passing suite.
Record counts and failures when the runner reports them. Do not claim manual checks were automated.

## Deliver

Return the plan in chat unless the user asked for a file in the repository's documented location.
Include scope, evidence, prioritized risks, scenario matrix, commands, prerequisites, and gates.
Separate existing coverage from proposed tests and executed results.
Identify required checks blocked by unavailable services or credentials and the precise next action.
Do not add dependencies, change tests, or publish a test-management record from a planning request.

Finish when each in-scope criterion and significant risk has a planned assertion or an explicit gap,
and the intended executor can tell what to run and what a successful result looks like.
