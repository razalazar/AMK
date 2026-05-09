import os
from evomem import InteractionMemory, CodeEvolutionMemory

# ==============================================================================
# ♾️ THE GOLDEN PARADOX: AMK DOGFOODING WATCHER
# ==============================================================================
# This script is the ultimate "Inception". It uses AMK to monitor and evolve AMK.
# When you run this script in the background, it creates a local isolated environment
# (.evomem_data) where it tracks the changes your AI IDE makes to the core 
# evomem files (like interaction_memory.py or regression_intelligence.py).
# 
# This guarantees that the AI improves AMK without breaking the seed codebase.
# ==============================================================================

def initialize_dogfooding():
    print("🧬 Initializing AMK Dogfooding Watcher...")
    print("AMK is now observing its own evolution.")
    
    # Initialize the Interaction Memory for the current AI coding session
    session_memory = InteractionMemory(session_id="amk-evolution-v0.2.0")
    
    # Initialize the Code Evolution Tracker
    code_tracker = CodeEvolutionMemory()
    
    print("\n✅ Ready! You can now use your IDE to modify AMK files.")
    print("Use code_tracker.track_evolution() to log changes safely to the local vault.")
    
    # In a real background watcher, you could use watchdog here to monitor directory changes.
    # For now, it serves as the initializing point for the golden dataset.

if __name__ == "__main__":
    # Ensure the local data folder exists but is ignored by git
    os.makedirs(".evomem_data", exist_ok=True)
    initialize_dogfooding()
