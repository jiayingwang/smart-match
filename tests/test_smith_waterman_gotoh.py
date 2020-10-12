import unittest
import smart_match

class TestSmithWatermanGotoh(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('SWG')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('GGTTGACTA', 'TGTTACGG'), 0.5625)
        smart_match.set_params(gap=-2, match=3, mismatch=-3)
        self.assertAlmostEqual(smart_match.similarity('GGTTGACTA', 'TGTTACGG'), 0.5416666666666666)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('GGTTGACTA', 'TGTTACGG'), 0.4375)
        smart_match.set_params(gap=-2, match=3, mismatch=-3)
        self.assertAlmostEqual(smart_match.dissimilarity('GGTTGACTA', 'TGTTACGG'), 0.45833333333333337)

if __name__ == '__main__':
    unittest.main()
