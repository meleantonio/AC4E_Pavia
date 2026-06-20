# Examples

These examples support the exercise path in `GUIDE.md`. They are deliberately
small, public, and safe to inspect with an agent.

## Available Examples

| Example | Use it for | Main command |
| --- | --- | --- |
| `mini-economics/` | setup verification, read-only explanation, small OLS review | `python3 -m pytest examples/mini-economics/tests` |
| `card-krueger-toy/` | difference-in-differences practice tied to the running case | `python3 -m pytest examples/card-krueger-toy/tests` |
| `prompt-patterns/` | reusable prompts for read-only, planning, implementation, and review workflows | read the README |

## Rules For Examples

- Treat example data as teaching data unless the README explicitly says
  otherwise.
- Document source, units, transformations, and sample restrictions before
  interpreting outputs.
- Do not modify raw data. Add cleaned or derived outputs in a separate folder if
  an exercise asks for them.
- Do not let an agent certify identification, causality, or interpretation.

## Full Example Check

```bash
python3 -m pytest examples/mini-economics/tests
python3 -m pytest examples/card-krueger-toy/tests
```
