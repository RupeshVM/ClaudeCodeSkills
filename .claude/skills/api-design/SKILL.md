---
name: api-design
description: Design or review an API contract, including operations, schemas, authorization, errors, compatibility, and examples. Use before implementing a new endpoint or changing an existing integration.
argument-hint: "<capability, endpoint, or integration> [consumers and constraints]"
---

# Design an API contract

Produce a contract that callers and implementers can evaluate before code changes. Default to a design in chat; write or modify specifications only when requested.

## Discover the contract's context

1. Read `$ARGUMENTS`, the user request, applicable repository instructions, existing API specifications, and related endpoints or client code.
2. Identify the consumer, business operation, expected input, observable outcome, and authorization boundary.
3. Establish whether this is a new API, a backward-compatible extension, or a breaking change to a deployed contract.
4. Inspect local conventions for transport, naming, serialization, schema generation, authentication, pagination, errors, and versioning.
5. Separate confirmed requirements from assumptions. Ask only for decisions that materially change the contract and cannot be inferred from available context.

Do not invent product policy, data retention requirements, identifier formats, or service-level targets. Mark unresolved requirements and explain their effect on the design.

## Define operations

- Choose the repository's established transport unless the task explicitly calls for a different one. Explain any proposed change.
- Describe each operation's actor, purpose, resource or action, and preconditions.
- For HTTP, specify the method, path, request headers, request body, status codes, and response body. Avoid mutating state through a safe read operation.
- For events, RPC, or GraphQL, use the corresponding existing operation, message, or schema conventions instead of forcing an HTTP endpoint design.
- Distinguish required, optional, omitted, empty, and null values. Define defaults only when their behavior is known or deliberately chosen.
- State validation rules, bounds, enums, timestamps, units, and ordering guarantees. Include examples that satisfy those rules.
- Expose only fields the consumer needs. Avoid leaking internal storage details or sensitive identifiers.

## Cover cross-cutting behavior

For each applicable concern, state the contract and how it will be checked:

| Concern | Questions to resolve |
| --- | --- |
| Authentication | Which supported identity mechanism applies? What happens when it is missing or expired? |
| Authorization | Which actor can perform the operation on which object? How is tenant isolation enforced? |
| Errors | Which stable error codes, status codes, safe messages, and correlation identifiers are returned? |
| Pagination | Which cursor or offset scheme, page bounds, stable ordering, and continuation behavior apply? |
| Idempotency | Can the operation be retried? How are keys scoped, conflicts handled, and expiry defined? |
| Concurrency | Are conditional updates, versions, or conflict responses required to avoid lost writes? |
| Limits | Which request sizes, rate limits, timeouts, and response bounds are established? |
| Privacy | Which fields are sensitive? What must be excluded from responses and logs? |
| Compatibility | How will existing callers, old clients, unknown fields, and enum additions behave? |
| Observability | Which existing logs, metrics, and traces identify failures without exposing secrets? |

Use “not applicable” with a reason rather than inventing behavior for every row. Never document a guarantee the implementation or infrastructure cannot support.

## Work through failure cases

Check invalid input, missing authentication, forbidden access, an absent resource, a conflict, duplicate submission, dependency failure, partial success, and retry behavior where relevant.

For a write spanning multiple systems, identify the consistency boundary and how callers learn the final outcome. Explain compensation or recovery rather than implying an atomic transaction where none exists.

If the operation is asynchronous, define acknowledgement, a job or resource identifier, progress or completion lookup, terminal states, and cancellation semantics only when supported.

## Specify examples and validation

Read [the contract template](references/contract-template.md) when assembling the proposed contract. Adapt it to the actual transport and omit irrelevant sections.

1. Include one successful exchange and representative failure exchanges. Use synthetic, clearly non-sensitive example data.
2. Map business acceptance criteria to contract tests, schema tests, and authorization checks.
3. If an existing schema validation or generation command is available, run it when the user requested specification changes.
4. Check that examples agree with field names, required fields, nullability, status codes, and error definitions.
5. Assess compatibility against the current schema or known consumers. Report an unresolved compatibility question explicitly.

Do not claim an API is implemented or operational because a design or schema validates. Do not contact a live integration or publish documentation without the appropriate user request.

## Deliver

Present the proposed contract, the main design decisions and tradeoffs, a compatibility or rollout approach, and open questions that block implementation.

When useful, compare a small number of realistic alternatives and recommend one based on the repository's constraints. Keep speculative future capabilities out of the required contract.
