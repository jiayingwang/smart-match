import unittest
import smart_match


class TestSimonWhite(unittest.TestCase):

    def setUp(self):
        smart_match.use('simon')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('abbcccdd', 'aaabccee'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('hello', 'hollow'), 0.7272727272727273)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)
        smart_match.set_params(level=2)
        self.assertAlmostEqual(smart_match.similarity('test', 'test string2'), 0.5)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('abbcccdd', 'aaabccee'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hollow'), 0.2727272727272727)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.5)

if __name__ == '__main__':
    unittest.main()