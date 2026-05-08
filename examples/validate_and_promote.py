"""
Example showing how to extract 'Golden Pairs' for SLM fine-tuning
from the recorded code evolutions.
"""

from evomem import CodeEvolutionMemory

def main():
    print("Starting EVOMEM Validate and Promote Example...")
    
    # Create some dummy evolutions
    code_mem = CodeEvolutionMemory()
    code_mem.track_evolution(
        original_code="print('hello')",
        improved_code="import logging\nlogging.info('hello')",
        reason="Switched to standard logging framework.",
        file_path="main.py"
    )
    
    # Extract golden pairs
    golden_dataset = code_mem.extract_golden_pairs()
    
    print(f"Extracted {len(golden_dataset)} golden pairs.")
    for idx, pair in enumerate(golden_dataset):
        print(f"\n--- Pair {idx + 1} ---")
        print("PROMPT:")
        print(pair["prompt"])
        print("\nCOMPLETION:")
        print(pair["completion"])
        print("-------------------")

if __name__ == "__main__":
    main()
