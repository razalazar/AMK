# EVOMEM Architecture

## Overview
EVOMEM is designed with a modular architecture to ensure flexibility and lightweight integration into any Python-based IDE workflow or standalone script.

## Core Components
1. **InteractionMemory**: Handles the persistence of dialogue turns and context. Uses local file storage (JSON) by default to avoid heavy DB dependencies.
2. **CodeEvolutionMemory**: Specifically designed to track the delta between code states, along with the natural language rationale. This is the engine that builds SLM-ready pairs.
3. **RegressionAnalyzer**: Provides analytics on the collected evolutions to spot files that are changing too frequently, which may indicate regressions.
4. **Exporters**: A suite of adapters (Vertex AI, HuggingFace, AWS Bedrock) that simulate the upload process for the generated datasets. They remain decoupled from cloud SDKs until strictly needed.

## Design Philosophy
- **No Heavy Cloud Bindings**: Keeps the library clean. 
- **Privacy First**: Logs are stored locally unless explicitly exported.
