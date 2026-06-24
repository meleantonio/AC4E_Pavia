# Participant Reference Guide

This is the long-form reference guide for **Agentic Coding for Economists**. It
is written as a small textbook: you can read it before the workshop, use it
during the exercises, or return to it later when you are applying agentic
coding to a real research project.

The guide assumes no previous knowledge of agentic coding. It assumes only that
you are an economist or economics researcher who works with research artifacts:
data, models, code, papers, tables, figures, replications, presentations, or
teaching materials. You may use R, Stata, MATLAB, Python, Julia, LaTeX, Excel,
shell scripts, or a mixture of tools. The workshop teaches a transferable way
of working with AI coding agents, not a single programming language.

## How This Guide Is Organized

The sequence follows the live Pavia schedule and syllabus.

1. **First, you learn what agentic coding is.** You learn what agents can do,
   what they cannot own, and how to use read-only, planning, implementation,
   and debugging workflows without letting the tool run ahead of your research.
2. **Then you learn the working environment.** You choose a tool lane and a
   research-language lane, open the repository, understand context, create
   privacy boundaries, and learn the basic GitHub vocabulary.
3. **Then you learn how to frame research work.** Only after the basics are in
   place do we introduce the project brief, research design memo,
   spec-driven development, literature mapping, data or model-input maps, and
   acceptance criteria.
4. **Then you learn advanced agent workflows.** Skills, subagents, MCP, cloud
   agents, swarms, hooks, verification loops, goals, and plugins come after you
   have a project, a repo, and reviewable tasks with acceptance criteria.
5. **Finally, you integrate and communicate the work.** The end point is a
   replication-oriented package, not a chat transcript.

You can also use the split topic chapters:

- [Chapter 1: Foundations, GitHub, and Governance](guide/01-foundations.md)
- [Chapter 2: Research Pipeline and Spec-Driven Development](guide/02-research-pipeline.md)
- [Chapter 3: Agents, Skills, Subagents, MCP, and Orchestration](guide/03-agents-orchestration.md)
- [Chapter 4: Replication, Presentation, and Adoption](guide/04-replication-presentation.md)

## What You Will Be Able To Do

By the end, you should be able to:

- explain what an AI coding agent is and when it is useful for economics work;
- choose the right level of autonomy for a task;
- control context so the agent is grounded in the right files, data, docs, and
  research assumptions;
- protect confidential data, secrets, and unpublished material;
- use GitHub issues, branches, pull requests, and reviews as the control plane
  for research work;
- turn a research idea into a project brief, design memo, data or model-input
  map, and testable backlog;
- use skills and subagents for repeated procedures and specialized reviews;
- coordinate parallel agent work without losing review discipline;
- configure hooks, run verification loops, and draft goal files with testable
  acceptance criteria;
- evaluate autonomous-agent tools before giving them access to research files;
- package a mini research project so another person can reproduce or inspect it.

## What Agentic Coding Means

Agentic coding means using an AI system that can reason over a task, inspect
project files, propose a plan, edit files when allowed, run commands when
allowed, and report the result. It differs from ordinary chat because the agent
can often interact with your project, not just answer a question.

For an economist, this can help with tasks such as:

- reading a codebase and explaining where analysis happens;
- drafting a project brief from a rough research idea;
- translating a research design into small implementation tasks;
- writing or revising R, Stata, MATLAB, Python, Julia, or shell scripts;
- creating LaTeX table notes and replication README sections;
- checking a bibliography for missing fields or inconsistent keys;
- reviewing whether a result is overclaimed relative to the design;
- running a clean-room replication checklist.

But the agent does not own:

- the research question;
- the identification argument;
- the interpretation of causal evidence;
- data access rights;
- confidentiality decisions;
- final claims in a paper or presentation;
- the decision to merge changes into a research repository.

Think of the agent as a fast research assistant that can draft, inspect, and
execute bounded tasks. It needs clear instructions, narrow context, and review.

## The Central Rule

Every important agent action should have three parts:

1. **Scope:** What is the agent allowed to read, change, or run?
2. **Evidence:** What output, diff, log, table, or explanation will show what
   happened?
3. **Review:** What does a human check before accepting the result?

If one of these is missing, slow down.

## Workshop Sequence At A Glance

| Time | What is introduced | What you produce |
| --- | --- | --- |
| Day 1 morning | Agent workflows, context, setup, repository orientation | tool-lane notes, setup verification |
| Day 1 mid-day | Governance, privacy, GitHub basics | `AGENTS.md`, privacy notes, first branch or PR path |
| Day 1 afternoon | Research question and project brief | `docs/project_brief.md`, initial backlog seed |
| Day 2 morning | Agent Skills, `/sdd`, literature, design memo, data/model-input map | `spec/` or memo-linked SDD artifacts, bibliography, data map |
| Day 2 afternoon | Acceptance criteria, context patterns, skill/subagent planning | prioritized issues, `notes/context_patterns.md` |
| Day 3 morning | Skills, subagents, swarms, hooks, loops, goals | skill/subagent use, hook config, goal file, `notes/orchestration_log.md` |
| Day 3 mid-day | Autonomous-agent risk, plugins | `agent-harness/autonomous_agent_risk_card.md` |
| Day 3 afternoon | Replication, packaging, presentation, adoption | `replication/README.md`, presentation, 30-day plan |

## Software And Language Lanes

The workshop is not language-specific. The same agentic workflow can support
many research stacks.

| Lane | Common files | Typical verification | Notes |
| --- | --- | --- | --- |
| R | `.R`, `.Rmd`, `renv.lock`, `DESCRIPTION`, `tests/testthat/` | `Rscript scripts/run_analysis.R`; `Rscript -e "testthat::test_dir('tests/testthat')"` | Strong for applied micro, visualization, reproducible reports, and package-style projects. |
| Stata | `.do`, `.ado`, `.dta`, `.smcl`, `.log` | `stata-mp -b do scripts/run_analysis.do`; inspect log for errors | Common in applied economics. Verification often depends on logs, output files, and path hygiene. |
| MATLAB | `.m`, `.mlx`, `.mat`, `matlab.prj` | `matlab -batch "run('scripts/run_analysis.m')"` | Strong for macro, numerical methods, dynamic models, simulations, and matrix workflows. |
| Python | `.py`, `.ipynb`, `requirements.txt`, `pyproject.toml`, `tests/` | `python scripts/run_analysis.py`; `pytest` | Useful for pipelines and software packaging, but only one possible lane. |
| Julia | `.jl`, `Project.toml`, `Manifest.toml` | `julia --project=. scripts/run_analysis.jl` | Useful for numerical economics and macro modelling. |
| LaTeX-heavy workflow | `.tex`, `.bib`, `figures/`, `tables/` | `latexmk -pdf paper/main.tex`; citation checks | Useful when the primary artifact is a paper or slides. |
| Mixed or other | Excel, shell, notebooks, proprietary tools | exact manual run checklist plus expected outputs | Still use issues, branches, review logs, and replication documentation. |

