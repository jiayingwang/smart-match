import unittest
import smart_match

class TestHammingDistance(unittest.TestCase):
    def setUp(self):
        smart_match.use('HD')
    
    def test_distance(self):
        self.assertEqual(smart_match.distance('12211','11111'), 2)
        self.assertEqual(smart_match.distance('hello','heool'), 3)
        self.assertEqual(smart_match.distance('aaabbb','aaaaaa'), 3)
        self.assertEqual(smart_match.distance('abcdxy','abcexy'), 1)
        self.assertEqual(smart_match.distance('abcdxy','abefxy'), 2)
        self.assertEqual(smart_match.distance('',''), 0)
        self.assertEqual(smart_match.distance(("a", "b", "c", "d"),("a", "b", "c", "e")), 1)
        self.assertEqual(smart_match.distance(("a", "b", "c", "d"),("a", "b", "e", "f")), 2)
        self.assertEqual(smart_match.distance(("a", "b", "c", None),("a", "b", "e", "f")), 2)

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('12211','11111'), 0.6)
        self.assertEqual(smart_match.similarity('hello','heool'), 0.4)
        self.assertEqual(smart_match.similarity('aaabbb', 'aaaaaa'), 0.5)
        self.assertEqual(smart_match.similarity('abcdxy', 'abcexy'), 0.8333333333333334)
        self.assertEqual(smart_match.similarity('abcdxy', 'abefxy'), 0.6666666666666667)
        self.assertEqual(smart_match.similarity(("a", "b", "c", "d"), ("a", "b", "c", "e")),  0.75)
        self.assertEqual(smart_match.similarity(("a", "b", "c", "d"), ("a", "b", "e", "f")),  0.5)
        self.assertEqual(smart_match.similarity('', ''),  1)
        self.assertEqual(smart_match.similarity(("a", "b", "c", None), ("a", "b", "e", "f")),  0.5)

if __name__=='__main__':
    unittest.main()
