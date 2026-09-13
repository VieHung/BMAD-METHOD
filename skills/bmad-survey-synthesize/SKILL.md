---
name: bmad-survey-synthesize
description: Synthesizes adjudicated evidence into neutral surveys. Use when the user says "synthesize this research" or "write the final survey".
---

# Survey Synthesizer

This skill renders an adjudicated survey workspace into a coherent report without laundering uncertainty into certainty. Act as a neutral academic editor. The output is a traceable survey that readers can use without access to the debate conversation.

## Resolution rules

- Bare paths and `{skill-root}` resolve from this skill's installed directory.
- `{project-root}` is the project working directory.

## Establish the synthesis boundary

Accept an adjudicated claim ledger, evidence cards, taxonomy coverage, critique outcomes, and decision context. Load `references/synthesis-contract.md` and use `assets/survey-report-template.md`. If central claims remain merely `proposed` or have no inspectable support, continue drafting only as a report marked `blocked`; do not silently research or invent the missing evidence.

Treat the workspace as the source of truth. Build prose only from claim records and link every central conclusion to claim IDs. Separate supported findings, interpretation, recommendations, stable disagreement, incomparable results, and insufficient evidence. Preserve qualifiers and operating conditions that affect applicability.

Copy the execution topology recorded by the workspace. Preserve per-run topology when evidence comes from mixed execution modes rather than collapsing it to the strongest label. A synthesis or final-review pass does not turn role-separated work into independent-agent corroboration; if the upstream topology is absent, label it `unspecified`, block publication readiness, and explain the limitation.

Create a comparison matrix whenever two or more approaches are evaluated. Include complexity, realized compute or latency where available, memory footprint, context or scale behavior, empirical performance, evaluation conditions, limitations, and evidence status. Do not rank incomparable results.

Write `survey.md` beside the supplied workspace, or under `{project-root}/_bmad-output/survey-debate/synthesis-{topic-slug}-{date}/` for standalone inputs. Before handoff, give a reviewer subagent only the adjudicated records, draft, and synthesis contract; forbid further delegation and request only blocking traceability, contradiction, overclaiming, and missing-controversy findings. If unavailable, run the same check sequentially.

Set publication readiness to `ready` only when the gate passes; otherwise set `blocked` and list the exact blockers. Return the report path, readiness, coverage gaps, termination reason, and counts for `proposed`, `supported`, `disputed`, `incomparable`, `insufficient-evidence`, and `rejected`.
