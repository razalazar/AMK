"""
Tests for the InteractionMemory class.
"""

import os
import shutil
import unittest
import json
from evomem import InteractionMemory


class TestInteractionMemory(unittest.TestCase):
    def setUp(self):
        self.storage_dir = "./test_amk_datasets"
        self.session_id = "test-session-123"
        self.memory = InteractionMemory(base_dir=self.storage_dir)

    def test_directory_creation(self):
        self.assertTrue(os.path.exists(os.path.join(self.storage_dir, "01_piloto")))
        self.assertTrue(os.path.exists(os.path.join(self.storage_dir, "02_produccion")))
        self.assertTrue(os.path.exists(os.path.join(self.storage_dir, "03_golden")))

    def test_log_interaction(self):
        interaction_id = self.memory.log_interaction(
            question="What is AMK?",
            answer="Agent Memory Kit",
            model_used="gemini-1.5-pro",
            tokens_used=150,
            environment="sandbox",
            session_id=self.session_id
        )
        self.assertIsNotNone(interaction_id)
        
        filepath = os.path.join(self.storage_dir, "01_piloto", f"{self.session_id}_piloto.jsonl")
        self.assertTrue(os.path.exists(filepath))
        
        with open(filepath, "r") as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 1)
            record = json.loads(lines[0])
            self.assertEqual(record["id"], interaction_id)
            self.assertEqual(record["question"], "What is AMK?")

    def tearDown(self):
        if os.path.exists(self.storage_dir):
            shutil.rmtree(self.storage_dir)

if __name__ == "__main__":
    unittest.main()
