# Day 3 Exercises - Agent Workflows And Orchestration

These exercises match `GUIDE.md` Part V. They introduce advanced agent
patterns only after a project, repo, and review workflow exist.

All exercises use the Card-Krueger DiD running case: fast-food employment in New
Jersey (NJ, treatment) and eastern Pennsylvania (PA, comparison), before and after
the April 1992 minimum wage increase. The data in this repository are **synthetic
teaching data** — no causal claim should follow from any exercise result.

Each exercise starts from acceptance criteria. Before beginning, state the acceptance
criteria you will use to judge whether the exercise is complete. This carries the Day 2
habit forward: acceptance criteria come first, then implementation.

## Exercise 1 - Use A Review Role On A Card-Krueger Diff

**Acceptance criteria for this exercise:**
- [ ] Review covers units (FTE employment), sample restriction (balanced panel), and
      the synthetic-data caveat.
- [ ] At least one blocker or one documentation gap is identified, or a clean verdict
      is recorded with evidence.
- [ ] An explicit merge or do-not-merge recommendation is stated.

Goal: separate implementation from review using the Card-Krueger DiD analysis as the
target.

Prompt:

```text
Read examples/card-krueger-toy/src/did_analysis.py and
examples/card-krueger-toy/README.md. Act as a read-only reviewer.
Check: (1) Is the unit of observation documented? (2) Is the sample restriction
stated? (3) Does the synthetic-data caveat appear? (4) Are any absolute paths
hardcoded? (5) Does the verification command in README.md match the actual file
structure? Return blockers first, then documentation gaps. Do not edit files.
```

Output to record:

- review findings with file references;
- open questions;
- one explicit merge or do-not-merge recommendation.

## Exercise 2 - Use The Replication-Checker Skill On The Card-Krueger Toy

**Acceptance criteria for this exercise:**
- [ ] The skill is invoked; each checklist step is applied to
      `examples/card-krueger-toy/`.
- [ ] A GREEN / YELLOW / RED verdict is stated with evidence.
- [ ] Any blocker names the exact file and line.

Goal: reuse a documented procedure.

Prompt:

```text
Use the replication-checker workflow in
agent-harness/cursor/skills/replication-checker/SKILL.md applied to
examples/card-krueger-toy/. Do not edit files. Identify the main entry point,
dependencies, hardcoded paths, private-data assumptions, expected outputs, and
readiness status. Assign a GREEN, YELLOW, or RED verdict.
```

Review check: the verdict should be about replication readiness (can the code
reproduce documented output?), not about whether the DiD identification is credible.

## Exercise 3 - Try Multiple Subagent Role Prompts

**Acceptance criteria for this exercise:**
- [ ] At least two subagent roles are tried (e.g. pr-reviewer and data-reviewer).
- [ ] The reviews differ: each role emphasises a different aspect of the work.
- [ ] A comparison note is recorded: what each role found that the other did not.

Goal: practice specialised review without losing control.

Task:

- Read `agent-harness/cursor/subagents/pr-reviewer.md` and
  `agent-harness/cursor/subagents/data-reviewer.md`.
- Paste each in turn as a role prompt in a read-only review of
  `examples/card-krueger-toy/`.
- Compare: which review caught the synthetic-data caveat? which checked panel balance?

Suggested prompts:

```text
[Paste pr-reviewer role here.]
Review examples/card-krueger-toy/. Do not edit files. Focus on scope, privacy,
reproducibility, and test evidence. Return blockers first.
```

```text
[Paste data-reviewer role here.]
Review examples/card-krueger-toy/data/toy_fast_food.csv and
examples/card-krueger-toy/src/did_analysis.py. Do not edit files. Return
blockers first, then documentation gaps.
```

Review check: the data-reviewer should flag the panel balance and variable coding;
the pr-reviewer should focus on scope drift and privacy.

## Exercise 4 - Orchestration Log For The Four-Stream CK Swarm

