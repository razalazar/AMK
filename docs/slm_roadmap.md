# SLM Roadmap

The journey from raw developer interactions to a highly specialized Small Language Model (SLM) involves 4 stages:

## 1. Piloto (Pilot)
- **Goal**: Raw data capture.
- **Action**: EVOMEM runs in the background of the IDE, logging all prompts, responses, and code changes without strict filtering.
- **Output**: Unstructured JSON logs.

## 2. Producción (Production)
- **Goal**: Cleaning and standardization.
- **Action**: Logs are parsed, metadata is validated, and malformed interactions are discarded.
- **Output**: Structured, clean datasets tracking specific files and sessions.

## 3. Golden Dataset
- **Goal**: Quality assurance.
- **Action**: Code evolutions are extracted. Only pairs with clear logic improvements (e.g., successful bug fixes, refactors) are promoted.
- **Output**: High-quality prompt-completion pairs ready for fine-tuning.

## 4. SLM (Small Language Model)
- **Goal**: Deployment of Green AI.
- **Action**: The Golden Dataset is used to fine-tune a lightweight base model (e.g., Llama 3 8B, Phi-3).
- **Result**: A specialized model that assists developers with near-zero latency and minimal environmental impact.
