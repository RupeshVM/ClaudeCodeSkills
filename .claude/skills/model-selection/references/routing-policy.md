# Model routing policy

Use stable family aliases rather than versioned model IDs. This is a local,
explainable heuristic, not a benchmark, pricing guarantee, or account capability
probe. The helper recommends a family; it does not call an API or switch a session.

Apply rules in order:

1. **Opus floor:** high risk or high complexity; high ambiguity combined with at
   least medium complexity; or large context combined with at least medium
   complexity. Recommend Opus even if low cost or fast output is requested.
2. **Haiku:** complexity, risk, and ambiguity are all low and context is small.
   This suits known-format transformations with a clear checkable result.
3. **Economy:** low complexity, low risk, no high ambiguity, and context smaller
   than large may use Haiku if low cost or fast output is explicitly preferred.
   An explicit quality budget takes precedence over fast latency and keeps the
   Sonnet default for this rule. It does not change the fully bounded rule above.
4. **Default:** Sonnet for other tasks.

Availability handling is separate. Without a list, availability is **unverified**.
With a list, retain the recommended family if possible. Otherwise choose the
least capable available family at or above the floor (Haiku < Sonnet < Opus).
If none meets it, report the strongest available family as an explicitly
inadequate fallback; do not silently treat it as suitable. An empty list means no
known available family and returns no selected alias.

| Requirement | Classification | Result |
| --- | --- | --- |
| Extract supplied titles into a fixed table | All low, small context | Haiku |
| Draft a story and identify missing acceptance cases | Medium complexity and ambiguity, low risk | Sonnet |
| Add an endpoint following an existing contract | Medium complexity, medium risk | Sonnet |
| Investigate intermittent payment duplication | High risk, high ambiguity | Opus |
| Compare designs for a shared authorization boundary | High complexity and risk | Opus |
| Reformat a large supplied document | Low complexity, low risk, large context | Sonnet; check actual context limits |
| Routine task with only Opus available | All low, small context, availability Opus | Opus; note cost tradeoff |
| High-risk task with only Haiku available | High risk, availability Haiku | Haiku reported below floor; request access or rescope |

Classify task risk separately from the model name. For example, a filename change
can affect a production migration, while a long text extraction can be low risk.
Do not infer exact context capacity from this table. Split large inputs only
where the task permits independent chunks and preserve the connections needed
for final validation.