**Acceptance criteria for this exercise:**
- [ ] `notes/orchestration_log.md` contains one row per stream (A–D from the swarm
      example).
- [ ] Dependencies and merge order are explicit (Stream C blocked by A and B; D
      blocked by C).
- [ ] Each row names the reviewer subagent.

Goal: coordinate more than one stream using the Card-Krueger swarm as the template.

Read `examples/card-krueger-swarm/README.md` and the issue templates in
`examples/card-krueger-swarm/issues/`. Then run:

```text
Read examples/card-krueger-swarm/README.md. Plan the four-stream Card-Krueger
swarm in notes/orchestration_log.md. For each stream: branch name, linked issue
template, dependency label, reviewer subagent, and merge order. Do not implement
any stream. Mark dependencies and merge order explicitly.
```

Review check: Stream C must be listed as blocked by A and B; D must be listed as
blocked by C. Merge order must be Wave 1 → Wave 2 → Wave 3.

## Exercise 5 - Autonomous-Agent Risk Card

**Acceptance criteria for this exercise:**
- [ ] All six risk-card fields are completed.
- [ ] One approval gate is named.
- [ ] One condition that would make the tool unacceptable is stated.

Goal: evaluate an autonomous agent tool before allowing it to run on the CK repo.

Prompt:

```text
Evaluate [tool] using agent-harness/autonomous_agent_risk_card.md applied to
the Card-Krueger DiD project. Identify read boundary (which files may be read),
write boundary (which files may be written), memory (does the tool persist state
across sessions?), execution environment (local or remote?), approval gate (when
does a human review?), and evidence trail (how is the run logged?).
Recommend: read-only, branch-isolated write use, or no use.
```

Output to record:

- completed risk card;
- one approval gate;
- one condition that would make the tool unacceptable for a project with restricted
  data.

## Exercise 6 - Configure And Trace A Hook

**Acceptance criteria for this exercise:**
- [ ] The hook configuration is identified (or drafted) for the participant's tool lane.
- [ ] The hook event type is named (e.g. `afterFileEdit`, `PostToolUse`).
- [ ] The verification command the hook would run is stated.
- [ ] The participant can describe what would happen if `did_analysis.py` were edited.

Goal: attach a postcondition listener to the Card-Krueger analysis script so that
the verification suite runs automatically after every edit.

Read `agent-harness/cursor/skills/hooks/SKILL.md`. Then:

1. Identify which tool lane you are using (Cursor, Claude Code, or Codex).
2. Find the hook configuration path for your tool (listed in the skill file).
3. Draft the hook entry that would fire `python3 -m pytest examples/card-krueger-toy/tests`
   after any edit to `examples/card-krueger-toy/src/did_analysis.py`.

Prompt:

```text
Read agent-harness/cursor/skills/hooks/SKILL.md. I am using [tool]. Draft the hook
configuration entry that fires the Card-Krueger verification suite after any
edit to did_analysis.py. Use the format appropriate for my tool. Do not
configure hooks not documented in the skill file.
```

Review check: the hook command must reference the relative path
`examples/card-krueger-toy/tests`, not an absolute path. The hook must fire on edit,
not on every agent response.

Output to record:

- hook event type;
- hook command;
- which file the configuration would go into;
- what output you would expect to see if the hook fired.

## Exercise 7 - Design And Run A Verification Loop

**Acceptance criteria for this exercise:**
- [ ] Acceptance criteria for the target task are stated before the loop starts.
- [ ] At least one loop iteration is recorded in `notes/orchestration_log.md`.
- [ ] A GREEN, YELLOW, or RED verdict is returned by the loop-verifier.
- [ ] The loop stops (GREEN or escalated blocker) within three iterations.

Goal: practice the execute-evaluate-revise loop using the loop-verifier subagent.

Read `agent-harness/cursor/skills/loop-on-verification/SKILL.md` and
`agent-harness/cursor/subagents/loop-verifier.md`. Choose one of:

