# Card-Krueger Goals Examples

This folder contains worked goal files for the Card-Krueger DiD running case.

A **goal** is a persistent task definition that tells a coding agent what to accomplish,
how to approach it, and—critically—what conditions must be true before the work is
considered complete. Goals serve the same function as a GitHub issue, but they live
inside the agent tool so the agent can retrieve them across sessions without a human
prompting every time.

These examples follow the goal-file format used in Codex and Claude Code. Verify the
exact field names and file location in your installed tool version before using them
in a live session.

## Goal-file anatomy

| Field | Purpose | Economic research translation |
| --- | --- | --- |
| `name` | One-line identifier | Matches the issue title or research task name |
| `description` | What should be true when done | The research output: a table, a figure, a sample-count report |
| `approach` | How to get there | Which files to edit, which method to use |
| `acceptance_criteria` | Verifiable completion conditions | Mechanically checkable: pytest passes, file exists, number appears in output |
| `constraints` | What must not change | Raw data untouched, causal claims absent, scope boundaries |

## Files in this folder

- `goals/ck-robustness-checks.md` — add two robustness specifications to the DiD
  panel and document the change in sample counts.
- `goals/ck-parallel-trends-figure.md` — generate a pre-trends figure showing NJ
  and PA employment across both survey waves.
- `goals/ck-replication-audit.md` — run the replication-checker skill and produce a
  documented status report.

## How to attach a goal to your agent

**Codex:** Open the Codex app, navigate to Goals, and paste or import the goal
markdown. Verify field names in your installed version.

**Claude Code:** Use the `/goal` command in Claude Code (desktop or app) and paste
the goal content. Claude will treat the acceptance criteria as the exit condition for
the session.

**Cursor Cloud Agent:** Paste the goal content into the task description when
launching a Cloud Agent session. The acceptance criteria become the review checklist
before merge.

## Important caveat

All examples in this folder reference `examples/card-krueger-toy/`, which contains
**synthetic teaching data**. These goals are for practising the agent workflow, not for
making a research claim. No result from these goal runs should be presented as a
replication of Card and Krueger (1994).
