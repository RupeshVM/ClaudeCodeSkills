---
name: implementation-plan
description: Break a scoped feature, fix, or technical design into ordered repository-specific changes, dependencies, meaningful validation, rollout, and reviewable milestones.
argument-hint: "<feature, bug, design, or issue reference>"
---

# Implementation plan

Turn an agreed outcome into a practical sequence of reviewable changes. This is
a planning workflow: do not implement, create external tickets, or deploy unless
the user also requests those actions. Draft the plan in chat by default.

## Inspect before planning

1. Read `$ARGUMENTS`, the conversation, applicable repository instructions,
   relevant requirements/designs, and the implementation and test paths likely
   to change. Inspect package scripts and CI for established checks.
2. Identify the observable behavior, acceptance criteria, exclusions, and
   required compatibility. Distinguish supplied requirements from assumptions.
3. Map the existing data flow and affected components. Cite existing paths;
   clearly label proposed new paths and verify their naming matches repository
   conventions. Do not claim a file or command exists without inspecting it.
4. Note dependencies: access, credentials, services, schema migrations, shared
   contracts, and external teams. Inspect names/presence only for credentials;
   never dump secrets or ask for values in chat.
5. Resolve contradictions that change the solution. Ask a focused question for
   a true blocker, while continuing work whose sequence is already clear.

## Build small, ordered changes

Create a dependency-ordered sequence, not a generic checklist. Each step should
have an observable outcome, affected files/components, prerequisites, concrete
changes, and a meaningful validation method. Prefer a vertical slice that can
be reviewed and exercised before broadening the implementation.

- Start with the smallest change that establishes the needed contract or
  behavior. Include a discovery spike only for an actual uncertainty and give
  it a decision-oriented exit condition.
- Sequence data and API changes for compatibility with old readers/writers and
  mixed-version deployments when relevant.
- Keep unrelated cleanup out of the feature plan. Include refactoring only
  when necessary to make the requested behavior safe or understandable.
- Identify work that can run in parallel and its shared interfaces. Do not
  assign overlapping files to parallel contributors without a coordination
  boundary.
- Separate source changes, local environment setup, generated artifacts,
  migrations, documentation, and release actions so ownership and validation
  are clear.
- Treat estimates as optional ranges with assumptions. Do not invent dates,
  velocity, staffing, or approvals.

## Plan validation proportional to risk

Map the acceptance criteria and likely regressions to the repository's existing
test, build, type-check, and functional verification commands. Use exact working
directories when commands differ across components.

Choose checks that can fail when the intended behavior is broken. A syntax
check, empty test selection, or process startup alone does not prove a feature
works. For straightforward reversible changes, avoid tests that merely repeat
implementation or add no useful failure signal.

Record required services, fixtures, credentials, and data isolation. Distinguish
checks to run during implementation from checks actually executed during this
planning task. Never report a planned command as passed.

## Plan review and release

Group steps into coherent review units with explicit dependencies. Include
documentation or contract changes needed by consumers and operators. Describe
rollout order, feature flag use where appropriate, readiness signals, and a
rollback/roll-forward strategy. Do not promise reversal of destructive data
changes without a recovery mechanism.

## Deliverable and completion

Read [the implementation plan template](references/plan.md) for the output.
Provide the goal, evidence-backed scope, ordered steps, validation matrix,
parallel work boundaries, risks, and release sequence. A small change may need
only a few steps; omit empty ceremony.

The plan is complete when an implementer can start the first unblocked step,
understand dependencies, and know what evidence will show each milestone works.
Name any blocked milestone and its prerequisite precisely. End with the next
executable step; do not claim implementation or release completion.
