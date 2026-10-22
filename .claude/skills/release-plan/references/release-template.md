# Release: <scope and target>

## Scope and evidence

- Current version: <verified version or unknown>
- Target artifact/version: <identifier and provenance>
- Change range: <verified comparison or supplied scope>
- Target environment and responsible roles: <details>
- User outcome: <observable behavior>
- Material assumptions and missing inputs: <details>

## Compatibility and sequencing

| Change | Dependency | Mixed-version behavior | Data or API impact |
| --- | --- | --- | --- |
| <change> | <precondition> | <supported/unsupported/unknown> | <effect> |

## Readiness gates

| Gate | Required evidence | Actual result | Responsible role |
| --- | --- | --- | --- |
| <check> | <functional outcome or metric> | <passed/failed/unrun> | <role> |

## Rollout steps

| Phase | Action / supported command | Expected result and gate | Owner |
| --- | --- | --- | --- |
| Prepare | <artifact/access/backup precondition> | <evidence> | <role> |
| Staging | <representative validation> | <evidence> | <role> |
| Initial exposure | <smallest supported cohort> | <metrics and observation window> | <role> |
| Expand | <next phase> | <gate> | <role> |

Mark proposed thresholds and commands needing confirmation explicitly.

## Recovery

- Trigger and decision owner: <observable condition and role>
- Recovery artifact and prerequisites: <verified details>
- Ordered actions: <including compatibility and data effects>
- Irreversible changes: <forward-fix or restoration strategy>
- Recovery verification: <functional and operational evidence>

## Follow-up

<Monitoring window, cleanup/flag removal, migration contraction, documentation,
open decisions, and responsible roles. Communications remain drafts unless sent
under an explicit user request.>
