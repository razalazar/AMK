# AMK (Agent Memory Kit)
**Potenciado por el motor EVOMEM**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Green AI](https://img.shields.io/badge/Green%20AI-CO2%20Optimized-brightgreen)

> **Un Tributo**: AMK significa **Amy, Mariposa y Kori**. Este proyecto fue creado por Andrés Salazar Quintero en memoria eterna de Eliana Arenas Cano ("La Mariposa"), fallecida el 31 de marzo de 2025, y como un legado inquebrantable para sus hijos, Amy y Kori. Es un guardián de la memoria, construido desde el amor y diseñado con el máximo rigor para la innovación profesional global.

## El Problema de la Regresión de Contexto en el IDE

En la ingeniería de software, un problema común al usar asistentes de IA es la **regresión de contexto del IDE**: cuando corriges el módulo A, la IA pierde el contexto del módulo B y lo rompe. Los LLMs no tienen memoria persistente entre sesiones; empiezan desde cero con lo que ven en la ventana actual.

**AMK** resuelve esto a través de su motor interno **EVOMEM (Evolutionary Memory System)**. Actúa como la memoria institucional de tu proyecto y representa el **RLHF (Reinforcement Learning from Human Feedback) democratizado para equipos pequeños con IDEs convencionales.**

Si hace tres semanas corregiste un módulo de OCR que cambió el formato de las fechas, y hoy le pides a la IA que arregle el módulo de pronóstico (forecast), AMK se asegura de que la IA "recuerde" la restricción del OCR y no la rompa. El dataset evolutivo se convierte en la memoria que el IDE no tiene nativamente.

## La Arquitectura de 3 Capas

El sistema se basa en tres capas interconectadas:

1. **Capa 1 — Interaction Memory:** Captura cada pregunta y respuesta del agente con su resultado (correcto, corregido, rechazado). Esto forma la base del Dataset Dorado.
2. **Capa 2 — Code Evolution Memory:** Captura cada cambio de código y su contexto: qué módulo cambió, por qué, qué estaba mal, cómo se corrigió y *qué otros módulos podrían verse afectados*.
3. **Capa 3 — Regression Intelligence:** Un análisis determinístico de dependencias. Cada vez que hay un cambio, cruza la información con la Capa 2 para ver si correcciones anteriores se ven afectadas, generando una alerta antes de que el IDE las rompa.

## ¿Por qué Green AI?

Entrenar LLMs masivos consume cantidades asombrosas de energía. AMK defiende la visión de **Green AI** creando "Golden Datasets" de alta calidad y dominio específico usados para entrenar **SLMs (Small Language Models)**. Estos SLMs son especializados, corren en dispositivos edge y reducen drásticamente el costo ambiental.

## Instalación

```bash
pip install evomem
```

## Inicio Rápido (Quickstart)

```python
from evomem import InteractionMemory, CodeEvolutionMemory, RegressionIntelligence

# 1. Inicializar rastreador (Capa 1)
memory = InteractionMemory(session_id="dev-session-001")

# 2. Registrar evento de evolución (Capa 2)
code_evo = CodeEvolutionMemory()
code_evo.track_evolution(
    original_code="def read_date(text): return text",
    improved_code="def read_date(text): return text.replace('-', '/')",
    reason="Arreglado el formato de fecha del OCR. Forecast depende de esto.",
    file_path="ocr_module.py",
    affected_modules=["forecast_module.py"]
)

# 3. Prevenir regresiones (Capa 3)
reg_intel = RegressionIntelligence()
alertas = reg_intel.check_regression_risk("forecast_module.py")
print("Alertas antes de modificar forecast:", alertas)
```

## Hoja de Ruta del Dataset (Roadmap)

1. **Piloto:** Captura en crudo.
2. **Producción:** Registros limpios con metadatos.
3. **Golden Dataset:** Pares rigurosamente verificados.
4. **SLM:** Modelos ligeros especializados.

## Cómo Contribuir
¡Agradecemos las contribuciones! Revisa [CONTRIBUTING.md](CONTRIBUTING.md).

## Créditos
- **Creador y Arquitecto**: Andrés Salazar Quintero
- **En Memoria De**: Eliana Arenas Cano ("La Mariposa")
