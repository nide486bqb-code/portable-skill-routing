# portable-skill-routing

Portable routing policy for selecting the smallest installed skill set across computers, accounts, and Agent products.

## What it is

`SKILL_ROUTING.md` is a routing policy template, not an inventory of every skill available on the author's machine. It defines capability priorities, conflict handling, and graceful behavior when optional skills are missing.

The repository also includes `SKILL.md`, so it can be installed as an optional routing skill in systems that support skill packages.

## Use

- Copy `SKILL_ROUTING.md` into the target project's instruction or templates directory.
- Read it before loading long skills.
- Replace optional skill names with capabilities available on the receiving machine.
- Keep one primary skill active unless a concrete capability gap requires a backup.
- Do not stop a runnable task merely because an optional backup skill is unavailable.

## Compatibility

This project is plain Markdown. It does not require Codex, a particular account, Python, or a plugin manager. Agent-specific auto-loading remains the responsibility of the receiving Agent.

