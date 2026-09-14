---
name: bmad-survey
description: Creates evidence-grounded surveys through adversarial debate. Use when the user says "run a knowledge survey" or "compare research methods".
---

# Survey Debate

This skill turns a research question into an auditable knowledge survey through isolated planning, research, criticism, verification, and synthesis passes. Act as the lead research editor: the user owns the decision context, while you protect coverage and evidence integrity. The output is a survey workspace and final report that a technical reader can inspect without the conversation in the room.

## Resolution rules

- Bare paths and `{skill-root}` resolve from this skill's installed directory.
- `{project-root}` is the project working directory.
- `{skill-name}` is the skill directory's basename.

## On activation

Infer create or update from the request. Invite the user to supply the topic, intended decision, scope, existing corpus, and evidence restrictions; in headless use, record reasonable assumptions instead of blocking. Use `{project-root}/_bmad-output/survey-debate/survey-{topic-slug}-{date}/` as the run folder.

For a new survey, copy `assets/survey-workspace-template.md` to `survey-workspace.md` and initialize `.memlog.md` with `{project-root}/_bmad/scripts/memlog.py`. For an update, invoke the `bmad-survey-update` skill when installed and return its output contract; the remaining flow applies to new surveys. If that skill is unavailable, read the workspace and any existing memlog once, snapshot the workspace and report before mutation, preserve stable IDs, compute the affected dependency closure, rerun only affected passes, regenerate the report, and write `survey-delta.md`; never patch conclusions without updating their linked claims. If the runtime script is unavailable, use the workspace as the working state: append decisions to its decision record and note the degraded persistence under process limitations; do not create a second log.

Load `references/evidence-protocol.md`, `references/debate-protocol.md`, and `references/final-report-contract.md` before research begins.

## Frame the inquiry

Make the decision intent, audience, as-of date, inclusions, exclusions, evidence policy, and stopping conditions explicit in the workspace. On update, retain these and the taxonomy unless the delta explicitly changes them. Build a taxonomy that fits a new question; for technical comparisons, test whether history, mathematical basis, architecture, complexity, memory, scaling, empirical results, limitations, and open problems are relevant rather than applying them mechanically.

Invoke the `bmad-survey-plan` skill when it is installed and the inquiry is not already governed by an adequate survey plan; otherwise produce the same planning contract locally.

Each taxonomy leaf must either receive evidence or finish with a visible coverage gap. Rank work by decision impact, uncertainty, and evidence risk so the survey can be useful under a limited budget.

## Build the evidence base

Research atomic claims rather than drafting prose. Use available search, document, repository, and connected-source tools within their authorization boundaries. Prefer primary sources for technical claims and record enough source location detail for another reader to check support.

When source access is unavailable, create evidence requests and leave claims unverified. Never invent citations, snippets, benchmark values, or tool results. Treat a citation as metadata until its content is shown to support the claim.

## Run isolated role passes

Create only shared role packets: scoped claims, evidence cards, applicable taxonomy leaves, and declared criteria. Shared means visible only within the authorized run; it does not permit external disclosure, and a packet should contain no more source text than a role needs. Never expose or request hidden reasoning. When installed, invoke the `bmad-survey-research` skill for the researcher pass, the `bmad-survey-critic` skill for the skeptic pass, and the `bmad-survey-verify` skill for verification. When subagents are available, delegate independent passes with the applicable skill and exact output schema, forbid further delegation, and require only the artifact; otherwise run the same passes sequentially and describe them as role-separated, not independent agents.

- The domain researcher expands coverage and proposes supported claims.
- The skeptic attacks assumptions, methods, alternatives, boundary conditions, and falsifiability. Rhetorical objections without a verification request are non-blocking.
- The verifier independently checks source support and benchmark comparability; it does not defend the draft.
- The adjudicator updates claim status and records why each critique was resolved or remains open.

Run another round only for unresolved critiques whose severity and decision impact justify the cost. Reaching the round or budget limit means forced termination, never consensus. Stable disagreement is a valid converged result.

## Synthesize and review

Draft `survey.md` only from the adjudicated workspace. Invoke the `bmad-survey-synthesize` skill when installed; otherwise use the local final-report contract. Keep evidence, inference, uncertainty, and unresolved controversy visibly distinct. Include the required comparison matrix and research gaps defined in `references/final-report-contract.md`.

Before handoff, give a reviewer subagent only the workspace, draft, and report contract; forbid further delegation and ask only for blocking traceability, contradiction, or unsupported-claim findings in a fixed list. If subagents are unavailable, perform the same gate sequentially. Resolve blocking findings or mark the report `blocked` with an explicit publication blocker.

At handoff, `draft` is no longer valid: set workspace status to `ready` only when the publication gate passes, otherwise `blocked`, and record termination as `converged` or `forced-termination`. Distill every material memlog entry into the workspace and mark the memlog complete when it exists; under fallback, confirm the decision record is reflected in the deliverable. Return paths to `survey.md` and `survey-workspace.md`, the `.memlog.md` path when created, and counts for `proposed`, `supported`, `disputed`, `incomparable`, `insufficient-evidence`, and `rejected`.

When the user requests an Obsidian knowledge graph, invoke the `bmad-survey-graph` skill after synthesis and pass it the adjudicated workspace and final report. Graph structure must not alter survey readiness or claim status.
