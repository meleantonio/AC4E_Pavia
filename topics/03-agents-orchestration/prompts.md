# Topic 3 Prompt Suggestions

## Skills and replication

```text
Create a reusable skill for checking replication readiness. Keep SKILL.md concise
and use references only if needed.
```

```text
Use the replication-checker workflow in
agent-harness/skills/replication-checker/SKILL.md applied to
examples/card-krueger-toy/. Assign a GREEN, YELLOW, or RED verdict with evidence.
Do not edit files.
```

## Subagents and review

```text
Act as a read-only PR reviewer for this economics repo. Check statistical
interpretation, reproducibility, path hygiene, and scope drift.
```

```text
[Paste data-reviewer role from agent-harness/subagents/data-reviewer.md.]
Review examples/card-krueger-toy/data/toy_fast_food.csv and
examples/card-krueger-toy/src/did_analysis.py. Return blockers first.
Do not edit files.
```

```text
[Paste literature-reviewer role from agent-harness/subagents/literature-reviewer.md.]
Review references/bibliography.bib and any in-text claims referencing Card-Krueger
(1994). Return missing BibTeX keys and any overclaiming. Do not edit files.
```

## Swarm planning

```text
Break the next Card-Krueger milestone into issues. Label tasks parallel, sequential,
or blocked-by. Include one data-validation issue (Stream A), one literature issue
(Stream B), one estimation issue (Stream C, blocked by A and B), and one review
issue. State acceptance criteria for each.
```

## Hooks

```text
Read agent-harness/skills/hooks/SKILL.md. I am using [tool]. Draft the hook
configuration entry that fires python3 -m pytest examples/card-krueger-toy/tests
after any edit to did_analysis.py. Use the format appropriate for my tool.
Do not configure anything not documented in the skill file.
```

## Verification loop

```text
[Paste loop-verifier role from agent-harness/subagents/loop-verifier.md.]
The target task is [task name]. The acceptance criteria are [list].
Evaluate the current state against each criterion. Run
python3 -m pytest examples/card-krueger-toy/tests and report the output.
Return GREEN, YELLOW, or RED with evidence. Do not edit files.
```

## Goal files

```text
Draft a goal file for [task]. Include: name, description (what should be true when
done, in economic language), approach (which files to edit, which method), acceptance
criteria (checkbox list, each item mechanically verifiable), constraints (raw data
untouched, synthetic-data caveat required, scope boundary). Save it to
examples/card-krueger-goals/goals/ck-my-goal.md.
```

## Autonomous agents and plugins

```text
Evaluate OpenClaw/Hermes/Eve with the autonomous-agent risk card. Do not recommend
connecting it to private data unless all risk categories are green.
```

```text
Read the plugin.json for [plugin name]. Identify the declared skills and rules.
For each skill, summarise what it does in one sentence. Do not edit files.
```
