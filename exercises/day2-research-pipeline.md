# Day 2 Exercises - Research Pipeline And SDD

These exercises match `GUIDE.md` Parts III-IV. They turn a research idea into
reviewable tasks before implementation starts.

## Exercise 1 - Research Design Memo

Goal: convert the project brief into a design.

Prompt:

```text
Read docs/project_brief.md. Draft a research design memo. Include literature
context, hypotheses or model claims, data or model inputs, method,
identification or assumptions, outputs, limitations, and replication
implications. Do not write code.
```

Output to record:

- `docs/research_design_memo.md`;
- three uncertainties that require human review;
- any claim the agent is not allowed to certify.

Review check: separate research claims from code mechanics.

## Exercise 2 - Literature Map

Goal: make the literature task bounded.

Task:

- select three to five starting references;
- record citation keys, links or DOIs, and why each paper matters;
- mark whether each reference supports motivation, method, data, or
  interpretation.

Prompt template:

```text
Using only the references I provide below, create a compact literature map.
Do not search the web. Do not invent findings. Separate motivation, method,
data, and interpretation.
```

Review check: the output should not make claims beyond the supplied sources.

## Exercise 3 - Data Or Model-Input Map

Goal: document what the project depends on.

Prompt:

```text
Create a data or model-input map. For empirical data, include source, access,
format, unit, variables, coverage, restrictions, and version. For theory or
macro modelling, include primitives, parameters, equations, calibration
targets, solver inputs, outputs, and checks.
```

*Do not read `data/raw/`, `data/private/`, or `.env`. Work from existing documentation, project notes, or paper metadata.*

Output to record:

- `docs/data_source_map.md`;
- source and access notes;
- units and sample restrictions;
- transformation notes.

Review check: raw data should remain untouched.

## Exercise 4 - Acceptance Criteria

Goal: define done before implementation.

Prompt:

```text
Read docs/research_design_memo.md and docs/data_source_map.md. Convert the
design into five issue-sized tasks. Each issue must include allowed files,
acceptance criteria, dependency label, verification evidence, and out-of-scope
note. Do not implement.
```

Review check: each issue should be small enough for one branch and one review.

## Exercise 5 - Running Case Practice

Goal: connect the Card-Krueger running case in `GUIDE.md` to a small runnable
example.

Task:

- read `examples/card-krueger-toy/README.md`;
- run the toy example;
- write one issue that would extend the example without touching raw data or
  making causal claims.

Commands:

```bash
python3 examples/card-krueger-toy/src/did_analysis.py
python3 -m pytest examples/card-krueger-toy/tests
```

Review check: the issue should call the data synthetic and should not describe
the estimate as evidence about the real Card-Krueger study.

## Extra Practice - Debugging Workflow

Take a failing command or traceback from your own project and ask for a
read-only debugging plan first:

```text
Read this traceback and the named files only. Do not edit files. Explain the
most likely cause, the smallest reproduction command, and the first safe fix to
try. Separate facts from guesses.
```
