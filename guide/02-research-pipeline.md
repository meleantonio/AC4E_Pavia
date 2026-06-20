# Guide Chapter 2: Research Pipeline and Spec-Driven Development

This chapter follows the Day 1 afternoon bridge and Day 2 core work. It begins
only after the basic agent workflow, repository orientation, privacy boundaries,
and GitHub concepts have been introduced. The goal is to turn a research idea
into a set of artifacts that can guide implementation and review.

## 2.1 Why Research Framing Comes Before Coding

Agents are eager to build. Research often benefits from the opposite order:
first define the question, then define the evidence, then build the smallest
workflow that can produce or inspect that evidence.

A vague instruction such as:

```text
Run the analysis for my minimum wage project.
```

is not enough. The agent would need to guess:

- which data source to use;
- which sample restrictions apply;
- which outcome matters;
- which comparison group is appropriate;
- which software lane to use;
- what output counts as success;
- which claim is allowed.

This chapter teaches the artifacts that remove those guesses.

## 2.2 The Project Brief

The project brief is the first research artifact. It is short, but it prevents
many later mistakes.

It should answer:

- What is the research question?
- Why does it matter?
- What contribution or learning goal is realistic?
- What data or model inputs are needed?
- What method or modelling approach will be used?
- What can be done during the workshop?
- What is explicitly out of scope?

Prompt:

```text
Here is my draft research idea. Do not edit files. Tell me whether it is
specific enough for a three-day prototype. Identify the likely unit of
observation, outcome, treatment or key variable, data or model inputs, method,
and one major blocker.

[paste idea]
```

Then:

```text
Draft a one-page project brief. Include title, research question, motivation,
expected contribution, data or model inputs, method, three-day deliverable, and
out-of-scope claims. Keep the implementation language neutral.
```

Only after review:

```text
Create or update docs/project_brief.md from the approved brief. Do not edit
analysis code.
```

## 2.3 Running Case: Card-Krueger Project Brief

Example:

```markdown
# Project Brief

## Title
Minimum Wage Increase and Fast-Food Employment

## Research question
Did fast-food employment in New Jersey change relative to eastern Pennsylvania
after New Jersey raised its minimum wage in April 1992?

## Motivation
The minimum wage is a central labor economics policy question. The
Card-Krueger study is a useful teaching case because the design is transparent
and the replication workflow can be kept small.

## Expected contribution
This is a replication-oriented workshop exercise. It aims to produce a clean
data map, design memo, baseline table, and replication README.

## Data or model inputs
Public Card-Krueger fast-food restaurant data, with observations before and
after the policy change.

## Method
Difference-in-differences comparison between New Jersey and eastern
Pennsylvania restaurants.

## Out of scope
No general claim about all minimum wage policies. No full literature review.
No unrestricted causal claim beyond the design.
```

## 2.4 Spec-Driven Development For Research

Spec-driven development, or SDD, separates the research goal from the
implementation steps.

| Stage | Question | Research artifact |
| --- | --- | --- |
| Intent | What are we trying to learn or produce? | project brief |
| Requirements | What must be true of the output? | acceptance criteria |
| Design | How will the project produce the output? | research design memo |
| Tasks | What work units can be assigned and reviewed? | GitHub issues |

The point is not to write a long software document. The point is to avoid
asking agents to infer unstated research decisions.

## 2.5 Intent

Intent should be specific.

Weak:

```text
Study labor markets.
```

Better:

```text
Produce a replication-oriented baseline estimate of how fast-food employment
changed in New Jersey relative to eastern Pennsylvania after the 1992 minimum
wage increase.
```

Macro example:

```text
Produce a small documented VAR or local-projection exercise showing how
inflation and unemployment move after a federal funds rate shock using FRED
series.
```

Theory example:

```text
Compute equilibrium quantities and comparative statics in a Cournot duopoly
with asymmetric marginal costs.
```

Econometrics example:

```text
Use simulation to compare OLS and IV bias as instrument strength changes in a
simple demand equation.
```

## 2.6 Requirements

Requirements should be observable. Use EARS-style language when helpful.

Applied example:

```text
WHEN the baseline analysis runs, it SHALL report sample counts by state and
survey wave before reporting treatment effects.
```

Macro example:

```text
GIVEN the selected FRED series, the data-preparation step SHALL document
frequency, units, transformation, and sample period.
```

Theory example:

```text
GIVEN parameter values in the model-input file, the solver SHALL report
equilibrium quantities and verify non-negative outputs.
```

Econometrics example:

```text
GIVEN a fixed random seed, the simulation SHALL reproduce the same summary
table of bias, variance, and coverage.
```

Blocked-data example:

```text
IF restricted data cannot be included, the replication README SHALL document
access requirements and provide a public or synthetic fallback where possible.
```

## 2.7 Research Design Memo

