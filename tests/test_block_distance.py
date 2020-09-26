import unittest
import smart_match

class TestBlockDistance(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('BD')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'hero'), 0.6666666666666667)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hero'), 0.3333333333333333)

    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'hero'), 3)
        self.assertEqual(smart_match.distance('hello', 'ehllo'), 0)

if __name__ == '__main__':
    unittest.main()