- The robustness-checks task from `examples/card-krueger-goals/goals/ck-robustness-checks.md`.
- The parallel-trends figure task from `examples/card-krueger-goals/goals/ck-parallel-trends-figure.md`.

Then run the loop: implement, evaluate with the loop-verifier, revise if YELLOW/RED,
repeat until GREEN or maximum three iterations.

Prompt (evaluation step):

```text
[Paste loop-verifier role here.]
The target task is [goal name]. The acceptance criteria are [list]. Evaluate the
current state of the work against each criterion. Run
python3 -m pytest examples/card-krueger-toy/tests and report the output. Return
GREEN, YELLOW, or RED with evidence.
```

Output to record (in `notes/orchestration_log.md`):

- task name;
- iteration number;
- loop-verifier verdict;
- action taken.

## Exercise 8 - Write A Goal File For The Card-Krueger Project

**Acceptance criteria for this exercise:**
- [ ] A goal file exists with at least the fields: name, description, acceptance
      criteria, constraints.
- [ ] Acceptance criteria are verifiable (pytest passes, file exists, number appears
      in output) — not vague.
- [ ] The constraints section prohibits modifying raw data and prohibits causal claims
      from synthetic data.

Goal: author a well-structured goal definition that a coding agent could act on
autonomously.

Read `examples/card-krueger-goals/README.md` and one of the worked goal files in
`examples/card-krueger-goals/goals/`. Then draft a new goal for a task of your
choosing — for example, a summary statistics table, a third robustness check, or a
formatted output section.

Use the goal-file anatomy from the README:

| Field | Guidance |
| --- | --- |
| `name` | One line; matches the research task |
| `description` | What should be true when done, in economic language |
| `approach` | Which files to edit, which method to use |
| `acceptance_criteria` | Checkbox list; each item must be mechanically verifiable |
| `constraints` | Raw data untouched; synthetic-data caveat required; scope boundary |

Write the goal file to `examples/card-krueger-goals/goals/ck-my-goal.md`.

Review check: every acceptance criterion must be answerable with a yes/no by running
a command or inspecting a file. Vague criteria ("the code is clean", "the output looks
good") should be replaced with specific ones ("pytest passes", "the word 'synthetic'
appears in the printed output").

## Exercise 9 - Explore A Plugin

**Acceptance criteria for this exercise:**
- [ ] The participant can name: what the plugin is, where its `plugin.json` lives, and
      what skill or rule it contributes.
- [ ] The participant can explain how one of the plugin's skills or rules would change
      their workflow on the CK project.
- [ ] No plugin is installed or configured without reading its manifest first.

Goal: understand how a Cursor plugin packages and distributes reusable skills and rules.

A Cursor plugin is a folder with a `plugin.json` manifest that declares skills, rules,
agents, and commands. It is a distribution mechanism — it lets you share a skill like
`replication-checker` or `literature-reviewer` across projects and teams.

Task:

1. Open the Cursor plugin panel (or navigate to `~/.cursor/plugins/`).
2. Find one installed plugin. Read its `plugin.json`.
3. Identify: plugin name, one skill or rule it provides, the file path of that skill.
4. Read the skill or rule.
5. Explain: if this plugin were installed in the CK project, what would it change?

Prompt:

```text
Read the plugin.json for [plugin name]. Do not edit files. Identify: plugin name,
declared skills (names and paths), declared rules (names and paths), and declared
agents. For each skill listed, read its SKILL.md and summarise what it does in
one sentence.
```

Output to record:

- plugin name and path;
- one skill or rule the plugin provides;
- how it would apply to the Card-Krueger DiD workflow.

---

## Extra Practice - Parallel Streams Without Scope Drift

Write three non-overlapping issues for the Card-Krueger swarm. Each issue must own a
different file set, name its dependencies, and state what evidence must come back
before integration. Use the issue templates in `examples/card-krueger-swarm/issues/`
as a model.
