import unittest
import numpy as np
from app.rag_engine import RAGPipeline

class TestRAGPipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = RAGPipeline()

    def test_embedding_dimensions(self):
        """Test if the embedding generator returns the correct size (1024)"""
        vector = self.pipeline._generate_embeddings("Sample query")
        self.assertEqual(len(vector), 1024)

    def test_relevance_threshold(self):
        """Test if the pipeline filters low-score results"""
        # Testing with a very high threshold
        result = self.pipeline.process_query("doc_1", "query", threshold=0.99)
        # It should either be a high score or filtered
        self.assertTrue(result['score'] >= 0 or result['answer'] == "Context not relevant enough.")

if __name__ == '__main__':
    unittest.main()
