# [CK] Stream B: Verify bibliography and literature notes

**Labels:** `parallel`, `day3`, `acceptance-criteria`
**Branch:** `ck/literature`
**Wave:** 1 (can run immediately)
**Reviewer subagent:** `agent-harness/cursor/subagents/literature-reviewer.md`

---

## Goal

Confirm that `references/bibliography.bib` contains complete and accurate entries for
the Card-Krueger (1994) minimum-wage study and its 1993 NBER working paper predecessor.
Add or correct any missing fields. Document in a short literature note what the original
study found — so that participants working on the estimation and write-up streams have
an accurate summary to cite.

---

## Allowed Files

- `references/bibliography.bib` (read and update)
- `notes/ck_literature_note.md` (create)

---

## Acceptance Criteria

- [ ] `references/bibliography.bib` contains an entry for Card and Krueger (1994) AER
      with correct author, year, journal (`American Economic Review`), volume (84),
      number (4), and pages (772–793).
- [ ] `references/bibliography.bib` contains an entry for the 1993 NBER Working Paper
      4509 with correct author, year, and number.
- [ ] `notes/ck_literature_note.md` exists and states: (a) the research question
      (does a minimum wage increase reduce fast-food employment?), (b) the data
      (NJ and PA fast-food stores, two-wave telephone survey, 1992), (c) the main
      finding (no statistically significant negative employment effect in NJ relative
      to PA), and (d) the caution that the synthetic toy data in this repository
      cannot replicate or extend this finding.
- [ ] No entry in `references/bibliography.bib` contains a factually wrong field for
      the Card-Krueger papers.
- [ ] `python3 -m pytest examples/card-krueger-toy/tests` passes (no regression).

---

## Verification

```bash
python3 -m pytest examples/card-krueger-toy/tests -v
```

Manual check: confirm author, year, journal, volume, number, pages for the 1994 AER
entry.

---

## Out of Scope

- Do not modify any file in `examples/card-krueger-toy/`.
- Do not add a claim that the synthetic DiD estimate replicates the 1994 paper.
- Do not run estimation (that is Stream C).
