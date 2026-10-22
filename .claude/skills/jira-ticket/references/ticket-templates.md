# Ticket templates

Replace placeholders with evidence. Omit irrelevant sections rather than filling them with generic text.
Keep `Unknown` or `To confirm` visible when a fact is unavailable.
These are Markdown drafts; the Jira integration determines the actual remote description representation.

## Story

**Summary:** [Actor can achieve outcome under relevant condition]

**Project / issue type:** [Verified values, or to confirm]

**Problem and value:** [What the actor cannot do today and why the outcome matters]

**Story:** As [actor], I want [capability], so that [value].

**Scope:** [Included behaviors]

**Out of scope:** [Explicit boundaries]

**Acceptance criteria:**

- Given [state], when [action], then [observable result].
- Given [relevant boundary or failure], when [action], then [expected handling].
- [Applicable permission, accessibility, data, or compatibility requirement.]

**Dependencies and risks:** [Verified links and unresolved dependencies]

**Open decisions:** [Decision, owner if known, and why it matters]

**Validation:** [How the criteria will be demonstrated]

## Bug

**Summary:** [Observable failure] when [specific trigger]

**Environment:** [Version, platform, configuration; no credentials or personal data]

**Impact and frequency:** [Affected users or operations, known frequency, evidence]

**Steps to reproduce:**

1. [Required initial state.]
2. [Minimal trigger.]
3. [Observation point.]

**Actual:** [Observed behavior, sanitized logs or references]

**Expected:** [Established requirement or current assumption to confirm]

**Acceptance criteria:** [Failure no longer occurs; applicable regressions and error handling]

**Workaround / investigation:** [Only verified workarounds; label hypotheses]

## Engineering task

**Summary:** [Concrete action and deliverable]

**Reason:** [Problem, prerequisite, maintenance need, or agreed technical outcome]

**Deliverables:** [Bounded artifacts or changes]

**Constraints and dependencies:** [Compatibility, rollout, access, and linked work]

**Completion checks:** [Commands, observable behavior, reviewable artifacts, or operating evidence]

**Estimate:** [Unset, or provisional value with units, method, and uncertainty]

## Proposed remote change record

**Operation / destination:** [Create or update; verified project or issue]

**Fields / transition / comment:** [Only changes explicitly within the user's request]

**Execution:** [Not requested, pending prerequisite, succeeded, failed, or uncertain]

**Verification:** [Readback result; verified issue key and URL if available]
