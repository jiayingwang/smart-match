import unittest
import smart_match

class TestOverlapCoefficient(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('OC')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'hero'), 0.75)

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'hero'), 0.25)

    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'hero'), 0.25)
        self.assertEqual(smart_match.distance('hello', 'ehllo'), 1-0.8)

if __name__ == '__main__':
    unittest.main()