The design memo expands the project brief into a plan.

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
assumptions, and blockers. Do not write code.
```

Review prompt:

```text
Review this design memo as a skeptical economist. Do not edit files. Flag
vague claims, missing variables or model inputs, weak identification statements,
unclear assumptions, and outputs that cannot be verified.
```

## 2.8 Literature Mapping

A literature map is not a substitute for reading. It is a structured way to
organize references and decide how they inform the project.

For each reference, record:

- citation;
- question;
- data or model;
- method;
- main result or proposition;
- relevance to your project;
- how your project differs.

Prompt:

```text
Search for 5 to 8 core references on [topic]. For each, provide citation,
question, data or model, method, main result, and relevance to my project.
Include links. Flag any uncertain bibliographic details.
```

For Card-Krueger:

```text
Create a literature map for the minimum wage employment debate around the
Card-Krueger study. Include the original study, at least one critique or
reanalysis, and one later review or meta-analysis. Do not invent citation
details.
```

## 2.9 Data Or Model-Input Map

Empirical projects need data maps. Theory and macro projects may need
model-input maps. The purpose is the same: document what the project depends
on.

Empirical map fields:

| Field | Description |
| --- | --- |
| Source | Where the data come from |
| Access | public, restricted, API, manual download, proprietary |
| Format | CSV, Stata, Excel, API, database |
| Unit | restaurant, firm, person, household, country-year |
| Key variables | outcome, treatment, controls, IDs, time |
| Coverage | geography and time period |
| Restrictions | license, confidentiality, access steps |
| Version | release or date accessed |

Model-input map fields:

| Field | Description |
| --- | --- |
| Primitive | preferences, technology, endowments, information |
| Parameter | value, source, calibration target |
| Equation | model block or equilibrium condition |
| Solver input | grid, tolerance, seed, initial condition |
| Output | moments, policy functions, equilibrium objects |
| Check | feasibility, convergence, market clearing |

Prompt:

```text
Create a data or model-input map. Use empirical fields for a data project. Use
primitives, parameters, equations, solver inputs, outputs, and checks for a
theory or macro modelling project. Do not write analysis code.
```

## 2.10 Turning Design Into Issues

Only now do research issues become useful. You have already learned GitHub
basics, created a project brief, and drafted the design. That gives the agent
enough structure.

Prompt:

```text
Read docs/project_brief.md and docs/research_design_memo.md. Create 8 to 10
issues. Each issue must include title, purpose, allowed files, acceptance
criteria, dependency label, verification command or manual check, and
out-of-scope note. Do not implement.
```

Example issue:

```text
Title: Document Card-Krueger data source and variables

Allowed files:
docs/data_source_map.md
references/bibliography.bib

Acceptance criteria:
- source link and access date are recorded;
- unit of observation is stated;
- treatment and comparison groups are identified;
- employment outcome is named;
- sample restriction risks are listed;
- no cleaning or estimation code is added.

Dependency:
Can run in parallel with literature mapping.

Verification:
Read-only review against the project brief and source links.

Out of scope:
Cleaning data or estimating effects.
```

## 2.11 Software-Lane Planning

After the design is stable, ask for implementation planning in your lane.

R:

```text
Plan an R implementation of this design. Include scripts, package setup,
run command, output files, and review checks. Do not assume Python.
```

Stata:

```text
Plan a Stata implementation. Include master do-file, cleaning do-file,
estimation do-file, log files, output tables, and path checks.
```

MATLAB:

```text
Plan a MATLAB implementation. Include main script, functions, parameter file,
solver settings, output files, and batch run command.
```

Python:

```text
Plan a Python implementation as one possible lane. Include scripts, dependency
file, test or assertion checks, output files, and run command.
```

## 2.12 Exercises

### Exercise 1: Draft A Project Brief

Use a real research idea or one of the examples:

- Card-Krueger minimum wage replication;
- FRED macro time-series exercise;
- Cournot duopoly comparative statics;
- OLS versus IV simulation;
- World Bank/Penn World Table coverage map.

### Exercise 2: Draft A Design Memo

Prompt:

```text
Read docs/project_brief.md. Draft docs/research_design_memo.md. Do not write
code. Clearly separate facts, assumptions, and blockers.
```

### Exercise 3: Build A Data Or Model-Input Map

Prompt:

```text
Read the design memo. Create a data or model-input map. Include units,
coverage, access, restrictions, version, and replication implications.
```

### Exercise 4: Create Issues

Prompt:

```text
Turn the memo and map into agent-friendly issues with acceptance criteria and
dependency labels. Do not implement.
```

## 2.13 Chapter Checklist

- [ ] Project brief exists.
- [ ] Research question is specific and bounded.
- [ ] Design memo exists.
- [ ] Literature map or reference list exists.
- [ ] Data or model-input map exists.
- [ ] Requirements are observable.
- [ ] Issues have allowed files and acceptance criteria.
- [ ] Software lane is documented.
- [ ] Out-of-scope claims are explicit.
