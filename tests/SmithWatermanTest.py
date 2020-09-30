import unittest
import smart_match


class SmithWatermanTest(unittest.TestCase):

    def setUp(self):
        smart_match.use('SWG')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('Sam Chapman','S Chapman'), 0.8888888888888888)
        smart_match.set_params(GapValue=-5, matchValue=5, misMatchValue =-3)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sealed'), 0.8333333333333334)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('Sam Chapman','S Chapman'), 0.11111111111111116)
        smart_match.set_params(GapValue=-5, matchValue=5, misMatchValue =-3)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Sealed'), 0.16666666666666663)


if __name__ == '__main__':
    unittest.main()