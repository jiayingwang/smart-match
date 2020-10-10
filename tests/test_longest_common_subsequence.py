import unittest
import smart_match

class TestLongestCommonSubsequence(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('LCSQ')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'hill'), 0.6)

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'hill'), 0.4)
    
    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'hill'), 3)
    
    def test_score(self):
        self.assertEqual(smart_match.score('hello', 'hill'), 3)

if __name__ == '__main__':
    unittest.main()
