# AMK (Agent Memory Kit) 
**Powered by the EVOMEM Engine**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Green AI](https://img.shields.io/badge/Green%20AI-CO2%20Optimized-brightgreen)

> **A Tribute**: AMK stands for **Amy, Mariposa, and Kori**. This project was created by Andrés Salazar Quintero in eternal memory of Eliana Arenas Cano ("Mariposa"), who passed away on March 31, 2025, and as a legacy for his children, Amy and Kori. It is a guardian of memory, built from love and engineered for the highest professional innovation.

## The IDE Context Regression Problem

In software engineering, a common problem when using AI coding assistants is **IDE Context Regression**: when you fix Module A, the AI loses the context of Module B and breaks it. LLMs lack persistent memory between sessions—they start from scratch based only on what they see in the current window.

**AMK** solves this through its internal engine, **EVOMEM (Evolutionary Memory System)**. It acts as the institutional memory of your project, representing **RLHF (Reinforcement Learning from Human Feedback) democratized for small teams with conventional IDEs.** 

If you fixed an OCR module three weeks ago that changed how dates are formatted, and today you ask the AI to fix the forecast module, AMK ensures the AI "remembers" that OCR constraint and doesn't break it. 

## The 3-Layer Architecture

The system is built on three interconnected layers:

1. **Layer 1 — Interaction Memory:** Captures every prompt and response from the agent with its outcome (correct, corrected, rejected). This forms the foundation of the Golden Dataset.
2. **Layer 2 — Code Evolution Memory:** Captures every code change and its context: what module changed, why, what was wrong, how it was fixed, and *which other modules might be affected*.
3. **Layer 3 — Regression Intelligence:** A deterministic dependency analysis. Every time code changes, it cross-references Layer 2 to see if previous corrections are impacted, generating a preemptive alert before the IDE breaks them.

## Why Green AI?

Training massive LLMs consumes staggering amounts of energy. AMK champions the **Green AI** vision by creating high-quality, domain-specific "Golden Datasets" used to train **SLMs (Small Language Models)**. These SLMs are highly specialized, run efficiently on edge devices, and drastically reduce the environmental cost of AI.

## Installation

```bash
pip install evomem
```

## Quickstart

```python
from evomem import InteractionMemory, CodeEvolutionMemory, RegressionIntelligence

# 1. Initialize memory tracker (Layer 1)
memory = InteractionMemory(session_id="dev-session-001")

# 2. Track a code evolution event (Layer 2)
code_evo = CodeEvolutionMemory()
code_evo.track_evolution(
    original_code="def read_date(text): return text",
    improved_code="def read_date(text): return text.replace('-', '/')",
    reason="Fixed OCR date format issue. Forecast module relies on this format.",
    file_path="ocr_module.py",
    affected_modules=["forecast_module.py"]
)

# 3. Check for regressions before making new changes (Layer 3)
reg_intel = RegressionIntelligence()
alerts = reg_intel.check_regression_risk("forecast_module.py")
print("Alerts before changing forecast:", alerts)
```

## Dataset Roadmap

1. **Piloto:** Raw, uncurated data capture from IDE sessions.
2. **Producción:** Cleaned interaction logs with valid metadata.
3. **Golden Dataset:** Rigorously verified pairs featuring the highest quality code evolutions.
4. **SLM (Small Language Model):** Specialized, fine-tuned lightweight models trained on the Golden Dataset.

## Contributing
We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits
- **Creator & Architect**: Andrés Salazar Quintero
- **In Memory Of**: Eliana Arenas Cano ("La Mariposa")
