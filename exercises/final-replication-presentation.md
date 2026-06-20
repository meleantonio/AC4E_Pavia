# Final Exercises - Replication, Presentation, And Adoption

These exercises match `GUIDE.md` Part VI. The goal is a reviewable project
package, not a chat transcript.

## Exercise 1 - Clean Run

Goal: verify that the teaching example still runs.

Run:

```bash
python3 -m pytest examples/mini-economics/tests
python3 examples/mini-economics/src/analysis.py
```

Output to record:

- command;
- date;
- result;
- any local environment notes.

Review check: passing tests are evidence about setup, not evidence that a
research design is correct.

## Exercise 2 - Replication README

Goal: make the project runnable or honestly document why it is not.

Prompt:

```text
Draft replication/README.md from the current project. Include overview,
software versions, data or model inputs, setup, run instructions, expected
outputs, troubleshooting, known limitations, and contact. Use my software lane,
not a default language.
```

Review check: the README should document sources, transformations, units, and
sample restrictions.

## Exercise 3 - Presentation Outline

Goal: communicate the research and the workflow.

Prompt:

```text
Draft a 5 to 7 minute presentation. Include research question, motivation,
data or model, method, main result or blocker, agentic workflow, replication
status, and next 30 days. Keep claims modest.
```

Output to record:

- `templates/presentation_outline.md` or `docs/`;
- one slide or note on what the agent did;
- one slide or note on what the human reviewed.

## Exercise 4 - 30-Day Adoption Plan

Goal: turn workshop habits into a small routine.

Task:

- fill `templates/adoption_plan_30d.md`;
- choose one recurring workflow to keep;
- choose one boundary you will keep even under time pressure.

Review check: the plan should be small enough to do without reorganizing the
whole research project.

## Exercise 5 - Final Review

Goal: make the final package inspectable.

Checklist:

- privacy boundaries documented;
- project brief complete;
- research design memo complete;
- bibliography or reference list started;
- data or model-input map complete;
- issues include acceptance criteria;
- orchestration log updated;
- risk card completed if a cloud or autonomous tool was considered;
- replication README includes exact run instructions;
- final claims remain modest.

Prompt:

```text
Review this repository as a final workshop package. Do not edit files. Check
privacy, reproducibility, source documentation, run instructions, and whether
claims are over-stated. Return blockers first.
```
