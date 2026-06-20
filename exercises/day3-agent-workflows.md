# Day 3 Exercises - Agent Workflows And Orchestration

These exercises match `GUIDE.md` Part V. They introduce advanced agent
patterns only after a project, repo, and review workflow exist.

## Exercise 1 - Use A Review Role

Goal: separate implementation from review.

Prompt:

```text
Act as a read-only reviewer for this diff. Check scope drift, reproducibility,
units, missingness, model assumptions, privacy, and overclaiming. Return
blockers first, then smaller issues, then any test gaps. Do not edit files.
```

Output to record:

- review findings with file references;
- open questions;
- one explicit merge or do-not-merge recommendation.

## Exercise 2 - Use A Skill-Style Workflow

Goal: reuse a procedure.

Prompt:

```text
Use the replication-checker workflow in
agent-harness/skills/replication-checker/SKILL.md. Do not edit files. Identify
the main entry point, dependencies, hardcoded paths, private-data assumptions,
expected outputs, and readiness status.
```

Review check: the answer should be about replication readiness, not research
validity.

## Exercise 3 - Try A Subagent Role Prompt

Goal: practice specialized review without losing control.

Task:

- read `agent-harness/subagents/pr-reviewer.md`;
- paste it as a role prompt in a read-only review;
- compare the review to your own checklist.

Suggested prompt:

```text
Use the PR reviewer role below. Review the current branch against AGENTS.md.
Do not edit files. Focus on scope, privacy, reproducibility, and test evidence.
```

Review check: the role prompt should not authorize file edits by itself.

## Exercise 4 - Orchestration Log

Goal: coordinate more than one task.

Update `notes/orchestration_log.md` with:

- task;
- branch;
- agent or tool used;
- reviewer;
- verification result;
- merge decision.

Prompt:

```text
Plan three workstreams for this project: data or model inputs, analysis or
simulation, and write-up or presentation. Mark dependencies, handoff files,
review checks, and merge order. Do not implement.
```

Review check: dependencies and merge order should be explicit.

## Exercise 5 - Autonomous-Agent Risk Card

Goal: evaluate an autonomous tool before using it.

Prompt:

```text
Evaluate [tool] using agent-harness/autonomous_agent_risk_card.md. Identify
read boundary, write boundary, memory, execution environment, approval gate,
and evidence trail. Recommend read-only, branch-isolated write use, or no use.
```

Output to record:

- completed risk card;
- one approval gate;
- one condition that would make the tool unacceptable.

## Extra Practice - Parallel Streams Without Scope Drift

Write three non-overlapping tasks for agents or collaborators. Each task must
own a different file set, name dependencies, and say what evidence must come
back before integration.
