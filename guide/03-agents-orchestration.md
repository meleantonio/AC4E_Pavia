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

## 3.9 Other Field Examples

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

## 3.10 Autonomous-Agent Risk Cards

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

## 3.11 Exercises

### Exercise 1: Create Or Use A Skill-Style Workflow

Use replication checker, literature mapper, data-contract checker, or
bibliography cleaner.

### Exercise 2: Use A Reviewer Role

Review a real diff, memo, PR, or replication README.

### Exercise 3: Plan Streams

Create at least three issue streams and identify dependencies.

### Exercise 4: Fill A Risk Card

Choose OpenClaw, Hermes, Eve, or another autonomous system. Complete the risk
card before using it on research files.

## 3.12 Chapter Checklist

- [ ] You can explain the difference between main agent, skill, subagent, MCP,
      cloud agent, and swarm.
- [ ] You used one skill or skill-style workflow.
- [ ] You used one subagent or reviewer role.
- [ ] You updated an orchestration log.
- [ ] You labelled tasks as parallel, sequential, or blocked.
- [ ] You reviewed before merging.
- [ ] You completed an autonomous-agent risk card before autonomous use.
