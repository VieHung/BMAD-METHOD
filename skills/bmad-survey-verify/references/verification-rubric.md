# Verification rubric

Use this rubric to judge claim support independently from writing quality. Record a source location or a concrete missing-information reason for every verdict.

## Verdicts

- `supported`: the cited source directly supports the scoped claim under matching conditions.
- `disputed`: credible inspected evidence supports materially conflicting conclusions.
- `incomparable`: the claim ranks results whose experimental conditions or metric meanings do not support direct comparison.
- `insufficient-evidence`: available material cannot establish or refute the claim.
- `rejected`: inspected evidence contradicts the claim or shows that it misstates the source.

## Severity

- `blocking`: changes a central conclusion, safety claim, or decision recommendation.
- `major`: changes an important section but not the overall conclusion.
- `minor`: localization, metadata, phrasing, or precision issue with no material conclusion impact.

## Evidence checks

For each claim, test source identity and accessibility, exact support location, semantic entailment, scope qualifiers, study design, independence from other cited evidence, and known contrary evidence. Treat abstracts, secondary summaries, and vendor claims as weaker evidence when primary material is available.

For empirical comparisons, record dataset and version, split, metric definition and direction, evaluation protocol, model and checkpoint, training or tuning budget, hardware, numeric precision, batch, sequence length, decoding or inference regime, and uncertainty or repeated-run information. Missing fields narrow the claim before they justify a verdict.

The audit passes publication readiness only when no blocking issue remains, every central claim is supported or explicitly qualified, and incomparable results are not presented as a ranking.
