import unittest
import smart_match

class TestGeneralizedJaccard(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('gjac')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'helo'), 0.8)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.3333333333333333)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'helo'), 0.2)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.6666666666666667)

if __name__ == '__main__':
    unittest.main()