# Validation and Evidence Methodology

This portfolio uses a simple rule: **the strength of the claim should not exceed the strength of the evidence**.

The projects described here use different proof methods depending on what is being claimed.

## Evidence layers

### 1. Implementation evidence

Shows that code, configuration, or product structure exists.

Examples:

- repository diff or commit;
- file/path inspection;
- schema or configuration inspection;
- deterministic unit-level behavior.

Implementation evidence does not automatically prove integration, deployed behavior, or product quality.

### 2. Integration evidence

Shows that relevant components work together across their intended interfaces.

Examples:

- integration tests;
- authenticated persistence flows;
- provider/runtime requests through the real adapter boundary;
- state transitions across client/server ownership;
- quota, billing, or persistence interactions.

### 3. Negative-path and recovery evidence

Shows that the system behaves deliberately when conditions are wrong or interrupted.

Examples:

- invalid or stale authority;
- duplicate operations;
- provider or network failure;
- persistence failure;
- interrupted execution;
- unknown remote outcome;
- rejected authentication or ownership.

A negative test should reach the actual guard it claims to test. Failing earlier for an unrelated reason is not equivalent proof.

### 4. Behavioral or semantic evidence

Used where correctness cannot be reduced to structure alone.

Examples:

- AI companion behavior;
- instruction following;
- differentiation between interaction roles;
- visual fidelity;
- user-facing quality judgments.

These claims may require human evaluation even when the underlying request/response machinery passes deterministic checks.

### 5. Environment-specific evidence

Used when the claim depends on where the system is running.

Examples:

- exact deployed revision;
- Preview behavior;
- database or provider environment;
- Production behavior.

A local pass is not silently promoted into deployed proof.

### 6. Release authority

Release is treated as a decision state, not merely another automated test.

A system can be implemented, integrated, and certified while still being intentionally unreleased because business, security, legal, operational, or product gates remain open.

## State vocabulary

The projects use distinctions similar to:

`IMPLEMENTED -> INTEGRATED -> CERTIFIED -> DEPLOYMENT-VERIFIED -> RELEASED`

Not every workstream needs every state, but later states are not inferred from earlier ones.

## Evidence reuse

Accepted evidence should be reused when it still supports the claim.

Before requiring fresh proof, I ask what changed:

- **authority** — did the controlling requirement or decision change?
- **dependency** — did something the result depends on change?
- **contract** — did an interface, schema, provider behavior, or acceptance contract change?
- **environment** — is the target environment different?
- **evaluation rule** — did the rubric or meaning of success change?
- **freshness requirement** — does this gate explicitly require current evidence?
- **contradiction** — is there new evidence that invalidates the prior result?

If none of those materially affect the supported claim, rerunning a large suite may add cost without increasing confidence.

## Failure classification

I try to distinguish at least four failure types:

1. **implementation defect** — the system behavior is wrong;
2. **proof defect** — the test, harness, fixture, or evaluation method is wrong;
3. **environment mismatch** — the behavior differs because the execution environment differs;
4. **unsupported assumption** — the available evidence never actually established the claim.

This prevents every red result from automatically triggering a rewrite of the product architecture.

## Human review

Human review is preserved when the acceptance claim is semantic, behavioral, or visual.

Automation is useful for repeatability and scale. It should not be used to create false precision around a judgment the machine-readable evidence does not actually establish.

## Unknown is a valid state

When the available evidence cannot distinguish success from failure, I prefer **UNKNOWN** to an invented answer.

That is especially important after interrupted remote operations, incomplete evidence capture, stale deployment identity, or inaccessible environments.

## Public portfolio boundary

This document summarizes the reasoning model used across the case studies. It is not a publication of private test suites, internal governance records, security findings, proprietary prompts, or controlled product evidence.
