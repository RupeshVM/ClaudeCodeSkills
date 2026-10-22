---
name: release-plan
description: "Plan a software release, migration, rollout, readiness review, or rollback using the actual code changes and operational constraints. Use when preparing delivery of a feature or version; this skill produces a plan and does not deploy or publish."
argument-hint: "<release scope or comparison range> [target environment] [constraints]"
---

# Release plan

Prepare an executable release plan with evidence-based gates and recovery steps.
Use `$ARGUMENTS` to identify the change range, target, and constraints. Return the
plan in chat unless the user requests a repository artifact.

## Define the release

1. Read repository release instructions, deployment configuration, version policy,
   CI workflows, migration practices, and relevant operational runbooks.
2. Identify the current deployed version and proposed target only from supplied
   or accessible evidence. Mark unknown versions rather than assuming them.
3. Inspect the proposed diff or change list. Separate application changes,
   schema/data migrations, infrastructure, configuration, dependencies, and API
   contracts so their sequencing and compatibility can be assessed.
4. Identify release owners, consumers, environments, maintenance constraints,
   approval requirements, and the artifact to be deployed. Use roles when no
   person has been designated; do not invent names or commitments.
5. Establish success measures, acceptable degradation, and the rollback decision
   owner. If thresholds are unknown, propose measurable thresholds for review
   rather than treating guessed numbers as established policy.

Ask only for information that prevents a useful plan. Continue independent diff
analysis and list unresolved inputs with their effect on the release decision.

## Analyze compatibility and irreversible work

- Check whether old and new application instances can coexist during rollout.
- Inspect added, removed, or renamed API fields, events, configuration variables,
  permissions, and dependency requirements for affected consumers.
- For database changes, identify locks, table size assumptions, backfills,
  transaction boundaries, and whether expansion and contraction must be staged.
- Distinguish schema rollback from data restoration. A reverse migration may
  discard data and must not be described as a safe recovery step without proof.
- Check background jobs, queue payloads, caches, feature flags, client versions,
  and integration behavior across the version boundary.
- Identify secrets and access requirements by name and destination, without
  copying values into plans or configuration examples.

## Build the plan

Read [the release template](references/release-template.md), then make each step
concrete: responsible role, artifact or command, prerequisites, expected result,
and the evidence needed to proceed. Use repository-supported commands; mark
unknown commands as unresolved rather than inventing deployment interfaces.

1. **Prepare:** create immutable artifacts, record versions, confirm dependencies,
   backups where appropriate, observability, access, and recovery prerequisites.
2. **Validate in staging:** exercise representative user paths, integration
   contracts, migration behavior, and failure recovery under relevant conditions.
3. **Decide readiness:** list required gates and evidence; distinguish required
   checks from optional observations. Record a failed or unrun gate honestly.
4. **Roll out:** sequence dependent changes, flags, canary cohorts, observation
   windows, and wider exposure. Specify which metrics or functional checks gate
   each phase. Keep proposed thresholds visibly provisional until agreed.
5. **Verify:** confirm deployed version and representative functionality, errors,
   latency, data correctness, background processing, and affected consumers.
6. **Recover:** state the trigger, decision owner, compatible rollback artifact,
   ordered actions, data implications, and verification after recovery.
7. **Close:** define the monitoring period, deferred cleanup, flag removal,
   migration contraction, documentation, and follow-up ownership.

Prefer a simpler rollout for low-risk reversible changes; do not add elaborate
canary machinery unsupported by the platform or disproportionate to the change.

## Validate the plan without executing a release

- Confirm referenced scripts and configuration paths exist and match the target.
- Reconcile the plan with actual test and CI results. Do not infer staging or
  production success from local checks.
- Use bounded read-only checks and safe existing local validation when useful.
- Check that recovery prerequisites exist before labeling rollback available.
- Trace every required gate to an owner and observable evidence; mark gaps.

Do not deploy, run production migrations, toggle production flags, tag a release,
publish packages, or send release communications from this planning request.
Explicitly requested execution is a separate scoped operation requiring the
relevant authority, access, and verified preconditions.

## Finish

Return the staged plan, required readiness evidence, recovery route, and concrete
open decisions. State whether evidence supports proceeding or which unresolved
gates prevent that conclusion. A complete plan is not proof that a release ran.
