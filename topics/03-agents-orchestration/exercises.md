# Topic 3 Exercises

Use `exercises/day3-agent-workflows.md` as the canonical Day 3 exercise path.
Exercises 1–5 are the core orchestration exercises. Exercises 6–9 are the new Day 3
additions covering hooks, verification loops, goal files, and plugins.

## Exercise focus

- Exercises 1–2: read-only review roles; replication-checker skill on the CK toy
- Exercise 3: multiple subagent role prompts (pr-reviewer, data-reviewer)
- Exercise 4: orchestration log structured around the four CK swarm streams
- Exercise 5: autonomous-agent risk card
- Exercise 6 (new): configure and trace a postcondition hook for the CK analysis
- Exercise 7 (new): design and run a verification loop with the loop-verifier subagent
- Exercise 8 (new): write a goal file with verifiable acceptance criteria
- Exercise 9 (new): explore a Cursor plugin manifest

## Minimum evidence for Topic 3

- Review output lists blockers before smaller issues.
- `notes/orchestration_log.md` records at least one stream entry with dependencies
  and merge decision.
- Risk card defines read boundary, write boundary, approval gate, and evidence trail
  before any autonomous or cloud tool is used.
- At least one hook configuration entry is drafted for the participant's tool lane.
- At least one loop iteration is recorded with a GREEN / YELLOW / RED verdict.
- At least one goal file exists with checkbox acceptance criteria that are
  mechanically verifiable.

## Acceptance-criteria discipline (Day 2 → Day 3)

State the acceptance criteria for each exercise before beginning. The criteria are
already written into exercises 1–9 in `exercises/day3-agent-workflows.md`. Read them
before running the exercise prompt.
