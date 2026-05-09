"""
Module for tracking code evolution and transitions across interactions.
"""

import json
import os
import time
import uuid
from typing import Dict, Any, List, Optional


class CodeEvolutionMemory:
    """
    Class designed to track code corrections and maintain dependency graphs.
    """

    def __init__(self, base_dir: str = "./memory_store"):
        self.base_dir = base_dir
        self.corrections_dir = os.path.join(base_dir, "code_evolution", "corrections")
        self.deps_dir = os.path.join(base_dir, "code_evolution", "dependencies")
        
        os.makedirs(self.corrections_dir, exist_ok=True)
        os.makedirs(self.deps_dir, exist_ok=True)

    def _append_jsonl(self, filepath: str, record: Dict[str, Any]):
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def log_correction(self, module_name: str, what_broke: str, root_cause: str, 
                       fix_applied: str, affected_modules: List[str], 
                       warning_for_ide: str, corrected_by: str = "system") -> str:
        """
        Records a code correction with full context.
        """
        record_id = str(uuid.uuid4())
        record = {
            "id": record_id,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "module": module_name,
            "what_broke": what_broke,
            "root_cause": root_cause,
            "fix_applied": fix_applied,
            "affected_modules": affected_modules,
            "warning_for_ide": warning_for_ide,
            "corrected_by": corrected_by
        }
        
        filepath = os.path.join(self.corrections_dir, "corrections_log.jsonl")
        self._append_jsonl(filepath, record)
        return record_id

    def update_dependencies(self, module_name: str, depends_on_list: List[str], depended_by_list: List[str]):
        """
        Updates the module dependency graph.
        """
        filepath = os.path.join(self.deps_dir, "module_dependencies.json")
        
        deps = {}
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                deps = json.load(f)
                
        deps[module_name] = {
            "depends_on": depends_on_list,
            "depended_by": depended_by_list
        }
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(deps, f, indent=4, ensure_ascii=False)
