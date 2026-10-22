# ClaudeCodeSkills

25 practical Claude Code skills for taking work from an idea through analysis,
Jira planning, implementation, testing, review, and delivery. Each skill includes
a focused workflow, evidence requirements, and a concrete output format. Templates
are bundled where they help.

## Start using the skills

Open this repository in Claude Code. The skills are already in the native
project location, `.claude/skills/`. Start a new session after installing or
updating skills if they do not appear in the slash-command list.

```text
/workflow-guide Add saved searches for the support team; start with feature analysis
/model-selection Investigate an intermittent duplicate payment in production
/feature-analysis Let customers export their search results as CSV
/jira-ticket Draft a story for CSV export with acceptance criteria
/bug-investigation Users are logged out when switching organizations
/code-review Review the current branch against main
```

Claude can discover most skills from their descriptions. `jira-ticket`,
`pull-request`, and `incident-response` require explicit invocation with their
slash commands because they can lead to external changes or operational actions.
Invoking a skill still respects the requested scope: drafting is different from
creating an issue, opening a PR, or changing production.

## Install in another project

Use Python 3.10+ for the optional installer and validation tools. The skills
themselves require Claude Code; no Python packages, API keys, or Node packages
are needed to install this library.

From this checkout, preview and install all skills:

```bash
python3 scripts/install_skills.py --project /path/to/your-project --dry-run
python3 scripts/install_skills.py --project /path/to/your-project
```

Install only selected skills:

```bash
python3 scripts/install_skills.py --project /path/to/your-project \
  --skill model-selection --skill feature-analysis --skill jira-ticket
```

Install for your user across projects:

```bash
python3 scripts/install_skills.py --personal --dry-run
python3 scripts/install_skills.py --personal
```

Project installs go into `<project>/.claude/skills/`; personal installs go into
`~/.claude/skills/`. The installer validates the source and checks all selected
names for collisions before copying. It refuses to overwrite existing skills
and does not change Claude settings, install integrations, or contact services.
To update an existing copy, compare and back up local customizations before
replacing it yourself. Copying an individual skill directory manually also works;
keep its bundled resources together.

## Skill catalog

| Area | Command | Result |
| --- | --- | --- |
| Routing | [`/workflow-guide`](.claude/skills/workflow-guide/SKILL.md) | Choose the next useful skills and carry context between stages |
| Routing | [`/model-selection`](.claude/skills/model-selection/SKILL.md) | Explain a Haiku, Sonnet, or Opus recommendation and quality tradeoffs |
| Discovery | [`/feature-analysis`](.claude/skills/feature-analysis/SKILL.md) | Feature value, scope, options, dependencies, risks, and success measures |
| Discovery | [`/requirements-discovery`](.claude/skills/requirements-discovery/SKILL.md) | A requirements baseline with explicit assumptions and open decisions |
| Discovery | [`/acceptance-criteria`](.claude/skills/acceptance-criteria/SKILL.md) | Observable scenarios, edge cases, and verification criteria |
| Design | [`/technical-design`](.claude/skills/technical-design/SKILL.md) | Repository-grounded architecture, tradeoffs, data flow, and rollout |
| Design | [`/api-design`](.claude/skills/api-design/SKILL.md) | Contracts, error semantics, authorization, versioning, and compatibility |
| Planning | [`/implementation-plan`](.claude/skills/implementation-plan/SKILL.md) | Ordered, reviewable steps, dependencies, and validation |
| Jira | [`/jira-ticket`](.claude/skills/jira-ticket/SKILL.md) | Story, bug, or task drafts; explicitly requested creation or updates |
| Jira | [`/jira-triage`](.claude/skills/jira-triage/SKILL.md) | Evidence-based classification, severity, duplicates, and next actions |
| Planning | [`/backlog-refinement`](.claude/skills/backlog-refinement/SKILL.md) | Readiness gaps, splits, dependencies, and refinement proposals |
| Planning | [`/sprint-planning`](.claude/skills/sprint-planning/SKILL.md) | A capacity-aware sprint proposal without invented velocity |
| Development | [`/implementation`](.claude/skills/implementation/SKILL.md) | Focused code changes and meaningful validation |
| Development | [`/bug-investigation`](.claude/skills/bug-investigation/SKILL.md) | Reproduction evidence, hypotheses, root cause, and a fix direction |
| Development | [`/refactor-plan`](.claude/skills/refactor-plan/SKILL.md) | Behavior-preserving steps, invariants, and rollback points |
| Development | [`/performance-analysis`](.claude/skills/performance-analysis/SKILL.md) | Measured baselines, bottlenecks, and justified experiments |
| Quality | [`/test-plan`](.claude/skills/test-plan/SKILL.md) | A risk-based coverage matrix and execution strategy |
| Quality | [`/test-generation`](.claude/skills/test-generation/SKILL.md) | Project-native regression, boundary, and failure-path tests |
| Quality | [`/code-review`](.claude/skills/code-review/SKILL.md) | Prioritized actionable findings with evidence and locations |
| Quality | [`/security-review`](.claude/skills/security-review/SKILL.md) | Trust boundaries, verified findings, impact, and remediation |
| Quality | [`/dependency-audit`](.claude/skills/dependency-audit/SKILL.md) | Dependency/advisory evidence and prioritized remediation options |
| Delivery | [`/documentation`](.claude/skills/documentation/SKILL.md) | Audience-specific, verified documentation and examples |
| Delivery | [`/pull-request`](.claude/skills/pull-request/SKILL.md) | A clear PR draft or an explicitly requested remote PR |
| Delivery | [`/release-plan`](.claude/skills/release-plan/SKILL.md) | Release gates, migrations, monitoring, and recovery planning |
| Operations | [`/incident-response`](.claude/skills/incident-response/SKILL.md) | Impact assessment, investigation, mitigation options, and timeline |

