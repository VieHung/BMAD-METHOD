---
name: bmad-survey-debate
description: Pressure-tests research claims through isolated debate. Use when the user says "debate these claims" or "challenge this literature review".
---

# Research Claim Debate

This skill pressure-tests an existing claim ledger or literature-review draft through isolated researcher, skeptic, verifier, and adjudicator passes. Act as a debate chair whose authority is procedural rather than epistemic. The output is an adjudication report that preserves both resolved criticism and stable disagreement.

## Resolution rules

- Bare paths and `{skill-root}` resolve from this skill's installed directory.
- `{project-root}` is the project working directory.

## Establish the debate packet

Accept claims with stable IDs and any available evidence. If the input is prose only, extract atomic provisional claims and clearly label that transformation. Load `references/debate-contract.md` and use `assets/debate-report-template.md` for output.

Define the decision context, maximum rounds or budget, and what counts as a major unresolved conflict. Pass roles only claims, evidence, critique records, and declared criteria shared within the authorized run. Shared does not mean externally publishable: preserve source restrictions, minimize excerpts, and never share or request hidden reasoning.

## Conduct and adjudicate

When installed, invoke the `bmad-survey-critic` skill for the skeptic pass and the `bmad-survey-verify` skill for verification. When subagents are available, run role passes independently with the applicable skill and schemas in the debate contract, forbid further delegation, and require only the declared records. Otherwise run them sequentially and report the execution as role-separated rather than independently corroborated.

The skeptic must turn objections into falsifiers, missing controls, alternative explanations, boundary conditions, or contradictory-source requests. The verifier checks evidence directly and never inherits the researcher's confidence. The adjudicator must answer every major critique with a status transition or an explicit unresolved reason.

Continue only while a new round targets unresolved high-impact issues. A fixed round limit, deadline, or exhausted evidence budget produces `forced-termination`, not consensus. Convergence means statuses have stabilized; `disputed` and `insufficient-evidence` may remain.

Write `debate-report.md` under `{project-root}/_bmad-output/survey-debate/debate-{topic-slug}-{date}/`. Preserve input files and propose changes by claim ID. Before handoff, run a second-pass reviewer with further delegation forbidden over the debate packet and draft report, or the same gate sequentially when subagents are unavailable. Return the report path, execution topology, termination reason, and counts for all six claim statuses, including `proposed`.
