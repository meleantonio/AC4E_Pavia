# Guide Chapter 3: Agents, Skills, Subagents, MCP, and Orchestration

This chapter corresponds to the Day 2 afternoon introduction and the Day 3
execution block. It assumes you already have the basics: a repository, privacy
boundaries, a project brief, a design memo, and issues or at least a clear
task list. Advanced agent patterns are useful only when the work is already
structured.

## 3.1 Why Advanced Agent Work Comes After SDD

Skills, subagents, MCP, cloud agents, and swarms can multiply productivity.
They can also multiply confusion. If you have not defined the research
question, data or model inputs, acceptance criteria, and review gates, then
parallel agents will produce parallel ambiguity.

Before using this chapter, check:

- Do you know your main software lane?
- Are private or restricted paths documented?
- Does a project brief exist?
- Does a design memo or issue description exist?
- Do you know how to review the result?

If not, return to Chapters 1 and 2.

## 3.2 Choosing The Right Harness Piece

| Need | Use | Example |
| --- | --- | --- |
| General reasoning and coordination | main agent | explain repo, plan next issue |
| Repeated procedure | skill or saved workflow | replication checker |
| Specialized independent role | subagent or role prompt | PR reviewer, bibliographer |
| Structured access to tools/data | MCP | FRED, filesystem, database |
| Long isolated task | cloud agent or worktree | documentation pass on one branch |
| Multiple workstreams | issue-labelled orchestration | data, analysis, writing, review |
| Autonomous system | risk card first | OpenClaw, Hermes, Eve, other agents |

Do not use a more powerful mechanism when a read-only prompt would do.

## 3.3 Skills

A skill is a reusable workflow. It gives the agent a procedure to follow when
the task matches the skill description.

Good skills for economists:

- replication checker;
- literature mapper;
- data-contract checker;
- bibliography cleaner;
- table-note reviewer;
- model-assumption checker;
- paper-polisher;
- presentation critic.

Skill design rules:

- keep the description specific;
- keep the body concise;
- use checklists for repeatable tasks;
- add scripts only when mechanical checks are useful;
- validate the skill on a real artifact.

Example:

```markdown
---
name: replication-checker
description: Use when checking whether a research project can run from a clean
state, has declared dependencies, avoids hardcoded paths, and documents outputs.
---

When invoked:
1. Identify the main entry point.
2. Compare run instructions to actual files.
3. Check software and package dependencies.
4. Look for hardcoded paths, secrets, and private-data assumptions.
5. Report status: green, yellow, or red.
6. List blockers before recommendations.
```

Prompt:

```text
Use the replication-checker workflow. Do not edit files. Identify the main
entry point, dependencies, hardcoded paths, private-data assumptions, expected
outputs, and readiness status.
```

## 3.4 Subagents And Role Prompts

A subagent is a specialized role, often with its own context. If your tool does
not support file-backed subagents, use a saved role prompt.

### PR Reviewer

```text
You are a read-only reviewer for an economics research repository. Review this
diff for scope drift, path problems, dependency problems, data privacy issues,
units, missingness, standard errors or model assumptions, overclaiming relative
to the design, and replication README consistency. Return blockers first, then
suggestions. Do not edit files.
```

### Bibliographer

```text
You are a bibliography reviewer for academic economics. Check .bib entries for
missing fields, inconsistent keys, duplicate entries, uncertain publication
details, missing DOI or URL where relevant, and mismatches between citations
and bibliography. Do not invent bibliographic facts.
```

### Replicator

```text
You are a replication reviewer. Starting from the README, determine whether a
new user can run the project from a clean checkout. Check software versions,
data access, run commands, expected outputs, hardcoded paths, and limitations.
```

### Theory Or Model Checker

```text
You are a theory and computational-model reviewer. Check primitives,
assumptions, equilibrium conditions, parameter restrictions, solver settings,
and numerical checks. Flag claims that do not follow from the model as written.
```

## 3.5 MCP

MCP, the Model Context Protocol, lets agents use structured external tools.

Economics uses:

- FRED or macro data APIs;
- scoped filesystem access;
- database access for large panels;
- search tools;
- possible local bridges to R, Stata, MATLAB, or Julia.

Use MCP when:

- the task is repeated;
- official structured access reduces errors;
- the tool can be scoped safely;
- secrets can be handled through environment variables;
- the output can be documented.

