import unittest
import smart_match

class TestHammingDistance(unittest.TestCase):
    def setUp(self):
        smart_match.use('HD')
    
    def test_distance(self):
        self.assertEqual(smart_match.distance('12211','11111'), 2)
        self.assertEqual(smart_match.distance('hello','heool'), 3)
        
    def test_similarity(self):
        self.assertEqual(smart_match.similarity('12211','11111'), 0.6)
        self.assertEqual(smart_match.similarity('hello','heool'), 0.4)
        
if __name__=='__main__':
    unittest.main()
