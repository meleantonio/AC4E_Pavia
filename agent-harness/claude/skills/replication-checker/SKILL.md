---
name: replication-checker
description: Use when asked to assess whether the repo can reproduce its documented outputs from a clean setup.
---

# Replication Checker

When invoked:

1. Read `AGENTS.md`, `replication/README.md`, and available tests.
2. Identify the smallest documented verification command.
3. Check for hardcoded absolute paths, secrets, private data, and undeclared dependencies.
4. Run the smallest safe verification command if allowed.
5. Report green/yellow/red with exact evidence.

Never mark replication green unless commands were run or equivalent evidence is present.
