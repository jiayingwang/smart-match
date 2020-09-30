import unittest
import smart_match


class TestSimonWhite(unittest.TestCase):

    def setUp(self):
        smart_match.use('simon')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('abbcccdd', 'aaabccee'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('hello', 'hollow'), 0.7272727272727273)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('abbcccdd', 'aaabccee'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hollow'), 0.2727272727272727)

if __name__ == '__main__':
    unittest.main()