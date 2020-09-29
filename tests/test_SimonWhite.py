import unittest
import smart_match


class TestDiceSimilarity(unittest.TestCase):

    def setUp(self):
        smart_match.use('simonwhite')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('abbcccdd', 'aaabccee'), 0.5)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('abbcccdd', 'aaabccee'), 0.5)

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'hollow'), 0.7273)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hollow'), 0.2727)


if __name__ == '__main__':
    unittest.main()