# Day 1 Exercises - Foundations, Context, And GitHub

These exercises match `GUIDE.md` Parts I-II. They are about learning the
working pattern before asking an agent to make research changes.

## Exercise 1 - Read The Repo

Goal: understand before editing.

Prompt:

```text
Read README.md, START_HERE.md, AGENTS.md, days/day1.md, and
examples/mini-economics/README.md. Do not edit files. Explain:
1. what this repository is for;
2. what I should do first;
3. which files or folders should not be exposed to agents;
4. which command verifies the setup;
5. what evidence I should record.
```

Output to record:

- one paragraph in `notes/context_patterns.md` explaining your tool lane;
- the setup command or manual check;
- any privacy boundary you need to add.

Review check: the answer should name the repo, the workshop purpose, the
privacy boundary, and the verification command.

## Exercise 2 - Context And Privacy Boundary

Goal: practice the central rule: scope, evidence, review.

Task:

- list the files an agent may read for setup help;
- list files an agent must not read;
- write one sentence explaining why private data and `.env` files are outside
  scope;
- record the result in `notes/context_patterns.md`.

Suggested prompt:

```text
Read AGENTS.md, README.md, SETUP.md, and START_HERE.md. Do not read data/raw/,
data/private/, or .env. Do not edit files. Propose a safe context boundary for
setup and Day 1 exercises, with evidence I should keep.
```

Review check: the boundary should be narrower than "read the whole repo".

## Exercise 3 - Choose A Tool And Language Lane

Goal: make the agent respect your research stack.

Task:

- choose one primary lane: R, Stata, MATLAB, Python, Julia, LaTeX-heavy, or
  mixed;
- write the exact command or manual checklist that verifies the lane;
- add a note to `notes/context_patterns.md`.

Prompt template:

```text
My main implementation lane is [lane]. Treat [file types] as the primary
artifacts. Do not translate the project into another language unless I ask.
Suggest the smallest setup check and the files that should provide context.
```

Review check: the lane note should mention files, commands, and expected
evidence.

## Exercise 4 - Create A Safe First Branch

Goal: learn issue -> branch -> pull request without touching research claims.

Task:

- create or identify an issue called `Day 1 setup verification`;
- create a branch in your fork;
- edit only `docs/project_brief.md` or `notes/context_patterns.md`;
- review the diff before merging.

Suggested branch:

```bash
git checkout -b day1-setup-verification
```

Acceptance criteria:

- documented setup verification command;
- chosen tool lane recorded;
- no private data added;
- project brief started but not overclaimed.

## Exercise 5 - Draft The Project Brief

Goal: state a research question before building.

Prompt:

```text
Here is my project idea: [paste]. Do not edit files. Ask up to three
clarifying questions only if needed. Then propose a one-page project brief with
question, motivation, data or model inputs, method, three-day deliverable, and
out-of-scope claims.
```

Output to record:

- a draft in `docs/project_brief.md`;
- an explicit "out of scope" section;
- one note saying what evidence would make the brief reviewable.

## Extra Practice - Rewrite A Vague Prompt

Rewrite this prompt:

```text
Improve my project.
```

as one read-only prompt, one planning prompt, and one implementation prompt.
Each version must state scope, evidence, and review.