When you ask the agent for help, name your lane explicitly:

```text
My main implementation lane is Stata. Do not translate the project into Python
unless I explicitly ask. Plan the workflow using do-files, logs, and output
tables.
```

```text
My main implementation lane is MATLAB. Treat scripts and functions as the
primary artifacts. Include a batch run command and expected output files.
```

```text
My main implementation lane is R. Use R scripts and, where useful, R Markdown.
Document packages and the exact Rscript command.
```

## Running Case Used Throughout: Card And Krueger

The guide uses Card and Krueger's minimum wage study as a running example. It
is useful because the research question is intuitive, the design is teachable,
and the project can be expressed in several software lanes.

Starting references:

- David Card data page: <https://davidcard.berkeley.edu/data_sets.html>
- NBER working paper page: <https://www.nber.org/papers/w4509>
- Paper PDF: <https://davidcard.berkeley.edu/papers/njmin-aer.pdf>

The simple version of the question is:

```text
What happened to fast-food employment in New Jersey relative to eastern
Pennsylvania after New Jersey raised its minimum wage in April 1992?
```

This can become an applied economics workflow:

1. Find the public data and document the source.
2. Identify unit of observation, treatment group, comparison group, outcome,
   timing, and sample restrictions.
3. Create a cleaned analysis file.
4. Estimate a baseline difference-in-differences comparison.
5. Check sensitivity and limitations.
6. Write a replication README.
7. Present the research result and the agentic workflow.

The same structure can be adapted to macro, econometrics, theory, or other
applied fields. The exact files and commands change; the workflow stays the
same.

# Part I: Foundations

## 1. What Agents Are Actually Doing

An AI coding agent receives a prompt and tries to complete a task. Depending on
the tool and settings, it may be able to:

- read files in the project;
- search the repository;
- search the web or official docs;
- edit files;
- run terminal commands;
- call tools through MCP or connectors;
- open pull requests;
- spawn subagents or background jobs.

This power is useful only if it is bounded. A vague prompt such as:

```text
Improve my project.
```

is dangerous because the agent must invent what "improve" means. For a research
project, it might change code, rewrite claims, alter tables, or create new
outputs without understanding the design.

A bounded prompt is better:

```text
Read README.md and scripts/run_analysis.do. Do not edit files. Explain what the
main analysis does, what inputs it expects, what outputs it creates, and what
could break on a clean machine.
```

This prompt defines:

- files to inspect;
- no-edit mode;
- questions to answer;
- a replication-oriented lens.

## 2. The Four Basic Workflows

The workshop uses four basic workflows. Tools may name them differently. Cursor
may expose mode labels; Codex and Claude Code may use prompts, slash commands,
or session behavior. The concept is more important than the UI label.

Verify in your Cursor version: UI labels for Agent, Plan, Debug, rules,
subagents, and skills can change. Prefer official docs and the labels in your
installed version.

### Read-Only Workflow

Use read-only mode when you want understanding before action. This is the first
workflow to learn.

Good uses:

- explain a repository;
- summarize a paper section;
- inspect a data source map;
- identify risks in a design;
- compare two possible modelling strategies;
- review a Stata log, R output, MATLAB error, or Python traceback.

Example:

```text
Read README.md, AGENTS.md, and days/day1.md. Do not edit files. Explain:
1. what this repository is for;
2. what I should do first;
3. which files or folders should not be exposed to agents;
4. which command or manual check verifies the setup.
```

Economist example:

```text
Read my draft research question below. Do not edit files. Tell me whether it is
testable, what the likely unit of observation is, what the main outcome could
be, and what data access risks I should resolve before coding.

Question: [paste question]
```

### Planning Workflow

Use planning mode when the task has several steps or when there are multiple
reasonable approaches.

Good uses:

- planning a data-cleaning workflow;
- deciding how to structure a do-file or script directory;
- decomposing a literature review into tasks;
- planning a model simulation;
- planning a replication package.

Example:

```text
Plan a workflow for estimating the baseline Card-Krueger minimum wage effect.
Do not edit files. Include data inputs, cleaning steps, estimation steps,
outputs, software-lane assumptions, review checks, and what is out of scope.
```

The answer should not be a wall of vague advice. It should produce an ordered
sequence that can become files or issues.

### Implementation Workflow

Use implementation mode only after the task is scoped.

Good uses:

- create a project brief from a template;
- add a Stata master do-file skeleton;
- add an R script that reads a documented CSV and writes a summary table;
- write a MATLAB function for a model block;
- update a replication README with exact commands.

Example:

```text
Implement this documentation issue only. Edit docs/data_source_map.md and no
other files. Add rows for FRED GDP, CPI, unemployment, and federal funds rate.
Include source URL, frequency, units, coverage, and access notes. Do not write
analysis code.
```

Notice that the prompt states:

- one issue;
- allowed file;
- expected content;
- explicit non-goal.

### Debugging Workflow

Debugging starts with evidence, not guessing.

A good debugging loop is:

1. Reproduce the symptom.
2. Read the error or inconsistent output.
3. Form a hypothesis.
4. Change one thing.
5. Rerun the check.
6. Record the evidence.

Examples:

```text
Read this Stata log. Do not edit files. Identify the first error that matters,
explain the likely cause, and propose one minimal fix.
```

```text
Read this MATLAB error and the function it references. Do not edit files. Is
the problem a missing input, a dimension mismatch, a path problem, or a toolbox
problem? Explain how to verify.
```

```text
Read this R traceback and the script. Do not edit files. Identify the smallest
change likely to fix the failing join, and say what check should be rerun.
```

## 3. Context: The Quality Lever

Context is what the agent can see or is told to use. Most weak agent outputs
come from bad context: too little context, too much context, or the wrong
context.

### Tight Context

Use tight context when precision matters.

```text
Only read START_HERE.md and AGENTS.md. Do not edit files. Identify what I
should do first, which files are off limits, and which setup check I should run.
```

Good for:

- one memo;
- one function;
- one do-file;
- one table note;
- one error message.

### Wide Context

Use wide context when consistency across files matters.

```text
Search the repository for every place where the outcome variable is named. Do
not edit files. Report inconsistencies in names, units, or definitions.
```

Good for:

- path consistency;
- variable naming;
- paper-table alignment;
- checking that README commands match actual files.

### External Context

Use external context when the answer depends on official docs, literature, or
data-source metadata.

```text
Search official documentation for this data source. Summarize variable
definitions, frequency, units, access method, citation requirement, and any
version caveats. Include links.
```

