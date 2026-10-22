---
name: requirements-discovery
description: Clarify vague requests into prioritized functional and nonfunctional requirements, explicit assumptions, open decisions, and a practical definition of ready.
argument-hint: "<request, feature idea, specification, or issue reference>"
---

# Requirements discovery

Convert an incomplete request into a useful requirements baseline without
turning every unknown into a blocker. Draft the result in chat; write files or
update external documents only when explicitly requested.

## Establish the available context

1. Read `$ARGUMENTS`, the conversation, applicable repository instructions, and
   relevant existing documentation, tests, and implementation entry points.
2. Restate the desired user outcome in plain language. Separate the underlying
   need from a suggested solution so both can be evaluated.
3. List actors and the decisions they need to make. Include service clients,
   administrators, and operators only when the workflow actually involves them.
4. Identify existing requirements that constrain this work. Attach source paths
   or links to requirements; mark user statements and assumptions explicitly.
   Do not treat historical behavior as proof that it must remain unchanged.

## Ask the questions that change the work

Group unknowns into user outcome, behavior, constraints, and release boundary.
Prioritize questions whose answers affect security, data loss, public contracts,
expensive commitments, or whether the solution solves the user's problem.

Ask no more than three focused questions at a time. Offer realistic options when
helpful, explain the consequence of each, and suggest a default for reversible
choices. Do not repeatedly ask questions already answered in the conversation.
Do not request credentials in chat; identify the secure configuration mechanism
only if access is necessary and not already available.

While waiting, continue repository inspection and prepare independent sections.
For a nonblocking unknown, state an assumption and how to verify it. For a
blocking unknown, state which specific decision or action cannot proceed and
why. Do not use a guessed answer to authorize an irreversible action.

## Build the requirements baseline

- Assign stable local IDs such as `FR-01` and `NFR-01`. These are document labels,
  not invented issue keys or tracker records.
- Write each functional requirement as an observable actor/system behavior.
  Keep independent requirements separate and avoid implementation prescriptions
  unless a real constraint requires them.
- Define inputs, outputs, state transitions, failure behavior, and permission
  boundaries. Clarify empty states, retries, duplicate requests, and concurrency
  where they affect the proposed capability.
- Record relevant quality requirements with a measurement method. If the target
  is unknown, record the question or a labeled proposal; avoid vague terms such
  as fast, secure, scalable, or user-friendly as acceptance conditions.
- State data ownership, collection, retention, deletion, sensitivity, and
  migration requirements when the feature handles persistent data.
- Prioritize requirements as must/should/could with a reason tied to user value,
  risk, or a release constraint. Treat priority as proposed unless supplied.
- Distinguish the first useful release from later work and explicit exclusions.

## Check coherence and readiness

Trace each requirement to an outcome or constraint and an observable acceptance
example. Remove contradictions or expose them as decisions. Look for unresolved
terms, incompatible priorities, hidden dependencies, and requirements that have
no clear actor or observable effect.

A requirement is ready for design when its intended behavior, scope, relevant
constraints, and material open decisions are clear enough to compare solutions.
Implementation may require more detail; do not label an entire specification
ready when one mandatory decision blocks it.

## Deliverable

Use [the requirements baseline template](references/requirements-baseline.md)
when presenting the result. Include the user outcome, prioritized requirements,
acceptance examples, scope exclusions, assumptions, and an open-question table.

Finish with the highest-value next step: targeted discovery, feature analysis,
technical design, or ticket drafting. Name any required answer precisely and
show which useful work can proceed independently. Do not create tracker issues,
publish documents, or implement the requirements as part of this skill alone.
