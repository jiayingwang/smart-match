import unittest
import smart_match

class TestLevenshtein(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('SWG')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('GGTTGACTA', 'TGTTACGG'), 0.3125)
        smart_match.set_params(gap=-2, match=3, mismatch=-3)
        self.assertAlmostEqual(smart_match.similarity('GGTTGACTA', 'TGTTACGG'), 0.2916666666666667)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('GGTTGACTA', 'TGTTACGG'), 0.6875)
        smart_match.set_params(gap=-2, match=3, mismatch=-3)
        self.assertAlmostEqual(smart_match.dissimilarity('GGTTGACTA', 'TGTTACGG'), 0.7083333333333333)

if __name__ == '__main__':
    unittest.main()