Use external search for:

- literature discovery;
- official API documentation;
- package documentation;
- data-source definitions;
- tool documentation.

For current product UI, official docs beat old slides. Add a "verify in your
version" note when interface names vary.

## 4. Privacy And Boundaries

Before using an agent on a research repo, decide what it should not read or
write.

Common protected material:

- `.env`, credentials, API keys, tokens;
- restricted microdata;
- confidential survey data;
- unpublished coauthor drafts if not cleared;
- proprietary datasets;
- identifiable individual-level data;
- private referee reports;
- paid data extracts that cannot be redistributed;
- large raw files that slow tools and are not useful in chat.

Project guidance should state boundaries plainly:

```markdown
## Privacy and data boundaries

- Do not read, summarize, upload, or edit files under `data/raw/` or
  `data/private/`.
- Do not read `.env`, credentials, tokens, or API keys.
- Do not paste restricted data into chat.
- Work from synthetic, public, or documented derived data unless explicitly told
  otherwise.
```

For Cursor users, `.cursorignore` or related ignore files may enforce some
boundaries. For other tools, use `AGENTS.md`, `CLAUDE.md`, tool settings, or
plain prompt instructions. Do not rely on memory alone.

## 5. Project Instructions With AGENTS.md

`AGENTS.md` is a shared instruction file for agents and collaborators. It is
not a dumping ground for every preference. It should be short enough that an
agent can follow it and a human can review it.

Recommended structure:

```markdown
# Agent Instructions

## Project
[One paragraph describing the research project.]

## Main software lane
[R / Stata / MATLAB / Python / Julia / mixed.]

## Key paths
- `docs/` — workshop notes and research documents introduced later.
- `scripts/` — runnable analysis or model scripts.
- `outputs/` — generated tables and figures.
- `replication/` — clean-run instructions.

## Rules
- Use relative paths.
- Do not edit raw data.
- Do not claim identification is valid without explicit design evidence.
- Before merge, document the run command or manual review check.

## Privacy
- Do not read `.env`, credentials, `data/private/`, or restricted files.
```

Tool adapters are optional:

- Cursor rules can add file-type guidance.
- Claude Code can use `CLAUDE.md` importing or summarizing `AGENTS.md`.
- Codex can use `AGENTS.md` and nested guidance.
- Other agents may use rules, memories, system prompts, or project instruction
  files.

The portable artifact is the shared guidance, not the specific UI.

# Part II: GitHub And The Research Repository

## 6. Why GitHub Appears Early

GitHub is introduced before advanced agent work because it gives you a control
plane. A control plane is the place where work is described, assigned, reviewed,
and accepted. Without one, important decisions get trapped in chat history.

You do not need to be a software engineer to use the basic loop:

1. repository: a folder with version history;
2. commit: a saved change;
3. branch: a safe line of work separate from main;
4. issue: a described task;
5. pull request: a proposed change with a diff;
6. review: a check before accepting the change;
7. merge: bringing accepted work into the main line.

## 7. Repository Orientation

Before creating or changing anything, ask the agent to explain the repository.

```text
Read README.md, START_HERE.md, AGENTS.md, and the day schedule. Do not edit
files. Explain the repository map, the expected workshop artifacts, the privacy
boundaries, and the setup verification command.
```

Then inspect the answer. It should tell you:

- where day instructions live;
- where topic readings live;
- where templates live;
- where setup notes and later research-document templates live;
- what verification command or manual check is expected.

If the answer is vague, ask a narrower follow-up:

```text
List only the files I am expected to edit on Day 1 and the files I should avoid.
Do not edit files.
```

## 8. First Branch Before First Big Task

A branch isolates work. Even if you work alone, branches keep experiments from
polluting the main version of your project.

Typical command pattern:

```bash
git checkout main
git pull
git checkout -b day1-repo-orientation
```

If you are uncomfortable with the terminal, use your tool's Source Control or
GitHub interface. The concept is the same.

Do not start by asking an agent to restructure your whole repo. Start with a
small documentation task or setup verification note.

## 9. Issues: Introduced Before They Are Required

An issue is a task card. It should be clear enough that a human, an agent, or a
future-you can tell when it is done.

An early issue can be simple:

```text
Title: Verify setup and record tool lane

Description:
Confirm that the participant repo opens in my chosen tool and that the setup
verification command or manual check has been run.

Acceptance criteria:
- chosen tool lane is recorded in notes/context_patterns.md;
- setup command or manual check is recorded;
- no private data or secrets are added;
- diff is reviewed before merge.
```

This issue does not require a project brief. It belongs early because it teaches
the work loop.

After the project brief is introduced later, issues become more research
specific.

## 10. Pull Requests And Review

A pull request is not just a request to merge code. It is a review surface. For
research work, the PR should answer:

- What changed?
- Why did it change?
- Which issue or task does it satisfy?
- What evidence shows it works?
- What did a human review?
- What should not be inferred from this change?

Example PR description:

```markdown
## Summary
- Adds first project brief for the minimum wage replication exercise.
- Defines treatment, comparison group, unit of observation, and initial output.

## Verification
- Read-only review against workshop guide.
- No data or code added.

## Research caveat
- This brief does not claim a causal estimate yet. It only scopes the project.
```

This level of discipline matters because agents can produce polished text that
sounds more certain than the evidence permits.

# Part III: Project Brief And Research Framing

## 11. Why The Project Brief Comes After Basic Setup

The project brief is the first research artifact. It should come after you know
where the repo is, how to ask read-only questions, and how to protect private
files. Otherwise you will be tempted to build before you have scoped the work.

A project brief is short. It is not a paper. It answers:

- What is the question?
- Why does it matter?
- What data, model inputs, or sources might be used?
- What method or modelling approach is plausible?
- What can be produced in the workshop?
- What is out of scope?

## 12. Project Brief Template

Use this structure:

```markdown
# Project Brief

## Title
[One-line project title.]

## Research question
[One clear, testable or model-specific question.]

## Motivation
[Why this matters for economics, policy, theory, or methods.]

## Expected contribution
[What this adds: replication, extension, new data, teaching example, model,
method comparison, or workflow.]

## Data or model inputs
[Sources, access, format, variables, calibration targets, primitives, or
assumptions.]

## Method
[Empirical strategy, theoretical model, simulation, calibration, descriptive
analysis, or literature mapping.]

## Three-day deliverable
[What can realistically be done in the workshop.]

## Out of scope
[What will not be claimed or built.]
```

## 13. Examples Of Research Questions

Weak:

```text
Study minimum wages.
```

Better:

```text
Did fast-food employment in New Jersey change relative to eastern Pennsylvania
after New Jersey raised its minimum wage in April 1992?
```

Weak:

```text
Look at monetary policy.
```