Do not use MCP when:

- a one-time manual download is simpler;
- the tool would expose private folders unnecessarily;
- you cannot explain what access you are granting;
- no review evidence will remain.

Prompt:

```text
Using the configured FRED or data-source tool, fetch metadata for GDP,
CPIAUCSL, UNRATE, and FEDFUNDS. Do not estimate a model. Update the data map
with series IDs, source, frequency, units, coverage, and access notes.
```

## 3.6 Cloud Agents And Branch Isolation

Cloud or background agents are useful for longer isolated work. They are not a
substitute for review.

Good cloud-agent tasks:

- update documentation for one folder;
- add comments or docstrings without changing logic;
- run a literature-map draft;
- implement one well-scoped issue on one branch;
- check a replication README against files.

Bad cloud-agent tasks:

- "finish my project";
- "fix all issues";
- "analyze private data";
- "merge when done";
- "decide the research conclusion."

Safe prompt:

```text
Work on issue #12 only on branch agent/replication-readme. Edit only
replication/README.md and docs/data_source_map.md. Do not edit analysis code
or raw data. Open a PR with changed files and verification notes.
```

## 3.7 Swarm Orchestration

A swarm is several humans and/or agents coordinated toward one outcome. In this
course, swarms are organized through GitHub issues and labels, not through
unstructured chat.

Labels:

- `parallel`: can be done independently;
- `sequential`: should wait for earlier work;
- `blocked-by:#N`: depends on a specific issue;
- `ready-for-review`: needs review;
- `replication`: affects clean-run path;
- `writing`: affects paper or presentation.

Example streams:

| Stream | Deliverable | Handoff |
| --- | --- | --- |
| Data or inputs | clean data, data map, calibration file | `notes/handoff_data_to_analysis.md` |
| Analysis or simulation | estimates, moments, IRFs, tables | `notes/handoff_analysis_to_writeup.md` |
| Writing | method notes, result interpretation, slides | `notes/handoff_writeup_to_replication.md` |
| Review | consistency and replication checks | `notes/review_log.md` |

Planner prompt:

```text
Break this milestone into issue streams. Mark each issue as parallel,
sequential, or blocked-by another issue. For each issue, specify allowed files,
handoff artifact, review check, and merge order. Do not implement.
```

Review prompt:

```text
Review all ready-for-review streams. Check path consistency, units, variable
names, assumptions, output files, and replication README alignment. Return
blockers first.
```

## 3.8 Running Case: Card-Krueger Orchestration

Possible streams:

| Stream | Task | Depends on |
| --- | --- | --- |
| Literature | Map minimum wage references | none |
| Data map | Document public data and variables | none |
| Cleaning | Create clean analysis dataset | data map |
| Baseline estimate | Estimate DiD table | cleaning |
| Write-up | Draft method and limitations | design memo, baseline |
| Replication | Write clean-run README | all runnable pieces |

Agent prompts:

```text
Plan the Card-Krueger project streams. Use labels parallel, sequential, and
blocked-by. Include handoff files and review checks. Do not implement.
```

```text
Act as a read-only reviewer for the baseline estimate PR. Check whether the
treatment group, comparison group, post period, outcome units, and sample
counts match the design memo.
```

## 3.9 Hooks

A hook is a postcondition listener: the agent tool fires a command when a specified
event occurs, without a human having to ask. For economists, hooks solve a common
problem — you edit an estimation script, the agent continues, and several steps later
you discover the edit broke the verification suite. A hook catches this immediately.

### What hooks can do

| Hook event | Typical use in research |
| --- | --- |
| After file edit | Run the verification suite after editing the analysis script |
| After shell execution | Append a timestamped entry to the orchestration log |
| Session stop | Remind the researcher to review the diff before closing |
| Before tool use | Block writes to the raw data folder |

### Cross-tool hook configuration

| Tool | Config location | Verify in your version |
| --- | --- | --- |
| Cursor | `.cursor/hooks.json` | `afterFileEdit`, `stop` |
| Claude Code | `~/.claude/settings.json` under `"hooks"` | `PostToolUse`, `Stop` |
| Codex | In-app Hooks section | Feature names vary by release |

### Card-Krueger worked example

For Cursor:

