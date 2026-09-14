#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Validate the structural and density invariants of a survey Obsidian graph."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
NODE_TYPES = {"moc", "cluster", "bridge"}
RELATIONS = {
    "contains",
    "supports",
    "contradicts",
    "qualifies",
    "depends-on",
    "compares-with",
    "refines",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an Obsidian graph generated from a BMAD survey.")
    parser.add_argument("graph_dir", type=Path, help="Topic graph directory")
    return parser.parse_args()


def positive_int(value: Any, field: str, errors: list[str]) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        errors.append(f"{field} must be a non-negative integer")
        return 0
    return value


def normalize_target(value: str) -> str:
    target = value.split("|", 1)[0].split("#", 1)[0].strip().replace("\\", "/")
    return target[:-3] if target.lower().endswith(".md") else target


def validate_relative_markdown_path(value: Any, node_id: str, errors: list[str]) -> str | None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"node {node_id}: path must be a non-empty string")
        return None
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or path.suffix.lower() != ".md":
        errors.append(f"node {node_id}: path must be a safe relative .md path: {value!r}")
        return None
    return path.as_posix()


def load_manifest(graph_dir: Path, errors: list[str]) -> dict[str, Any]:
    manifest_path = graph_dir / "_graph" / "graph-manifest.json"
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing manifest: {manifest_path}")
        return {}
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read valid JSON manifest: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append("manifest root must be an object")
        return {}
    return data


