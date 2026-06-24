# Topic 3 Reading - Agents, Skills, Subagents, Orchestration

Advanced agent work is not about letting the model run wild. It is about using
the right harness piece for the job.

## Harness Pieces

| Need | Use |
| --- | --- |
| Persistent rules | `AGENTS.md`, `CLAUDE.md`, Cursor rules |
| Repeated procedure | skill (`SKILL.md`) |
| Independent review | subagent/custom agent |
| Long isolated work | branch agent, cloud agent, or worktree |
| Many workstreams | GitHub issues and labels |
| New autonomous systems | risk card before execution |

## Tool Updates Checked June 18, 2026

- Codex: app, CLI, web, IDE, GitHub workflows, `AGENTS.md`, skills, subagents, hooks, goals.
- Claude Code: app, CLI, web, IDE, skills, subagents, hooks, goals/checkpoints, GitHub workflows.
- Cursor: Cloud Agents, subagents, Agent Skills, CLI, MCP, hooks, review surfaces, plugins.
- Other agents: use the same review discipline even when UI and terminology differ.

## Hooks

A hook is a postcondition listener: the agent tool fires a command when a specified
event occurs (file edit, shell execution, session stop). For economists:

- After editing `did_analysis.py` → run `pytest` automatically.
- After the agent stops → write a stop-event to the orchestration log.

Configuration paths:

| Tool | Config file | Event type |
| --- | --- | --- |
| Cursor | `.cursor/hooks.json` | `afterFileEdit`, `stop` |
| Claude Code | `~/.claude/settings.json` | `PostToolUse`, `Stop` |
| Codex | In-app Hooks section | Varies — verify in your version |

Worked example: `agent-harness/cursor/skills/hooks/SKILL.md`

## Verification Loops

A loop runs one evaluation after another on the same task until acceptance criteria are
met. It is not a swarm (which runs tasks in parallel). The pattern is:
implement → evaluate → revise → repeat (max three times).

Worked example: `agent-harness/cursor/skills/loop-on-verification/SKILL.md`
Evaluator: `agent-harness/cursor/subagents/loop-verifier.md`

## Goals and the `/goal` Command

A goal is a persistent task definition — name, description, approach, acceptance
criteria, constraints — that a coding agent retrieves across sessions. Goals serve the
same function as a GitHub issue, but they live inside the tool.

Good acceptance criteria in a goal are mechanically verifiable: pytest passes, a file
exists, a number appears in output. Vague criteria ("the code is clean") do not belong
in a goal file.

Worked examples: `examples/card-krueger-goals/goals/`

Official references:

- Claude Code goals: <https://code.claude.com/docs/en/goal>
- Codex goals: verify in your installed Codex version (feature names vary by release)

## Plugins

A Cursor plugin is a folder with a `plugin.json` manifest that packages skills, rules,
agents, and commands. It is a distribution mechanism for reusable harness pieces.

To inspect a plugin: navigate to `~/.cursor/plugins/` and read `plugin.json` for any
installed plugin. Look at the declared skills and rules.

Cursor plugin docs: <https://cursor.com/docs/plugins> (verify in your version)

## Swarm Orchestration — Card-Krueger Example

Worked example with four streams (data cleaning, literature, estimation, figure):
`examples/card-krueger-swarm/`

## Autonomous Agents

Read these as examples of where the field is moving:

- OpenClaw: <https://github.com/openclaw/openclaw>
- OpenClaw skills: <https://docs.openclaw.ai/tools/skills>
- Hermes Agent by Nous Research: <https://hermes-agent.nousresearch.com/>
- Eve by Vercel: <https://vercel.com/eve>

Eve is especially new in the public Vercel surface. Verify its current docs before
teaching from screenshots or live commands.
