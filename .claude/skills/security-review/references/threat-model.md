# Threat-model worksheet

## Scope

- Component or change:
- Relevant files, interfaces, and deployment assumptions:
- In-scope environments and authorized testing:
- Out-of-scope systems:
- Open questions:

## Assets and actors

| Asset | Required security property | Actors allowed to access it | Evidence |
| --- | --- | --- | --- |
| Concrete data or capability | Confidentiality / integrity / availability | Actual roles or owners | Source or assumption |

## Trust boundaries

| Entry point or flow | Caller trust | Destination trust | Untrusted inputs | Required controls | Observed implementation |
| --- | --- | --- | --- | --- | --- |
| Request or event | Actor | Component | Fields or bytes | Specific checks | File reference or unknown |

## Candidate attack paths

| Candidate | Attacker prerequisites | Controlled input | Path and violated property | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- |
| Concrete scenario | Access needed | Input | Causal sequence | Code or isolated test | Confirmed / suspected |

## Findings

For each actionable finding:

- Severity and rationale:
- Location:
- Trigger and attacker prerequisites:
- Security impact:
- Supporting evidence:
- Uncertainty or untested assumptions:
- Focused correction:
- Regression test and legitimate control case:

## Validation and limits

- Commands and current-run outcomes:
- Scanner versions and scopes, if used:
- Interfaces and controls not assessed:
- Missing capabilities or evidence:
- Concrete next action:
