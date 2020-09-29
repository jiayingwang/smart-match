import unittest
import smart_match

class TestJaroWinkler(unittest.TestCase):
    def setUp(self):
        smart_match.use('JW')
        
    def test_jaro_sinkler_similarity1(self):
        self.assertAlmostEqual(smart_match.similarity('DwAyNE', 'DuANE'), 0.84)
        self.assertAlmostEqual(smart_match.similarity('TRATE', 'TRACE'), 0.9066666666666667)
        
if __name__=='__main__':
    unittest.main()