Better:

```text
How do unemployment and inflation respond after a federal funds rate shock in a
small quarterly VAR using FRED data?
```

Weak:

```text
Model competition.
```

Better:

```text
In a Cournot duopoly with linear demand and asymmetric marginal costs, how does
a cost shock for one firm change equilibrium quantities, prices, and profits?
```

Weak:

```text
Compare estimators.
```

Better:

```text
In a simulated demand equation with an endogenous price regressor, how do OLS
and IV estimates differ as instrument strength varies?
```

## 14. Project Brief Prompts

First, ask for a read-only critique:

```text
Here is my draft research idea. Do not edit files. Tell me whether it is
specific enough for a three-day prototype. Identify the likely unit of
observation, outcome, treatment or key variable, data or model inputs, and one
major risk.

[paste idea]
```

Then ask for a draft:

```text
Draft a one-page project brief from this idea. Keep the implementation language
neutral. Include question, motivation, contribution, data or model inputs,
method, three-day deliverable, and out-of-scope claims.
```

Then, and only then, ask for a file edit:

```text
Create or update docs/project_brief.md from the approved brief. Do not edit
analysis code. Keep the brief concise and label assumptions clearly.
```

## 15. Running Case: Card-Krueger Brief

Possible brief:

```markdown
# Project Brief

## Title
Minimum Wage Increase and Fast-Food Employment

## Research question
Did fast-food employment in New Jersey change relative to eastern Pennsylvania
after New Jersey raised its minimum wage in April 1992?

## Motivation
The minimum wage is a core labor economics policy question. The Card-Krueger
study is a canonical empirical example because it uses a transparent comparison
between nearby labor markets before and after a policy change.

## Expected contribution
This workshop project is a replication-oriented teaching exercise. It aims to
produce a clean design memo, data map, baseline comparison, and replication
README, not a new contribution to the minimum wage literature.

## Data or model inputs
Public Card-Krueger fast-food data, with restaurant-level observations before
and after the New Jersey minimum wage increase.

## Method
Baseline difference-in-differences comparison between New Jersey and eastern
Pennsylvania restaurants.

## Three-day deliverable
A documented mini replication package with one baseline table and clear
limitations.

## Out of scope
No claim that all minimum wage policies have the same effect. No full
literature review. No unrestricted causal generalization beyond the design.
```

## 16. Other Field Examples

Macro:

```text
Build a small, documented macro time-series project using FRED data to examine
the relationship between inflation, unemployment, GDP growth, and the policy
rate. The deliverable is a clean data map, transformation notes, one baseline
VAR or local-projection specification, and a replication README.
```

Micro theory:

```text
Build a computational note for a Cournot duopoly with asymmetric marginal costs.
The deliverable is a model statement, equilibrium derivation or solver, a small
comparative statics table, and a README explaining how to reproduce the
calculation.
```

Econometrics:

```text
Build a Monte Carlo study comparing OLS and IV estimates when the instrument
varies in strength. The deliverable is a design memo, simulation script in the
chosen software lane, a summary table, and a replication README.
```

Development or trade:

```text
Build a panel data map for a country-year analysis using World Bank and Penn
World Table indicators. The deliverable is a data source map, merge plan,
coverage table, and documented blockers.
```

# Part IV: Spec-Driven Development For Research

## 17. What SDD Means Here

Spec-driven development means you define the target before asking an agent to
build. In research, the target is not just "make the code run." It includes
research intent, data definitions, model assumptions, expected outputs, and
replication criteria.

The sequence is:

1. **Intent:** What are we trying to learn or produce?
2. **Requirements:** What must be true of the output?
3. **Design:** How will the project produce the output?
4. **Tasks:** What small units of work can be assigned and reviewed?

## 18. Intent

Intent is the research purpose.

Bad intent:

```text
Do a regression.
```

Better intent:

```text
Produce a transparent baseline estimate of the employment change in New Jersey
relative to Pennsylvania after the 1992 minimum wage increase, using the public
fast-food data and documenting sample restrictions.
```

Intent should name the object of interest and the limits of the exercise.

## 19. Requirements

Requirements say what the project must do. They should be observable.

Use EARS-style language when helpful:

- **WHEN** something happens, the project **SHALL** do something.
- **GIVEN** a condition, the project **SHALL** produce a defined output.
- **IF** a failure or blocker occurs, the project **SHALL** document it.

Examples:

```text
WHEN the clean-data script runs, it SHALL create one analysis dataset in the
documented output path.
```

```text
GIVEN the analysis dataset, the baseline script SHALL report sample counts by
state and survey wave.
```

```text
IF the public data cannot be downloaded automatically, the replication README
SHALL document the manual download step and expected file location.
```

For theory:

```text
GIVEN parameter values in the calibration file, the MATLAB or Julia solver
SHALL report equilibrium quantities and verify non-negative output.
```

For econometrics:

```text
GIVEN a fixed random seed, the simulation SHALL reproduce the same bias and
coverage summary table.
```

## 20. Design

Design explains the workflow.

For an empirical project:

- raw or public data source;
- cleaning steps;
- analysis file;
- estimation or descriptive method;
- tables and figures;
- review checks;
- replication path.

For a macro model:

- data or calibration targets;
- model equations;
- parameter file;
- solver or estimation method;
- output moments or impulse responses;
- numerical checks.

For a theory project:

- primitives;
- assumptions;
- equilibrium concept;
- proof or computational strategy;
- comparative statics;
- output note or figure.

For an econometrics simulation:

- data-generating process;
- estimators;
- parameters varied;
- repetitions and seed;
- summary metrics;
- output table.

## 21. Tasks

Tasks are introduced after the brief, GitHub basics, and SDD concepts because
they depend on all three.

A good issue has:

- title;
- purpose;
- allowed files;
- acceptance criteria;
- dependencies;
- verification command or manual review;
- out-of-scope note.

Example:

```text
Title: Create Card-Krueger data source map

Purpose:
Document public data source, variables, access method, unit of observation,
timing, and replication caveats.

Allowed files:
docs/data_source_map.md
references/bibliography.bib

Acceptance criteria:
- source link and access date are recorded;
- unit of observation is stated;
- treatment and comparison groups are identified;
- employment outcome is named;
- missingness or sample restriction risks are listed;
- no analysis code is added.

Verification:
Read-only review against project brief and public source notes.

Out of scope:
Cleaning data or estimating effects.
```

## 22. Research Design Memo

The research design memo is the bridge between a project brief and
implementation work.

Recommended sections:

```markdown
# Research Design Memo

## Research question

## Motivation and literature

## Hypotheses, model claims, or object of interest

## Data or model inputs

## Method

## Identification, assumptions, or equilibrium conditions

## Outputs

## Limitations

## Replication implications
```

