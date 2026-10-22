# Example workflows

These prompts illustrate intended use. They are not transcripts or evidence of
live integration testing. Supply the real repository context and constraints;
do not substitute production secrets or sensitive customer records.

## From an idea to delivery

```text
/feature-analysis Support agents need saved searches they can share within a team.
Assess value, minimum scope, tenancy risks, dependencies, and unknowns.

/requirements-discovery Refine the saved-search proposal into requirements.
Use the analysis above and identify decisions that affect implementation.

/acceptance-criteria Define testable criteria for private and team-shared searches,
including authorization, deletion, invalid filters, and concurrent edits.

/technical-design Design this in the current repository. Compare a minimal
approach with alternatives and explain the migration and rollout.

/implementation-plan Break the chosen design into reviewable steps with tests.

/jira-ticket Draft stories for those steps. Do not publish them to Jira.
```

Use only the stages needed. If requirements and design already exist, start at
implementation rather than regenerating every artifact.

## Choose a model

```text
/model-selection Extract supplied ticket titles into a fixed table; low stakes,
no interpretation needed, and low latency matters.

/model-selection Investigate cross-tenant authorization failures in production.
We need correctness and evidence; budget is secondary.
```

Expect an explainable recommendation, availability caveats, and a `/model` command
to run. The first task typically fits Haiku; the second sets an Opus quality
floor. The skill does not silently switch the conversation's model.

## Work with Jira

```text
/jira-ticket Draft a bug for duplicate export jobs. Include reproduction gaps
and leave project-specific fields unset if metadata is unavailable.

/jira-ticket Create that bug in the project I supplied, using the connected Jira
integration. Preserve the acceptance criteria from the draft.

/jira-triage Analyze the supplied backlog export and recommend priorities.
Do not update any issues.

/sprint-planning Propose a sprint from these ready stories using the team capacity
I supplied. Keep estimates in the team's existing unit and identify blocked work.
```

The create request requires a usable integration and a known destination. A
planning prompt does not authorize assignments, notifications, or sprint changes.

## Build and verify a change

```text
/implementation Add the approved CSV export behavior using the existing job
runner and API conventions. Preserve the current uncommitted changes.

/test-generation Cover empty exports, expired permissions, retries, and duplicate
job submission using the existing test framework.

/code-review Review the implementation diff against the agreed base. Prioritize
correctness and regressions; cite affected files and lines.

/security-review Review export authorization and tenant isolation. Separate
confirmed findings from risks that need more evidence.
```

Expect actual code changes only for the implementation/test requests, and real
test outcomes. Reviews return findings rather than silently rewriting code.

## Diagnose before changing code

```text
/bug-investigation Export jobs sometimes run twice. Reproduce in local tests,
compare hypotheses, and report the root cause before suggesting a fix.

/performance-analysis Investigate the slow saved-search endpoint. Establish a
representative local baseline and identify evidence for the main bottleneck.

/dependency-audit Review the current lockfile for relevant security and support
risks. Do not upgrade dependencies or rewrite the lockfile.
```

## Prepare delivery and operations

```text
/documentation Update the export API docs and examples to match the implementation.

/pull-request Draft a PR title and body for the current diff. Do not publish it.

/release-plan Plan a staged rollout including data compatibility, readiness gates,
monitoring, and recovery. Do not deploy.

/incident-response Assess the supplied incident timeline and sanitized logs.
Use read-only investigation and propose mitigations; do not execute changes.
```
