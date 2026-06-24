# Card-Krueger Swarm Orchestration Example

This folder illustrates how to organise a parallel agent effort around the
Card-Krueger fast-food DiD running case using GitHub issues and labels as the control
plane.

## What is a swarm?

A swarm is several agents (or humans with agents) working toward one research output
in coordinated parallel. The coordination mechanism is not a single multi-agent
framework — it is your **GitHub issue board**: each issue defines one stream of work,
its scope boundary, its acceptance criteria, and its dependency on other issues.

Agents implement issues on isolated branches. A review subagent checks each PR before
merge. No stream merges to `main` until its acceptance criteria pass and a human has
reviewed the diff.

## Four streams for the Card-Krueger project

```
Wave 1 (parallel):
  Stream A — Data cleaning and panel validation    [issues/ck-data-cleaning.md]
  Stream B — Literature and bibliography           [issues/ck-literature.md]

Wave 2 (after Wave 1 merges):
  Stream C — DiD estimation and robustness checks  [issues/ck-estimation.md]

Wave 3 (after Stream C merges):
  Stream D — Pre-trends figure and write-up        [issues/ck-parallel-trends-figure.md]
  Stream E — Replication audit                     [issues/ck-replication-audit.md]
```

## Label convention

| Label | Meaning |
| --- | --- |
| `parallel` | Can start as soon as its prerequisites are met; safe to run alongside other `parallel` issues |
| `sequential` | Must wait for the previous wave to merge before starting |
| `blocked-by:#N` | Explicitly blocked until issue #N is merged |
| `day3` | Part of the Day 3 sprint |
| `acceptance-criteria` | Issue contains a full acceptance-criteria checklist |
| `hooks` | Issue involves configuring or verifying a lifecycle hook |

## Dependency graph

```
[A: Data cleaning]  ──┐
                       ├── merge both ──► [C: Estimation] ──► merge ──► [D: Figure]
[B: Literature]    ──┘                                               └──► [E: Replication audit]
```

Streams A and B run in parallel. Stream C waits for both. Streams D and E run in
parallel after C.

## Orchestration log

Record every stream in `notes/orchestration_log.md`:

| Stream | Branch | Issue | Status | PR | Reviewer | Merge |
| --- | --- | --- | --- | --- | --- | --- |
| A: Data cleaning | `ck/data-cleaning` | #N | | | pr-reviewer | |
| B: Literature | `ck/literature` | #N | | | literature-reviewer | |
| C: Estimation | `ck/estimation` | #N | `blocked-by:#A,#B` | | data-reviewer | |
| D: Figure | `ck/parallel-trends-figure` | #N | `blocked-by:#C` | | pr-reviewer | |
| E: Replication | `ck/replication-audit` | #N | `blocked-by:#C` | | loop-verifier | |

## Merge rules

1. No merge without a completed review from the assigned reviewer subagent.
2. Merge in dependency order: A and B before C; C before D and E.
3. After each merge, run `python3 -m pytest examples/card-krueger-toy/tests` from
   `main` to confirm integration.
4. Record the merge decision in `notes/orchestration_log.md`.

## Issue templates

The `issues/` subfolder contains one markdown template per stream. Each template is a
model GitHub issue ready to open in the repository, with goal, allowed files,
acceptance criteria, verification command, and out-of-scope note.

Copy, adapt, and open them as real issues when you run the swarm lab.