Prompt:

```text
Read docs/project_brief.md. Draft a research design memo using the sections
above. Keep implementation language neutral. Separate confirmed facts,
assumptions, and open blockers. Do not write code.
```

Review prompt:

```text
Review this research design memo as a skeptical economist. Do not edit files.
Flag vague claims, missing data definitions, weak identification statements,
unclear model assumptions, and outputs that cannot be verified.
```

## 23. Literature Mapping

Agentic coding does not replace literature judgment. It can help structure the
search and summarize relevance, but you must verify bibliographic details and
read the key papers yourself.

A good literature map records:

- citation;
- research question;
- data or model;
- method;
- main result or proposition;
- relevance to your project;
- how your project differs.

Prompt:

```text
Search for 5 to 8 core references on [topic]. For each, provide citation,
question, data or model, method, main result, and relevance to my project.
Include links. Flag any citation details you are not sure about.
```

For Card-Krueger:

```text
Create a literature map for the minimum wage employment debate around the
Card-Krueger study. Include the original study, at least one critique or
reanalysis, and one later review or meta-analysis. Do not invent citation
details.
```

## 24. Data Or Model-Input Map

Not every economist uses "data" in the same way. A theory or macro modelling
project may have model inputs, calibration targets, parameters, or equations
instead of a CSV file. The guide uses "data or model-input map" to include all
of these.

For empirical projects:

| Field | Meaning |
| --- | --- |
| Source | Where the data come from |
| Access | public, restricted, API, manual download, proprietary |
| Format | CSV, Stata, Excel, API, database, text, PDF |
| Unit | individual, household, firm, restaurant, country-year, region-month |
| Key variables | outcome, treatment, controls, IDs, time |
| Coverage | years, geography, population |
| Restrictions | license, confidentiality, access steps |
| Version | release, date accessed, package version |

For model projects:

| Field | Meaning |
| --- | --- |
| Primitive | preferences, technology, information, endowments |
| Parameter | value, source, calibration target |
| Equation | model block or equilibrium condition |
| Solver input | grid, tolerance, initial condition, seed |
| Output | moments, policy functions, equilibrium objects |
| Check | feasibility, market clearing, convergence |

Prompt:

```text
Create a data or model-input map for this project. Use empirical data fields if
the project is data-based. Use primitives, parameters, equations, solver inputs,
outputs, and checks if the project is theoretical or computational. Do not
write analysis code.
```

## 25. Acceptance Criteria Across Fields

Applied labor:

```text
The analysis SHALL report the number of restaurants by state and wave before
estimating the baseline comparison.
```

Macro:

```text
The data script SHALL document transformations from levels to growth rates or
logs before estimating the VAR.
```

Theory:

```text
The solver SHALL verify that equilibrium quantities are non-negative and that
market-clearing residuals are below the stated tolerance.
```

Econometrics:

```text
The simulation SHALL use a fixed seed and report Monte Carlo standard errors
for the main performance metrics.
```

Development/trade:

```text
The merge step SHALL report country-year coverage before and after joining data
sources.
```

# Part V: Advanced Agent Workflows

## 26. Why Advanced Workflows Come Later

Skills, subagents, MCP, cloud agents, and swarms are powerful, but they are not
where a beginner should start. They make sense only after you have:

- a repository;
- project instructions;
- privacy boundaries;
- a project brief;
- a design memo or clear task;
- review criteria.

Without those, advanced agents only automate confusion.

## 27. Main Agent, Skill, Subagent, MCP, Cloud Agent

| Need | Best fit | Example |
| --- | --- | --- |
| General help | main agent | "Explain this repo." |
| Repeated checklist | skill | replication checker, loop-on-verification |
| Specialized independent review | subagent or role prompt | PR reviewer, data-reviewer, literature-reviewer |
| Auto-verify after an edit | hook | run verification suite after editing `did_analysis.py` |
| One task until criteria pass | verification loop | loop-verifier subagent on a robustness check |
| Persistent task across sessions | goal file | `/goal` in Claude Code or Codex Goals |
| Structured external access | MCP | FRED, filesystem, database |
| Long isolated branch task | cloud agent or worktree | documentation pass |
| Multiple workstreams | issue-labelled swarm | Card-Krueger four-stream example |
| Share harness pieces across a team | Cursor plugin | packaged skills and reviewer roles |

## 28. Skills

A skill is a reusable workflow that the agent can load when a task matches its
description. The concept transfers across tools even when paths and UI differ.

Good skill candidates for economists:

- replication checker (`agent-harness/skills/replication-checker/SKILL.md`);
- literature mapper;
- data-contract checker;
- bibliography cleaner;
- table-note reviewer;
- model-assumption checker;
- paper-polisher for LaTeX style and citation hygiene;
- hooks (`agent-harness/skills/hooks/SKILL.md`) — configure postcondition verification;
- loop-on-verification (`agent-harness/skills/loop-on-verification/SKILL.md`) — execute-evaluate-revise protocol.

Example skill body:

```markdown
---
name: replication-checker
description: Use when checking whether a research project can run from a clean
state, has declared dependencies, avoids hardcoded paths, and documents outputs.
---

When invoked:
1. Identify the main entry point.
2. Compare run instructions to actual files.
3. Check dependencies and software version notes.
4. Look for hardcoded paths, secrets, and private-data assumptions.
5. Report status: green, yellow, or red.
6. List blockers before recommendations.
```

Prompt:

```text
Use the replication-checker workflow on this project. Do not edit files.
Report green/yellow/red status, blockers, minimal run command, expected outputs,
and missing documentation.
```

## 29. Subagents And Role Prompts

A subagent is a specialized agent with a role. If your tool does not support
file-backed subagents, save the role prompt and use it manually.

Portable subagents in this repository (`agent-harness/subagents/`):

| Subagent | Use when |
| --- | --- |
| `pr-reviewer.md` | Reviewing a PR for scope, reproducibility, and economics interpretation |
| `data-reviewer.md` | Checking Card-Krueger panel balance, variable coding, synthetic-data caveat |
| `literature-reviewer.md` | Verifying BibTeX accuracy and citation–claim matching for minimum-wage literature |
| `loop-verifier.md` | One iteration of the execute-evaluate-revise loop against acceptance criteria |
| `sdd-orchestrator.md` | Managing the SDD lifecycle |

PR reviewer:

```text
You are a read-only reviewer for an economics research repository. Review the
diff for:
- scope drift;
- path and dependency problems;
- data privacy issues;
- units and missingness;
- standard errors, assumptions, or model checks;
- overclaiming relative to the design;
- replication README consistency.

Return blockers first, then suggestions. Do not edit files.
```

Bibliographer:

