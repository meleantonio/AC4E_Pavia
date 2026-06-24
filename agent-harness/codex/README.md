# Codex harness examples

Copy into project-native Codex locations after reading each file.

| Asset | Harness path | Project path |
| --- | --- | --- |
| Skills | `skills/<name>/SKILL.md` | `.agents/skills/<name>/SKILL.md` |
| Subagents | `agents/<name>.toml` | `.codex/agents/<name>.toml` |
| Hooks | `hooks/economics-hooks-example.json` | `.codex/hooks.json` |
| Hook scripts | `hooks/post_edit_did_analysis.py` | `.codex/hooks/` |
| MCP | `mcp/config.toml.example` | `.codex/config.toml` |

Trust hooks with `/hooks` in the Codex CLI after copying.

Invoke subagents by name in prompts, e.g. `Use data-reviewer to review the panel read-only.`

Official docs: [Codex subagents](https://developers.openai.com/codex/subagents), [Codex skills](https://developers.openai.com/codex/skills), [Codex hooks](https://developers.openai.com/codex/hooks).
