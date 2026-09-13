---
name: bmad-survey-verify
description: Audits survey claims and benchmark comparability. Use when the user says "verify this survey" or "check these research claims".
---

# Survey Verifier

This skill audits a survey, claim ledger, or technical comparison without silently repairing it. Act as an evidence auditor who does not inherit the author's confidence. The output is a verification report that authors and reviewers can use to correct unsupported claims, misleading comparisons, and citation failures.

## Resolution rules

- Bare paths and `{skill-root}` resolve from this skill's installed directory.
- `{project-root}` is the project working directory.

## Audit

Accept a draft, claim ledger, or critique packet plus its sources, bibliography, evidence cards, or survey workspace. Establish what the audit can actually inspect; inaccessible sources and absent experimental metadata are limitations, not implicit passes. Load `references/verification-rubric.md` and use `assets/verification-report-template.md` for the output.

Check every decision-relevant claim for semantic support, not citation presence alone. Check quotations against the cited location, causal language against study design, and benchmark comparisons against dataset, split, metric, model version, hardware, precision, batch, context length, and inference regime. Do not rank results that fail comparability; mark them `incomparable` and explain the mismatched dimensions.

Use available authorized tools to inspect sources. If required support cannot be accessed and no other inspected evidence establishes the claim, mark it `insufficient-evidence`; otherwise record the access limitation without discarding valid prior support. Never reconstruct source content from memory. Preserve the input unchanged and write `verification-report.md` under `{project-root}/_bmad-output/survey-debate/verification-{topic-slug}-{date}/`.

When handling critique records produced by invoking the `bmad-survey-debate` skill, answer each critique separately with its `critique_id`, evidence checked, exact source locations, finding, limitations, and recommended claim status. Do not merge critiques merely because they target the same claim.

Before handoff, give a reviewer subagent only the input paths, audit draft, and rubric; forbid further delegation and require only a fixed list of missed high-severity issues. If subagents are unavailable, run the same second-pass check sequentially. Set publication readiness to `ready` only when the rubric gate passes and to `blocked` otherwise; `draft` is only an in-progress value. Return the report path, audit limitations, and counts for each verdict.
