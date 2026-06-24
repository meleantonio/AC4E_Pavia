# Codex examples for AC4E Pavia

Project-scoped Codex configuration mirroring the Cursor examples in `.cursor/`.

Verify paths and UI labels in your installed Codex version before a live demo.

## Layout

| Asset | Path | Notes |
| --- | --- | --- |
| Custom subagents | `.codex/agents/*.toml` | TOML manifests; invoke by name in prompts |
| Hooks | `.codex/hooks.json` or `.codex/hooks/hooks.json` | Copy one file to `.codex/hooks.json` at repo root |
| Hook scripts | `.codex/hooks/*.py` | Called from `hooks.json` |
| Project config | `.codex/config.toml` | MCP servers, feature flags |
| Skills | `.agents/skills/<name>/SKILL.md` | Codex discovers repo skills here (not under `.codex/`) |

## Skills

Codex scans `.agents/skills/` from the working directory up to the repository root.
This repo includes:

- `sdd` — Spec-Driven Development lifecycle
- `replication-checker`, `hooks`, `loop-on-verification` — from `agent-harness/codex/skills/`

Invoke explicitly with `$skill-name` or let Codex match on the skill description.

## Subagents

Example prompt:

```text
Use the data-reviewer subagent to review examples/card-krueger-toy/ in read-only mode.
```

Official docs: [Codex subagents](https://developers.openai.com/codex/subagents).

## Hooks

1. Copy `.codex/hooks/hooks.json` to `.codex/hooks.json` (or merge entries).
2. Run `codex` and open `/hooks` to review and trust hook definitions.
3. Make a safe edit to `examples/card-krueger-toy/src/did_analysis.py` and confirm pytest runs.

Official docs: [Codex hooks](https://developers.openai.com/codex/hooks).

## MCP

See `agent-harness/codex/mcp/config.toml.example` for the workshop FRED server.
Register with `codex mcp get fred` after editing `.codex/config.toml`.

## Portable harness

Tool-neutral teaching copies live in `agent-harness/codex/`. Copy into this tree
when you want project-native Codex files.
