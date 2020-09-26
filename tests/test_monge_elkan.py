import unittest
import smart_match

class TestLevenshtein(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('ME')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity(['Hello', 'world'], ['Hero', 'world']), 0.8)

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity(['Hello', 'world'], ['Hero', 'world']), 0.2)

class TestLevenshtein(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('ME', 'cos')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity(['Hello', 'world'], ['Hero', 'world']), 0.7834733547569204)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity(['Hello', 'world'], ['Hero', 'world']), 0.21652664524307963)

if __name__ == '__main__':
    unittest.main()