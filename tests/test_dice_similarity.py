import unittest
import smart_match

class TestDiceSimilarity(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('dice')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'hero'), 0.75)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hero'), 0.25)

if __name__ == '__main__':
    unittest.main()