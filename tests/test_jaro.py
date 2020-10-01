import unittest
import smart_match

class TestJaro(unittest.TestCase):
    def setUp(self):
        smart_match.use('jaro')
        
    def test_jaro_similarity1(self):
        self.assertAlmostEqual(smart_match.similarity('ABC','CBA'), 0.5555555555555555)
        self.assertAlmostEqual(smart_match.similarity('CRATE','TRACE'), 0.7333333333333334)
        self.assertAlmostEqual(smart_match.similarity('CRATE','TRACE'), 0.7333333333333334)
        self.assertAlmostEqual(smart_match.similarity('AABABCAAAC', 'ABAACBAAAC'), 0.9333333333333332)
        
if __name__=='__main__':
    unittest.main()
