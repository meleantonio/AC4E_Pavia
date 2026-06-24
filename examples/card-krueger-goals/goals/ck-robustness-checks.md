---
name: ck-robustness-checks
---

# Goal: Robustness Checks for the Card-Krueger DiD Estimate

## Description

Extend the Card-Krueger difference-in-differences analysis with two robustness
specifications. The main estimate compares mean full-time-equivalent (FTE) employment
for New Jersey (NJ) stores with Pennsylvania (PA) stores across the before and after
waves of the 1992 survey. The robustness checks assess whether the main finding is
sensitive to influential employment observations and to stores with any missing data.

When this goal is complete, `src/did_analysis.py` will print three panels:

1. **Main specification** — all stores with a balanced before/after observation (no
   missing FTE employment).
2. **Robustness 1: trim top 2% of FTE observations** — drop stores in the top
   percentile of FTE employment (pooled across both states and waves) before computing
   group means.
3. **Robustness 2: balanced completers only** — additionally require that the store
   was present and had positive employment in both waves.

Each panel reports: NJ mean (before), PA mean (before), NJ mean (after), PA mean
(after), NJ change, PA change, DiD estimate.

## Approach

1. Read `examples/card-krueger-toy/src/did_analysis.py` and
   `examples/card-krueger-toy/data/toy_fast_food.csv`.
2. Add a `trim_top_pct(df, col, pct)` function that drops rows where `col` exceeds
   the `pct`-th percentile. Apply it with `pct=0.98` for Robustness 1.
3. Add a `balanced_completers(df)` function that keeps only stores with positive FTE
   in both waves. Apply it after the trim for Robustness 2.
4. Print results for all three panels with clear labels. The synthetic-data caveat
   must appear in each panel header.
5. Add a test in `examples/card-krueger-toy/tests/test_did_analysis.py` that
   confirms trimming reduces the sample count and that the DiD estimate can be
   computed for each subsample without error.
6. Update `examples/card-krueger-toy/README.md` to document the two new
   specifications, their motivation, and the expected sample-count reduction.

Do not modify `data/toy_fast_food.csv`.

## Acceptance Criteria

- [ ] Running `python3 examples/card-krueger-toy/src/did_analysis.py` prints three
      clearly labelled panels: main, robustness 1 (trim), robustness 2 (completers).
- [ ] Each panel header contains the phrase "synthetic teaching data" or equivalent.
- [ ] Each panel reports NJ mean (before/after), PA mean (before/after), and DiD
      estimate.
- [ ] Sample counts for each subsample are printed alongside the estimates.
- [ ] `python3 -m pytest examples/card-krueger-toy/tests` passes with zero failures.
- [ ] `examples/card-krueger-toy/README.md` documents both robustness specifications
      and their sample-size implications.
- [ ] `data/toy_fast_food.csv` is unmodified (verify with `git diff --stat`).

## Constraints

- Do not remove the main specification. All three panels must appear together.
- Do not claim the trimmed estimate is more credible than the main estimate without
  providing an economic justification.
- The phrase "synthetic data" or "teaching data" must appear in every panel header and
  in the updated README section.
- Scope is limited to `src/did_analysis.py`, `tests/test_did_analysis.py`, and
  `README.md` inside `examples/card-krueger-toy/`. Do not edit other files.
