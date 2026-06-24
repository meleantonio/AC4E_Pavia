# Tool Lane - Claude Code App

Use this lane if you prefer Anthropic's Claude Code desktop/app surface.

## Setup

1. Install and sign in to Claude Code.
2. Open this folder in the Code/project surface.
3. Create `CLAUDE.md` if your workflow needs it:

   ```markdown
   # Claude Code Instructions

   Follow the shared project instructions in @AGENTS.md.
   ```

4. Ask Claude to summarize the project instructions without editing files.

## Workshop Pattern

- Keep `AGENTS.md` as the shared course instruction source.
- Use `CLAUDE.md` as the Claude-specific adapter.
- Use checkpoint prompts for long-running work.
- Use `/agents` or project agent files when available for specialized review.
- Use skills only after reading `SKILL.md`.
- Review diffs and run tests before merging.

## Files To Use

- `AGENTS.md`
- optional `CLAUDE.md`
- `agent-harness/cursor/skills/replication-checker/SKILL.md`
- `agent-harness/cursor/subagents/pr-reviewer.md`

## Verify In Your Version

Claude Code app and CLI session histories may differ. Confirm current behavior
for skills, subagents, hooks, and goals in the installed version.
