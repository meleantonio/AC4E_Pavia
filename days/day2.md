# Day 2 - Research Pipeline, SDD, Context Control, Tool Update Lab

## Definition Of Done

- Draft `docs/research_design_memo.md`.
- Update `docs/data_source_map.md`.
- Add or clean `references/bibliography.bib`.
- Convert the research design into issues with acceptance criteria.
- Scope one skill and one subagent/custom-agent role.
- Complete tool update notes for your lane.

## Flow

| Time | Activity |
| --- | --- |
| 09:30-09:45 | Recap and scope check |
| 09:45-10:00 | Agent Skills intro (`SKILL.md`, attach/invoke, project vs user scope) |
| 10:00-10:20 | Demo: SDD via `/sdd` (intent → requirements → design → tasks) |
| 10:20-11:30 | Sprint: memo, bibliography, data map (using SDD artifacts) |
| 11:45-12:30 | Sprint: issue backlog and acceptance criteria |
| 13:30-14:20 | Tool update lab |
| 14:20-15:15 | Agent harness lab |
| 15:15-15:30 | Wrap-up |

## Read

- [`topics/02-research-pipeline/reading.md`](../topics/02-research-pipeline/reading.md)
- [`topics/03-agents-orchestration/reading.md`](../topics/03-agents-orchestration/reading.md)

## Do

Use `/sdd` (or the instructor SDD skill) during Sprint A to scaffold `spec/` or linked memo sections, then turn tasks into GitHub issues. Each issue should state:

- allowed files;
- acceptance criteria;
- verification command or manual check;
- whether the work is parallel or blocked by another issue.

### SDD skill and orchestrator (bundled)

This repo includes the instructor SDD workflow so you can run the Day 2 demo from a fresh clone.

| Asset | Cursor path | Portable copy |
| --- | --- | --- |
| SDD skill | `.cursor/skills/sdd/SKILL.md` | `agent-harness/cursor/skills/sdd/SKILL.md` |
| SDD orchestrator | `.cursor/agents/sdd-orchestrator.md` | `agent-harness/cursor/subagents/sdd-orchestrator.md` |

**Verify (Cursor):**

1. Open this repository in Cursor.
2. Type `/sdd` or ask: "Use the SDD skill to run `init`."
3. Confirm `spec/` and `steering/` are scaffolded from repo-local templates.
4. Delegate: "Use the sdd-orchestrator subagent to draft requirements from intent."

**Intent template:** `templates/spec/intent.md`

For Claude Code or Codex, copy assets from `agent-harness/` into your tool's skill and agent paths (see `agent-harness/README.md`). Verify UI labels in your Cursor version.
