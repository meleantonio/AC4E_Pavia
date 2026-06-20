# Card-Krueger Toy Example

This example mirrors the running case in `GUIDE.md`: fast-food employment in
New Jersey and eastern Pennsylvania before and after New Jersey's April 1992
minimum wage increase.

The data here are **synthetic teaching data**. They are not Card and Krueger's
raw data and should not be used for a research claim.

## Project Map

- `data/toy_fast_food.csv` - small synthetic balanced panel.
- `src/did_analysis.py` - loads the CSV, checks the panel, estimates a simple
  difference-in-differences comparison, and prints a replication note.
- `tests/test_did_analysis.py` - fast checks for the teaching workflow.

## Data Documentation

- **Source:** hand-written synthetic CSV in this example folder.
- **Unit:** store-wave observation.
- **Outcome:** full-time-equivalent employment, in workers.
- **Treatment group:** New Jersey stores, coded `NJ`.
- **Comparison group:** eastern Pennsylvania stores, coded `PA`.
- **Timing:** `before` and `after` waves.
- **Sample restriction:** stores with exactly one before and one after
  observation and no missing employment value.
- **Transformation:** create `treated` and `post` indicators, compute group
  means, then compare the NJ change with the PA change.

## Run

From the repository root:

```bash
python3 examples/card-krueger-toy/src/did_analysis.py
python3 -m pytest examples/card-krueger-toy/tests
```

## Practice Prompts

Read-only:

```text
Read examples/card-krueger-toy/README.md and
examples/card-krueger-toy/src/did_analysis.py. Do not edit files. Explain the
unit of observation, treatment group, comparison group, outcome, timing,
sample restriction, and verification command.
```

Planning:

```text
Plan one issue that extends the Card-Krueger toy example with a robustness
check. Do not implement. Include allowed files, acceptance criteria,
verification evidence, and an out-of-scope note saying this synthetic example
cannot establish a causal claim.
```

Review:

```text
Review a diff to this example. Check whether data source, transformations,
units, sample restrictions, and research caveats remain documented. Return
blockers first.
```
