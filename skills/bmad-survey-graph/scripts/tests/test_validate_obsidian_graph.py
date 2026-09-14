# /// script
# requires-python = ">=3.11"
# ///
"""Behavior tests for the survey Obsidian graph validator."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "validate_obsidian_graph.py"


def write_graph(root: Path, *, max_core_nodes: int = 2) -> None:
    (root / "Clusters").mkdir(parents=True)
    (root / "_graph").mkdir()
    (root / "00 - Smoke Map.md").write_text(
        "# Smoke map\n\n- contains [[Clusters/C01 - Core]] because it is central.\n",
        encoding="utf-8",
    )
    (root / "Clusters" / "C01 - Core.md").write_text(
        "# Core\n\nClaim C-001 is the central finding.\n",
        encoding="utf-8",
    )
    manifest = {
        "schema_version": 1,
        "topic": "Smoke test",
        "source": {"workspace": "fixture", "readiness": "ready"},
        "graph_readiness": "ready",
        "budget": {
            "max_core_nodes": max_core_nodes,
            "max_cluster_nodes": 1,
            "max_bridge_nodes": 0,
            "max_outgoing_links": 5,
            "exception_reason": "Small deterministic fixture",
        },
        "central_claim_ids": ["C-001"],
        "nodes": [
            {
                "id": "MOC",
                "type": "moc",
                "title": "Smoke Map",
                "path": "00 - Smoke Map.md",
                "claim_ids": [],
            },
            {
                "id": "C01",
                "type": "cluster",
                "title": "Core",
                "path": "Clusters/C01 - Core.md",
                "claim_ids": ["C-001"],
            },
        ],
        "edges": [
            {
                "from": "MOC",
                "to": "C01",
                "relation": "contains",
                "rationale": "Only cluster in the smoke fixture",
                "claim_ids": [],
            }
        ],
        "omitted_central_claims": [],
        "lineage": [],
    }
    (root / "_graph" / "graph-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")


class ValidateObsidianGraphTest(unittest.TestCase):
    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(root)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_accepts_traceable_graph_within_budget(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_graph(root)
            result = self.run_validator(root)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Validation passed", result.stdout)

    def test_rejects_graph_over_node_budget(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_graph(root, max_core_nodes=1)
            result = self.run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("core node count 2 exceeds budget 1", result.stderr)


if __name__ == "__main__":
    unittest.main()
