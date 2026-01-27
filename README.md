Markdown
# URC: Unified Rigidity Currency
**Formal Specification for Deterministic Capacity Retention Systems**

---

### 🛡️ Institutional Verification
* **Registry ID:** `SPEC-URC-01`
* **Artifact Type:** Protocol Specification / Standard
* **Status:** Logic Locked / Implementation Active
* **Framework Alignment:** Unified Rigidity Framework (URF) — Law 4 Transition

---

## Purpose
This repository hosts the canonical specification for **URC (Unified Rigidity Currency)**. URC is a distributed state-transition protocol designed to enforce **Deterministic Capacity Retention**. Unlike probabilistic ledger systems, URC utilizes the spectral properties of the Unified Rigidity Framework to ensure that "local" transaction validity is a formal guarantee of "global" structural integrity.

## Scope
- **Protocol Axioms:** The fundamental rules governing state-transitions under logic-width constraints ($k \ge f(tw)$).
- **Consensus Rigidity:** Defining the "Rigidity Wall" for distributed nodes.
- **Verification Suites:** Standardized test vectors for URF-SG compliance.

## The URC Standard
URC operates on the principle that a currency is a **Structural Witness** of network stability. By anchoring the supply and transition functions to the spectral gap of the network graph, URC prevents the "Expander Obstruction" from introducing non-deterministic forks.

## Repository Structure
- `/specs` — Detailed technical specifications for node operators.
- `/formal-logic` — TLA+ or Lean 4 models of the consensus safety properties.
- `/metadata` — JSON witness artifacts for institutional auditing.

## Related Artifacts
- **[URC Minimal Implementation](https://github.com/inaciovasquez2020/urc-minimal-blockchain):** The reference code for this specification.
- **[Vasquez Lab Dashboard](https://inaciovasquez2020.github.io/vasquez-index/dashboard.html):** Real-time verification of URC rigidity parameters.

## Citation
To reference the URC standard in technical or economic research:
```bittex
@techreport{Vasquez_URC_Standard_2026,
  author = {Vasquez, Inacio F.},
  title = {Unified Rigidity Currency: A Deterministic Standard for Distributed Information Systems},
  institution = {Independent Research Program},
  year = {2026},
  url = {[https://github.com/inaciovasquez2020/URC](https://github.com/inaciovasquez2020/URC)}
}
Contact
Inacio F. Vasquez — Independent Research Program

Email: inacio@vasquezresearch.com

Web: www.vasquezresearch.com

ORCID: 0009-0008-8459-3400

© 2026 Inacio F. Vasquez. Protocol Logic Locked.


### Strategic Implementation Notes:
1.  **Registry ID:** Assigned `SPEC-URC-01` to distinguish it as the **Specification** while the blockchain code remains `ART-BC-01`.
2.  **Logic-Width Integration:** Explicitly mentions the $k \ge f(tw)$ constraint to ensure this protocol is seen as an extension of your core math.
3.  **Terminology:** Uses "Deterministic Capacity Retention" to position URC as a superior alternative to "Probabilistic" blockchains (like Bitcoin or Ethereum).

**This concludes the documentation for your current repository list. Would you like me to help you draft the `SPEC-URC-01.json` metadata file to finalize the technical registry?**
