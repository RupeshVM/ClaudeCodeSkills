# API contract: <capability>

## Purpose and consumers

- Business outcome:
- Consumer and actor:
- Existing behavior and evidence:
- Confirmed requirements:
- Assumptions or unresolved decisions:

## Operation

- Transport and operation name:
- HTTP method and path, if applicable:
- Preconditions:
- Authentication mechanism:
- Authorization and tenant boundary:

## Request

| Field or header | Type | Required / nullable | Validation or default |
| --- | --- | --- | --- |
| <field> | <type> | <rule> | <constraint> |

## Response

| Field | Type | Required / nullable | Meaning |
| --- | --- | --- | --- |
| <field> | <type> | <rule> | <meaning> |

## Failure behavior

| Condition | Status or result | Stable error code | Caller recovery |
| --- | --- | --- | --- |
| <condition> | <result> | <code> | <action> |

## Operational semantics

- Pagination, filtering, and ordering:
- Idempotency and retry behavior:
- Concurrency and consistency:
- Request size, rate, and timeout limits:
- Logging, privacy, and observability:

## Examples

Provide one valid request and response and representative errors using synthetic data. Ensure examples conform to the schemas above.

## Compatibility and delivery

- Existing consumers affected:
- Compatible extension or breaking change:
- Migration, versioning, or rollout:
- Contract tests and authorization tests:
- Decisions required before implementation:
