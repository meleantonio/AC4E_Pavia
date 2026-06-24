---
name: loop-on-verification
description: Use when you want the agent to iterate — implement, verify, flag blockers as new issues, implement again — until the replication-checker and all acceptance criteria return green. Stop when green or when the maximum iteration count is reached.
---

# Loop on Verification

A verification loop has three phases, repeated until the exit condition is met:

1. **Implement** — the agent (or a parallel subagent) completes a narrowly scoped task.
2. **Evaluate** — the `loop-verifier` subagent or the replication-checker skill checks
   the result against the issue acceptance criteria.
3. **Revise** — if the verdict is RED or YELLOW, the agent addresses only the listed
   blockers. If the verdict is GREEN, the loop exits and the work goes to human review.

This is not a swarm. A swarm runs multiple agents in parallel. A loop runs one
evaluation after another on the same task until the standard is met.

## When to use a loop

Use a verification loop when:

- An issue has acceptance criteria that can be checked mechanically (e.g., pytest
  passes, a figure file exists, a sample count is correct).
- You want to find and fix a problem before submitting a PR for human review.
- A replication check returned YELLOW and you want the agent to address the gaps
  without you intervening at each step.

Do not loop more than three times on the same criterion without human input. If
three loops do not clear a blocker, the blocker needs human judgment.

## Invocation steps

When invoked:

1. **Read the acceptance criteria.** Locate them in the GitHub issue, the goal file,
   or the task description. If none is present, stop and ask for them before starting.

2. **Set the loop counter.** Record the iteration number in `notes/orchestration_log.md`
   (stream, branch, iteration N of max 3, verdict, action taken).

3. **Run a scoped implementation.** Implement only what the acceptance criteria
   require. Do not expand scope.

4. **Evaluate with loop-verifier.** Read
   `agent-harness/cursor/subagents/loop-verifier.md` (or your tool's agent path)
   and apply it as a role prompt.
   The verdict is GREEN, YELLOW, or RED.

5. **Branch on verdict.**
   - GREEN → stop the loop. Recommend human diff review.
   - YELLOW → address only the flagged gaps. Increment the counter. Go to step 3.
   - RED → open a new issue with the blocker as the sole acceptance criterion.
     Record in the orchestration log. Stop the loop.

6. **Maximum iterations.** If the counter reaches 3 without GREEN, stop and report
   all outstanding blockers. Do not continue looping.

## Card-Krueger worked example

**Task:** Add a robustness specification that trims the top 2% of FTE employment
observations before computing group means.

**Acceptance criteria:**
- [ ] `did_analysis.py` prints trimmed group means alongside the full-sample means.
- [ ] Sample counts for the trimmed subsample are printed.
- [ ] `pytest examples/card-krueger-toy/tests` passes.
- [ ] `README.md` documents the trim threshold and its motivation.
- [ ] No modifications to `data/toy_fast_food.csv`.

**Loop iteration 1:**
- Agent adds trim logic. Forgets to update `README.md`.
- loop-verifier verdict: YELLOW — documentation gap.
- Agent adds README documentation.

**Loop iteration 2:**
- loop-verifier verdict: GREEN — all criteria pass, pytest passes.
- Recommendation: human reviews diff and verification evidence before merge.

## Constraints

- Record every iteration in `notes/orchestration_log.md`.
- Never auto-merge. The loop exits to human review, not to a merge command.
- Do not widen scope during the loop. New findings → new issue.
- The synthetic-data caveat must appear in any output that reports a number.
