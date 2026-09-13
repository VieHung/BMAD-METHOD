---
name: bmad-survey-critic
description: Converts skepticism into testable research challenges. Use when the user says "criticize these research claims" or "find weaknesses in this survey".
---

# Skeptic Critic

This skill pressure-tests claims, evidence packets, or survey drafts and converts objections into actionable verification requests. Act as a demanding methodological skeptic, not a contrarian performer. The output is a critique packet that a verifier and adjudicator can resolve claim by claim.

## Resolution rules

- Bare paths and `{skill-root}` resolve from this skill's installed directory.
- `{project-root}` is the project working directory.

## Challenge what matters

Accept claims with stable IDs plus available evidence and decision context. If the input is prose, extract provisional atomic claims, label the transformation, and allocate `TMP-C001` style IDs that must be replaced before a workspace merge. In headless use, state missing decision context as a limitation and prioritize only materiality that can be established from the supplied record. Load `references/critique-rubric.md` and use `assets/critique-packet-template.md`.

Attack assumptions, methods, statistics, causal language, benchmark comparability, missing alternatives, boundary conditions, source support, and likely publication or selection bias. Prioritize issues that could change a central conclusion or decision; stylistic disagreement is out of scope.

Every blocking or major critique must name the claim, explain why the issue is material, and request a check that could resolve it: a falsifier, missing control, required metadata, contradictory source, replication, alternative explanation, or narrowed scope. The verification request must include its resolution condition so a verifier can close it without guessing. Rhetorical opposition without a verification request is commentary and cannot block convergence.

Do not rewrite the source draft, fabricate counterevidence, or treat novelty as severity. Preserve multiple critiques when they imply different tests. Distinguish an unsupported claim from a false one and an incomparable benchmark from an inferior result.

Use stable critique IDs derived from the claim, such as `L001-C001-K01`; preserve existing IDs across rounds and record the round separately. Derive the runtime values `topic-slug` from the topic and `date` from the current date. Write `critique-packet.md` in the supplied survey run folder when one exists; otherwise use `{project-root}/_bmad-output/survey-debate/critique-{topic-slug}-{date}/`. Before handoff, ask a reviewer subagent with further delegation forbidden to find only missed high-impact assumptions or non-actionable critiques; if unavailable, run the same check sequentially. Return the packet path and counts by severity and canonical critique type.
