# Guide Chapter 1: Foundations, GitHub, and Governance

This chapter corresponds to the first part of Day 1. It is the foundation for
the rest of the workshop. Do not skip it if you are new to agentic coding. Most
problems later in the workflow come from weak foundations: vague prompts, poor
context, missing privacy boundaries, and changes that are not reviewable.

## 1.1 What Agentic Coding Is

Agentic coding means working with an AI system that can do more than answer a
question. Depending on the tool and permissions, an agent can inspect files,
search a repository, propose a plan, edit files, run commands, call tools, and
summarize the result.

For economists, this is useful because research projects contain many
interdependent artifacts:

- data dictionaries;
- do-files, scripts, notebooks, or MATLAB functions;
- model equations and calibration files;
- tables and figures;
- bibliography files;
- LaTeX papers and slides;
- replication READMEs;
- review notes and coauthor comments.

An agent can help connect those artifacts, but it needs guidance. It does not
know your identification strategy, data license, coauthor norms, or publication
standards unless you make them explicit.

The basic rule is:

```text
The agent may help draft, inspect, edit, and verify bounded tasks. The economist
owns the question, assumptions, interpretation, data rights, and final claims.
```

## 1.2 What Agents Are Good At

Agents are useful for:

- explaining unfamiliar code or project structure;
- drafting first versions of documentation;
- turning rough notes into structured templates;
- creating small scripts or do-file sections;
- writing tests or manual verification checklists;
- spotting missing paths, inconsistent variable names, and unclear run
  instructions;
- reviewing whether code and README instructions match;
- helping convert a large goal into smaller tasks.

They are weaker at:

- deciding whether an identification strategy is credible;
- knowing private data restrictions;
- recognizing subtle institutional context;
- verifying facts they have not grounded in sources;
- making judgment calls about research claims;
- preserving scope if the prompt is vague.

This is why the course emphasizes workflow, context, and review rather than
"magic prompts."

## 1.3 The Four Basic Workflows

Different tools expose these workflows differently. Cursor may show visible
mode labels; Codex and Claude Code may express the same pattern through
threads, slash commands, planning prompts, or permission settings. Use the
concept even if your tool names it differently.

Verify in your Cursor version: UI labels for Agent, Plan, Debug, rules,
subagents, skills, hooks, and review surfaces can change. Prefer official docs
and your installed version over screenshots in older materials.

### Read-Only Workflow

Use read-only prompts before you let the agent edit anything.

Good read-only tasks:

- "Explain this repository."
- "Which files should I avoid?"
- "What does this Stata log error mean?"
- "What assumptions are missing from this model note?"
- "Does this table note overclaim?"

Example:

```text
Read README.md, START_HERE.md, AGENTS.md, and days/day1.md. Do not edit files.
Explain what this repository is for, what I should do first, which files I
should not expose to an agent, and how setup is verified.
```

Why this works:

- it names files;
- it says not to edit;
- it asks for concrete outputs;
- it checks privacy and verification.

### Planning Workflow

Use planning prompts when there are multiple steps.

Example:

```text
Plan how I should set up this repository for a Stata-based applied micro
project. Do not edit files. Include folder conventions, where to put do-files,
how to record logs, privacy boundaries, and the first small task.
```

Planning should produce an ordered list of decisions and tasks. It should not
silently edit files.

### Implementation Workflow

Use implementation only after the scope is clear.

Example:

```text
Edit only notes/context_patterns.md. Add a section describing my tool lane
(Cursor), my software lane (Stata), files that should not be read, and the
manual check I will use for Stata logs. Do not edit any other file.
```

Implementation prompts should specify:

- allowed files;
- expected change;
- non-goals;
- verification evidence.

### Debugging Workflow

Debugging should start from a symptom.

Example:

```text
Read this R error and the script that produced it. Do not edit files. Identify
the first failing line, the likely cause, and one minimal fix. Say what command
I should rerun after the fix.
```

Debugging is not "try random changes." It is evidence, hypothesis, small fix,
rerun.

## 1.4 Context Control

Context is what the agent can see and what it is told to prioritize. Context is
the most important quality lever in agentic coding.

### Tight Context

Use tight context for precision.

```text
Only read START_HERE.md and AGENTS.md. Do not edit files. Identify what I
should do first, which files are off limits, and which setup check I should run.
```

Tight context is best when:

- one file matters;
- a prompt should not drift;
- the task has a clear boundary;
- private data must be excluded.

### Wide Context

Use wide context for consistency.

```text
Search the repository for every mention of the main outcome variable. Do not
edit files. Report inconsistent variable names, units, or sample restrictions.
```

Wide context is best when:

- paths must align across README and scripts;
- tables and text must match;
- code uses multiple modules;
- a replication command must be checked against actual files.

### External Context

Use web or official documentation when the answer depends on facts outside your
repo.

```text
Search official documentation for this data source. Summarize access method,
variable definitions, coverage, citation requirements, and any version caveats.
Include links.
```

Use external context for:

- literature;
- data source documentation;
- software package syntax;
- agent-tool documentation.

## 1.5 Privacy Boundaries

Before using agents on research files, decide what they should not see.

Common boundaries:

