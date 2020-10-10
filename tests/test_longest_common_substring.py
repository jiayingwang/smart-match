import unittest
import smart_match

class TestLongestCommonSubstring(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('LCST')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'low'), 0.4)

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'low'), 0.6)
    
    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'low'), 4)
    
    def test_score(self):
        self.assertEqual(smart_match.score('hello', 'low'), 2)

if __name__ == '__main__':
    unittest.main()