```json
{
  "afterFileEdit": [
    {
      "match": "examples/card-krueger-toy/src/did_analysis.py",
      "command": "python3 -m pytest examples/card-krueger-toy/tests -q 2>&1 | tail -10"
    }
  ]
}
```

For Claude Code (in `~/.claude/settings.json`):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          { "type": "command",
            "command": "python3 -m pytest examples/card-krueger-toy/tests -q 2>&1 | tail -10" }
        ]
      }
    ]
  }
}
```

The full worked example is in `agent-harness/skills/hooks/SKILL.md`. An illustrative
Cursor configuration is in `.cursor/hooks/economics-hooks-example.json`.

### Constraints

- Do not commit hook config to a shared branch without noting it in the PR description.
- Hooks do not replace human review of a diff.
- Verify exact event names in your installed tool version before a live session.

---

## 3.10 Verification Loops

A verification loop has three phases repeated until exit:

1. **Implement** — complete a narrowly scoped task.
2. **Evaluate** — check the result against the issue acceptance criteria.
3. **Revise** — if criteria are not met, address only the listed gaps.

Exit conditions:

- **GREEN** — all criteria pass. Go to human diff review.
- **YELLOW after one iteration** — minor gaps; address and loop again.
- **RED or three iterations without GREEN** — open a new issue with the blocker as
  the acceptance criterion. Stop looping.

### Why not loop indefinitely?

Three iterations without GREEN indicates either unclear acceptance criteria (fix the
issue), an estimation or data problem that needs human judgment, or scope that is
too large for one PR. None of these is solved by looping again.

### Card-Krueger worked example

**Task:** Add the robustness trim to `did_analysis.py`.

**Acceptance criteria:**
1. `python3 examples/card-krueger-toy/src/did_analysis.py` prints trimmed group means.
2. Sample counts for the trimmed subsample are printed.
3. `pytest examples/card-krueger-toy/tests` passes.
4. `README.md` documents the trim threshold.
5. `data/toy_fast_food.csv` is unmodified.

**Iteration 1:** Agent adds trim logic but omits README update. Criteria 4 fails.
**Iteration 2:** Agent updates README. All criteria pass. Verdict: GREEN.
**Action:** Human reviews diff before merge.

The evaluator for the loop is the `loop-verifier` subagent in
`agent-harness/subagents/loop-verifier.md`. The loop protocol is in
`agent-harness/skills/loop-on-verification/SKILL.md`.

### Difference from a swarm

A swarm runs multiple agents in parallel on different issues. A loop runs one agent
iteratively on one issue. Both use acceptance criteria as exit conditions.

---

## 3.11 Goals and the `/goal` Command

A goal is a persistent task definition that a coding agent retrieves across sessions.
It is the agent-tool equivalent of a GitHub issue.

### Goal-file anatomy

| Field | What to write | Economics translation |
| --- | --- | --- |
| `name` | One-line identifier | Match the issue title or research task name |
| `description` | What should be true when done | The research output: a table, figure, status report |
| `approach` | How to get there | Which files to edit, which estimation method |
| `acceptance_criteria` | Verifiable completion conditions | Checkbox list; each item mechanically checkable |
| `constraints` | What must not change | Raw data untouched, synthetic caveat required, scope boundary |

### Why acceptance criteria must be verifiable

A goal criterion such as "the code is well-documented" cannot be checked by the agent
or by you without interpretation. A criterion such as "pytest passes with zero failures"
can be confirmed with one command. Use the second kind.

Bad:

> The analysis is clean and the results make sense.

Good:

> `python3 -m pytest examples/card-krueger-toy/tests` returns zero failures. The
> phrase "synthetic teaching data" appears in the console output. `data/toy_fast_food.csv`
> is unmodified (confirmed with `git diff --stat`).

### How goals connect to GitHub issues

A GitHub issue is the control-plane record: it is visible to collaborators, linked to
a branch and PR, and archived in the project history. A goal file is the agent's
local task state: it persists the task description across sessions so the agent
does not need to re-read the issue every time.

For a well-managed project, goals and issues should agree. The acceptance criteria in
the goal file should match (or be a subset of) the acceptance criteria in the issue.

### Card-Krueger worked examples

Three worked goal files are in `examples/card-krueger-goals/goals/`:

- `ck-robustness-checks.md` — add two robustness specifications to the DiD panel.
- `ck-parallel-trends-figure.md` — generate a pre-trends figure.
- `ck-replication-audit.md` — run the replication-checker and produce a status report.

### How to attach a goal to your tool

**Claude Code:** Use the `/goal` command and paste or import the goal content.

**Codex:** Open the Goals section in the Codex app and create a new goal from the
markdown. Verify field names in your installed version.

**Cursor Cloud Agent:** Paste the goal content into the task description when
launching a Cloud Agent session.

---

## 3.12 Other Field Examples

Macro:

- Data stream fetches FRED series and documents transformations.
- Model stream estimates VAR or local projections.
- Review stream checks frequency alignment and units.

Theory:

- Model stream writes primitives and equilibrium conditions.
- Solver stream implements computational check.
- Review stream checks assumptions and comparative statics.

Econometrics:

- Simulation stream creates data-generating process.
- Estimator stream implements OLS/IV comparison.
- Review stream checks seeds, repetitions, bias, variance, and coverage.

Development/trade:

- Data stream maps World Bank/PWT sources.
- Merge stream checks country-year coverage.
- Review stream checks missingness and sample selection.

## 3.13 Autonomous-Agent Risk Cards

Autonomous systems can read, write, schedule, call tools, and persist memory.
Evaluate them before connecting them to research files.

Risk card sections:

- read boundary;
- write or trigger boundary;
- memory and persistence;
- execution environment;
- approval gate;
- evidence trail;
- decision.

Prompt:

```text
Evaluate [tool] using the autonomous-agent risk card. Identify read boundary,
write boundary, memory, execution environment, approval gate, and evidence
trail. Recommend read-only use, branch-isolated write use, no use, or more
documentation needed.
```

## 3.14 Exercises

See `exercises/day3-agent-workflows.md` for the full exercise set (Exercises 1–9).

### Exercise 1: Use A Review Role On The Card-Krueger Diff

Review `examples/card-krueger-toy/` as a read-only reviewer. Check units, sample
restriction, and synthetic-data caveat. State acceptance criteria before beginning.

### Exercise 2: Replication-Checker Skill

Apply the replication-checker to `examples/card-krueger-toy/`. Assign a GREEN,
YELLOW, or RED verdict with evidence.

### Exercise 3: Multiple Subagent Roles

Use the pr-reviewer and data-reviewer role prompts in turn. Record what each caught
that the other did not.

### Exercise 4: Orchestration Log For The CK Swarm

Populate `notes/orchestration_log.md` with the four streams from
`examples/card-krueger-swarm/README.md`. Dependencies and merge order must be
explicit.

### Exercise 5: Autonomous-Agent Risk Card

Complete `agent-harness/autonomous_agent_risk_card.md` for a tool of your choice.

### Exercise 6 (new): Configure A Hook

Draft the hook configuration entry for your tool lane that fires the CK verification
suite after editing `did_analysis.py`. See `agent-harness/skills/hooks/SKILL.md`.

### Exercise 7 (new): Verification Loop

Run one loop iteration using the loop-verifier subagent against a CK task. Record
the verdict in `notes/orchestration_log.md`.

### Exercise 8 (new): Write A Goal File

Draft `examples/card-krueger-goals/goals/ck-my-goal.md` with mechanically verifiable
acceptance criteria for a CK task of your choosing.

### Exercise 9 (new): Explore A Plugin

Read the `plugin.json` for one installed Cursor plugin. Name one skill or rule it
provides and explain what it adds to the CK workflow.

## 3.15 Chapter Checklist

- [ ] You can explain the difference between main agent, skill, subagent, MCP,
      cloud agent, swarm, hook, loop, and goal.
- [ ] You used one skill or skill-style workflow.
- [ ] You used one subagent or reviewer role (pr-reviewer, data-reviewer, or
      literature-reviewer).
- [ ] You updated an orchestration log with stream entries and dependencies.
- [ ] You labelled tasks as parallel, sequential, or blocked.
- [ ] You reviewed before merging.
- [ ] You completed an autonomous-agent risk card before autonomous use.
- [ ] You drafted or identified a hook configuration for your tool lane.
- [ ] You recorded at least one loop iteration with a GREEN/YELLOW/RED verdict.
- [ ] You authored a goal file with verifiable acceptance criteria.
- [ ] You read one plugin manifest and described what it contributes.
