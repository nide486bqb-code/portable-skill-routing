# portable-skill-routing

[![Tests](https://github.com/nide486bqb-code/portable-skill-routing/actions/workflows/test.yml/badge.svg)](https://github.com/nide486bqb-code/portable-skill-routing/actions/workflows/test.yml)
[![Release](https://img.shields.io/github/v/release/nide486bqb-code/portable-skill-routing)](https://github.com/nide486bqb-code/portable-skill-routing/releases)

An Agent-neutral routing policy for selecting the smallest installed skill set across computers, accounts, and Agent products.

## What it solves

As skill collections grow, loading every skill creates unnecessary context and increases routing conflicts. This project keeps the routing decision compact:

- choose one primary installed capability;
- load a backup only after a concrete capability gap is visible;
- treat unavailable skill names as missing capabilities;
- continue with the core workflow when an optional skill is absent;
- keep local runtime paths and installed-skill inventories out of shared policy.

## What it does not do

This is a routing policy and skill template. It does not scan skill directories, build a keyword index, call an LLM, install hooks, or automatically install missing skills. Those are separate responsibilities in dynamic routers such as [SkillRouter](https://github.com/jax-agent/skill-router).

## Quick start

Clone the repository:

```powershell
git clone https://github.com/nide486bqb-code/portable-skill-routing.git .\portable-skill-routing
```

Copy the policy into a project template directory:

```powershell
Copy-Item .\portable-skill-routing\SKILL_ROUTING.md `
  .\templates\SKILL_ROUTING.md -Force
```

For an Agent that supports skills, install the repository as `portable-skill-routing`. For an Agent without native skill discovery, add [AGENT_INSTRUCTIONS.md](AGENT_INSTRUCTIONS.md) to its project rules or prompt.

## Use with a project

1. Read `SKILL_ROUTING.md` before loading long skill instructions.
2. Match the task to an installed capability.
3. Load only the primary skill first.
4. Load a backup only when the primary skill lacks a required capability.
5. Record missing optional skills or platform limitations when they affect the result.

## Portability rules

The policy deliberately avoids assuming:

- a particular Agent product;
- a specific account or home directory;
- a fixed skill inventory;
- a universal skill name for a capability;
- a lifecycle template that may not exist on the receiving machine.

## Repository layout

```text
SKILL.md
SKILL_ROUTING.md
AGENT_INSTRUCTIONS.md
README.md
MANIFEST.json
tests/test_routing.py
```

## Related conventions

The repository follows the common Agent Skills layout of a frontmatter-based `SKILL.md` and a human-facing `README.md`. See [Vercel Agent Skills](https://github.com/vercel-labs/skills), [Skill Anatomy](https://github.com/ravidsrk/agent-skills/blob/main/docs/skill-anatomy.md), and [SkillRouter](https://github.com/jax-agent/skill-router) for related installation and routing patterns.

## License

MIT. See [LICENSE](LICENSE).
