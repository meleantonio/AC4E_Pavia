---
name: ck-parallel-trends-figure
---

# Goal: Pre-Trends Figure for the Card-Krueger DiD Analysis

## Description

Generate a figure that displays mean FTE employment for New Jersey (NJ) and
Pennsylvania (PA) fast-food stores across the two survey waves — before and after
New Jersey's April 1992 minimum wage increase. The figure supports the parallel-trends
narrative: if both groups moved together before the policy change, the post-period
divergence can be attributed to the policy.

Because the data are synthetic and the toy panel has only two time points, the figure
will show pre- and post-period group means rather than a multi-period trend. It
nonetheless illustrates the DiD visual intuition and serves as a teaching exhibit.

When this goal is complete, a figure file will exist at
`examples/card-krueger-goals/figures/parallel_trends.png` and the analysis script
will document how to reproduce it.

## Approach

1. Read `examples/card-krueger-toy/src/did_analysis.py` and
   `examples/card-krueger-toy/data/toy_fast_food.csv`.
2. Create a new script `examples/card-krueger-goals/figures/make_figure.py` that:
   - Loads `data/toy_fast_food.csv` from a relative path.
   - Computes group means: NJ before, NJ after, PA before, PA after.
   - Plots two lines on a single set of axes: one for NJ stores, one for PA stores.
   - X-axis: survey wave (`Before April 1992`, `After April 1992`).
   - Y-axis: mean FTE employment (workers).
   - Includes a figure title and a subtitle noting "synthetic teaching data — not for
     research claims".
   - Saves the figure to `examples/card-krueger-goals/figures/parallel_trends.png`
     using a relative path.
3. Add a section to `examples/card-krueger-goals/README.md` explaining how to run the
   figure script and how to read the figure in a DiD context.
4. Do not modify any file in `examples/card-krueger-toy/`.

## Acceptance Criteria

- [ ] `python3 examples/card-krueger-goals/figures/make_figure.py` runs without error
      from the repository root.
- [ ] `examples/card-krueger-goals/figures/parallel_trends.png` exists after running
      the script.
- [ ] The figure shows two clearly labelled lines: one for NJ stores, one for PA
      stores, over two time points.
- [ ] The figure title or subtitle contains "synthetic teaching data".
- [ ] The script uses only relative paths; no absolute paths appear in the code.
- [ ] `examples/card-krueger-goals/README.md` documents the run command and explains
      how the figure relates to the parallel-trends assumption.
- [ ] `python3 -m pytest examples/card-krueger-toy/tests` still passes (no regression
      from this change).

## Constraints

- Do not modify any file inside `examples/card-krueger-toy/`. The figure script is
  standalone.
- Do not claim the synthetic figure demonstrates a real causal effect. The figure
  is a teaching illustration only.
- Use `matplotlib` (already available via the standard teaching environment). Do not
  add new package dependencies without updating `requirements.txt`.
- The output figure must be saved to disk, not only displayed interactively.
