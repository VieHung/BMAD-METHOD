---
name: bmad-survey-update
description: Updates surveys while preserving claim provenance. Use when the user says "update this survey" or "incorporate new research".
---

# Survey Updater

This skill incorporates new or changed evidence into an existing survey without rebuilding stable work or losing provenance. Act as a change-control editor. The output is an updated workspace, regenerated report, and delta record that reviewers can trace to prior claim states.

## Resolution rules

- Bare paths and `{skill-root}` resolve from this skill's installed directory.
- `{project-root}` is the project working directory.

## Establish the baseline

Accept an existing `survey-workspace.md`, its report, and new sources or an updated as-of date. Load `references/update-contract.md` and use `assets/survey-delta-template.md`. Read the workspace and any existing memlog once, then preserve immutable snapshots of both workspace and report before changing either; never overwrite an existing snapshot. If no structured workspace exists, stop with a migration plan rather than pretending a prose diff preserves provenance.

Identify changed inputs and map them to affected taxonomy leaves, evidence cards, claims, critiques, and conclusions. Preserve stable IDs for unchanged entities. Give new entities new IDs; never recycle deleted or rejected IDs. Record supersession links when evidence or claims are replaced.

Invoke the `bmad-survey-research` skill for new evidence, the `bmad-survey-critic` skill for affected claims, and the `bmad-survey-verify` skill for their evidence and critique responses when installed; otherwise apply the same artifact contracts locally. Only adjudication changes claim status. Invoke the `bmad-survey-synthesize` skill to regenerate the report when installed; otherwise synthesize from the updated adjudicated workspace without importing prose from the old report as evidence.

Inspect new sources under the same evidence policy as the baseline unless the user explicitly changes it. A policy change is a scope change and must be visible in the delta. Re-open adjudication only for affected claims or for claims whose dependencies changed. Do not let a new publication date outweigh methodological fit, replication, or direct support.

Regenerate the final report from the updated workspace rather than patching prose fragments. An inaccessible new source cannot support a transition; mark new claims that depend on it `insufficient-evidence`, while retaining an existing claim's prior status when its inspected support is unchanged. Never infer the update from titles, abstracts, or secondary descriptions alone.

Write `survey-delta.md` beside the workspace and record the snapshot paths in it. Preserve the baseline execution topology and record the update topology separately; update or review passes do not upgrade prior evidence independence. Append update decisions to the existing memlog when available; otherwise use the workspace decision record and note the fallback. Before handoff, give a reviewer subagent only the before state, after state, and delta; forbid further delegation and request a fixed list of silent ID changes, unexplained status transitions, stale conclusions, or scope drift. If unavailable, run the same check sequentially.

Return the updated workspace and report paths, snapshot paths, delta path, affected claim IDs, unchanged claim count, readiness, update termination, new as-of date, and counts for `proposed`, `supported`, `disputed`, `incomparable`, `insufficient-evidence`, and `rejected`.
