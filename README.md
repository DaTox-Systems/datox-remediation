# 🛡️ DaTox Remediation: AI-Debt & Architectural Governance Bureau

> **We restore predictability, modularity, and testability to AI-assisted and legacy codebases.**  
> *Transforming fragile Cursor/Claude prototypes into robust, production-grade Clean Architecture systems.*

[![Architecture](https://img.shields.io/badge/Methodology-Clean%20Cortex-00E676)]()
[![Linter](https://img.shields.io/badge/Quality%20Gate-0%20Issues-brightgreen)]()
[![Tests](https://img.shields.io/badge/Tests-100%25%20Passing-brightgreen)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 📌 The Problem We Solve: AI-Debt & Architectural Drift

Modern AI development tools (Cursor, Claude, Copilot) empower founders and indie builders to create functional MVPs rapidly. However, once a codebase exceeds **1,000–2,000 LOC**, unconstrained AI generation leads to severe architectural degradation:

* **Tightly coupled UI & Infrastructure:** Direct network/database calls from widgets, causing cascading breakage.
* **Leaking UI Contexts:** `BuildContext` passed into background logic, triggering asynchronous crashes.
* **0% Dependency Inversion:** Hardcoded instantiations (`new Service()`) making unit testing impossible.
* **Fear of Iteration:** Adding a new feature breaks 2–3 existing screens, stalling development.

We provide **systematic architectural triage and deep remediation**, enabling teams and founders to continue developing safely with AI without fear of regressions.

---

## 🧭 Our 4-Axis Diagnostic Framework

Every codebase undergoes rigorous evaluation across four objective engineering axes:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      DTX 4-AXIS AUDIT FRAMEWORK                        │
├────────────────────────────┬───────────────────────────────────────────┤
│  1. COUPLING & ISOLATION   │  2. STATE & LIFECYCLE RIGOR               │
│  Layer boundary leaks      │  Context leaks, state cross-talk, memory  │
├────────────────────────────┼───────────────────────────────────────────┤
│  3. DI & COMPOSITION ROOT  │  4. CODE HYGIENE & TESTABILITY            │
│  Inversion of Control      │  Isolated unit testability, dead code     │
└────────────────────────────┴───────────────────────────────────────────┘
```

---

## 📂 Remediation Portfolio & Case Studies

| Case ID | Target / Domain | Original Stack | ARI Reduction | Case Study & Code |
| :--- | :--- | :--- | :--- | :--- |
| **CASE-01** | **Akıllı Market Listem** (Grocery & Price Tracker) | Flutter / Provider / SQLite | **83.5 $\rightarrow$ 11.0 (-87%)** | [**View Showcase Repo ➔**](https://github.com/DaTox-Systems/case-01-flutter-ai-market-list) |

---

## 🛠️ Standards & Documentation

Our operational methodology is fully open and documented:
* [`/docs/standards/DTX_AUDIT_STANDARD.md`](./docs/standards/DTX_AUDIT_STANDARD.md) — 60-minute express architectural audit protocol.
* [`/docs/standards/DTX_REFACTORING_STD.md`](./docs/standards/DTX_REFACTORING_STD.md) — 7-step Quality Gate & verification pipeline.
* [`/docs/standards/DTX_CASE_STUDY_STD.md`](./docs/standards/DTX_CASE_STUDY_STD.md) — Evidence-based case packaging standard.

---

## ⚖️ Attribution & Ethics

All remediation case studies are independent architectural analyses conducted on open-source codebases under MIT/Apache licenses or Fair Use educational guidelines. Original authors and repositories are explicitly credited in each individual showcase repository.

---

## 🤝 Need Architectural Triage?

Working with an AI-generated codebase that has become fragile or unmaintainable?  
We offer independent architectural audits and structured codebase remediation.

📬 Reach out via **GitHub Discussions**, **LinkedIn**, or **Upwork** to discuss your project.
