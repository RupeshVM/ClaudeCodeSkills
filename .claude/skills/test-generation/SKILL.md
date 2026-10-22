---
name: test-generation
description: Add meaningful automated tests for a feature, bug fix, or uncovered behavior using the repository's established test framework, fixtures, and assertions.
argument-hint: "[behavior, source path, bug, or acceptance criteria to test]"
---

# Test generation

Implement tests that can detect a real behavioral regression.
Use `$ARGUMENTS` and the user's requested scope to identify the behavior under test.
If the user requested only test ideas or a plan, return that artifact instead of editing files.
An explicit request to add tests authorizes the relevant local test changes and execution.

## Learn the local conventions

1. Read repository instructions and inspect the working tree; preserve unrelated changes.
2. Identify the runner, language version, dependency manager, test discovery rules, and CI commands.
3. Read representative nearby tests, reusable fixtures, helpers, and configuration.
4. Inspect the target's public contract, callers, failure modes, and existing coverage.
5. Identify any required service, database, browser, environment variable name, or generated fixture.
   Never print credential values or copy production data into tests.

Use the installed, repository-pinned toolchain and existing helpers where practical.
Do not silently introduce a new framework, alter a lockfile, or replace the runner to add a test.
If no test infrastructure exists, explain the smallest suitable approach and add only the
infrastructure required by the authorized task; surface material dependency choices first.

## Select useful scenarios

Map tests to an explicit requirement or failure, not simply to a function's current implementation.
Prioritize the normal path, the reported regression, important boundaries, and security decisions.
For each candidate, state what observable incorrect behavior would make the test fail.
Discard tests that merely assert a mock was configured, return a constant, or duplicate production
logic in a way that would reproduce the same bug in both the implementation and the expected result.

Choose an appropriate layer:

- Unit tests for deterministic logic with clear inputs and outputs.
- Integration tests for interactions that require actual storage, serialization, or runtime behavior.
- Contract tests for agreed request, response, and compatibility semantics.
- A small number of end-to-end tests for essential user workflows.

Avoid large combinatorial suites when a few carefully chosen boundary cases prove the contract.
Use table-driven or property-based cases only when the repository supports them and the invariant
is meaningful. State legitimate ranges and constraints so generated cases remain interpretable.

## Write robust tests

1. Name each test after the behavior and relevant condition.
2. Arrange the minimum representative state, perform one logical action, and assert its result.
3. Assert meaningful output, persisted state, permission outcomes, or documented side effects.
4. Test error type and useful contract details without pinning irrelevant internal wording.
5. Mock nondeterministic or unavailable external boundaries, not the core behavior being tested.
   Keep at least an appropriate integration check where a mock cannot prove the real boundary.
6. Use synthetic fixtures and deterministic clocks, seeds, or IDs where needed.
7. Isolate state and clean up resources even when assertions fail.
8. Prefer observable readiness or completion conditions over arbitrary sleeps.

Check ownership boundaries and repeated or invalid operations when those are part of the feature.
For asynchronous code, await work and failures so background errors cannot make a test pass.
For concurrency, coordinate the relevant interleaving explicitly when the runner supports it.
Do not encode nondeterminism as a broad timeout, unconditional retry, or flaky-test exemption.

## Verify the tests prove something

For a regression, demonstrate that the new test detects the original failure when feasible without
discarding user work or rewriting history. A narrowly scoped reversible simulation may suffice.
If testing the unfixed state is unsafe or impractical, explain that limitation instead of claiming
a red-to-green result. Do not modify production behavior merely to manufacture a passing test.

Inspect assertions for false positives, overbroad exception catches, disabled cases, and conditional
paths that can skip the only meaningful check. Never delete or weaken assertions to pass a suite.
Add a production fix only when the user requested a fix or it is already within the authorized scope.

## Execute and report

1. Run the smallest relevant command from its documented working directory.
2. Confirm discovery selected the intended tests and that a nonzero number executed.
3. Investigate failures; distinguish defects, bad assumptions, missing setup, and pre-existing failures.
4. Run the appropriate nearby suite and required checks for the final change.
5. Review the diff for unintended source, fixture, snapshot, or lockfile changes.

Preserve the command's real exit status when capturing output.
Use result files only when they belong to the current run and selected tests.
Keep passed, failed, expected-failure, skipped, and unrun outcomes distinct.
Do not assert that all tests passed because a command exited successfully with zero tests.

Summarize the behavior covered, changed test files, commands, counts when available, and limitations.
If execution is blocked, provide the exact missing prerequisite and the test command to resume.
Finish when the authorized tests are implemented and meaningfully verified, or when a concrete
external blocker prevents validation after useful independent checks have been completed.
