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
print("In eternal memory of Eliana Arenas Cano ('La Mariposa') y en amor a sus Amy & Kori")
print("="*80)
print("✨ ¡Has creado un sistema que literalmente se observa y aprende de sí mismo!")
print("✨ You have created a system that literally observes and learns from itself!")
print("\n🌍 Green AI & Sovereign SLMs:")
print("   - Descentralizas la IA / Decentralizing AI")
print("   - Ahorras miles de litros de agua y CO2 / Saving thousands of liters of water & CO2")
print("="*80 + "\n")
