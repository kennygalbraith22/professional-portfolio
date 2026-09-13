#!/usr/bin/env python3
"""Synthetic evidence reuse / invalidation demo.

This example is intentionally generic. It contains no KaelUX, Emet, or
Riff & Rondo production code, private project data, proprietary prompts,
credentials, or internal evidence records.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class Decision:
    evidence_id: str
    claim: str
    decision: str
    reasons: tuple[str, ...]


def _as_set(value: Any) -> set[str]:
    if value is None:
        return set()
    if not isinstance(value, list):
        raise ValueError("expected a JSON array")
    return {str(item) for item in value}


def decide_evidence(change: dict[str, Any], evidence: dict[str, Any]) -> Decision:
    """Classify one evidence record as REUSE, RERUN, or UNSUPPORTED."""

    evidence_id = str(evidence["id"])
    claim = str(evidence["claim"])
    status = str(evidence.get("status", "unknown")).lower()

    if status != "accepted":
        return Decision(
            evidence_id,
            claim,
            "UNSUPPORTED",
            (f"evidence status is {status!r}, not 'accepted'",),
        )

    reasons: list[str] = []

    if evidence_id in _as_set(change.get("contradicted_claims")):
        reasons.append("new evidence contradicts the prior result")

    if evidence_id in _as_set(change.get("requires_fresh_evidence")):
        reasons.append("the current gate explicitly requires fresh evidence")

    if evidence.get("authority_revision") != change.get("authority_revision"):
        reasons.append("controlling authority revision changed")

    if evidence.get("contract_revision") != change.get("contract_revision"):
        reasons.append("applicable contract revision changed")

    if evidence.get("evaluation_revision") != change.get("evaluation_revision"):
        reasons.append("evaluation rule revision changed")

    changed_dependencies = _as_set(change.get("changed_dependencies"))
    evidence_dependencies = _as_set(evidence.get("dependencies"))
    affected = sorted(changed_dependencies & evidence_dependencies)
    if affected:
        reasons.append("changed dependency affects this claim: " + ", ".join(affected))

    evidence_environment = str(evidence.get("environment", "any"))
    current_environment = str(change.get("environment", "unknown"))
    portable = bool(evidence.get("portable_across_environments", False))
    if evidence_environment not in {"any", current_environment} and not portable:
        reasons.append(
            f"evidence environment {evidence_environment!r} does not prove "
            f"current environment {current_environment!r}"
        )

    if reasons:
        return Decision(evidence_id, claim, "RERUN", tuple(reasons))

    return Decision(
        evidence_id,
        claim,
        "REUSE",
        (
            "no material authority, dependency, contract, environment, "
            "evaluation, freshness, or contradiction change found",
        ),
    )


def classify(
    change: dict[str, Any], records: Iterable[dict[str, Any]]
) -> list[Decision]:
    return [decide_evidence(change, record) for record in records]


def render_table(decisions: Iterable[Decision]) -> str:
    rows = list(decisions)
    headers = ("Evidence", "Decision", "Reason")
    data = [
        (decision.evidence_id, decision.decision, "; ".join(decision.reasons))
        for decision in rows
    ]
    widths = [
        max([len(headers[index])] + [len(row[index]) for row in data])
        for index in range(3)
    ]

    def fmt(row: tuple[str, str, str]) -> str:
        return " | ".join(row[index].ljust(widths[index]) for index in range(3))

    separator = "-+-".join("-" * width for width in widths)
    return "\n".join([fmt(headers), separator, *(fmt(row) for row in data)])


def load_json(path: str | Path) -> Any:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Classify synthetic prior evidence as REUSE, RERUN, or UNSUPPORTED."
        )
    )
    parser.add_argument("change", help="Path to synthetic change manifest JSON")
    parser.add_argument("evidence", help="Path to synthetic evidence records JSON")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    decisions = classify(load_json(args.change), load_json(args.evidence))

    if args.json:
        print(json.dumps([decision.__dict__ for decision in decisions], indent=2))
    else:
        print(render_table(decisions))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
