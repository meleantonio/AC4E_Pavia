# Agent Harness

Portable agent assets for **Cursor**, **Codex**, and **Claude Code**. Each tool
has a folder with the same economics workflows adapted to that tool's file formats
and discovery rules.

Shared MCP server code stays in `mcp/fred/` (one Python implementation; three
config examples).

## Tool folders

| Folder | Subagents | Skills | Hooks | MCP config |
| --- | --- | --- | --- | --- |
| `cursor/` | `subagents/*.md` | `skills/<name>/SKILL.md` | `hooks/economics-hooks-example.json` | `mcp/mcp.json.example` |
| `codex/` | `agents/*.toml` | `skills/<name>/SKILL.md` | `hooks/economics-hooks-example.json` | `mcp/config.toml.example` |
| `claude/` | `agents/*.md` | `skills/<name>/SKILL.md` | `hooks/settings.example.json` | `mcp/mcp.json.example` |

## Project-native locations (copy after reading)

| Tool | Skills | Subagents / agents | Hooks | MCP |
| --- | --- | --- | --- | --- |
| **Cursor** | `.cursor/skills/<name>/SKILL.md` | `.cursor/agents/<name>.md` | `.cursor/hooks.json` | `.cursor/mcp.json` |
| **Codex** | `.agents/skills/<name>/SKILL.md` | `.codex/agents/<name>.toml` | `.codex/hooks.json` | `.codex/config.toml` → `[mcp_servers.*]` |
| **Claude Code** | `.claude/skills/<name>/SKILL.md` | `.claude/agents/<name>.md` | `.claude/settings.json` → `"hooks"` | `.mcp.json` at repo root |

This repository also ships working examples at the repo root: `.cursor/`,
`.codex/`, `.claude/`, and `.agents/skills/`.

Verify UI labels, hook event names, and trust flows in your installed version.

## Skills (all tools)

| Skill | Use when |
| --- | --- |
| `replication-checker` | Checking whether the project runs from a clean state |
| `sdd` | Running the Spec-Driven Development lifecycle |
| `hooks` | Configuring postcondition hooks |
| `loop-on-verification` | Execute-evaluate-revise loop until acceptance criteria are green |

## Subagents (by tool)

| Role | Cursor / Claude (`.md`) | Codex (`.toml`) |
| --- | --- | --- |
| PR reviewer | `pr-reviewer` | `pr-reviewer.toml` |
| SDD orchestrator | `sdd-orchestrator` | `sdd-orchestrator.toml` |
| Data reviewer | `data-reviewer` | `data-reviewer.toml` |
| Literature reviewer | `literature-reviewer` | `literature-reviewer.toml` |
| Loop verifier | `loop-verifier` | `loop-verifier.toml` |

## MCP

| Server | Path | Use when |
| --- | --- | --- |
| FRED | `mcp/fred/` | Fetching macroeconomic series from FRED |

See `mcp/fred/README.md` for setup. Register per tool using the example in
`cursor/mcp/`, `codex/mcp/`, or `claude/mcp/`.

## Other assets

- `autonomous_agent_risk_card.md` — complete before connecting any autonomous agent to research files

## Documentation

- Participant mapping: `GUIDE.md` § Agent harness by coding agent
- Tool lanes: `tool-lanes/codex-app.md`, `tool-lanes/claude-app.md`
