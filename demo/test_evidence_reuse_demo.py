import unittest

from demo.evidence_reuse_demo import decide_evidence


BASE_CHANGE = {
    "authority_revision": "A3",
    "contract_revision": "C7",
    "evaluation_revision": "E2",
    "environment": "preview",
    "changed_dependencies": [],
    "requires_fresh_evidence": [],
    "contradicted_claims": [],
}

BASE_EVIDENCE = {
    "id": "example",
    "claim": "A previously accepted claim",
    "status": "accepted",
    "dependencies": ["auth_session"],
    "authority_revision": "A3",
    "contract_revision": "C7",
    "evaluation_revision": "E2",
    "environment": "preview",
    "portable_across_environments": False,
}


class EvidenceReuseTests(unittest.TestCase):
    def test_reuses_unchanged_accepted_evidence(self):
        decision = decide_evidence(BASE_CHANGE, BASE_EVIDENCE)
        self.assertEqual("REUSE", decision.decision)

    def test_reruns_when_dependency_changes(self):
        change = dict(BASE_CHANGE, changed_dependencies=["auth_session"])
        decision = decide_evidence(change, BASE_EVIDENCE)
        self.assertEqual("RERUN", decision.decision)
        self.assertIn("auth_session", " ".join(decision.reasons))

    def test_reruns_when_environment_changes(self):
        change = dict(BASE_CHANGE, environment="production")
        decision = decide_evidence(change, BASE_EVIDENCE)
        self.assertEqual("RERUN", decision.decision)
        self.assertIn("environment", " ".join(decision.reasons))

    def test_unsupported_when_prior_evidence_was_not_accepted(self):
        evidence = dict(BASE_EVIDENCE, status="blocked")
        decision = decide_evidence(BASE_CHANGE, evidence)
        self.assertEqual("UNSUPPORTED", decision.decision)

    def test_reruns_when_semantic_rubric_changes(self):
        change = dict(BASE_CHANGE, evaluation_revision="E3")
        decision = decide_evidence(change, BASE_EVIDENCE)
        self.assertEqual("RERUN", decision.decision)
        self.assertIn("evaluation", " ".join(decision.reasons))


if __name__ == "__main__":
    unittest.main()
