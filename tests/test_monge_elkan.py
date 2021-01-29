import unittest
import smart_match

class TestMongeElkan(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('Monge Elkan')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity(['Hello', 'world'], ['Hero', 'world']), 0.8)
        smart_match.set_params(method='Cosine')
        self.assertAlmostEqual(smart_match.similarity(['Hello', 'world'], ['Hero', 'world']), 0.7834733547569204)
        smart_match.set_params(method='Exact', level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'),  0.5)
        self.assertAlmostEqual(smart_match.similarity('test', 'test string2'),   0.7071067811865476)
        self.assertAlmostEqual(smart_match.similarity('', 'test string2'),   0.0)
        self.assertAlmostEqual(smart_match.similarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'),   0.75)
        self.assertAlmostEqual(smart_match.similarity('a b c d', 'a b c e'),   0.75)
        self.assertAlmostEqual(smart_match.similarity('Sam J Chapman', 'Samuel John Chapman'),    0.3333333333333333)


    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity(['Hello', 'world'], ['Hero', 'world']), 0.2)
        smart_match.set_params(method='Cosine')
        self.assertAlmostEqual(smart_match.dissimilarity(['Hello', 'world'], ['Hero', 'world']), 0.21652664524307963)
        

if __name__ == '__main__':
    unittest.main()