```text
You are a bibliography reviewer for an economics paper. Check .bib entries for
missing required fields, inconsistent keys, duplicate entries, missing DOIs or
URLs when relevant, and mismatch between in-text citations and the bibliography.
Do not invent bibliographic facts.
```

Theory/model checker:

```text
You are a theory and computational-model reviewer. Check whether primitives,
assumptions, equilibrium conditions, parameter restrictions, and numerical
checks are stated consistently. Flag claims that do not follow from the model
as written.
```

## 30. MCP

MCP, the Model Context Protocol, lets agents use structured tools. For
economists, common uses include:

- FRED or macro data APIs;
- scoped filesystem access to a safe folder;
- SQL or database access;
- search tools;
- potential bridges to R, Stata, MATLAB, or other local tools.

Use MCP when it gives repeatable, documented access. Do not add MCP just
because it sounds advanced.

Good MCP task:

```text
Using the configured FRED tool, fetch metadata for GDP, CPIAUCSL, UNRATE, and
FEDFUNDS. Do not estimate a model. Update the data map with series IDs,
frequency, units, source, and access notes.
```

Bad MCP task:

```text
Connect to everything and figure out my project.
```

## 31. Cloud Agents And Branch Work

Cloud or background agents are useful when a task is:

- clearly scoped;
- branch-isolated;
- reviewable;
- not dependent on private data;
- not time-critical for a live demo.

Good cloud-agent prompt:

```text
Work on issue #12 only on branch agent/docs-replication. Update only
replication/README.md and docs/data_source_map.md. Do not edit analysis code.
When done, open a PR with a summary and verification notes.
```

Review the PR before merging. Never let remote or autonomous output enter the
main research branch without review.

## 32. Swarms

A swarm is several humans and/or agents working on coordinated tasks. In this
workshop, the safest swarm pattern is GitHub issues plus branches.

First, label tasks:

- `parallel`: can be done independently;
- `sequential`: should wait for earlier work;
- `blocked-by:#N`: depends on a specific issue;
- `ready-for-review`: implementation is done and needs checking.

Then assign streams:

| Stream | Example task | Handoff |
| --- | --- | --- |
| Data or inputs | clean data, document calibration inputs | `notes/handoff_data_to_analysis.md` |
| Analysis or simulation | estimate model, run solver, create tables | `notes/handoff_analysis_to_writeup.md` |
| Writing | draft paper section, table notes, presentation | `notes/handoff_writeup_to_replication.md` |
| Review | check consistency, replication, interpretation | `notes/review_log.md` |

Swarm prompt:

```text
Break this milestone into issue streams. Mark each issue as parallel,
sequential, or blocked-by another issue. For each stream, specify allowed files,
handoff artifact, review check, and merge order. Do not implement.
```

