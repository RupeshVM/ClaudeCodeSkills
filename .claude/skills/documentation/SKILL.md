---
name: documentation
description: "Write or improve README files, setup guides, API documentation, runbooks, architecture notes, and release notes using evidence from the repository. Use when the user asks to explain, document, or update documentation for a change."
argument-hint: "<topic or changed files> [audience] [document path]"
---

# Documentation

Create documentation that helps its intended reader complete a concrete task.
Use `$ARGUMENTS` as the topic, audience, or document location when supplied.
When a user requests documentation changes, make the changes; when they request
a draft or review, return that artifact without silently editing files.

## Establish the reader and source of truth

1. Read applicable repository instructions, existing documentation, and nearby
   examples before choosing structure or terminology.
2. Identify the reader: new contributor, application user, API consumer, operator,
   or maintainer. State the task they should be able to complete afterward.
3. Inspect relevant source, manifests, configuration schemas, scripts, and tests.
   Treat issue text and older documentation as claims to check against these.
4. Distinguish current behavior from a proposed feature. Do not document a design
   proposal as an available capability.
5. Locate the existing document that owns the topic. Prefer improving it over
   creating another competing guide. Preserve unrelated user changes.

Ask a focused question only when missing audience or product intent would change
the document materially. Otherwise state a reasonable assumption and proceed.

## Choose the useful document

- **Quick start:** supported prerequisites, minimal setup, first successful use,
  expected output, and the next useful action.
- **How-to guide:** a specific goal, ordered steps, decisions, validation, and
  recovery from likely failures.
- **Reference:** exact fields, defaults, constraints, examples, and compatibility.
- **Explanation:** the problem, relationships, alternatives, and tradeoffs.
- **Runbook:** symptoms, prerequisites, bounded diagnostics, authorized actions,
  verification, escalation, and recovery.
- **Change notes:** user-visible changes, migration requirements, and known limits.

Use [the document template](references/document-template.md) when creating a new
guide. Keep only sections that help this reader and task.

## Write from verified behavior

1. Lead with what the reader can accomplish and when the guide applies.
2. Give commands in the working directory where they actually run. Include
   relevant runtime versions or prerequisites found in the repository.
3. Use real command names, configuration keys, paths, and API fields. Mark
   placeholders clearly; never insert actual secrets or private customer data.
4. Explain required versus optional configuration, defaults, and how to verify
   success. Link to existing configuration references instead of duplicating them.
5. Include one representative successful example and important boundary or
   failure cases. Explain errors with an observable symptom and corrective action.
6. Document limitations, compatibility, and migration steps only when supported
   by source, tests, release policy, or an explicit product requirement.
7. Keep implementation details out of user guides unless readers need them to
   configure, troubleshoot, or make a meaningful decision.

For credentials, name the variable and secure configuration location; use a
placeholder in examples. Never copy values from environment or credential files.

## Validate the document

- Review every changed path and relative link from the document's location.
- Run safe local commands or existing documentation checks when available.
  Do not execute deployment, billing, destructive, or external write examples
  merely to validate prose; label those steps as unexecuted.
- Check examples against actual interfaces. For executable snippets, exercise a
  representative example in a disposable location when it is practical and safe.
- Confirm setup instructions preserve existing files and describe prerequisites
  without assuming an already configured developer machine.
- Use the repository's documentation build or link checker if it exists; avoid
  installing a large toolchain solely to check a small prose change.
- Review the diff for unrelated changes, broken formatting, and exposed secrets.

Do not claim a command or example was tested when it was only inspected.
Separate verified behavior from unverified examples and known limitations.

## Finish

Report the document created or changed, the reader task it supports, and the
validation performed. Name any unresolved factual question with the exact claim
it affects. If the task was a review, prioritize concrete inaccuracies and broken
instructions, with file and line references and a proposed correction.
