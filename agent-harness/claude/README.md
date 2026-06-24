# Claude Code harness examples

Copy into `.claude/` at the repository root (this repo already includes live
examples in `.claude/`).

| Asset | Harness path | Project path |
| --- | --- | --- |
| Skills | `skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` |
| Subagents | `agents/<name>.md` | `.claude/agents/<name>.md` |
| Hooks | `hooks/settings.example.json` | `.claude/settings.json` |
| Hook scripts | `hooks/post_edit_did_analysis.py` | `.claude/hooks/` |
| MCP | `mcp/mcp.json.example` | `.mcp.json` at repo root |

Trust project hooks with `/hooks` after copying settings.

Official docs: [Claude Code skills](https://code.claude.com/docs/en/skills), [Claude Code hooks](https://code.claude.com/docs/en/hooks).
