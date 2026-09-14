# Obsidian survey graph contract

## Purpose

The graph is an orientation layer over an adjudicated survey, not a lossless serialization of its ledger. Full claim and evidence detail remains in the survey workspace and inside cluster notes; the visible Obsidian graph exposes only the conceptual structure needed to reason about the decision.

## Abstraction layers

| Layer | Note type | Admission rule | Typical content |
| --- | --- | --- | --- |
| 0 | Map of content | Exactly one | Synthesis, reading paths, cluster index, contested areas |
| 1 | Cluster | Answers a distinct decision question and owns a coherent claim set | Model, trade-offs, conditions, findings, uncertainty |
| 2 | Bridge concept | Materially connects at least two clusters and cannot be explained clearly in either one | Cross-cutting mechanism, constraint, or comparison axis |
| Ledger | No graph node | Claim, evidence, source, author, paper, dataset, or incidental term | Inline IDs, citations, and manifest records |

For an ordinary survey, budget one map, four to twelve clusters, and no more than `min(6, ceil(cluster_count / 2))` bridge concepts. A genuinely small survey may use fewer clusters. Set `max_core_nodes`, `max_cluster_nodes`, `max_bridge_nodes`, and `max_outgoing_links` in the manifest before generating notes.

A candidate cluster passes only when all answers are yes:

1. Does it answer a question that affects the survey's decision intent?
2. Can its scope be summarized in one sentence without becoming a miscellaneous bucket?
3. Does it combine multiple material claims, or one exceptional high-impact claim with necessary context?
4. Is it meaningfully different from every existing cluster?

If not, merge it into the closest cluster or retain it as inline detail. Do not use taxonomy depth as graph depth automatically.

## Claim ownership and status

Every central claim belongs to exactly one cluster. Include its stable ID beside each material statement, for example `[C-014, supported]`. Other clusters may mention the claim but do not list it as owned.

Preserve the canonical survey statuses: `proposed`, `supported`, `disputed`, `incomparable`, `insufficient-evidence`, and `rejected`. A rejected claim may appear when its rejection is decision-relevant; describe it as rejected rather than as an alternative finding. Never turn a forced termination into consensus.

Evidence IDs and source links remain ordinary Markdown, not wikilinks, unless the user explicitly requests a source graph as a separate layer. This prevents bibliographic volume from dominating the conceptual graph.

## Edge vocabulary

Every wikilink corresponds to one manifest edge and uses one of these relations:

- `contains`: the map of content navigates to a visible node;
- `supports`: one concept materially strengthens another;
- `contradicts`: findings or assumptions conflict under comparable conditions;
- `qualifies`: one concept narrows the applicability of another;
- `depends-on`: understanding or validity requires the target concept;
- `compares-with`: the nodes are alternatives under an explicit comparison frame;
- `refines`: the source adds a more specific model or boundary to the target.

Write an edge as a sentence or list item containing the relation, wikilink, and a short rationale. Every non-navigation edge cites at least one claim ID that justifies the relation. Shared vocabulary, chronology, or co-citation alone does not justify an edge. Do not mirror a link merely to make it bidirectional; Obsidian already provides backlinks.

The default maximum conceptual out-degree is five per cluster or bridge node. The map's `contains` links are exempt. A justified hub may use a higher declared budget, but the manifest must explain why navigation improves rather than collapses into a generic hub.

## File and identity rules

Use stable IDs such as `MOC`, `C01`, and `X01`. Prefer filenames like `Clusters/C01 - Evaluation Reality.md`; keep the ID and path stable when wording changes. Avoid creating index notes for folders because they add graph nodes without adding knowledge.

The output must work with Obsidian core features alone. Do not change `.obsidian/`, install plugins, or depend on Dataview. Tags are optional metadata; use a small fixed vocabulary rather than a tag per topic.

## Manifest schema

Write valid JSON to `_graph/graph-manifest.json` with this shape:

```json
{
  "schema_version": 1,
  "topic": "Example topic",
  "source": {
    "workspace": "path recorded as provenance",
    "report": "optional report path",
    "as_of": "YYYY-MM-DD",
    "readiness": "ready"
  },
  "graph_readiness": "ready",
  "budget": {
    "max_core_nodes": 12,
    "max_cluster_nodes": 8,
    "max_bridge_nodes": 3,
    "max_outgoing_links": 5,
    "exception_reason": ""
  },
  "central_claim_ids": ["C-001", "C-002"],
  "nodes": [
    {
      "id": "MOC",
      "type": "moc",
      "title": "Example Topic Map",
      "path": "00 - Example Topic Map.md",
      "claim_ids": []
    },
    {
      "id": "C01",
      "type": "cluster",
      "title": "Decision Drivers",
      "path": "Clusters/C01 - Decision Drivers.md",
      "claim_ids": ["C-001", "C-002"]
    }
  ],
  "edges": [
    {
      "from": "MOC",
      "to": "C01",
      "relation": "contains",
      "rationale": "Primary reading path",
      "claim_ids": []
    }
  ],
  "omitted_central_claims": [],
  "lineage": []
}
```

`omitted_central_claims` entries contain `claim_id` and `reason`. Omission is acceptable only when explicit, such as a duplicate claim, out-of-scope claim, or unusable source record. It is not a way to hide inconvenient disagreement.

## Readiness gate

The graph passes when:

- all central claim IDs have exactly one owning cluster or an explicit omission;
- every cluster owns at least one claim and states its decision question;
- proposed or unresolved claims are visibly qualified;
- every wikilink resolves to a declared node;
- every wikilink has one typed, justified edge in the manifest, and every non-navigation edge cites a claim ID;
- the map of content has a `contains` edge to every other visible node;
- node counts and conceptual out-degree stay within the declared budget;
- no claim, evidence, source, author, paper, dataset, or incidental-keyword nodes were generated by default;
- the map offers a coherent reading path rather than an alphabetical directory.

Graph readiness describes structure and traceability. It does not override source readiness from the survey.
