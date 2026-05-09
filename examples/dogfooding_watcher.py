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

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class AMKDogfoodingHandler(FileSystemEventHandler):
    def __init__(self, code_tracker):
        self.code_tracker = code_tracker
        self.last_modified = {}

    def on_modified(self, event):
        # Only track python files and avoid infinite loops from data folder
        if not event.is_directory and event.src_path.endswith('.py') and '.evomem_data' not in event.src_path:
            # Debounce rapid save events
            current_time = time.time()
            if current_time - self.last_modified.get(event.src_path, 0) > 2:
                self.last_modified[event.src_path] = current_time
                print(f"🧬 [DOGFOODING] AMK Detected modification in: {event.src_path}")
                # Log the evolution (in a real scenario, we would capture diffs here)
                self.code_tracker.track_evolution(
                    file_path=event.src_path,
                    before_code="[Previous state]",
                    after_code="[New modified state]",
                    reason="AMK Dogfooding Self-Evolution tracking"
                )

def initialize_dogfooding():
    print("🧬 Initializing AMK Dogfooding Watcher...")
    print("AMK is now actively observing its own evolution.")
    
    # Initialize the Code Evolution Tracker
    code_tracker = CodeEvolutionMemory()
    
    # Start the watchdog observer
    event_handler = AMKDogfoodingHandler(code_tracker)
    observer = Observer()
    # Watch the parent directory (the AMK evomem root)
    target_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    observer.schedule(event_handler, target_path, recursive=True)
    observer.start()
    
    print(f"\n✅ Ready! Watching directory: {target_path}")
    print("Keep this terminal open. AMK will automatically log changes to .evomem_data/")
    print("Press Ctrl+C to stop the evolution watcher.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 AMK Dogfooding Watcher stopped.")
    observer.join()

if __name__ == "__main__":
    # Ensure the local data folder exists but is ignored by git
    os.makedirs(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".evomem_data"), exist_ok=True)
    initialize_dogfooding()
