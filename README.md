# URC — Unified Rigidity Currency
**Protocol Specification for Deterministic Capacity Retention Systems**

---

## Institutional Verification

* **Registry ID:** `SPEC-URC-01`  
* **Artifact Type:** Protocol Specification / Technical Standard  
* **Status:** Logic Locked / Implementation Active  
* **Framework Alignment:** Unified Rigidity Framework (URF) — Law 4 Transition  

---

## Role in the Scientific Infrastructure

This repository contains the **formal specification** for URC.

It is **not a theorem repository**.  
It is **not a proof repository**.  
It is **not a research frontier**.

It defines a **technical standard** derived from closed URF results.

In infrastructure terms:

> URC is a **Tier B module — Engineering Standard**

---

## Purpose

URC (Unified Rigidity Currency) is a distributed state-transition protocol
designed to enforce **Deterministic Capacity Retention**.

It applies URF rigidity principles to distributed ledgers by ensuring that:

- local transaction validity implies global consistency,
- refinement cannot amplify entropy,
- forks cannot arise from expander-type structures.

This is achieved by constraining network topology and state transitions
using logic-width bounds.

---

## Scope

This repository defines:

- **Protocol Axioms:** Formal rules for node state transitions.  
- **Consensus Constraints:** Structural invariants for fork prevention.  
- **Verification Schemas:** JSON / formal models for auditing implementations.

This repository does **not**:

- define cryptoeconomic incentives,  
- prove new mathematical results,  
- replace URF core theory.

---

## The URC Standard

URC treats a currency as a **Structural Witness** of network stability.

The protocol enforces:

\[
k \ge f(\mathrm{tw})
\]

so that any admissible transaction graph is guaranteed to preserve
global structural integrity.

This prevents:

- probabilistic finality,
- emergent forks,
- entropy amplification.

---

## Repository Structure

- `/specs` — Formal protocol definitions  
- `/formal-logic` — TLA+ / Lean 4 safety models  
- `/metadata` — Registry schemas and audit descriptors  

---

## Related Artifacts

- **Reference Implementation:**  
  https://github.com/inaciovasquez2020/urc-minimal-blockchain  

- **Verification Dashboard:**  
  https://inaciovasquez2020.github.io/vasquez-index/dashboard.html  

---

## Ontological Status

In the infrastructure model:

| Component | Role |
|----------|------|
| URF-Core / Chronos / Radiative Rigidity | Theorems |
| chronos-urf-rr | Verification layer |
| **URC (this repo)** | **Engineering standard** |
| urc-minimal-blockchain | Applied witness |
| scientific-infrastructure | Kernel manifest |

URC is **a standard**, not a discovery.

---

## Research Status

URC is structurally complete as a protocol specification.  
Any uncertainty concerns **deployment and interpretation only**, not logic.

---

## Citation

```bibtex
@techreport{Vasquez_URC_Standard_2026,
  author       = {Vasquez, Inacio F.},
  title        = {Unified Rigidity Currency — Deterministic Capacity Retention Standard},
  institution  = {Independent Research Program},
  year         = {2026},
  url          = {https://github.com/inaciovasquez2020/URC}
}
