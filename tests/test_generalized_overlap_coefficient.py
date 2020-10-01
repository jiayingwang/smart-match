import unittest
import smart_match

class TestOverlapCoefficient(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('GOC')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'hero'), 0.75)

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'hero'), 0.25)
        self.assertEqual(smart_match.dissimilarity('hello', 'ehllo'), 0)        

if __name__ == '__main__':
    unittest.main()
