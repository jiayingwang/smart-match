import unittest
import smart_match

class TestGeneralizedJaccard(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('gjac')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'helo'), 0.8)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'helo'), 0.2)

if __name__ == '__main__':
    unittest.main()