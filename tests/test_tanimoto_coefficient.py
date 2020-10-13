import unittest
import smart_match

class TestTanimotoCoefficient(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('TC')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('test', 'test string1'), 0.5773502691896257)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test', 'test string2'), 0.7071067811865475)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('test', 'test string1'), 0.42264973081037427)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test', 'test string2'), 0.29289321881345254)

if __name__ == '__main__':
    unittest.main()
