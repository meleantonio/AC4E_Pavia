# Guide Chapter 4: Replication, Presentation, and Adoption

This chapter corresponds to the Day 3 integration and final presentation
blocks. The goal is to turn workshop activity into a research package another
person can inspect, run, or extend.

## 4.1 Why Replication Is Not Cleanup

Replication packaging is part of the research product. In economics, "it works
on my machine" is not enough. A colleague, referee, research assistant, or
future-you needs to know:

- what the project is about;
- what data or model inputs are required;
- what software is needed;
- what command or manual sequence runs the project;
- what outputs to expect;
- what limitations remain;
- what cannot be shared.

Agents can help write and check these instructions, but they cannot certify
that a result is meaningful. The human researcher reviews the claims and the
evidence.

## 4.2 Integration Checklist

Before writing the final presentation, integrate the project.

Check:

- repository paths match across scripts and README;
- data or model-input names are consistent;
- units are documented;
- output files exist or blockers are explained;
- claims in text match tables, figures, or model outputs;
- private data and secrets are excluded;
- run instructions are literal;
- review evidence is recorded.

Prompt:

```text
Review this project for final integration. Do not edit files. Check whether
paths, variable names, units, output files, README commands, and research claims
are consistent. Return blockers first.
```

## 4.3 Replication README Structure

Use this structure:

```markdown
# Replication README

## Overview
[Question, method, and package contents.]

## Software and versions
[R/Stata/MATLAB/Python/Julia/other versions and packages.]

## Data or model inputs
[Sources, access, restrictions, manual steps, calibration files.]

## Setup
[Environment, package install, folder expectations.]

## Run instructions
[Exact command or manual sequence.]

## Expected outputs
[Tables, figures, logs, datasets, model objects.]

## Troubleshooting
[Likely failures and fixes.]

## Known limitations
[What is blocked, restricted, preliminary, or out of scope.]

## Contact or ownership
[Who maintains the package.]
```

## 4.4 Language-Lane Run Instructions

R:

```bash
Rscript scripts/run_analysis.R
```

If using `renv`, document restore steps:

```bash
Rscript -e "renv::restore()"
```

Stata:

```bash
stata-mp -b do scripts/run_analysis.do
```

Document:

- Stata version;
- required ado packages;
- expected log path;
- expected output tables;
- how errors appear in the log.

MATLAB:

```bash
matlab -batch "run('scripts/run_analysis.m')"
```

Document:

- MATLAB version;
- required toolboxes;
- solver settings;
- random seeds;
- expected `.mat`, table, or figure outputs.

Python:

```bash
python scripts/run_analysis.py
```

Document:

- environment setup;
- dependency file;
- test or assertion command;
- expected outputs.

Julia:

```bash
julia --project=. scripts/run_analysis.jl
```

Other:

```text
Write the shortest exact sequence a colleague can follow. Include install,
configuration, run, and output inspection.
```

## 4.5 Replication Prompts

Draft:

```text
Draft replication/README.md from the current project. Use my software lane,
not a default language. Include overview, software versions, data or model
inputs, setup, run instructions, expected outputs, troubleshooting, known
limitations, and contact.
```

Review:

```text
Review replication/README.md as a skeptical replicator. Starting from a clean
checkout, identify missing setup steps, unclear data access, hardcoded paths,
missing outputs, private-data risks, and claims that are not supported by the
documented run.
```

Clean-run log:

```text
I ran the project from a clean checkout. Convert these notes into a clean-run
evidence section. Redact secrets and private paths. Include commands, runtime,
software versions, outputs, and blockers.

[paste notes]
```

## 4.6 Running Case: Card-Krueger Replication README

A minimal README for the running case should include:

- research question;
- public source link and access date;
- software lane;
- manual or scripted data preparation;
- baseline estimation command;
- expected baseline table path;
- sample-count output;
- limitations.

Important limitation language:

```text
This package is a workshop replication exercise. It demonstrates a baseline
difference-in-differences workflow and review process. It does not provide a
new estimate for policy generalization beyond the original design.
```

## 4.7 Presentation Structure

The final presentation is 5 to 7 minutes. It should be short and honest.

Use this order:

1. Research question.
2. Why it matters.
3. Data or model and method.
4. Main result, prototype, or blocker.
5. Agentic workflow: what the agent did and what a human reviewed.
6. Replication status.
7. Next 30 days.

Good presentation language:

```text
The agent helped draft the data map and create a first pass at the cleaning
workflow. I reviewed variable definitions, sample restrictions, and the output
table. The current package runs through the baseline table, while robustness
checks remain future work.
```

Bad presentation language:

```text
The AI proved the effect.
```

Do not outsource proof, identification, or interpretation to the agent.

## 4.8 Presentation Prompts

Draft:

```text
Draft a 5 to 7 minute presentation from docs/project_brief.md,
docs/research_design_memo.md, notes/orchestration_log.md, notes/review_log.md,
and replication/README.md. Keep claims modest. Include one slide on what the
agent did and what I reviewed.
```

Tighten:

```text
This presentation is too long. Cut it to 5 to 7 minutes. Preserve research
question, method, one main result or blocker, workflow, replication status, and
next steps.
```

Review:

```text
Review this presentation as a skeptical economist. Flag overclaims, missing
limitations, unclear method language, and anything that sounds like the agent
certified the research claim.
```

## 4.9 30-Day Adoption Plan

The workshop should leave you with a habit, not just a folder.

Week 1: consolidate

- add or improve `AGENTS.md` in one active research repo;
- document privacy boundaries;
- define one verification command or manual check.

Week 2: apply

- choose one real research task;
- create an issue;
- work on a branch;
- review the diff before merge.

Week 3: extend

- create one reusable skill or saved prompt;
- create one reviewer role;
- use both on a real artifact.

Week 4: sustain

- run one replication check;
- update the README;
- share the workflow with a coauthor, RA, or colleague.

Prompt:

```text
Create a 30-day adoption plan for my actual research workflow. My software lane
is [R/Stata/MATLAB/Python/Julia/other]. My constraints are [teaching load,
coauthors, deadlines, data access]. Include one weekly habit, one artifact, one
review gate, and one privacy rule per week.
```

## 4.10 Final Handoff Note

If someone else will continue the project, write a handoff note:

```markdown
# Handoff

## Current status

## What runs

## What is blocked

## Data or model-input access

## Agent work used

## Human review completed

## Next recommended issue
```

Prompt:

```text
Draft a handoff note from the project brief, design memo, orchestration log,
review log, and replication README. Keep it factual. Separate completed work,
blockers, and next recommended issue.
```

## 4.11 Exercises

### Exercise 1: Write Replication README

Use your actual software lane. Do not let the agent default to a different
language.

### Exercise 2: Run Or Document Clean Run

Run the documented command or manual sequence. If it fails, document the
smallest failing step and the blocker.

### Exercise 3: Draft Presentation

Prepare 5 to 7 minutes. Include what the agent did and what you reviewed.

### Exercise 4: Draft 30-Day Plan

Make it realistic enough to do during a normal work month.

## 4.12 Chapter Checklist

- [ ] Integration review completed.
- [ ] `replication/README.md` exists.
- [ ] Software lane and versions are documented.
- [ ] Data or model-input access is documented.
- [ ] Run command or manual sequence is literal.
- [ ] Expected outputs are listed.
- [ ] Clean run passed or blocker is documented.
- [ ] Presentation outline exists.
- [ ] Agent contribution and human review are visible.
- [ ] 30-day adoption plan exists.
