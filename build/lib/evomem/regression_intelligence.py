"""
Module for Regression Intelligence: Deterministic dependency analysis.
"""

import json
import os
from typing import List, Dict, Any


class RegressionIntelligence:
    """
    Analyzes code evolutions to prevent IDE context regression and assess system maturity.
    """

    def __init__(self, base_dir: str = "./memory_store"):
        self.base_dir = base_dir
        self.corrections_path = os.path.join(base_dir, "code_evolution", "corrections", "corrections_log.jsonl")
        self.analysis_dir = os.path.join(base_dir, "analysis")
        os.makedirs(self.analysis_dir, exist_ok=True)

    def _read_corrections(self) -> List[Dict[str, Any]]:
        corrections = []
        if os.path.exists(self.corrections_path):
            with open(self.corrections_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        corrections.append(json.loads(line))
        return corrections

    def check_regression_risk(self, module_to_modify: str) -> Dict[str, Any]:
        """
        Queries past corrections to find regression risks for a module.
        """
        corrections = self._read_corrections()
        risks = []
        affected_tests = []
        
        for cor in corrections:
            if module_to_modify in cor.get("affected_modules", []) or module_to_modify == cor.get("module"):
                risks.append({
                    "date": cor.get("timestamp"),
                    "warning": cor.get("warning_for_ide", "Unspecified warning.")
                })
                # Simulated heuristic for affected tests
                affected_tests.append(f"tests/test_{os.path.basename(module_to_modify)}")
                
        return {
            "module": module_to_modify,
            "regression_risks": risks,
            "affected_tests": list(set(affected_tests))
        }

    def analyze_error_patterns(self) -> Dict[str, Any]:
        """
        Analyzes frequent points of failure.
        """
        # Simulation
        report = {
            "most_frequent_modules": ["src/api_gateway.py", "src/auth.py"],
            "common_errors": ["Type mismatch", "Missing validation"],
            "avg_time_to_fix_mins": 45
        }
        with open(os.path.join(self.analysis_dir, "quality_report.json"), "w") as f:
            json.dump(report, f, indent=4)
        return report

    def generate_session_context(self, use_case: str, output_dir: str = ".claude") -> str:
        """
        Generates a markdown file to be injected into the IDE at session start.
        """
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, f"session_context_{use_case}.md")
        
        corrections = self._read_corrections()
        latest = corrections[-5:] if len(corrections) >= 5 else corrections
        
        score = self.compute_evolution_score()
        
        content = f"# Session Context: {use_case}\n\n"
        content += f"**Evolution Score**: {score['score']}/100 ({score['status']})\n\n"
        content += "## Recent Critical Corrections\n"
        for cor in latest:
            content += f"- **{cor.get('module')}** ({cor.get('timestamp')}): {cor.get('what_broke')} -> {cor.get('fix_applied')}\n"
            content += f"  *Warning*: {cor.get('warning_for_ide')}\n\n"
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
        return filepath

    def compute_evolution_score(self) -> Dict[str, Any]:
        """
        Calculates maturity score from 0 to 100.
        """
        # Simulated logic
        score = 65 
        status = "production_stable"
        if score < 20: status = "prototype"
        elif score <= 50: status = "validating"
        elif score > 80: status = "ready_for_slm"
        
        report = {"score": score, "status": status}
        with open(os.path.join(self.analysis_dir, "slm_readiness.json"), "w") as f:
            json.dump(report, f, indent=4)
        return report
