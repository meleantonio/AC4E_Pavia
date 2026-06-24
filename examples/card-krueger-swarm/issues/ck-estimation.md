# [CK] Stream C: Run DiD estimation and add robustness checks

**Labels:** `sequential`, `day3`, `acceptance-criteria`, `blocked-by:#A`, `blocked-by:#B`
**Branch:** `ck/estimation`
**Wave:** 2 (requires Streams A and B to merge first)
**Reviewer subagent:** `agent-harness/subagents/data-reviewer.md`

---

## Goal

Extend the Card-Krueger DiD analysis with two robustness specifications (see goal file
`examples/card-krueger-goals/goals/ck-robustness-checks.md`). The main estimate and
both robustness panels should print to the console with clearly labelled sample counts
and the synthetic-data caveat.

**Prerequisite:** Stream A (data validation) and Stream B (literature) must both be
merged before this branch is opened.

---

## Allowed Files

- `examples/card-krueger-toy/src/did_analysis.py` (extend)
- `examples/card-krueger-toy/tests/test_did_analysis.py` (extend)
- `examples/card-krueger-toy/README.md` (update with new specifications)

Do not modify `data/toy_fast_food.csv`.

---

## Acceptance Criteria

- [ ] Running `python3 examples/card-krueger-toy/src/did_analysis.py` prints three
      clearly labelled panels: (1) main specification, (2) robustness — trim top 2%
      of FTE observations, (3) robustness — balanced completers only.
- [ ] Each panel reports: NJ mean before, PA mean before, NJ mean after, PA mean after,
      NJ change, PA change, DiD estimate.
- [ ] Each panel header contains the phrase "synthetic teaching data".
- [ ] Sample counts for each subsample are printed alongside the estimates.
- [ ] `python3 -m pytest examples/card-krueger-toy/tests` passes with zero failures.
- [ ] `examples/card-krueger-toy/README.md` documents both robustness specifications.
- [ ] `data/toy_fast_food.csv` is unmodified (verify with `git diff --stat`).

---

## Verification

```bash
python3 examples/card-krueger-toy/src/did_analysis.py
python3 -m pytest examples/card-krueger-toy/tests -v
git diff --stat data/  # must show no changes
```

---

## Out of Scope

- Do not run the parallel-trends figure (that is Stream D).
- Do not modify any file outside `examples/card-krueger-toy/`.
- Do not interpret the estimates as establishing a causal effect.
