# Debate contract

Each role receives only the packet shared within the authorized run and returns only its declared records. Shared does not mean externally publishable; preserve source restrictions and include only the source text needed for the role. Role names do not imply independent evidence when the same model performs several passes.

## Public claim

`claim_id`, `statement`, `scope`, `taxonomy_leaf`, `importance`, `current_status`, `evidence_ids`, `qualifiers`.

## Critique record

`critique_id`, `claim_id`, `type`, `challenge`, `why_material`, `severity`, `verification_request`, `round`.

Allowed critique types are assumption, method, statistics, comparability, boundary, missing-alternative, contradiction, and source-support. A critique without a falsifier or verification request is commentary and cannot block convergence.

## Verification response

`critique_id`, `evidence_checked`, `finding`, `source_locations`, `limitations`, `recommended_status`.

## Adjudication record

`claim_id`, `prior_status`, `new_status`, `resolved_critique_ids`, `open_critique_ids`, `rationale`, `round`.

Statuses are `proposed`, `supported`, `disputed`, `incomparable`, `insufficient-evidence`, and `rejected`. An adjudicator may narrow a statement or add qualifiers, but must preserve the prior wording and explain the transition.

## Termination

Use `converged` only when all blocking critiques are resolved or stabilized as explicit disagreement. Use `forced-termination` for round, time, token, tool, or source limits. Record both the reason and remaining blocking critiques.
