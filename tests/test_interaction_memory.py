"""
Tests for the InteractionMemory class.
"""

import os
import unittest
from evomem import InteractionMemory


class TestInteractionMemory(unittest.TestCase):
    def setUp(self):
        self.session_id = "test-session-123"
        self.storage_dir = "./test_memory_store"
        self.memory = InteractionMemory(self.session_id, self.storage_dir)

    def test_log_interaction(self):
        self.memory.log_interaction("user", "Hello EVOMEM")
        self.assertEqual(len(self.memory.interactions), 1)
        self.assertEqual(self.memory.interactions[0]["role"], "user")
        self.assertEqual(self.memory.interactions[0]["content"], "Hello EVOMEM")

    def test_save_and_load(self):
        self.memory.log_interaction("user", "Save this")
        filepath = self.memory.save_session()
        self.assertTrue(os.path.exists(filepath))
        
        # Load into a new instance
        new_memory = InteractionMemory("new-id", self.storage_dir)
        new_memory.load_session(filepath)
        self.assertEqual(new_memory.session_id, self.session_id)
        self.assertEqual(len(new_memory.interactions), 1)
        
        # Cleanup
        os.remove(filepath)
        os.rmdir(self.storage_dir)

if __name__ == "__main__":
    unittest.main()
