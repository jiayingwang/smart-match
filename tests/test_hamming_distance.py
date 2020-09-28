import unittest
import smart_match

class TestHammingDistance(unittest.TestCase):
    def setUp(self):
        smart_match.use('HD')
    def test_hammingdistance1(self):
        self.assertEqual(smart_match.distance('12211','11111'),2)
    def test_hammingdistance2(self):
        self.assertEqual(smart_match.distance('hello','heool'),3)
        
if __name__=='__main__':
    unittest.main()
