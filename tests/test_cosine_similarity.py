import unittest
import smart_match

class TestCosineSimilarity(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('cos')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'hero'), 0.5669467095138409)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hero'), 0.43305329048615915)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.5)

if __name__ == '__main__':
    unittest.main()