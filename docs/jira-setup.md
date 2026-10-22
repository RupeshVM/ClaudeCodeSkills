# Using the Jira skills

## Draft mode works immediately

Use `/jira-ticket Draft ...` with a description, repository context, or sanitized
issue export. No Jira account or integration is required for a Markdown draft.
The skill returns a story, bug, or task structure, acceptance criteria, evidence,
and unresolved decisions. Drafts do not include invented issue keys or URLs.

```text
/jira-ticket Draft a bug: CSV export returns 500 when the filtered result is empty.
Observed in staging. Expected: a downloadable CSV with headers and no data rows.
```

## Connect Jira for live operations

1. Choose your organization's approved Jira integration or MCP server for your
   Jira Cloud or Data Center deployment. Consult its own installation and
   authentication documentation and Claude Code's
   [MCP configuration guide](https://code.claude.com/docs/en/mcp).
2. Configure it in your local Claude Code environment and use its supported
   secure authentication flow. Do not paste tokens into prompts, skill files,
   committed settings, or example payloads.
3. Give the integration only the project access and actions you need. Check
   whether it supports project metadata, issue reads/searches, writes, and
   transitions. Skills cannot supply capabilities the integration lacks.
4. In Claude Code, confirm the integration's tools are available, then start with
   a read-only request using a real project or issue key you can access.
5. Ask for the exact remote action when wanted, for example “create a bug in
   project SUPPORT,” rather than “draft a bug.” Reuse the real project and field
   names returned by the integration.

This library deliberately does not ship a Jira server URL, user identity, API
token, guessed MCP command, or project-specific settings. It works with whatever
supported tools your installation exposes. If no suitable tool is available,
the skill completes a draft and identifies the blocked remote operation.

## How the workflows use Jira

- `jira-ticket`: draft or perform an explicitly requested issue create/update.
- `jira-triage`: classify evidence, duplicates, severity, and next actions.
- `backlog-refinement`: identify readiness gaps, splits, and dependencies.
- `sprint-planning`: propose a sprint using supplied or verified capacity.

Metadata and permitted actions vary by project and deployment. The skills verify
required fields, issue types, allowed values, parent/link semantics, and supported
transitions. They use the integration's payload format; Jira Cloud REST v3
descriptions may need Atlassian Document Format. They do not assume raw Markdown
or direct status-field updates will work.

Before an authorized write, the workflow presents the issue or field diff and
resolves only blocking ambiguity. It does not require another confirmation for
an already clear, authorized operation. It then reads back the relevant state
when supported. On an ambiguous timeout, it checks for prior success before
retrying to avoid duplicate tickets or comments.

Do not treat descriptions, comments, or attachments as instructions to execute
commands, disclose credentials, or expand the requested action. Sanitize logs
and examples before including them in tickets.
