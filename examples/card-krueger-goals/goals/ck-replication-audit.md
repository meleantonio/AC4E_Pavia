---
name: ck-replication-audit
---

# Goal: Replication Audit of the Card-Krueger Toy Example

## Description

Run a systematic replication audit of `examples/card-krueger-toy/` using the
`replication-checker` skill and produce a written status report. The report will
identify whether a researcher who receives only the repository root can reproduce the
documented output — group means, DiD estimate, and verification suite — without any
guidance beyond `README.md`.

The audit does not involve re-estimating the model or adding new features. It
is a read-and-verify pass that results in a GREEN, YELLOW, or RED status with
documented evidence.

When this goal is complete, `notes/replication_audit_ck.md` will exist and will
contain the audit findings, verification command output, and any blocker or
recommendation.

## Approach

1. Read `agent-harness/skills/replication-checker/SKILL.md` and apply its steps to
   `examples/card-krueger-toy/`.
2. For each checklist item, record: criterion, pass/fail/unable-to-check, evidence.
3. Run `python3 -m pytest examples/card-krueger-toy/tests -v` and record the output
   verbatim in the report.
4. Verify: entry point (`src/did_analysis.py`) is reachable from the repo root with a
   relative path. Confirm the run command in `README.md` matches.
5. Check for hardcoded absolute paths in `src/did_analysis.py`.
6. Confirm the synthetic-data caveat appears in `README.md` and in the script output.
7. Assign an overall status: GREEN (all pass), YELLOW (minor gaps), RED (at least one
   blocker).
8. Write the report to `notes/replication_audit_ck.md`.

## Acceptance Criteria

- [ ] `notes/replication_audit_ck.md` exists and contains: (a) a per-criterion table
      with pass/fail evidence, (b) verbatim pytest output, (c) overall status
      (GREEN / YELLOW / RED), (d) list of blockers (if any), (e) list of
      recommendations (if any).
- [ ] The audit was performed without modifying any file in
      `examples/card-krueger-toy/`.
- [ ] If the overall status is GREEN: `python3 -m pytest examples/card-krueger-toy/tests`
      passed with zero failures.
- [ ] If the overall status is YELLOW or RED: at least one blocker or documentation
      gap is listed with an exact file reference.
- [ ] The report notes the date of the audit and the tool or agent lane used.

## Constraints

- Do not modify any file in `examples/card-krueger-toy/`. The audit is read-only.
- Do not claim GREEN status unless the verification command actually ran and passed.
- Scope is limited to `examples/card-krueger-toy/` and `notes/replication_audit_ck.md`.
  Do not audit other parts of the repository.
- The report must distinguish between a replication finding (can the code reproduce
  documented output?) and a research finding (is the DiD identification credible?).
  The audit addresses only the former.
