---
name: dependency-audit
description: Audit a project's resolved dependencies for known vulnerabilities, support risks, and actionable upgrade paths without modifying manifests or lockfiles. Use for dependency security or maintenance assessments.
argument-hint: "<project or dependency scope> [security, maintenance, or license focus]"
---

# Audit dependencies

Assess the dependencies the project actually uses and separate confirmed advisory matches from uncertain exposure. Default to a read-only audit and a report in chat.

## Establish scope and sources

1. Read `$ARGUMENTS`, the user's focus, applicable repository instructions, dependency policies, and CI audit configuration.
2. Identify the ecosystem, package manager, toolchain pins, manifests, workspaces, lockfiles, and dependency groups in scope.
3. Record the relevant revision and lockfile state. Preserve existing user changes and do not regenerate or normalize lockfiles.
4. Distinguish direct, transitive, development, optional, build-time, and runtime dependencies when the ecosystem supports that information.
5. Inspect existing audit tools and scripts before selecting commands. Use the repository's pinned tooling and documented registries.

Do not install another package manager, add an audit dependency to the project, or run an install merely to obtain an audit report. If required tooling is absent, complete inventory and code-based analysis, then report the missing capability.

## Run supported read-only checks

- Use a native advisory command or established repository audit script only after checking its behavior and arguments.
- An audit may update an external advisory cache or retrieve public metadata. It must not change project manifests, lockfiles, or installed dependency versions.
- Avoid automatic remediation commands such as audit-fix, blanket upgrades, or lockfile refresh operations.
- Do not run untrusted package lifecycle scripts as part of an audit.
- If the tool needs a scratch file or database, use an appropriate ignored or external temporary path and preserve existing files.
- Respect configured registries, TLS verification, artifact integrity checks, and existing authentication. Never print tokens or dump credential files.
- Report a blocked registry or advisory source specifically; a network failure is not a clean security result.
- Keep the scanner's exit status and diagnostic output. Many scanners return a nonzero status for findings, which is different from a tool execution failure.

Record each tool version, command, scope, source, and execution time. If an advisory database has a known timestamp, include it. Do not imply an online scan occurred when only cached data was available.

## Interpret findings

For each material finding, determine:

1. The exact package identity, resolved version, ecosystem, and advisory identifier or authoritative source.
2. The affected version range and whether the resolved version falls within it.
3. The dependency path from the project to the vulnerable package, including separate copies at different versions.
4. Whether the dependency is shipped, executed in CI, used only during development, or conditionally included.
5. The vulnerable behavior and its prerequisites, such as attacker-controlled input, an exposed feature, platform, or configuration.
6. Evidence that the vulnerable path is used, evidence that it is not used, or the limits of available reachability analysis.
7. Available fixed versions, supported mitigations, and compatibility constraints.

An advisory match establishes a version-level finding; it does not prove exploitation or runtime reachability. Conversely, a development-only dependency can still matter when it executes in CI or handles untrusted files.

Deduplicate repeated reports by advisory and resolved package instance while retaining distinct dependency paths and deployment contexts that affect remediation.

## Rank actionable risk

Use published severity as one input, then explain exposure and impact in this project. Keep the following separate:

- **Confirmed affected version:** a reliable advisory applies to the resolved package.
- **Exposure evidence:** observed use, plausible use requiring investigation, or a demonstrated reason the vulnerable behavior is unreachable in the assessed scope.
- **Confidence:** the strength and limits of the evidence.
- **Priority:** the recommended order of remediation given impact, exposure, and operational constraints.

Do not relabel an advisory as harmless solely because a text search found no direct import. Transitive callers, framework integration, build steps, and dynamic loading may matter.

For maintenance checks, verify release and support information from authoritative sources where available. Do not infer abandonment from a single quiet release period. If license review was requested, report detected license metadata and missing evidence; do not invent organizational policy or provide a legal clearance claim.

## Propose remediation

1. Prefer a supported patch or compatible upgrade that removes the affected resolved instance.
2. For a transitive dependency, identify the direct parent upgrade or documented package-manager override mechanism, including compatibility risks.
3. Check that a proposed fixed version exists and satisfies the relevant advisory before recommending it as verified.
4. If no fix is available, describe an authoritative mitigation and its assumptions, or identify an unresolved blocker.
5. Specify the focused tests, build, and repeat audit needed to validate remediation.

Do not change dependencies, add overrides, remove packages, or suppress findings unless the user explicitly asks for remediation. Never recommend deleting the lockfile or disabling integrity verification as a fix.

## Deliver

Provide scope and tooling, actual scan outcomes, prioritized findings, dependency paths, evidence and confidence, proposed actions, and unassessed areas. Include advisory links when verified and useful.

Finish by checking that the audit left manifests, lockfiles, and tracked files unchanged. A report with no findings means only that the stated checks found no matching issues in their stated scope; it is not proof that all dependencies are secure.
