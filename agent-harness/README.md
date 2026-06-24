# Agent Harness

This folder contains portable agent assets. Copy into tool-native locations only
after reading each file.

## Skills

| Skill | Path | Use when |
| --- | --- | --- |
| Replication checker | `skills/replication-checker/SKILL.md` | Checking whether the project can run from a clean state |
| SDD | `skills/sdd/SKILL.md` | Running the Spec-Driven Development lifecycle |
| Hooks | `skills/hooks/SKILL.md` | Configuring postcondition hooks for Cursor, Claude Code, or Codex |
| Loop on verification | `skills/loop-on-verification/SKILL.md` | Running the execute-evaluate-revise loop until acceptance criteria are green |

## Subagents

| Subagent | Path | Use when |
| --- | --- | --- |
| PR reviewer | `subagents/pr-reviewer.md` | Reviewing a pull request for scope, reproducibility, and economics interpretation |
| SDD orchestrator | `subagents/sdd-orchestrator.md` | Managing the SDD lifecycle |
| Data reviewer | `subagents/data-reviewer.md` | Checking Card-Krueger panel balance, variable coding, and synthetic-data caveat |
| Literature reviewer | `subagents/literature-reviewer.md` | Verifying BibTeX completeness, citation accuracy, and overclaiming for CK literature |
| Loop verifier | `subagents/loop-verifier.md` | Evaluating one iteration of the execute-evaluate-revise loop |

## MCP servers

| Server | Path | Use when |
| --- | --- | --- |
| FRED | `mcp/fred/` | Fetching macroeconomic series from the St. Louis Fed database |

## Other assets

- `autonomous_agent_risk_card.md` — complete before connecting any autonomous agent to research files

## Tool path mapping

Copy harness assets into tool-native locations only after reading them:

| Tool | Skill path | Agent/subagent path |
| --- | --- | --- |
| Codex | `.agents/skills/<name>/SKILL.md` or current documented path | tool-native subagent/custom agent config or explicit role prompt |
| Claude Code | `.claude/skills/<name>/SKILL.md` | `.claude/agents/<name>.md` |
| Cursor | `.cursor/skills/<name>/SKILL.md` | `.cursor/agents/<name>.md` |
