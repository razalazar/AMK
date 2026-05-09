"""
Module containing the core InteractionMemory class.
"""

import json
import os
import time
import uuid
from typing import Dict, Any, List, Optional


class InteractionMemory:
    """
    Core class to track AI-human interactions.
    Manages the lifecycle of datasets from pilot to golden.
    """

    def __init__(self, base_dir: str = "./amk_datasets"):
        """
        Initialize the InteractionMemory with a 3-tier structure.

        Args:
            base_dir (str): Root directory for memory storage.
        """
        self.base_dir = base_dir
        self.dirs = {
            "piloto": os.path.join(base_dir, "01_piloto"),
            "produccion": os.path.join(base_dir, "02_produccion"),
            "golden": os.path.join(base_dir, "03_golden")
        }
        
        for path in self.dirs.values():
            os.makedirs(path, exist_ok=True)

    def _append_jsonl(self, filepath: str, record: Dict[str, Any]):
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def log_interaction(self, question: str, answer: str, model_used: str, 
                        tokens_used: int, environment: str, session_id: str,
                        metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Logs a single interaction turn to the pilot dataset.
        """
        interaction_id = str(uuid.uuid4())
        record = {
            "id": interaction_id,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "session_id": session_id,
            "environment": environment,
            "question": question,
            "answer": answer,
            "model_used": model_used,
            "tokens_used": tokens_used,
            "validation_status": "pending"
        }
        if metadata:
            record.update(metadata)
            
        filepath = os.path.join(self.dirs["piloto"], f"{session_id}_piloto.jsonl")
        self._append_jsonl(filepath, record)
        return interaction_id

    def validate(self, interaction_id: str, session_id: str, leader: str, 
                 validation_type: str, correction: Optional[str] = None, 
                 is_perfect: bool = False, response_time_sec: float = 0.0) -> None:
        """
        Validates an interaction and promotes it across the dataset tiers.
        validation_type: "correct" | "corrected" | "rejected"
        """
        # In a real app, you would read, find the ID, and move it. 
        # For this neutral framework, we simulate the promotion logic.
        record = {
            "id": interaction_id,
            "validated_by": leader,
            "validation_type": validation_type,
            "correction_applied": correction,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }
        
        if validation_type == "corrected":
            # Save correction in production
            filepath = os.path.join(self.dirs["produccion"], f"{session_id}_prod.jsonl")
            self._append_jsonl(filepath, record)
            
        elif validation_type == "correct":
            # Promote to production
            prod_filepath = os.path.join(self.dirs["produccion"], f"{session_id}_prod.jsonl")
            self._append_jsonl(prod_filepath, record)
            
            # Check Golden conditions
            if is_perfect and response_time_sec < 2.0:
                golden_filepath = os.path.join(self.dirs["golden"], f"{session_id}_golden.jsonl")
                self._append_jsonl(golden_filepath, record)
                
        elif validation_type == "rejected":
            # Just tag as rejected in production for negative learning
            filepath = os.path.join(self.dirs["produccion"], f"{session_id}_prod.jsonl")
            self._append_jsonl(filepath, record)

    def get_slm_readiness(self) -> Dict[str, Any]:
        """
        Calculates if the dataset is ready for fine-tuning.
        """
        # Simulation of file counting
        return {
            "piloto_count": 150,
            "produccion_count": 80,
            "golden_count": 25,
            "quality_score": 75.5,
            "mvp_threshold": 1000,
            "robust_threshold": 5000,
            "estimated_days_to_mvp": 30,
            "ready_for_finetuning": False,
            "recommendation": "Continue capturing daily interactions. Golden dataset is below MVP threshold."
        }
