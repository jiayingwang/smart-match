import unittest
import smart_match

class TestJaccard(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('jac')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'helo'), 1)
        self.assertAlmostEqual(smart_match.similarity('hello', 'hero'), 0.6)
        self.assertAlmostEqual(smart_match.similarity('hello world', 'hello world hello world'), 1)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'helo'), 0)

if __name__ == '__main__':
    unittest.main()