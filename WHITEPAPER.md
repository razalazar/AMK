# AMK: The Agent Memory Kit Whitepaper
**A Framework for Evolutionary Memory, Context Preservation, and Green AI**

## 1. Abstract & Legacy
In modern software engineering, Artificial Intelligence coding assistants (LLMs) suffer from severe "Context Regression"—they fix one module but break another because they lack institutional memory across sessions. **AMK (Agent Memory Kit)**, powered by the EVOMEM engine, solves this by acting as a local, evolutionary memory vault. 

AMK is an open-source architectural framework built as a deeply human legacy in memory of Eliana Arenas Cano ("La Mariposa"). It proves that AI can be specialized locally, saving not only developer hours but also significantly reducing the massive water and carbon footprint of global data centers.

---

## 2. The Core Problem: IDE Context Regression
When an AI fixes "Module A" today, and three weeks later you ask it to modify "Module B", the AI has forgotten the constraints of Module A. It starts from scratch. This forces developers to repeatedly write massive prompts to remind the AI of past decisions, burning millions of tokens and wasting energy.

---

## 3. The 3-Layer EVOMEM Architecture
AMK solves this through a deterministic 3-layer structure:
1. **Interaction Memory:** Logs the exact prompts and outcomes.
2. **Code Evolution Memory:** Captures the "Before", "After", and the "Why" of a code change, tracking which other files depend on it.
3. **Regression Intelligence:** A pre-flight check that warns the developer *before* an AI modifies a file if that modification risks breaking a previously established memory rule.

---

## 4. The Agnostic AI Factory (SLM Democratization)
Giant LLMs are excellent "teachers" but are unsustainable for daily production. AMK acts as a **Sandbox Funnel**:
* **Phase A (Present):** You use a giant LLM in your IDE. AMK captures the successful corrections.
* **Phase B (Funnel):** AMK injects context backward to save tokens, while simultaneously curating a "Golden Dataset".
* **Phase C (Future):** You use the Golden Dataset to train a Small Language Model (SLM). The SLM becomes a sovereign, hyper-fast domain expert that runs locally at zero API cost.

---

## 5. The Green AI Thesis (Water & Carbon)
Every 10 to 50 queries to a massive LLM consume a 500ml bottle of fresh water for data center cooling, and emit roughly 4.3 grams of CO2 per query. By giving the IDE local memory, AMK prevents thousands of redundant queries. Moving to SLMs completely decentralizes the computing cost, aligning software engineering with critical ESG (Environmental, Social, and Governance) goals.

---

## 6. The Golden Paradox: Self-Evolution (Dogfooding)
Can an AI evolve its own memory engine without corrupting the original seed? Yes. Through a technique called *Dogfooding* and *Environment Isolation*, developers can run AMK as a background watcher while modifying AMK's own codebase. The local logs capture the evolution safely. Once validated, the new DNA is pushed to the global repository.

---

## 7. Open Source Security & Governance
To ensure enterprise trust, AMK guarantees:
* **Zero-Telemetry:** It operates locally. It does not send proprietary code to external APIs.
* **Air-Gapped Auditing:** It functions perfectly offline, proving mathematically that data is not being exfiltrated.
* **MIT License:** The code is 100% transparent and auditable by cybersecurity teams.
