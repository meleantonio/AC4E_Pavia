# Prompt Patterns

These prompts match the central rule in `GUIDE.md`: scope, evidence, review.
Copy them into your agent and replace the bracketed text.

## Read-Only Understanding

```text
Read [specific files]. Do not edit files. Explain what the project does, which
inputs it expects, which outputs it creates, what could break on a clean
machine, and which command or manual check verifies the result.
```

Good evidence:

- file list inspected;
- summary of inputs and outputs;
- setup or verification command;
- explicit uncertainty list.

## Planning Before Implementation

```text
Read [brief/design/data map]. Do not edit files. Propose issue-sized tasks.
For each task, include allowed files, acceptance criteria, verification
evidence, dependencies, and out-of-scope claims.
```

Good evidence:

- tasks small enough for separate branches;
- clear dependency order;
- no implementation hidden inside the plan.

## Bounded Implementation

```text
Implement [one task] by editing only [allowed files]. Preserve the documented
data source, units, transformations, and sample restrictions. Run [command] and
summarize the diff and verification result.
```

Good evidence:

- scoped diff;
- command output;
- note of anything not run.

## Debugging

```text
Read this traceback and [named files] only. Do not edit files yet. Identify the
most likely cause, the smallest reproduction command, and the first safe fix.
Separate facts from guesses.
```

Good evidence:

- reproducible command;
- one smallest fix;
- no broad refactor before diagnosis.

## Review

```text
Review this branch against AGENTS.md and the research design memo. Do not edit
files. Check scope drift, privacy, reproducibility, data source documentation,
units, transformations, sample restrictions, test evidence, and overclaiming.
Return blockers first.
```

Good evidence:

- findings with file references;
- missing tests or commands;
- explicit merge recommendation.
