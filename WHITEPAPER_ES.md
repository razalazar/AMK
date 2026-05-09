# AMK: El Whitepaper de Agent Memory Kit
**Un Framework para Memoria Evolutiva, Preservación de Contexto y Green AI**

## 1. Resumen y Legado
En la ingeniería de software moderna, los asistentes de Inteligencia Artificial (LLMs) sufren de una severa "Regresión de Contexto": arreglan un módulo pero rompen otro porque carecen de memoria institucional entre sesiones. **AMK (Agent Memory Kit)**, impulsado por el motor EVOMEM, resuelve esto actuando como una bóveda de memoria local y evolutiva.

AMK es una arquitectura de código abierto construida como un legado profundamente humano en memoria de Eliana Arenas Cano ("La Mariposa"). Demuestra que la IA puede ser especializada localmente, ahorrando no solo horas de desarrollo, sino también reduciendo drásticamente la enorme huella de agua y carbono de los centros de datos globales.

---

## 2. El Problema Central: Regresión de Contexto en el IDE
Cuando una IA arregla el "Módulo A" hoy, y tres semanas después le pides que modifique el "Módulo B", la IA ya ha olvidado las restricciones del Módulo A. Comienza desde cero. Esto obliga a los desarrolladores a escribir repetidamente enormes *prompts* para recordarle a la IA decisiones pasadas, quemando millones de tokens y desperdiciando energía.

---

## 3. La Arquitectura EVOMEM de 3 Capas
AMK resuelve esto mediante una estructura determinista de 3 capas:
1. **Memoria de Interacción:** Registra los *prompts* exactos y sus resultados.
2. **Memoria de Evolución de Código:** Captura el "Antes", el "Después" y el "Por Qué" de un cambio de código, rastreando qué otros archivos dependen de él.
3. **Inteligencia de Regresión:** Una alerta temprana que advierte al desarrollador *antes* de que una IA modifique un archivo si esa modificación corre el riesgo de romper una regla de memoria establecida previamente.

---

## 4. La Fábrica de IA Agnóstica (Democratización de SLMs)
Los LLMs gigantes son excelentes "maestros" pero son insostenibles para la producción diaria. AMK actúa como un **Embudo Sandbox**:
* **Fase A (Presente):** Usas un LLM gigante en tu IDE. AMK captura las correcciones exitosas.
* **Fase B (Embudo):** AMK inyecta contexto hacia atrás para ahorrar tokens hoy, mientras simultáneamente cura un "Dataset de Oro" (Golden Dataset).
* **Fase C (Futuro):** Usas el Dataset de Oro para entrenar un Modelo de Lenguaje Pequeño (SLM). El SLM se convierte en un experto de dominio soberano e hiper-rápido que corre localmente con costo de API cero.

---

## 5. La Tesis de Green AI (Agua y Carbono)
Cada 10 a 50 consultas a un LLM masivo consumen una botella de 500ml de agua dulce para enfriar los servidores, y emiten aproximadamente 4.3 gramos de CO2 por consulta. Al darle memoria local al IDE, AMK previene miles de consultas redundantes. Migrar a SLMs descentraliza por completo el costo de computación, alineando la ingeniería de software con los objetivos críticos ESG (Ambientales, Sociales y de Gobernanza).

---

## 6. La Paradoja de Oro: Auto-Evolución (Dogfooding)
¿Puede una IA evolucionar su propio motor de memoria sin corromper la semilla original? Sí. A través de una técnica llamada *Dogfooding* y *Aislamiento de Entornos*, los desarrolladores pueden correr AMK de fondo como observador mientras modifican el propio código de AMK. Los registros locales capturan la evolución de forma segura. Una vez validado, el nuevo ADN se empuja al repositorio global.

---

## 7. Seguridad y Gobernanza Open Source
Para garantizar la confianza corporativa, AMK garantiza:
* **Cero-Telemetría:** Opera localmente. No envía código propietario a APIs externas.
* **Auditoría Air-Gapped:** Funciona perfectamente sin internet, demostrando matemáticamente que no se roban datos.
* **Licencia MIT:** El código es 100% transparente y auditable por equipos de ciberseguridad.
