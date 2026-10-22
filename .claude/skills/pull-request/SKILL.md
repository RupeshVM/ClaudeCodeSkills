---
name: pull-request
description: "Prepare a focused pull request title, description, review summary, and validation evidence, or create a draft PR when the user explicitly requests it. Use after implementing a change or when asked to open or describe a PR."
argument-hint: "<change or branch> [base branch] [draft-only or create]"
disable-model-invocation: true
---

# Pull request

Turn the actual final diff into a reviewable pull request. Treat `$ARGUMENTS` as
the requested scope; distinguish writing PR text from creating a remote PR.
Default to a draft title and body in chat unless the user requests creation.

## Establish repository state

1. Read applicable repository instructions and PR/contribution templates.
2. Inspect the working tree, staged changes, current branch, recent commits, and
   relevant remotes. Preserve pre-existing files and changes.
3. Determine the intended base from the user's request, repository configuration,
   or an existing PR. Do not assume the base is named `main`.
4. Inspect both the committed branch diff against its merge base and any local
   changes relevant to the requested task. Record which changes are not committed.
5. Check whether a PR already exists for this branch before creating another.
   Use available service tools or an installed CLI; do not invent API tool names.

Do not expose credential-bearing remote URLs. A request to open or create a PR
authorizes the necessary non-destructive branch, commit, and push steps for the
requested changes. Preserve unrelated user work; do not include it in a commit.
An instruction to draft PR text authorizes none of those steps. Merging, closing
a PR, deleting branches, rewriting history, and force pushes require separate
explicit scope. If a required action is blocked, finish the accurate draft and
explain the specific prerequisite.

## Review what a reviewer will receive

- Read the entire relevant diff, including tests, migrations, configuration,
  generated artifacts, and dependency changes.
- Identify the concrete problem, its trigger, and the resulting behavior.
- Check for accidentally included secrets, debugging output, unrelated files,
  and generated artifacts that conflict with repository conventions.
- Identify compatibility changes, migration steps, operational effects, and
  material limitations that affect review or rollout.
- Distinguish unrelated existing changes from the requested work; do not silently
  rewrite or discard them to make a smaller PR.

If the diff contains an unresolved defect, report it concretely. Make corrective
edits only when authorized by the implementation task; do not hide a defect in
the PR description or claim the branch is ready when required checks fail.

## Validate the branch

1. Find the checks required by repository instructions, CI, and changed behavior.
2. Reuse relevant current results only when they apply to this exact change.
   Run missing appropriate checks when practical.
3. Record the exact commands and working directories, relevant test counts, and
   passed, failed, skipped, or unrun outcomes separately.
4. Explain a failure using evidence, distinguishing existing failures, defects,
   environment blockers, and uninvestigated outcomes.

Do not rerun every unrelated suite for a small change or replace meaningful
checks with a formatter result. Do not describe a CI run as passing before it
has completed successfully for the relevant commit.

## Write the title and body

Use the repository's template; otherwise adapt
[the PR template](references/pr-template.md). Lead with the concrete problem and
what the change does for users or maintainers. Include a before/after example
when useful. Explain design decisions only when they help assess the final diff.

Keep the title accurate and concise. Describe the final implementation rather
than the conversation, abandoned approaches, or an outdated initial scope.
Include validation evidence and unresolved limitations. Link only real issues,
commits, screenshots, or artifacts; never manufacture ticket identifiers.

## Create or update only when requested

1. Use the repository's existing authenticated integration. If CLI auth appears
   missing, verify the operation through the available supported authentication;
   a missing token variable or login state alone does not prove missing access.
2. Confirm the intended repository, head branch, base branch, and draft state.
   For a new PR requested without a readiness preference, prefer draft creation.
3. Ensure the remote head contains the changes described. Perform necessary
   authorized branch, commit, and push steps without asking again. If unrelated
   changes cannot be safely separated or access is denied, report the blocker
   with the completed PR text; do not discard or publish unrelated work.
4. Preserve exact Markdown newlines. With a CLI, write the body to a temporary
   file and pass `--body-file` rather than interpolating multiline shell text.
5. Re-read the created or updated PR and verify its URL, title, base, head, body,
   and draft state. A command request alone is not proof of creation.

Return the verified PR link when created; otherwise provide the ready-to-use
title and body. Include checks and concrete blockers without overstating readiness.
