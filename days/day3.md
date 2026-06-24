# Day 3 - Orchestration, Autonomous Agents, Replication, Presentation

## Definition Of Done

- Use one skill or complete a logged skill-style workflow.
- Use one subagent/custom-agent role or complete a logged delegated review.
- Fill `agent-harness/autonomous_agent_risk_card.md`.
- Produce a prototype or documented blocker.
- Complete `replication/README.md`.
- Draft `templates/presentation_outline.md` or your own short presentation.
- Draft `templates/adoption_plan_30d.md`.
- Draft or review one hook configuration entry for your tool lane.
- Run at least one verification-loop iteration and record the verdict in
  `notes/orchestration_log.md`.
- Draft one goal file (Codex or Claude Code `/goal` format) with verifiable acceptance
  criteria for a Card-Krueger task.
- Inspect one plugin manifest (`plugin.json`) and explain what it adds to the workflow.

## Flow

| Time | Activity |
| --- | --- |
| 09:30-09:45 | Recap and integration goals |
| 09:45-10:15 | Demo: orchestration and replication protocol |
| 10:15-11:30 | Sprint: parallel execution and review |
| 11:45-12:30 | Autonomous agents: OpenClaw, Hermes, Eve |
| 13:30-14:30 | Sprint: replication packaging |
| 14:30-15:15 | Presentation and adoption plan |
| 15:15-15:30 | Final handoff |

## Read

- [`topics/03-agents-orchestration/reading.md`](../topics/03-agents-orchestration/reading.md)
- [`topics/04-replication-presentation/reading.md`](../topics/04-replication-presentation/reading.md)

## New In Day 3 (June 2026)

The following harness pieces have been added since the Milan edition. All are
anchored to the Card-Krueger running case.

| Asset | Path | What it adds |
| --- | --- | --- |
| data-reviewer subagent | `agent-harness/cursor/subagents/data-reviewer.md` | Panel balance, variable coding, synthetic-data caveat |
| literature-reviewer subagent | `agent-harness/cursor/subagents/literature-reviewer.md` | BibTeX accuracy, citation–claim matching, overclaiming check |
| loop-verifier subagent | `agent-harness/cursor/subagents/loop-verifier.md` | Execute-evaluate-revise loop for acceptance-criteria verification |
| hooks skill | `agent-harness/cursor/skills/hooks/SKILL.md` | Postcondition hook config for Cursor, Claude Code, Codex |
| loop-on-verification skill | `agent-harness/cursor/skills/loop-on-verification/SKILL.md` | Structured loop protocol with escalation rules |
| Goals examples | `examples/card-krueger-goals/` | Three worked goal files (robustness, figure, audit) |
| Swarm example | `examples/card-krueger-swarm/` | Four-stream swarm with issue templates and dependency graph |

## Do

Before any autonomous agent touches a repo, complete:

```text
agent-harness/autonomous_agent_risk_card.md
```

Then run or document the clean-run path in `replication/README.md`.

Exercises for today: [`exercises/day3-agent-workflows.md`](../exercises/day3-agent-workflows.md)
(Exercises 1–9; Exercises 6–9 are the new Day 3 additions for hooks, loops, goals,
and plugins).