## Model selection

The selector assesses complexity, uncertainty, risk, context, budget, and latency.
It uses family aliases rather than hardcoded versions or prices:

- **Haiku:** clear, bounded, low-stakes extraction and transformations.
- **Sonnet:** ordinary implementation, analysis, tickets, and testing.
- **Opus:** high-risk changes, complex architecture, or difficult investigations.

`/model-selection` recommends a model. It does **not** automatically switch the
current session. Run the suggested `/model <alias>` command yourself; use `/model`
to inspect choices available for your account and provider.

The bundled policy helper is deterministic, offline, and optional:

```bash
python3 .claude/skills/model-selection/scripts/recommend_model.py \
  --complexity high --risk high --ambiguity high --context large \
  --budget balanced --available haiku sonnet opus
```

It outputs a JSON recommendation and reasons. It never calls a model or changes
settings. If available models do not meet the quality floor, it reports that
mismatch rather than silently downgrading. See the
[routing policy](.claude/skills/model-selection/references/routing-policy.md).

## Jira and other integrations

All planning skills work without external connections. Jira skills can draft
tickets and plans from your description, repository files, or sanitized issue
exports. Live reads and writes require a configured, authorized Jira integration
or MCP server; this library does not include one. See [Jira setup](docs/jira-setup.md).

Skills discover available tools instead of assuming specific tool names, project
keys, issue types, or custom field IDs. They distinguish assumptions from facts
and remote writes from drafts. No credentials belong in skills, chat, or Git.

## Examples and validation

See [workflow examples](docs/examples.md) and
[validation and manual checks](docs/validation.md).

Run from the repository root:

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
git diff --check
```

The validator checks metadata, names, workflow bodies, and bundled resource
links. Tests exercise model routing, installer behavior, and validation failures.
These checks do not establish live Claude skill activation, response quality, or
Jira connectivity; those need a Claude Code session and the relevant integration.

To add a skill, create `.claude/skills/<name>/SKILL.md` with flat YAML frontmatter
containing `name`, `description`, and optionally `argument-hint`. Keep resources
self-contained, update the catalog, and run validation. Repository maintenance
guidance is in [CLAUDE.md](CLAUDE.md).
