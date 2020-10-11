import unittest
import smart_match


class TestBlockDistance(unittest.TestCase):

    def setUp(self):
        smart_match.use('BD')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'hero'), 0.6666666666666667)
        self.assertAlmostEqual(smart_match.similarity('hello', 'ehllo'), 1)

        self.assertAlmostEqual(smart_match.similarity("Healed", "Sealed"), 0.8333333333333334)
        self.assertAlmostEqual(smart_match.similarity("Healed", "Healthy"), 0.6153846153846154)
        self.assertAlmostEqual(smart_match.similarity("Healed", "Heard"), 0.7272727272727272)
        self.assertAlmostEqual(smart_match.similarity("Healed", "Herded"), 0.6666666666666666)
        self.assertAlmostEqual(smart_match.similarity("Healed", "Help"), 0.6)
        self.assertAlmostEqual(smart_match.similarity("Healed", "Sold"), 0.4)
        self.assertAlmostEqual(smart_match.similarity("Healed", "Help"), 0.6)

        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string1'), 1)
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.similarity("test", "test string2"), 0.6666666666666667)
        self.assertAlmostEqual(smart_match.similarity("", "test string2"), 0)

        self.assertAlmostEqual(smart_match.similarity("aaa bbb ccc ddd", "aaa bbb ccc eee"), 0.75)
        self.assertAlmostEqual(smart_match.similarity("aaa bbb", "aaa aaa"), 0.5)
        self.assertAlmostEqual(smart_match.similarity("aaa", "aaa aaa"), 0.6666666666666667)

        self.assertAlmostEqual(smart_match.similarity("a b c d", "a b c e"), 0.7500)
        self.assertAlmostEqual(smart_match.similarity("a b c d", "a b e f"), 0.5000)
        self.assertAlmostEqual(smart_match.similarity("a b c", "a b c e f g"), 0.6666666666666667)
        self.assertAlmostEqual(smart_match.similarity("a b b c c", "a b c e f g"), 0.5454545454545454)

        smart_match.set_params(level='char')
        self.assertAlmostEqual(smart_match.similarity(["test", ""], ["test", "string2"]), 0.5)
        self.assertAlmostEqual(smart_match.similarity([], ["test", "string2"]), 0.0)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hero'), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'ehllo'), 0)

        self.assertAlmostEqual(smart_match.dissimilarity("Healed", "Sealed"), 0.16666666666666666)
        self.assertAlmostEqual(smart_match.dissimilarity("Healed", "Healthy"), 0.38461538461538464)
        self.assertAlmostEqual(smart_match.dissimilarity("Healed", "Heard"), 0.2727272727272727)
        self.assertAlmostEqual(smart_match.dissimilarity("Healed", "Herded"), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.dissimilarity("Healed", "Help"), 0.4)
        self.assertAlmostEqual(smart_match.dissimilarity("Healed", "Sold"), 0.6)
        self.assertAlmostEqual(smart_match.dissimilarity("Healed", "Help"), 0.4)

        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string1'), 0.0000)
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity("test", "test string2"), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.dissimilarity("", "test string2"), 1)

        self.assertAlmostEqual(smart_match.dissimilarity("aaa bbb ccc ddd", "aaa bbb ccc eee"), 0.25)
        self.assertAlmostEqual(smart_match.dissimilarity("aaa bbb", "aaa aaa"), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity("aaa", "aaa aaa"), 0.3333333333333333)

        self.assertAlmostEqual(smart_match.dissimilarity("a b c d", "a b c e"), 0.25)
        self.assertAlmostEqual(smart_match.dissimilarity("a b c d", "a b e f"), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity("a b c", "a b c e f g"), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.dissimilarity("a b b c c", "a b c e f g"), 0.45454545454545453)

        smart_match.set_params(level='char')
        self.assertAlmostEqual(smart_match.dissimilarity(["test", ""], ["test", "string2"]), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity([], ["test", "string2"]), 1)

    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'hero'), 3)
        self.assertEqual(smart_match.distance('hello', 'ehllo'), 0)

        self.assertEqual(smart_match.distance("Healed", "Sealed"), 2)
        self.assertEqual(smart_match.distance("Healed", "Healthy"), 5)
        self.assertEqual(smart_match.distance("Healed", "Heard"), 3)
        self.assertEqual(smart_match.distance("Healed", "Herded"), 4)
        self.assertEqual(smart_match.distance("Healed", "Help"), 4)
        self.assertEqual(smart_match.distance("Healed", "Sold"), 6)
        self.assertEqual(smart_match.distance("Healed", "Help"), 4)

        self.assertEqual(smart_match.distance('test string1', 'test string1'), 0)
        self.assertEqual(smart_match.distance('test string1', 'test string2'), 2)
        self.assertEqual(smart_match.distance("test", "test string2"), 8)
        self.assertEqual(smart_match.distance("", "test string2"), 12)

        self.assertEqual(smart_match.distance("aaa bbb ccc ddd", "aaa bbb ccc eee"), 6)
        self.assertEqual(smart_match.distance("aaa bbb", "aaa aaa"), 6)
        self.assertEqual(smart_match.distance("aaa", "aaa aaa"), 4)
        self.assertEqual(smart_match.distance("a b c d", "a b c e"), 2)
        self.assertEqual(smart_match.distance("a b c d", "a b e f"), 4)
        self.assertEqual(smart_match.distance("a b c", "a b c e f g"), 6)
        self.assertEqual(smart_match.distance("a b b c c", "a b c e f g"), 6)

        # smart_match.set_params(level='char')
        self.assertEqual(smart_match.distance(["test", ""], ["test", "string2"]), 2)
        self.assertEqual(smart_match.distance([], ["test", "string2"]), 2)


if __name__ == '__main__':
    unittest.main()