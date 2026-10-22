---
name: model-selection
description: Recommend a Claude model for a task based on complexity, uncertainty, stakes, context, budget, and latency. Use for model choice, routing requirements, or deciding between Haiku, Sonnet, and Opus.
argument-hint: "[task or requirement, constraints, and available models]"
---

# Select a model for the work

Recommend an available model family and explain the decision. A skill cannot change
the model of the current conversation by writing an instruction. Do not claim that
selection or delegation happened unless the runtime confirms it.

## Inspect the task

1. Read the request, relevant project instructions, and a small representative
   sample of the affected code or requirements. Do not scan an entire repository
   merely to decide a model.
2. Identify the desired deliverable: extraction, ticket draft, feature analysis,
   implementation, debugging, review, or architecture decision.
3. Classify the following dimensions using concrete evidence:

   | Dimension | Values | Evidence |
   | --- | --- | --- |
   | Complexity | low / medium / high | Number of interacting components and decisions |
   | Risk | low / medium / high | Impact of a wrong answer, not urgency alone |
   | Ambiguity | low / medium / high | Missing requirements or competing explanations |
   | Context | small / medium / large | Necessary cross-file or cross-system reasoning |
   | Budget | balanced / low-cost / quality | User preference, not an invented spending cap |
   | Latency | normal / fast | Whether quick turnaround is an explicit constraint |

4. Treat authentication, payments, destructive migrations, production incidents,
   and security boundaries as high stakes. A short prompt can still be high risk.
5. Use supplied preferences. Otherwise assume medium complexity, medium risk,
   medium ambiguity, medium context, balanced budget, and normal latency; state
   only the defaults that materially affect the recommendation.

## Apply the routing policy

Read [the decision policy](references/routing-policy.md) for the exact rules and
examples. For a repeatable recommendation, run the bundled helper using its actual
path relative to this skill's directory:

```bash
python3 <skill-directory>/scripts/recommend_model.py \
  --complexity medium --risk low --ambiguity medium --context medium \
  --budget balanced --latency normal
```

Replace `<skill-directory>` with the resolved location of this skill; do not send
the literal placeholder to the shell. Arguments describe the assessment; the
helper does not understand natural language or inspect source code.

- Use Haiku for bounded, well-specified, low-stakes extraction or formatting.
- Use Sonnet as the default for implementation, test work, ticket writing with
  reasoning, and ordinary feature analysis.
- Use Opus for high risk, complex architecture, significant ambiguity, or broad
  reasoning across a large system.
- Cost or latency preferences may reduce a low-stakes choice. They do not silently
  reduce the quality floor on high-stakes work.
- Availability is account/provider specific. If the user supplies a verified
  list, pass `--available` followed by aliases from that list. Do not infer account
  access, exact model versions, token limits, prices, or provider IDs.
- If the required family is unavailable, report the mismatch. The helper returns
  a suggestion with `meets_quality_floor: false`; do not describe it as equivalent.
  If no supported alias is available, report that selection needs provider details.

## Apply the recommendation honestly

For an interactive Claude Code session, give `/model haiku`, `/model sonnet`, or
`/model opus` as the command the user can run. Ask them to use `/model` to inspect
the available choices if an alias is unsupported. Account configuration may map
aliases to different versions. Do not edit global settings, start paid API calls,
or change provider configuration merely to make a recommendation.

If the user has already authorized delegation and the installed runtime supports
a model option for subagents, select an available model through that runtime's
documented option. Keep integration, security decisions, and final verification
at the required quality level. Do not spawn nested model-selection tasks.

## Report and revisit

Return:

1. **Recommended family** and a one-sentence reason tied to the task.
2. **Assumptions and availability**, including any quality-floor mismatch.
3. **How to select it**, or the actual confirmed delegation if one was performed.
4. **Escalation trigger**: new cross-system dependencies, failed hypotheses,
   unresolved ambiguity, or higher risk. Explain why before increasing cost.

Example: a bug ticket assembled from supplied reproduction steps can use Sonnet;
a production authorization flaw warrants Opus plus concrete verification. A more
capable model does not replace tests, authorization, or missing evidence.
