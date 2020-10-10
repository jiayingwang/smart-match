import unittest
import smart_match

class TestOverlapCoefficient(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('OC')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'hero'), 0.75)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'hero'), 0.25)
        self.assertEqual(smart_match.dissimilarity('hello', 'ehllo'), 0)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.5)

if __name__ == '__main__':
    unittest.main()
