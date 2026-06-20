# Exercises

These exercises follow the sequence in `GUIDE.md`. Use them as the canonical
practice path for the workshop. The topic pages in `topics/` point back here
for the longer version of each exercise.

Every exercise should leave three things behind:

1. **Scope:** what the agent was allowed to read, edit, or run.
2. **Evidence:** the diff, command output, note, checklist, or prompt record.
3. **Review:** what a human must check before accepting the work.

Do not add secrets, private data, confidential manuscripts, or unpublished
research material to these exercises. Do not ask an agent to read `data/raw/`,
`data/private/`, or `.env`.

## Exercise Path

| Workshop moment | Guide sections | Exercise file | Main evidence |
| --- | --- | --- | --- |
| Day 1 foundations | Parts I-II | `day1-foundations.md` | `notes/context_patterns.md`, first branch or PR path, `docs/project_brief.md` |
| Day 2 research pipeline | Parts III-IV | `day2-research-pipeline.md` | `docs/research_design_memo.md`, data/model-input map, issue acceptance criteria |
| Day 3 agent workflows | Part V | `day3-agent-workflows.md` | review role output, skill/subagent notes, `notes/orchestration_log.md`, risk card |
| Final integration | Part VI | `final-replication-presentation.md` | replication README, presentation outline, 30-day adoption plan |

## Practice Examples

Use `examples/` alongside these exercises:

- `examples/mini-economics/` for setup verification and a tiny synthetic OLS
  example.
- `examples/card-krueger-toy/` for a synthetic difference-in-differences
  walkthrough tied to the running case in `GUIDE.md`.
- `examples/prompt-patterns/` for reusable prompt examples using scope,
  evidence, and review.

Before claiming an exercise batch is complete, run the documented repository
check:

```bash
python3 -m pytest examples/mini-economics/tests
```