**Card-Krueger worked example:** `examples/card-krueger-swarm/` — four streams
(data validation, literature, estimation, figure) with issue templates, label
convention, and dependency graph. Model GitHub issues with acceptance criteria
are also open in the repository (issues #10–#14).

## 33. Autonomous-Agent Risk

Autonomous-agent systems can act across tools, schedules, files, or remote
environments. Evaluate them before use.

Risk-card questions:

- What can it read?
- What can it write, run, schedule, publish, or trigger?
- What memory persists?
- Where does it execute: local, sandbox, cloud, production, or mixed?
- What human approval gate exists?
- What logs, diffs, transcripts, or run outputs prove what happened?

Decision:

- safe for read-only use;
- safe for branch-isolated write use;
- not safe for this workshop repo;
- needs more documentation before use.

Prompt:

```text
Evaluate [OpenClaw/Hermes/Eve/other] using the autonomous-agent risk card. Do
not recommend connecting it to private data unless read boundary, write
boundary, memory, execution, approval, and evidence are all acceptable.
```

## 34. Day 2 To Day 3: Acceptance Criteria In Action

On Day 2 you wrote acceptance criteria into GitHub issues. On Day 3 those
criteria do work in three new roles:

| Day 3 feature | What acceptance criteria do |
| --- | --- |
| Verification loop | Exit condition — the loop stops when all criteria are GREEN |
| Goal file | Completion contract — the agent checks criteria at session start |
| Hook | Postcondition guard — verification runs after every relevant edit |

**Card-Krueger example:** "`python3 -m pytest examples/card-krueger-toy/tests`
passes and the phrase *synthetic teaching data* appears in the output" is a
criterion that all three can test mechanically.

Every Day 3 exercise in `exercises/day3-agent-workflows.md` states its
acceptance criteria before the prompt. Read them first.

## 35. Running Case: Card-Krueger Orchestration

The running case is fast-food employment in New Jersey (treatment) and eastern
Pennsylvania (comparison) before and after the April 1992 minimum wage
increase. The toy data in `examples/card-krueger-toy/` are synthetic teaching
data — no causal claim should follow from them.

Possible orchestration streams:

| Stream | Task | Depends on |
| --- | --- | --- |
| Literature | Map minimum wage references | none |
| Data validation | Document panel balance and variable coding | none |
| Baseline estimate | DiD comparison and robustness checks | data validation |
| Figure / write-up | Pre-trends figure, method notes | baseline estimate |
| Replication audit | Replication-checker status report | runnable pipeline |

The four-stream swarm lab uses `examples/card-krueger-swarm/` with issue
templates in `examples/card-krueger-swarm/issues/`.

Planner prompt:

```text
Plan the Card-Krueger project streams. Use labels parallel, sequential, and
blocked-by. Include handoff files and review checks. Do not implement.
```

Review prompt:

```text
Act as a read-only reviewer for the baseline estimate PR. Check whether the
treatment group, comparison group, post period, outcome units, and sample
counts match the design memo. Use agent-harness/subagents/data-reviewer.md as
the role prompt if helpful.
```

## 36. Hooks

A hook is a postcondition listener: the agent tool fires a command when a
specified event occurs, without you having to ask. For economists, the most
useful hook runs the documented verification command automatically after every
edit to an analysis script.

| Tool | Config location | Useful events |
| --- | --- | --- |
| Cursor | `.cursor/hooks.json` | `afterFileEdit`, `stop` |
| Claude Code | `~/.claude/settings.json` under `"hooks"` | `PostToolUse`, `Stop` |
| Codex | In-app Hooks section | Verify in your installed version |

Card-Krueger example (Cursor):

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

Full skill: `agent-harness/skills/hooks/SKILL.md`. Illustrative config:
`.cursor/hooks/economics-hooks-example.json`.

Constraints:

- Hooks do not replace human diff review before merge.
- Use relative paths in hook commands.
- Verify exact event names in your installed tool version before a live session.

## 37. Verification Loops

A verification loop repeats implement → evaluate → revise on one task until
acceptance criteria are met. It is not a swarm: a swarm runs parallel issues; a
loop iterates on one issue.

Protocol:

1. **Implement** — complete a narrowly scoped task.
2. **Evaluate** — check against issue or goal acceptance criteria (`loop-verifier` subagent).
3. **Revise** — if not GREEN, address only the listed gaps; repeat (max three iterations).

Exit: **GREEN** → human diff review; **RED** or three iterations without GREEN →
open a new issue with the blocker as acceptance criterion.

Card-Krueger example: add a robustness trim to `did_analysis.py`. Iteration 1
may miss README documentation (YELLOW). Iteration 2 clears all criteria (GREEN).

Skill: `agent-harness/skills/loop-on-verification/SKILL.md`. Evaluator:
`agent-harness/subagents/loop-verifier.md`.

## 38. Goals And The `/goal` Command

A goal is a persistent task definition the agent retrieves across sessions — the
agent-tool equivalent of a GitHub issue.

| Field | What to write |
| --- | --- |
| `name` | One-line identifier matching the research task |
| `description` | What should be true when done, in economic language |
| `approach` | Which files to edit, which method, in what order |
| `acceptance_criteria` | Checkbox list — each item mechanically verifiable |
| `constraints` | Raw data untouched; synthetic caveat; scope boundary |

**Verifiable criterion test:** can you answer YES or NO by running one command
or inspecting one file? If not, rewrite the criterion.

Worked examples: `examples/card-krueger-goals/goals/` — robustness checks,
parallel-trends figure, replication audit. See `examples/card-krueger-goals/README.md`.

Attach to your tool:

- **Claude Code:** `/goal` command; paste the goal markdown.
- **Codex:** Goals section in the Codex app (verify field names in your version).
- **Cursor Cloud Agent:** paste goal content into the task description.

Goals and GitHub issues should agree on acceptance criteria.

## 39. Plugins

A Cursor plugin packages skills, rules, agents, and commands into one installable
unit via a `plugin.json` manifest. It is a distribution mechanism: share a
replication-checker skill and a data-reviewer subagent with your research group
without manual file copying.

```
my-plugin/
├── .cursor-plugin/plugin.json
├── skills/replication-checker/SKILL.md
├── rules/economics-standards.mdc
└── README.md
```

Exercise: open one installed plugin's `plugin.json`, name one skill or rule it
provides, and explain what it adds to the Card-Krueger workflow.

Read the manifest before installing. Do not install untrusted plugins on a
machine with restricted research data.

# Part VI: Replication, Presentation, And Adoption

## 40. Integration Before Presentation

At the end of the workshop, the goal is not to show that an agent produced many
files. The goal is to show that you have a coherent, reviewable research
package.

Integration means:

- paths match across scripts, docs, and README;
- variable names and units are consistent;
- output files exist or blockers are documented;
- claims match the evidence;
- privacy boundaries are still respected;
- a clean-run path exists or the failure is explained.

## 41. Replication README

A replication README should be literal. A colleague should be able to follow it
without guessing.

Recommended structure:

```markdown
# Replication README

## Overview

## Software and versions

## Data or model inputs

## Setup

## Run instructions

## Expected outputs

## Troubleshooting

## Known limitations

## Contact or ownership
```

Language-lane examples:

R:

```bash
Rscript scripts/run_analysis.R
```

Stata:

```bash
stata-mp -b do scripts/run_analysis.do
```

MATLAB:

```bash
matlab -batch "run('scripts/run_analysis.m')"
```

Python:

```bash
python scripts/run_analysis.py
```

Julia:

```bash
julia --project=. scripts/run_analysis.jl
```

If your workflow cannot be run from a single command, write the shortest manual
sequence and expected outputs.

Replication review prompt:

```text
Review replication/README.md as a skeptical replicator. Starting from a clean
checkout, identify the exact setup steps, run command or manual sequence,
expected outputs, missing dependencies, private-data risks, hardcoded paths,
and unclear claims. Return blockers first.
```

## 42. Presentation

The final presentation is 5 to 7 minutes. It should not become a full seminar.

Use this sequence:

1. Research question.
2. Why it matters.
3. Data or model and method.
4. Main result, prototype, or blocker.
5. Agentic workflow: what the agent did and what you reviewed.
6. Replication status.
7. Next 30 days.

Good presentation language:

```text
The agent helped draft the data map and generate the first cleaning script.
I reviewed the variable definitions, sample restrictions, and output table.
The current package runs through the baseline table, but the robustness checks
remain future work.
```

Weak presentation language:

```text
The AI proved the effect.
```

Do not say that. Agents do not prove empirical claims. Designs, assumptions,
data, and review evidence support claims.

Presentation prompt:

```text
Draft a 5 to 7 minute presentation from my project brief, design memo,
orchestration log, review log, and replication README. Keep the research claim
modest. Include one slide on what the agent did and what a human reviewed.
```

## 43. 30-Day Adoption Plan

The goal after the workshop is one sustainable habit.

Week 1:

- add or improve `AGENTS.md` in one active research repo;
- document privacy boundaries;
- define one verification command or manual review check.

Week 2:

- choose one real task;
- create an issue;
- work on a branch;
- review the diff before merge.

Week 3:

- create one reusable skill or saved prompt;
- create one reviewer role prompt;
- use them on a real artifact.

Week 4:

- run one replication check;
- update the README;
- share the workflow with a coauthor, RA, or colleague.

Prompt:

```text
Create a 30-day adoption plan for my actual research workflow. My software lane
is [R/Stata/MATLAB/Python/other]. My constraints are [teaching, coauthors,
deadlines, data access]. Include one weekly habit, one artifact, one review
gate, and one privacy rule.
```

# Part VII: Exercises

## 44. Day 1 Exercises

### Exercise 1: Read The Repo

Goal: understand before editing.

Prompt:

```text
Read README.md, START_HERE.md, AGENTS.md, and days/day1.md. Do not edit files.
Explain what this repo is, what I should do first, what files I should avoid,
and how setup is verified.
```

Output to record:

- one paragraph in `notes/context_patterns.md` explaining your tool lane;
- the setup command or manual check;
- any privacy boundary you need to add.

### Exercise 2: Create A Safe First Branch

Goal: learn the branch workflow without touching research claims.

Task:

- create a branch;
- edit only a note or brief placeholder;
- review the diff;
- merge only after checking it.

### Exercise 3: Draft The Project Brief

Goal: state a research question before building.

Prompt:

```text
Here is my project idea: [paste]. Do not edit files. Ask up to three
clarifying questions only if needed. Then propose a one-page project brief with
question, motivation, data or model inputs, method, deliverable, and out of
scope claims.
```

## 45. Day 2 Exercises

### Exercise 4: Design Memo

Goal: convert the brief into a research design.

Prompt:

```text
Read docs/project_brief.md. Draft a research design memo. Include literature
context, hypotheses or model claims, data or model inputs, method,
identification or assumptions, outputs, limitations, and replication
implications. Do not write code.
```

### Exercise 5: Data Or Model-Input Map

Goal: document what the project depends on.

Prompt:

```text
Create a data or model-input map. For empirical data, include source, access,
format, unit, variables, coverage, restrictions, and version. For theory or
macro modelling, include primitives, parameters, equations, calibration
targets, solver inputs, outputs, and checks.
```

### Exercise 6: Acceptance Criteria

Goal: define done before implementation.

Prompt:

```text
Convert the design memo into issues with acceptance criteria. Each issue must
have allowed files, verification evidence, dependency label, and out-of-scope
note. Do not implement.
```

## 46. Day 3 Exercises

Use `exercises/day3-agent-workflows.md` as the canonical exercise path. All
nine exercises use the Card-Krueger DiD running case. Each exercise states
acceptance criteria before the prompt — carry the Day 2 habit forward.

| # | Exercise | Focus |
| --- | --- | --- |
| 1 | Review role on CK diff | Read-only review of `examples/card-krueger-toy/` |
| 2 | Replication-checker skill | GREEN / YELLOW / RED verdict with evidence |
| 3 | Multiple subagent roles | `pr-reviewer` and `data-reviewer` compared |
| 4 | Orchestration log | Four CK swarm streams in `notes/orchestration_log.md` |
| 5 | Autonomous-agent risk card | `agent-harness/autonomous_agent_risk_card.md` |
| 6 | Configure and trace a hook | Postcondition hook for `did_analysis.py` |
| 7 | Verification loop | `loop-verifier` subagent; record verdict in orchestration log |
| 8 | Write a goal file | Draft goal with verifiable acceptance criteria |
| 9 | Explore a plugin | Read `plugin.json`; explain CK workflow contribution |

### Exercise 1: Review Role On The Card-Krueger Diff

**Acceptance criteria:** review covers units, sample restriction, synthetic-data
caveat; blockers or clean verdict with evidence; explicit merge recommendation.

```text
Read examples/card-krueger-toy/src/did_analysis.py and
examples/card-krueger-toy/README.md. Act as a read-only reviewer. Check unit of
observation, sample restriction, synthetic-data caveat, hardcoded paths, and
verification command. Return blockers first. Do not edit files.
```

### Exercise 2: Replication-Checker On The Card-Krueger Toy

**Acceptance criteria:** skill invoked; GREEN / YELLOW / RED verdict with evidence.

```text
Use the replication-checker workflow in
agent-harness/skills/replication-checker/SKILL.md applied to
examples/card-krueger-toy/. Do not edit files. Assign a GREEN, YELLOW, or RED
verdict with evidence.
```

### Exercise 3: Multiple Subagent Role Prompts

**Acceptance criteria:** at least two roles tried; comparison note recorded.

Use `agent-harness/subagents/pr-reviewer.md` and
`agent-harness/subagents/data-reviewer.md` in turn on
`examples/card-krueger-toy/`.

### Exercise 4: Orchestration Log For The CK Swarm

**Acceptance criteria:** one row per stream; dependencies and merge order explicit.

Read `examples/card-krueger-swarm/README.md` and populate
`notes/orchestration_log.md`.

### Exercise 5: Autonomous-Agent Risk Card

**Acceptance criteria:** all six risk-card fields completed; one approval gate
and one unacceptable-use condition stated.

```text
Evaluate [tool] using agent-harness/autonomous_agent_risk_card.md applied to
the Card-Krueger project. Recommend read-only, branch-isolated write use, or no use.
```

### Exercise 6: Configure And Trace A Hook

**Acceptance criteria:** hook event type named; verification command stated;
config file location identified for your tool lane.

Read `agent-harness/skills/hooks/SKILL.md`. Draft the hook entry that fires
`python3 -m pytest examples/card-krueger-toy/tests` after edits to
`did_analysis.py`.

### Exercise 7: Design And Run A Verification Loop

**Acceptance criteria:** one loop iteration recorded in `notes/orchestration_log.md`
with GREEN / YELLOW / RED verdict.

Read `agent-harness/skills/loop-on-verification/SKILL.md` and apply
`agent-harness/subagents/loop-verifier.md` to a CK task from
`examples/card-krueger-goals/goals/`.

### Exercise 8: Write A Goal File

**Acceptance criteria:** goal file with name, description, approach, verifiable
acceptance criteria, and constraints (raw data, synthetic caveat).

Draft `examples/card-krueger-goals/goals/ck-my-goal.md` using worked examples in
`examples/card-krueger-goals/goals/` as a model.

### Exercise 9: Explore A Plugin

**Acceptance criteria:** plugin name, one skill or rule identified, CK workflow
contribution explained.

```text
Read the plugin.json for [plugin name]. Identify declared skills and rules.
Summarise what one skill does. Do not edit files.
```

## 47. Final Exercises

### Exercise 11: Replication README

Goal: make the project runnable or honestly document why it is not.

Prompt:

```text
Draft replication/README.md from the current project. Include overview,
software versions, data or model inputs, setup, run instructions, expected
outputs, troubleshooting, known limitations, and contact. Use my software lane,
not a default language.
```

### Exercise 12: Presentation

Goal: communicate the research and workflow.

Prompt:

```text
Draft a 5 to 7 minute presentation. Include research question, motivation,
data or model, method, main result or blocker, agentic workflow, replication
status, and next 30 days. Keep claims modest.
```

## 48. Final Checklist

By the end of the workshop, aim to have:

- repository opened in a chosen agent;
- privacy boundaries documented;
- `AGENTS.md` or equivalent project guidance;
- project brief;
- research design memo;
- bibliography or reference list;
- data or model-input map;
- issue backlog with acceptance criteria;
- context patterns note;
- one skill or reusable workflow used;
- one subagent or reviewer role used (e.g. pr-reviewer, data-reviewer, or
  literature-reviewer);
- orchestration log with at least one stream entry and loop iteration if applicable;
- hook configuration drafted or identified for your tool lane;
- one goal file with verifiable acceptance criteria;
- one plugin manifest read and its contribution documented;
- autonomous-agent risk card;
- replication README;
- clean-run evidence or documented blocker;
- presentation outline;
- 30-day adoption plan.

## 49. The Habit To Keep

The workshop is not about memorizing prompts. It is about changing the shape of
research work so that each step is explicit, reviewable, and reproducible.

Before asking an agent to act, ask yourself:

1. What exactly do I want?
2. What context does the agent need?
3. What should it not touch?
4. What evidence will show that the task is done?
5. What do I, as the economist, still need to review?

If you can answer those five questions, agentic coding becomes a serious
research workflow rather than a collection of clever prompts.
