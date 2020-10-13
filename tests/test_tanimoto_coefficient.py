import unittest
import smart_match

class TestTanimotoCoefficient(unittest.TestCase):
    def setUp(self):
        smart_match.use('TC')
        
    def test_similarity(self):
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity('test', 'test string1')), .5774)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("test string1", "test string2")), 0.5000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("test", "test string2")), 0.7071)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("", "test string2")), 0.0000)

        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("aaa bbb ccc ddd", "aaa bbb ccc eee")), 0.7500)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("aaa bbb ccc ddd aaa bbb ccc ddd", "aaa bbb ccc eee")), 0.7500)

        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("a b c d", "a b c e")), 0.7500)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("a b c d", "a b e f")), 0.5000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("a b c", "a b c e f g")), 0.7071)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("a b b c c", "a b c e f g")), 0.7071)

        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Sealed")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Healthy")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Heard")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Herded")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Help")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Sold")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Help")), 0.0000)

        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Sam J Chapman", "Samuel John Chapman")), 0.3333)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Sam Chapman", "S Chapman")), 0.5000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("John Smith", "Samuel John Chapman")), 0.4082)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("John Smith", "Sam Chapman")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("John Smith", "Sam J Chapman")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("John Smith", "S Chapman")), 0.0000)

        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications","Web Database Applications with PHP & MySQL")), 0.6547)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications","Creating Database Web Applications with PHP and ASP")), 0.6124)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications","Structural Assessment: The Role of Large and Full-Scale Testing")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications","Web Application Development With PHP")), 0.2582)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Aplications","Web Application Development With PHP")), 0.3162)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Aplications","Web Database Applications with PHP & MySQL")), 0.2673)

    def test_dissimilarity(self):
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity('test', 'test string1')), 0.4226)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("test string1", "test string2")), 0.5000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("test", "test string2")), 0.2929)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("", "test string2")), 1.0000)

        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("aaa bbb ccc ddd", "aaa bbb ccc eee")), 0.2500)
        self.assertAlmostEqual(
            float('%.4f' % smart_match.dissimilarity("aaa bbb ccc ddd aaa bbb ccc ddd", "aaa bbb ccc eee")), 0.2500)

        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("a b c d", "a b c e")), 0.2500)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("a b c d", "a b e f")), 0.5000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("a b c", "a b c e f g")), 0.2929)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("a b b c c", "a b c e f g")), 0.2929)

        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Sealed")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Healthy")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Heard")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Herded")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Help")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Sold")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Help")), 1.0000)

        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Sam J Chapman", "Samuel John Chapman")),
                               0.6667)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Sam Chapman", "S Chapman")), 0.5000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("John Smith", "Samuel John Chapman")), 0.5918)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("John Smith", "Sam Chapman")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("John Smith", "Sam J Chapman")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("John Smith", "S Chapman")), 1.0000)

        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Database Applications",
                                                                     "Web Database Applications with PHP & MySQL")),
                               0.3453)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Database Applications",
                                                                     "Creating Database Web Applications with PHP and ASP")),
                               0.3876)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Database Applications",
                                                                     "Structural Assessment: The Role of Large and Full-Scale Testing")),
                               1.0000)
        self.assertAlmostEqual(float(
            '%.4f' % smart_match.dissimilarity("Web Database Applications", "Web Application Development With PHP")),
                               0.7418)
        self.assertAlmostEqual(
            float('%.4f' % smart_match.dissimilarity("Web Aplications", "Web Application Development With PHP")),
            0.6838)
        self.assertAlmostEqual(
            float('%.4f' % smart_match.dissimilarity("Web Aplications", "Web Database Applications with PHP & MySQL")),
            0.7327)
        
if __name__ == '__main__':
    unittest.main()
