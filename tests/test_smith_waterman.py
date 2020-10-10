import unittest
import smart_match

class TestSmithWaterman(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('SW')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Web Application Development With PHP'), 0.8666666666666667)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications', 'Web Application Development With PHP'), 0.1333333333333333)
        
    def test_score(self):
        self.assertEqual(smart_match.score('Web Aplications', 'Web Application Development With PHP'), 65)

if __name__ == '__main__':
    unittest.main()
