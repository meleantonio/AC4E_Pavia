# [CK] Stream D: Generate the pre-trends figure

**Labels:** `sequential`, `day3`, `acceptance-criteria`, `blocked-by:#C`
**Branch:** `ck/parallel-trends-figure`
**Wave:** 3 (requires Stream C to merge first)
**Reviewer subagent:** `agent-harness/subagents/pr-reviewer.md`

---

## Goal

Produce a figure that displays mean FTE employment for NJ and PA fast-food stores
across both survey waves, following the goal file
`examples/card-krueger-goals/goals/ck-parallel-trends-figure.md`. The figure will
serve as a teaching illustration of the DiD visual intuition: if the two groups moved
together before the policy, post-period divergence can be tentatively attributed to
the minimum wage increase.

**Prerequisite:** Stream C (estimation) must be merged before this branch is opened.

---

## Allowed Files

- `examples/card-krueger-goals/figures/make_figure.py` (create)
- `examples/card-krueger-goals/figures/parallel_trends.png` (generated output)
- `examples/card-krueger-goals/README.md` (update with figure documentation)

Do not modify any file in `examples/card-krueger-toy/`.

---

## Acceptance Criteria

- [ ] `python3 examples/card-krueger-goals/figures/make_figure.py` runs without error
      from the repository root.
- [ ] `examples/card-krueger-goals/figures/parallel_trends.png` exists after running
      the script.
- [ ] The figure shows two clearly labelled lines (NJ and PA) across two time points
      (before / after).
- [ ] The figure title or subtitle contains "synthetic teaching data".
- [ ] The script uses only relative paths.
- [ ] `examples/card-krueger-goals/README.md` documents the run command and explains
      how the figure relates to the parallel-trends assumption.
- [ ] `python3 -m pytest examples/card-krueger-toy/tests` still passes (no regression).

---

## Verification

```bash
python3 examples/card-krueger-goals/figures/make_figure.py
ls examples/card-krueger-goals/figures/parallel_trends.png
python3 -m pytest examples/card-krueger-toy/tests -v
```

---

## Out of Scope

- Do not modify any file in `examples/card-krueger-toy/`.
- Do not claim the figure demonstrates a real causal effect.
- Do not run the replication audit (that is Stream E).
