"""
Tests for the CodeEvolutionMemory class.
"""

import unittest
from evomem import CodeEvolutionMemory


class TestCodeEvolutionMemory(unittest.TestCase):
    def setUp(self):
        self.memory = CodeEvolutionMemory()

    def test_track_evolution(self):
        self.memory.track_evolution(
            original_code="pass",
            improved_code="return True",
            reason="Implemented return statement"
        )
        self.assertEqual(len(self.memory.get_all_evolutions()), 1)

    def test_extract_golden_pairs(self):
        self.memory.track_evolution(
            original_code="a = 1",
            improved_code="a = 2",
            reason="Fixed off-by-one"
        )
        pairs = self.memory.extract_golden_pairs()
        self.assertEqual(len(pairs), 1)
        self.assertIn("Fixed off-by-one", pairs[0]["prompt"])
        self.assertEqual(pairs[0]["completion"], "a = 2")

if __name__ == "__main__":
    unittest.main()
