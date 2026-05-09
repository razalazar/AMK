"""
Tests for the CodeEvolutionMemory class.
"""

import os
import shutil
import unittest
import json
from evomem import CodeEvolutionMemory


class TestCodeEvolutionMemory(unittest.TestCase):
    def setUp(self):
        self.storage_dir = "./test_amk_datasets"
        self.memory = CodeEvolutionMemory(base_dir=self.storage_dir)

    def test_directory_creation(self):
        self.assertTrue(os.path.exists(os.path.join(self.storage_dir, "04_code_evolution", "corrections")))
        self.assertTrue(os.path.exists(os.path.join(self.storage_dir, "04_code_evolution", "dependencies")))

    def test_log_correction(self):
        record_id = self.memory.log_correction(
            module_name="src/api.py",
            what_broke="Type mismatch on invoice validation",
            root_cause="Missing strict parsing",
            fix_applied="Added pydantic validation",
            affected_modules=["src/billing.py"],
            warning_for_ide="Ensure billing receives strictly typed data"
        )
        self.assertIsNotNone(record_id)
        
        filepath = os.path.join(self.storage_dir, "04_code_evolution", "corrections", "corrections_log.jsonl")
        self.assertTrue(os.path.exists(filepath))
        
        with open(filepath, "r") as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 1)
            record = json.loads(lines[0])
            self.assertEqual(record["id"], record_id)
            self.assertEqual(record["module"], "src/api.py")

    def tearDown(self):
        if os.path.exists(self.storage_dir):
            shutil.rmtree(self.storage_dir)

if __name__ == "__main__":
    unittest.main()
