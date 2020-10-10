import unittest
import smart_match

class TestNeedlemanWunch(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('NW')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.9583333333333334)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.similarity('GATTACA', 'GCATGCU'), 0.5)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.04166666666666663)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.dissimilarity('GATTACA', 'GCATGCU'), 0.5)
        
    def test_score(self):
        self.assertEqual(smart_match.score('test string1', 'test string2'), -1)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertEqual(smart_match.score('GATTACA', 'GCATGCU'), 0)

if __name__ == '__main__':
    unittest.main()
