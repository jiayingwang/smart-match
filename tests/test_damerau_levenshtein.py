import unittest
import smart_match

class TestDamerauLevenshtein(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('DL')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'hero'), 0.6)

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'hero'), 0.4)

    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'hero'), 2)
        self.assertEqual(smart_match.distance('hello', 'ehllo'), 1)

if __name__ == '__main__':
    unittest.main()