"""
Example showing how to capture basic interactions and code evolution
using EVOMEM.
"""

from evomem import InteractionMemory, CodeEvolutionMemory

def main():
    print("Starting EVOMEM Basic Capture Example...")
    
    # 1. Initialize interaction memory
    mem = InteractionMemory(session_id="example-session-001")
    mem.log_interaction("user", "Can you fix the bug in calculate_total?")
    mem.log_interaction("assistant", "Sure, I found that taxes were not included. Here is the updated code.")
    
    # 2. Track the code evolution
    code_mem = CodeEvolutionMemory()
    original = "def calculate_total(price):\n    return price"
    improved = "def calculate_total(price, tax=0.05):\n    return price * (1 + tax)"
    
    code_mem.track_evolution(
        original_code=original,
        improved_code=improved,
        reason="Added tax calculation parameter to fix pricing bug.",
        file_path="pricing.py"
    )
    
    # 3. Save the session memory
    save_path = mem.save_session()
    print(f"Session saved to {save_path}")
    print("Evolutions captured:")
    print(code_mem.get_all_evolutions())

if __name__ == "__main__":
    main()
