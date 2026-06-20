# Mini Economics Example

This is a tiny synthetic example for setup verification and Day 1 agent
exercises. It generates a Phillips-curve-style dataset and estimates a simple
OLS slope.

## Research Context

- **Data source:** generated in `src/analysis.py`; no external data files are
  read.
- **Unit:** one synthetic macro observation.
- **Variables:** unemployment rate and inflation rate, both in percentage
  points.
- **Transformation:** demean unemployment and inflation before calculating the
  one-regressor OLS slope.
- **Sample restriction:** default sample is 40 generated observations with a
  fixed random seed.
- **Research caveat:** this example is for software practice only. It does not
  estimate a real Phillips curve or support a policy claim.

Run tests:

```bash
python3 -m pytest examples/mini-economics/tests
```

Run script:

```bash
python3 examples/mini-economics/src/analysis.py
```