- `.env`, tokens, credentials, API keys;
- restricted microdata;
- confidential surveys;
- proprietary data extracts;
- unpublished coauthor drafts if not cleared;
- identifiable individual-level data;
- private referee reports;
- large raw files that do not help the task.

Write boundaries in project instructions:

```markdown
## Privacy

- Do not read or summarize files under `data/raw/`, `data/private/`, or
  `restricted/`.
- Do not read `.env`, credentials, tokens, or API keys.
- Do not paste individual-level records into chat.
- Use synthetic, public, or derived data unless explicitly authorized.
```

For Cursor, also use ignore files where appropriate. For Codex, Claude Code, or
other agents, use their project-instruction and permission surfaces. The exact
UI differs; the rule is stable.

## 1.6 Project Instructions

`AGENTS.md` is the shared front door for agents. It tells the agent what the
project is, how to work, and what not to touch.

Minimal structure:

```markdown
# Agent Instructions

## Project
This repository contains a [software lane] economics research project on
[question].

## Main software lane
[R / Stata / MATLAB / Python / Julia / mixed.]

## Key paths
- `docs/` — workshop notes and research documents introduced later.
- `scripts/` — runnable scripts or do-files.
- `outputs/` — generated results.
- `replication/` — clean-run instructions.

## Rules
- Use relative paths.
- Do not edit raw data.
- Do not claim causality beyond the stated research design.
- Record verification evidence before merge.

## Privacy
- Do not read `.env`, credentials, or restricted data folders.
```

Tool-specific adapters can help, but they should not replace shared
instructions:

- Cursor: `.cursor/rules/` for file-specific rules.
- Claude Code: `CLAUDE.md` can import or summarize shared instructions.
- Codex: `AGENTS.md` and nested instruction files.
- Other agents: rules, memories, routines, or project prompts.

## 1.7 GitHub Basics

GitHub appears early because it gives you a control plane. A control plane is
where work is described, isolated, reviewed, and accepted.

Basic vocabulary:

- **Repository:** project folder with version history.
- **Commit:** saved change.
- **Branch:** separate line of work.
- **Issue:** task card.
- **Pull request:** proposed change with a diff.
- **Review:** check before accepting.
- **Merge:** accept work into the main branch.

You do not need advanced Git to use the course workflow. The basic loop is:

```text
issue -> branch -> change -> review -> merge
```

## 1.8 First Safe Issue

The first issue should not require a research design memo. The design memo has
not been introduced yet. Start with setup or orientation.

Example:

```text
Title: Day 1 setup verification

Description:
Confirm that the repository opens in my chosen agent and that I know the setup
verification command or manual check.

Acceptance criteria:
- chosen agent/tool lane recorded;
- software lane recorded if known;
- setup check run or blocker documented;
- no private data added;
- diff reviewed before merge.
```

This teaches the issue workflow before research-specific tasks.

## 1.9 First Pull Request

A pull request should tell a reviewer what changed and how to check it.

Example:

```markdown
## Summary
- Records my tool lane and software lane.
- Adds initial context notes.

## Verification
- Read-only agent review of Day 1 instructions.
- No private data or analysis code added.

## Notes
- Research question will be drafted later in the project brief step.
```

## 1.10 Exercises

### Exercise 1: Read The Repository

Prompt:

```text
Read README.md, START_HERE.md, AGENTS.md, and days/day1.md. Do not edit files.
Explain the repository in five bullets and identify the setup check.
```

Expected output:

- a repo map;
- setup command or manual check;
- files to avoid;
- next safe action.

### Exercise 2: Record Your Lanes

Choose:

- main agent/tool lane: Codex, Claude Code, Cursor, CLI, other;
- research software lane: R, Stata, MATLAB, Python, Julia, mixed, other.

Prompt:

```text
Edit only notes/context_patterns.md. Record my agent/tool lane, research
software lane, files that should not be read, and the setup verification check.
Do not edit other files.
```

### Exercise 3: Create A Safe First Issue

Create an issue for setup verification or repository orientation. Do not create
research implementation issues until the project brief and SDD sections have
been introduced.

### Exercise 4: Review One Diff

Prompt:

```text
Review this diff before I merge it. Focus on scope drift, private data,
unrelated edits, and whether it satisfies the issue acceptance criteria.
```

## 1.11 Field Examples

Labor:

- Day 1 output is not the DiD estimate. It is the project setup and initial
  project brief scaffold.

Macro:

- Day 1 output is not a VAR. It is a repo that can later document FRED series,
  transformations, and run commands.

Theory:

- Day 1 output is not a solved model. It is a model-note scaffold and clear
  software lane, such as MATLAB or Julia.

Econometrics:

- Day 1 output is not a Monte Carlo table. It is a clear simulation project
  brief scaffold and verification habit.

## 1.12 Chapter Checklist

- [ ] You can explain what an agent can and cannot own.
- [ ] You have used a read-only prompt before editing.
- [ ] You know your main agent/tool lane.
- [ ] You know your research software lane or have recorded that it is undecided.
- [ ] Privacy boundaries are written down.
- [ ] `AGENTS.md` or equivalent project guidance exists.
- [ ] You understand issue, branch, pull request, review, and merge.
- [ ] You have one safe first issue or setup note.
