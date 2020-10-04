import unittest
import smart_match

class TestEuclideanDistance(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('ED')

    def test_similarity(self):
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hero'), 0.34921514788478913)

    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'hero'), 2.23606797749979)
        self.assertEqual(smart_match.distance('hello', 'ehllo'), 0)

if __name__ == '__main__':
    unittest.main()