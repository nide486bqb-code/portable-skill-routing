# Skill routing

Use the smallest installed capability set that covers the task. If a named optional skill is unavailable, continue with the core workflow and state the limitation.

## Priority

1. An explicitly named skill, when installed and readable.
2. Local project execution, rerun, overwrite, reproducibility, commands, or QA: `reproducible-project-runner`.
3. Code changes: the host's minimal code-editing capability, if available.
4. A domain skill only when the task materially requires it: GIS, modeling, documents, spreadsheets, PDFs, figures, or UI.

## Portable routing rules

- Do not assume a skill name exists on another computer or account.
- Do not load multiple overlapping skills because of keyword similarity.
- Keep runtime paths, package versions, and tool availability local to the receiving machine.
- A missing backup skill is a limitation to record, not a reason to stop a runnable workflow.
- Apply any lifecycle or validation template only when that file is present.

