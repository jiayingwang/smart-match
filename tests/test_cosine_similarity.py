import unittest
import smart_match

class TestCosineSimilarity(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('COS')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'hero'), 0.5669467095138409)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hero'), 0.43305329048615915)

if __name__ == '__main__':
    unittest.main()