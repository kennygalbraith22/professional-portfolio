# Kenny Galbraith

**Operational Excellence | Manufacturing Transformation | AI-Assisted Product Delivery**

> **Status:** Private portfolio draft under review. This repository is not yet intended for public distribution.

I turn operating problems into systems with clear ownership, practical standards, and evidence that the work holds up.

My professional background spans defense manufacturing and high-volume consumer production, progressing from hands-on equipment and material-support work into frontline leadership and Autonomous Maintenance coordination. My work has centered on equipment ownership, defect management, root-cause action, standardized work, reliability, and developing people to own and improve their processes.

Alongside that career, I independently direct AI-assisted product development across three software projects: **KaelUX Writing Engine**, **Emet**, and **Riff & Rondo**. I use AI tools extensively and openly. My contribution is not a claim of manually authoring every line of code; it is defining the problem, establishing architecture and ownership boundaries, translating requirements into executable work, directing implementation, designing acceptance criteria, investigating failures, and deciding whether the evidence is strong enough to treat work as complete.

This portfolio focuses on that intersection: **operational discipline applied to AI-assisted technical delivery**.

## 30-second view

| Area | What I bring |
| --- | --- |
| **Operational Excellence** | Equipment ownership, TPM/Autonomous Maintenance, defect management, root-cause thinking, standardized work, reliability, and frontline capability development |
| **Technical Program Delivery** | Requirements, dependency mapping, acceptance criteria, bounded execution, failure investigation, and evidence-backed closure |
| **Applied AI Delivery** | Multi-provider AI product work, behavioral evaluation, persistence/continuity boundaries, AI-assisted implementation, and explicit claim/release states |
| **Validation** | Deterministic tests, negative paths, recovery, human semantic review, environment-specific proof, and evidence reuse/invalidation |

## Selected case studies

| Project | Focus | Case study |
| --- | --- | --- |
| **Emet** | AI-assisted engineering governance, proof planning, evidence reuse, and failure handling | [From generated output to evidence-backed delivery](case-studies/01-emet-evidence-governance.md) |
| **KaelUX Writing Engine** | Multi-provider AI companions, continuity, behavioral evaluation, and controlled release boundaries | [Building and validating a governed AI writing system](case-studies/02-kaelux-writing-engine.md) |
| **Riff & Rondo** | Music-learning progression, authoritative persistence, notation, learner UX, and testing | [Building reliable progression into a learning product](case-studies/03-riff-and-rondo.md) |

Each case study now includes a simplified visual system diagram. The diagrams are intentionally sanitized and communicate ownership/decision boundaries rather than private implementation detail.

## Runnable synthetic demonstration

The portfolio includes one small executable example: [`demo/`](demo/README.md).

It demonstrates an evidence-reuse decision model by comparing a synthetic change manifest with prior evidence and returning:

- `REUSE` when accepted evidence still supports the claim;
- `RERUN` when a relevant authority, dependency, contract, environment, evaluation rule, freshness requirement, or contradiction changed;
- `UNSUPPORTED` when the prior record was never accepted evidence for the claim.

Run it with only the Python standard library:

```bash
python demo/evidence_reuse_demo.py demo/sample_change.json demo/sample_evidence.json
python -m unittest demo.test_evidence_reuse_demo
```

This is a teaching example derived from the portfolio methodology, **not** a release of Emet source code.

## What this portfolio is meant to demonstrate

- **Operational excellence:** ownership, standards, root-cause thinking, defect containment, and continuous improvement.
- **Technical program delivery:** turning ambiguous goals into scoped work, dependencies, acceptance criteria, and verifiable outcomes.
- **AI-assisted development:** using AI as a high-leverage implementation tool without treating generated output as automatic proof.
- **Validation discipline:** separating implementation, integration, certification, deployed proof, and release authority.
- **Cross-functional thinking:** connecting product intent, technical behavior, user experience, privacy, persistence, and operational risk.

## Repository map

```text
professional-portfolio/
├── README.md
├── ABOUT_MY_WORK.md
├── AI_ASSISTED_WORK_DISCLOSURE.md
├── NOTICE.md
├── case-studies/
│   ├── 01-emet-evidence-governance.md
│   ├── 02-kaelux-writing-engine.md
│   └── 03-riff-and-rondo.md
├── demo/
│   ├── evidence_reuse_demo.py
│   ├── sample_change.json
│   ├── sample_evidence.json
│   └── test_evidence_reuse_demo.py
└── evidence/
    ├── methodology.md
    └── claim-boundaries.md
```

## How I work

A few principles recur across both my manufacturing and software work:

1. **Define ownership before activity.** A defect, requirement, or failure should have a clear owner and a clear acceptance boundary.
2. **Separate visible activity from durable completion.** A passing command or generated artifact is not the same as an accepted result.
3. **Test the failure path, not just the happy path.** Recovery, interruption, stale state, invalid input, and incorrect authority matter.
4. **Keep evidence proportional to the claim.** Structural tests can prove structure; behavioral claims may require human evaluation; deployed claims require deployed evidence.
5. **Preserve valid proof.** If the relevant authority, dependency, contract, environment, and evidence remain valid, rerunning everything can add cost without adding knowledge.
6. **Keep unknowns visible.** I would rather label a state unknown than turn an assumption into a fact.

## Background

My manufacturing career includes frontline production, material and engineering support, team leadership, Autonomous Maintenance, Total Productive Maintenance, equipment reliability, training, and operational improvement. My independent product work began in 2025; Riff & Rondo and Emet are 2026 projects.

I am most interested in roles where **operational excellence, manufacturing or digital transformation, implementation, technical program delivery, and applied AI** meet.

## Portfolio notes

- The case studies are **sanitized professional summaries**, not releases of private product source code or controlled company records.
- Product code, internal evidence, credentials, user data, security-sensitive detail, and private project records are intentionally excluded.
- This portfolio documents my technical contribution; it is not a claim of KaelUX LLC company ownership or company-binding commercial/public-release authority.
- Current product/release state can change after a case study is written. The portfolio describes the demonstrated work and its stated evidence boundary rather than claiming every project is publicly released.
- AI use and authorship boundaries are described in [AI_ASSISTED_WORK_DISCLOSURE.md](AI_ASSISTED_WORK_DISCLOSURE.md).
- Validation and evidence practices are summarized in [evidence/methodology.md](evidence/methodology.md).
- Public-claim boundaries are documented in [evidence/claim-boundaries.md](evidence/claim-boundaries.md).

## More about my role

See [ABOUT_MY_WORK.md](ABOUT_MY_WORK.md) for a fuller explanation of how my manufacturing experience and AI-assisted product work connect.
