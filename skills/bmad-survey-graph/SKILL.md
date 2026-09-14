---
name: bmad-survey-graph
description: Exports an adjudicated BMAD survey as a low-density Obsidian knowledge graph organized around large conceptual clusters. Use when the user wants survey results as an Obsidian vault, map of content, or navigable knowledge graph.
---

# Survey Graph for Obsidian

Turn a survey workspace into a portable Obsidian graph whose visible nodes represent decision-relevant knowledge clusters, not every claim, source, or keyword. Preserve the survey's evidence status and provenance while optimizing the graph for orientation and controlled exploration.

## Resolution rules

- Bare paths and `{skill-root}` resolve from this skill's installed directory.
- `{project-root}` is the project working directory.

## Establish the source and destination

Accept `survey-workspace.md` as the source of truth and use `survey.md` for readable context when available. If the topic has not been surveyed, invoke the `bmad-survey` skill first. If only a narrative report exists, continue only when useful, label claim-level traceability as degraded, and do not upgrade unsupported statements to facts.

Use the destination requested by the user. Otherwise create `obsidian-graph/` beside the survey workspace. When the destination is an existing vault, write into one topic-scoped folder, preserve unrelated notes and `.obsidian/`, and resolve filename collisions before writing.

Read `references/graph-contract.md` before designing the graph. Use `assets/map-of-content-template.md` and `assets/cluster-note-template.md` as output templates. Standard Markdown and Obsidian wikilinks are the canonical format; create a Canvas only when the user explicitly requests one.

## Design the abstraction

Derive clusters from the decision intent, taxonomy, central conclusions, comparison dimensions, and unresolved controversies. Draft the cluster map before writing notes.

Apply the compression rules in the graph contract:

- The default visible graph is one map of content, four to twelve cluster notes, and only a few necessary bridge-concept notes.
- A cluster must answer one distinct decision question and compress several related claims into a coherent model. Merge weak clusters that are merely labels, sources, methods, or adjacent taxonomy leaves.
- Create a bridge concept only when it explains a material relation across at least two clusters. Repeated vocabulary is not a reason to create a node.
- Keep claim IDs, evidence IDs, citations, authors, papers, and datasets inside cluster notes or the manifest by default. Do not create one note per claim, evidence card, source, or keyword.
- Set the graph budget before generation. Exceed it only when the user asks for greater granularity, and record the reason in the manifest.

Assign every central claim to exactly one owning cluster. A cluster may refer to claims owned elsewhere through a typed relation, but duplicated ownership is not allowed. Preserve the claim's qualifiers and adjudicated status; disputed, incomparable, and insufficient-evidence claims remain visibly labeled.

## Write the graph package

Create this portable structure under the topic folder:

```text
00 - Topic Map.md
Clusters/
Concepts/
_graph/graph-manifest.json
```

Omit `Concepts/` when no bridge node passes the admission rule. The map of content provides a short synthesis, a deliberate reading path, links to every visible node, contested areas, source readiness, and a legend for relation types and evidence statuses.

Each cluster note contains:

- one-sentence scope and the decision question it answers;
- a compressed synthesis with inline claim IDs;
- boundaries, operating conditions, and disagreements;
- the minimum useful evidence trail using ordinary Markdown citations rather than wikilinks;
- a small set of typed outgoing relations to other conceptual nodes.

Use wikilinks only for declared graph edges. Express the relation in prose, for example `qualifies [[Clusters/C03 - Scaling Limits]] because ...`; do not link every mention. Obsidian backlinks provide the reverse traversal, so do not add a mirrored edge unless it has a different meaning.

Write `_graph/graph-manifest.json` last. It records source identity, budgets, stable node IDs and paths, claim ownership, typed edges with rationales, omitted central claims with reasons, source readiness, and graph readiness. This file is not a Markdown note, so provenance metadata does not pollute Graph View.

## Update without graph drift

When a manifest already exists, preserve node IDs and paths whose semantic scope is unchanged. Recompute only clusters affected by changed claim IDs. Record merge or split lineage instead of silently reusing an ID for a different concept. Never overwrite a note not declared as generated in the prior manifest.

Keep retired generated notes out of the visible graph and report them for user-directed archival or deletion; do not delete user content. Reassess the budget after a split or merge so incremental updates do not gradually produce a dense graph.

## Validate and hand off

Run `python3 scripts/validate_obsidian_graph.py <topic-folder>`. Then inspect the map and the highest-degree cluster as a reader: every link must answer why the connected node matters, and the graph must remain understandable without opening provenance metadata.

Set graph readiness to `ready` only when all central claims are owned or explicitly omitted, every wikilink resolves, every edge is typed and justified, node and degree budgets pass, and uncertainty is preserved. Source readiness may remain `blocked`; in that case the graph can be structurally ready but must present itself as a map of incomplete research.

Return the topic-folder path, map path, graph and source readiness, cluster and bridge counts, maximum conceptual out-degree, omitted central claims, and validator result.
