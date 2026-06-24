# Cursor examples for AC4E Pavia

Project-scoped Cursor configuration for the workshop.

| Asset | Path | Notes |
| --- | --- | --- |
| Subagents | `.cursor/agents/*.md` | YAML frontmatter + role prompt |
| Skills | `.cursor/skills/<name>/SKILL.md` | Auto-discovered |
| Hooks | `.cursor/hooks/economics-hooks-example.json` | Merge into `.cursor/hooks.json` |
| MCP | `agent-harness/cursor/mcp/mcp.json.example` | Copy to `.cursor/mcp.json` |

Portable harness copies: `agent-harness/cursor/`.

Verify hook event names and UI labels in your installed Cursor version.
