---
name: feature-analysis
description: Analyze a proposed feature, user problem, scope, alternatives, dependencies, risks, and success measures before implementation or ticket breakdown.
argument-hint: "<feature idea, problem statement, or existing issue>"
---

# Feature analysis

Turn a feature request into an evidence-backed decision brief. This skill analyzes
the proposal; implementation, ticket creation, and external updates require a
separate user request. Produce the brief in chat unless a file is requested.

## Establish the problem

1. Treat `$ARGUMENTS` and the conversation as the starting request. Identify the
   intended user, their job, the current obstacle, and the desired outcome.
2. Read applicable repository instructions and relevant product documentation,
   implementation paths, tests, and existing requirements. Use connected issue
   or document tools only when they are available and relevant to this request.
3. Distinguish observed facts, supplied requirements, assumptions, and open
   questions. Cite repository paths or source links for material claims. Never
   invent customer research, usage data, stakeholder approval, or issue history.
4. Ask up to three questions only when their answers materially change the
   problem, audience, or constraints. Continue useful analysis with labeled
   assumptions when the missing information does not block it.

## Assess value and scope

- Describe the current user journey and the proposed change at its actual point
  of use. Include a concrete before/after example.
- Identify the primary user and affected secondary users, including operators,
  support staff, and administrators when applicable.
- Define the smallest useful release. Separate required behavior, optional
  improvements, and explicit exclusions. List work needed for the release to be
  usable, such as permissions, migration, accessibility, or observability.
- Capture functional constraints and relevant nonfunctional requirements:
  latency, availability, privacy, compliance, compatibility, and cost. Label
  unmeasured targets as proposed rather than established requirements.
- Avoid feature expansion that does not solve the stated problem. If the
  request bundles unrelated outcomes, expose the separable decisions.

## Compare approaches

Compare the current behavior and at least one realistic implementation approach.
Add a second implementation option only when it represents a meaningful choice.
For each, explain user value, complexity, operating cost, delivery uncertainty,
and reversibility. A configuration change or smaller workflow improvement may
be sufficient; do not assume new code is always necessary.

Map dependencies to evidence: affected components, data sources, integrations,
permissions, ownership, and sequencing. Mark owners as unknown when not supplied.
Identify risks by trigger, impact, mitigation, and the evidence needed to resolve
them. Keep required discoveries separate from optional refinements.

## Define success and a decision

1. Propose a primary outcome metric and relevant guardrails. State the unit,
   population, measurement window, baseline if known, and collection mechanism.
   Use `baseline unknown` when the data is unavailable.
2. Define observable acceptance examples covering the main path, an important
   failure path, and access restrictions where relevant.
3. Recommend proceed, run a discovery spike, revise scope, or defer. Explain the
   decisive evidence and what would change the recommendation.
4. Identify the next concrete action and unresolved decisions. Do not present
   uncertain estimates as commitments or assign work without authorization.

## Deliverable

Read [the feature brief template](references/feature-brief.md) when composing the
result. Scale it to the request; omit irrelevant sections and state why a material
section cannot yet be completed. Include:

- Problem, audience, desired outcome, and source evidence.
- Recommended release scope and exclusions.
- Options and decision rationale.
- Dependencies, risks, and proposed success measures.
- Acceptance examples, assumptions, and specific next actions.

The analysis is complete when a reader can decide whether to invest, see which
assumptions could change that decision, and identify the smallest useful next
step. If a mandatory decision remains unresolved, call the brief provisional
and name the exact missing evidence rather than fabricating certainty.
