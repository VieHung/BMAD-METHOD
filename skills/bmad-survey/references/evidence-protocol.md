# Evidence protocol

Research into the survey workspace, not directly into narrative prose. Every decision-relevant statement is an atomic claim with a stable ID, scope, qualifiers, importance, status, and linked evidence cards.

An evidence card identifies the source, exact support location, a brief paraphrase or minimum necessary excerpt of the inspected support, applicability conditions, source quality, and claims it supports. Preserve source-access and quotation limits. A citation without inspected support is metadata, not evidence. Never invent missing bibliographic fields, quotations, experimental settings, or results.

Use these claim statuses consistently:

- `proposed`: not yet adjudicated.
- `supported`: inspected evidence directly supports the scoped statement.
- `disputed`: credible inspected evidence materially conflicts.
- `incomparable`: a ranking or equivalence is invalid under mismatched conditions.
- `insufficient-evidence`: accessible material cannot settle the claim.
- `rejected`: inspected evidence contradicts or exposes a material misstatement.

For benchmark claims, capture dataset and version, split, metric meaning, evaluation protocol, model and checkpoint, training or tuning budget, hardware, precision, batch, context length, inference regime, and uncertainty. If material dimensions differ, narrow the claim or mark it incomparable.

Evidence discovered through the same citation chain is not independent corroboration. Record source relationships and distinguish primary studies, replications, reviews, vendor material, and commentary.