def main() -> int:
    args = parse_args()
    graph_dir = args.graph_dir.resolve()
    errors: list[str] = []
    manifest = load_manifest(graph_dir, errors)
    if not manifest:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if manifest.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if manifest.get("graph_readiness") not in {"ready", "blocked"}:
        errors.append("graph_readiness must be ready or blocked")
    source = manifest.get("source")
    if not isinstance(source, dict):
        errors.append("source must be an object")
    elif source.get("readiness") not in {"ready", "blocked"}:
        errors.append("source.readiness must be ready or blocked")

    nodes = manifest.get("nodes")
    edges = manifest.get("edges")
    budget = manifest.get("budget")
    central_claim_ids = manifest.get("central_claim_ids")
    omissions = manifest.get("omitted_central_claims", [])

    if not isinstance(nodes, list):
        errors.append("nodes must be an array")
        nodes = []
    if not isinstance(edges, list):
        errors.append("edges must be an array")
        edges = []
    if not isinstance(budget, dict):
        errors.append("budget must be an object")
        budget = {}
    if not isinstance(central_claim_ids, list) or not all(isinstance(item, str) and item for item in central_claim_ids):
        errors.append("central_claim_ids must be an array of non-empty strings")
        central_claim_ids = []
    if not isinstance(omissions, list):
        errors.append("omitted_central_claims must be an array")
        omissions = []

    max_core_nodes = positive_int(budget.get("max_core_nodes"), "budget.max_core_nodes", errors)
    max_cluster_nodes = positive_int(budget.get("max_cluster_nodes"), "budget.max_cluster_nodes", errors)
    max_bridge_nodes = positive_int(budget.get("max_bridge_nodes"), "budget.max_bridge_nodes", errors)
    max_outgoing_links = positive_int(budget.get("max_outgoing_links"), "budget.max_outgoing_links", errors)

    node_by_id: dict[str, dict[str, Any]] = {}
    path_by_id: dict[str, str] = {}
    lookup: dict[str, list[str]] = {}
    note_links: dict[str, list[str]] = {}
    claim_owners: Counter[str] = Counter()
    type_counts: Counter[str] = Counter()

    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            errors.append(f"nodes[{index}] must be an object")
            continue
        node_id = node.get("id")
        node_type = node.get("type")
        if not isinstance(node_id, str) or not node_id:
            errors.append(f"nodes[{index}].id must be a non-empty string")
            continue
        if node_id in node_by_id:
            errors.append(f"duplicate node id: {node_id}")
            continue
        node_by_id[node_id] = node
        if node_type not in NODE_TYPES:
            errors.append(f"node {node_id}: unsupported type {node_type!r}")
        else:
            type_counts[node_type] += 1

        relative_path = validate_relative_markdown_path(node.get("path"), node_id, errors)
        if relative_path is None:
            continue
        if relative_path in path_by_id.values():
            errors.append(f"duplicate node path: {relative_path}")
        path_by_id[node_id] = relative_path

        claims = node.get("claim_ids", [])
        if not isinstance(claims, list) or not all(isinstance(claim, str) and claim for claim in claims):
            errors.append(f"node {node_id}: claim_ids must be an array of non-empty strings")
            claims = []
        if node_type == "cluster" and not claims:
            errors.append(f"cluster {node_id}: must own at least one claim")
        if node_type == "cluster":
            claim_owners.update(claims)

        note_path = graph_dir / relative_path
        try:
            text = note_path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"node {node_id}: cannot read {relative_path}: {exc}")
            continue
        note_links[node_id] = [normalize_target(match) for match in WIKILINK_RE.findall(text)]

        path_without_suffix = str(PurePosixPath(relative_path).with_suffix(""))
        keys = {
            path_without_suffix,
            PurePosixPath(relative_path).stem,
            str(node.get("title", "")).strip(),
        }
        for key in keys:
            if key:
                lookup.setdefault(key, []).append(node_id)

    if type_counts["moc"] != 1:
        errors.append(f"expected exactly one moc node, found {type_counts['moc']}")
    if len(node_by_id) > max_core_nodes:
        errors.append(f"core node count {len(node_by_id)} exceeds budget {max_core_nodes}")
    if type_counts["cluster"] > max_cluster_nodes:
        errors.append(f"cluster count {type_counts['cluster']} exceeds budget {max_cluster_nodes}")
    if type_counts["bridge"] > max_bridge_nodes:
        errors.append(f"bridge count {type_counts['bridge']} exceeds budget {max_bridge_nodes}")

    resolved_links: Counter[tuple[str, str]] = Counter()
    for source_id, targets in note_links.items():
        for target in targets:
            matches = lookup.get(target, [])
            if not matches:
                errors.append(f"node {source_id}: unresolved or undeclared wikilink [[{target}]]")
            elif len(matches) > 1:
                errors.append(f"node {source_id}: ambiguous wikilink [[{target}]]")
            else:
                resolved_links[(source_id, matches[0])] += 1

    declared_edges: Counter[tuple[str, str]] = Counter()
    conceptual_out_degree: Counter[str] = Counter()
    contained_targets: set[str] = set()
    moc_ids = {node_id for node_id, node in node_by_id.items() if node.get("type") == "moc"}
    for index, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"edges[{index}] must be an object")
            continue
        source_id = edge.get("from")
        target_id = edge.get("to")
        relation = edge.get("relation")
        rationale = edge.get("rationale")
        edge_claims = edge.get("claim_ids", [])
        if source_id not in node_by_id or target_id not in node_by_id:
            errors.append(f"edge {index}: from and to must reference declared nodes")
            continue
        if source_id == target_id:
            errors.append(f"edge {index}: self-links are not allowed")
        if relation not in RELATIONS:
            errors.append(f"edge {index}: unsupported relation {relation!r}")
        if not isinstance(rationale, str) or not rationale.strip():
            errors.append(f"edge {index}: rationale must be a non-empty string")
        if not isinstance(edge_claims, list) or not all(isinstance(claim, str) and claim for claim in edge_claims):
            errors.append(f"edge {index}: claim_ids must be an array of non-empty strings")
            edge_claims = []
        if relation == "contains":
            if source_id not in moc_ids:
                errors.append(f"edge {index}: contains edges must originate at the moc")
            contained_targets.add(target_id)
        elif not edge_claims:
            errors.append(f"edge {index}: conceptual edges must cite at least one claim ID")
        pair = (source_id, target_id)
        declared_edges[pair] += 1
        if relation != "contains":
            conceptual_out_degree[source_id] += 1
        if resolved_links[pair] == 0:
            errors.append(f"edge {index}: no matching wikilink from {source_id} to {target_id}")

    for node_id in node_by_id.keys() - moc_ids:
        if node_id not in contained_targets:
            errors.append(f"node {node_id}: missing contains edge from the moc")

    for pair, count in resolved_links.items():
        if declared_edges[pair] == 0:
            errors.append(f"wikilink {pair[0]} -> {pair[1]} has no declared edge")
        if count > 1:
            errors.append(f"wikilink {pair[0]} -> {pair[1]} appears {count} times")
    for pair, count in declared_edges.items():
        if count > 1:
            errors.append(f"edge {pair[0]} -> {pair[1]} is declared {count} times")

    for node_id, degree in conceptual_out_degree.items():
        if degree > max_outgoing_links:
            errors.append(f"node {node_id}: conceptual out-degree {degree} exceeds budget {max_outgoing_links}")

    omitted_ids: set[str] = set()
    for index, omission in enumerate(omissions):
        if not isinstance(omission, dict):
            errors.append(f"omitted_central_claims[{index}] must be an object")
            continue
        claim_id = omission.get("claim_id")
        reason = omission.get("reason")
        if not isinstance(claim_id, str) or not claim_id:
            errors.append(f"omitted_central_claims[{index}].claim_id is required")
            continue
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"omitted central claim {claim_id}: reason is required")
        omitted_ids.add(claim_id)

    for claim_id in central_claim_ids:
        dispositions = claim_owners[claim_id] + int(claim_id in omitted_ids)
        if dispositions != 1:
            errors.append(f"central claim {claim_id}: expected one owner or omission, found {dispositions}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    max_degree = max(conceptual_out_degree.values(), default=0)
    print(
        "Validation passed: "
        f"{type_counts['cluster']} clusters, {type_counts['bridge']} bridges, "
        f"{len(edges)} edges, max conceptual out-degree {max_degree}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
