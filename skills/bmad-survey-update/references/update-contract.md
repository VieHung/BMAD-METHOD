# Update contract

An update is a provenance-preserving state transition, not a prose rewrite. Before mutation, preserve collision-safe immutable snapshots of the baseline workspace and report. The current files may then advance, but the delta must identify the exact snapshots used as the before state.

Classify incoming changes as new source, revised source, retraction or correction, new benchmark version, changed decision scope, changed evidence policy, or editorial-only. Editorial-only changes cannot alter claim status.

Preserve claim, evidence, critique, taxonomy, and decision IDs when identity is unchanged. New records receive new monotonic IDs within their entity type. Superseded records remain visible with `superseded_by`; rejected records remain visible with their adjudication. Never recycle an ID. Every status transition records prior status, new status, evidence or critique IDs, rationale, and update date.

Compute the affected set through explicit links: changed evidence affects linked claims; changed claims affect their critiques, adjudications, comparison cells, and conclusions. Re-evaluate only that closure plus a reviewer-selected sample of unchanged central claims. A source that was not inspected cannot justify a transition, and does not invalidate unchanged inspected evidence by itself.

The delta must disclose snapshot paths, source additions and removals, ID allocations and supersessions, status transitions, taxonomy changes, changed conclusions, unchanged central claims, policy or scope changes, new gaps, update termination, and publication readiness. Preserve baseline and update execution topology as separate records; never use a stronger update topology to relabel prior evidence. A newer as-of date does not imply improved coverage.
