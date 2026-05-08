"""
Tests for the exporters.
"""

import unittest
from evomem import VertexAIExporter, HuggingFaceExporter, AWSBedrockExporter


class TestExporters(unittest.TestCase):
    def setUp(self):
        self.dummy_data = [{"prompt": "Fix this", "completion": "Fixed"}]

    def test_vertex_exporter(self):
        exporter = VertexAIExporter()
        result = exporter.export(self.dummy_data, "gs://test")
        self.assertTrue(result)

    def test_hf_exporter(self):
        exporter = HuggingFaceExporter()
        result = exporter.export(self.dummy_data, "test/repo")
        self.assertTrue(result)

    def test_aws_exporter(self):
        exporter = AWSBedrockExporter()
        result = exporter.export(self.dummy_data, "s3://test")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
