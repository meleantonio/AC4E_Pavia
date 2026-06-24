# [CK] Stream A: Validate and document the Card-Krueger panel

**Labels:** `parallel`, `day3`, `acceptance-criteria`
**Branch:** `ck/data-cleaning`
**Wave:** 1 (can run immediately)
**Reviewer subagent:** `agent-harness/subagents/data-reviewer.md`

---

## Goal

Confirm that `examples/card-krueger-toy/data/toy_fast_food.csv` is a valid,
well-documented synthetic balanced panel for a DiD study of NJ fast-food employment
before and after the April 1992 minimum wage increase. Document the validation
findings. Do not modify the data file.

---

## Allowed Files

- `examples/card-krueger-toy/README.md` (read and update)
- `examples/card-krueger-toy/src/did_analysis.py` (read only for this stream)
- `docs/data_source_map.md` (update with CK panel entry)

Do not modify `examples/card-krueger-toy/data/toy_fast_food.csv`.

---

## Acceptance Criteria

- [ ] `examples/card-krueger-toy/README.md` documents: data source (synthetic), unit
      of observation (store-wave pair), outcome variable (FTE employment), treatment
      group (NJ stores), comparison group (PA stores), wave labels (before / after),
      sample restriction (balanced panel, no missing FTE), and the causal-claim
      prohibition.
- [ ] A panel balance report is printed or documented: total stores, NJ stores, PA
      stores, stores with exactly two waves, stores dropped due to imbalance or
      missing FTE.
- [ ] `state` takes only values `NJ` and `PA`; `wave` takes only values `before` and
      `after`; `fte_employment` is numeric and non-negative. These checks are
      documented in `README.md`.
- [ ] `docs/data_source_map.md` contains an entry for the CK toy panel with source,
      unit, outcome, and restriction.
- [ ] `python3 -m pytest examples/card-krueger-toy/tests` passes with zero failures.

---

## Verification

```bash
python3 -m pytest examples/card-krueger-toy/tests -v
```

---

## Out of Scope

- Do not modify `data/toy_fast_food.csv`.
- Do not add new variables to the dataset.
- Do not run or extend the DiD estimation (that is Stream C).
- Do not claim causal identification from the synthetic panel.
