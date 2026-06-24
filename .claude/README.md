# Claude Code examples for AC4E Pavia

Project-scoped Claude Code configuration mirroring the Cursor examples in `.cursor/`.

Verify paths and hook event names in your installed Claude Code version before a live demo.

## Layout

| Asset | Path | Notes |
| --- | --- | --- |
| Subagents | `.claude/agents/<name>.md` | YAML frontmatter + role prompt |
| Skills | `.claude/skills/<name>/SKILL.md` | Auto-discovered from repo root upward |
| Hooks | `.claude/settings.json` | Project hooks; see `settings.example.json` |
| Hook scripts | `.claude/hooks/*.py` | Called from settings |
| MCP | `.mcp.json` at repo root | See `agent-harness/claude/mcp/mcp.json.example` |

## Skills

Included skills:

- `sdd` — Spec-Driven Development lifecycle
- `replication-checker`, `hooks`, `loop-on-verification` — from harness

Use `/skills` to browse. Invoke with `/skill-name` or let Claude match on description.

Official docs: [Claude Code skills](https://code.claude.com/docs/en/skills).

## Subagents

Example prompt:

```text
Use the data-reviewer subagent to review examples/card-krueger-toy/ read-only.
```

Agents in `.claude/agents/`:

- `data-reviewer`, `literature-reviewer`, `sdd-orchestrator`
- `pr-reviewer`, `loop-verifier` (from agent harness)

Official docs: Claude Code subagents in `.claude/agents/`.

## Hooks

1. Copy `.claude/settings.example.json` to `.claude/settings.json`.
2. Run `/hooks` and trust project hooks.
3. Edit `examples/card-krueger-toy/src/did_analysis.py` and confirm pytest runs.

Official docs: [Claude Code hooks](https://code.claude.com/docs/en/hooks).

## Verification loops

Load `loop-on-verification` skill and invoke `loop-verifier` agent for one
execute-evaluate-revise iteration. Record verdicts in `notes/orchestration_log.md`.

## Portable harness

Tool-neutral teaching copies live in `agent-harness/claude/`.
