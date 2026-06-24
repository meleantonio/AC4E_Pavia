# Tool Lane - Codex App

Use this lane if you want an OpenAI app-first workflow.

## Setup

1. Install and sign in to Codex.
2. Open this repository as the project folder.
3. Start a thread from the repo root.
4. Ask Codex to summarize active instructions:

   ```text
   Read AGENTS.md and START_HERE.md. Do not edit files. List the active project
   instructions and the setup verification command.
   ```

## Workshop Pattern

- Use read-only prompts before edits.
- Ask for a plan before multi-file work.
- Use `AGENTS.md` as the shared project instruction source.
- Use skills and subagents only after reading their prompt/instructions.
- Review `/diff` or the app diff before accepting edits.
- For longer work, use a goal/checkpoint workflow and stop at verification gates.

## Files To Use

- `AGENTS.md`
- `agent-harness/cursor/skills/replication-checker/SKILL.md`
- `agent-harness/cursor/subagents/pr-reviewer.md`
- `notes/orchestration_log.md`

## Verify In Your Version

Codex feature names and UI locations can vary by release. Confirm current labels
for goals, hooks, skills, and subagents before live demos.
