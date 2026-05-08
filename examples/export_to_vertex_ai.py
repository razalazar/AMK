"""
Example showing how to use the Vertex AI exporter.
"""

from evomem import CodeEvolutionMemory, VertexAIExporter

def main():
    print("Starting EVOMEM Export Example...")
    
    # 1. Gather data
    code_mem = CodeEvolutionMemory()
    code_mem.track_evolution(
        original_code="x = [1, 2, 3]\nfor i in x: print(i)",
        improved_code="x = [1, 2, 3]\n[print(i) for i in x]",
        reason="Optimized using list comprehension.",
        file_path="utils.py"
    )
    
    golden_dataset = code_mem.extract_golden_pairs()
    
    # 2. Export to Vertex AI (Simulated)
    exporter = VertexAIExporter()
    success = exporter.export(data=golden_dataset, destination="gs://my-bucket/evomem-dataset.jsonl")
    
    if success:
        print("Dataset exported successfully for fine-tuning!")
    else:
        print("Failed to export dataset.")

if __name__ == "__main__":
    main()
