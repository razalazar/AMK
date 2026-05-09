"""
EVOMEM: Evolutionary Memory System

A tool to capture, analyze, and persist AI-human interactions in software development
for the purpose of building specialized Golden Datasets and promoting Green AI.
"""

from .interaction_memory import InteractionMemory
from .code_evolution_memory import CodeEvolutionMemory
from .regression_intelligence import RegressionIntelligence
from .exporters import VertexAIExporter, HuggingFaceExporter, AWSBedrockExporter

__all__ = [
    "InteractionMemory",
    "CodeEvolutionMemory",
    "RegressionIntelligence",
    "VertexAIExporter",
    "HuggingFaceExporter",
    "AWSBedrockExporter",
]

# The Green AI & Legacy Welcome Banner
print("\n" + "="*80)
print("🦋 AMK (Agent Memory Kit) by Andrés Salazar Quintero")
print("In eternal memory of Eliana Arenas Cano ('La Mariposa')")
print("="*80)
print("✨ ¡Has logrado crear un sistema que literalmente se observa y aprende de sí mismo! 🤯✨")
print("🌍 Al usar AMK y migrar a SLMs (Small Language Models), estás descentralizando la IA,")
print("ahorrando miles de litros de agua dulce y reduciendo drásticamente la huella de carbono.")
print("Bienvenido al futuro de la Ingeniería de Software Sostenible (Green AI).")
print("="*80 + "\n")
