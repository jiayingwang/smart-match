import unittest
import smart_match

class TestJaro(unittest.TestCase):
    def setUp(self):
        smart_match.use('jaro')
        
    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('ABC','CBA'), 0.5555555555555555)
        self.assertAlmostEqual(smart_match.similarity('CRATE','TRACE'), 0.7333333333333334)
        self.assertAlmostEqual(smart_match.similarity('DwAyNE','DuANE'), 0.8222222222222223)
        self.assertAlmostEqual(smart_match.similarity('AABABCAAAC', 'ABAACBAAAC'), 0.9333333333333332)
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.9444444444444443)
        
if __name__=='__main__':
    unittest.main()
