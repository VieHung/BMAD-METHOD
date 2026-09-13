# Taxonomy design

A survey taxonomy is a coverage contract, not a generic table of contents. Derive branches from the decision being supported and give every leaf a question whose answer can change that decision.

For technical comparisons, test the relevance of origin and problem framing, mathematical assumptions, architecture and mechanism, theoretical complexity, realized compute and memory, scaling behavior, training and inference regimes, evaluation design, empirical results, robustness, failure modes, adoption constraints, and open problems. Omit irrelevant branches and add domain-specific ones.

Detect overlap by asking whether two leaves could be answered by the same claim and evidence. Merge true duplicates; keep cross-cutting dimensions as tags rather than duplicating work. Detect gaps by asking what evidence could reverse the expected conclusion, which stakeholder would disagree with the framing, and which operating condition changes the ranking.

A leaf is complete only when it has scoped claims, inspected evidence or an explicit evidence gap, known counterevidence, and an adjudicated status. Source count alone is not a completion test.

Use stable IDs as merge keys, not row numbers. Allocate `L001`, `L002`, and so on once; claims and evidence inherit the leaf namespace (`L001-C001`, `L001-E001`). Never renumber issued IDs after reprioritizing or inserting a branch. Give cross-cutting claims one primary leaf and reference secondary leaves explicitly.
