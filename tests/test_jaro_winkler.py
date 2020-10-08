import unittest
import smart_match

class TestJaroWinkler(unittest.TestCase):
    def setUp(self):
        smart_match.use('JW')
        
    def test_similarity1(self):
        self.assertAlmostEqual(smart_match.similarity('DwAyNE', 'DuANE'), 0.84)
        self.assertAlmostEqual(smart_match.similarity('TRATE', 'TRACE'), 0.9066666666666667)
        self.assertAlmostEqual(smart_match.similarity("test string1", "test string2"), 0.9666666666666666)
        
if __name__=='__main__':
    unittest.main()
