import unittest
import smart_match

class TestOverlapCoefficient(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('Overlap Coefficient')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'hero'), 0.75)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)
        self.assertEqual(smart_match.similarity("aaa bbb ccc ddd", "aaa bbb ccc eee"),0.7500)
        self.assertEqual(smart_match.similarity("aaa bbb ccc ddd aaa bbb ccc ddd", "aaa bbb ccc eee"),0.7500)
        self.assertEqual(smart_match.similarity("a b c d", "a b c e"),0.7500)
        self.assertEqual(smart_match.similarity( "a b c d", "a b e f"),0.5000)
        self.assertEqual(smart_match.similarity("a b c", "a b c e f g"),1.0000)
        self.assertEqual(smart_match.similarity("a b b c c", "a b c e f g"),1.0000)
        self.assertEqual(smart_match.similarity("Healed", "Sealed"),0.0000)
        self.assertEqual(smart_match.similarity("Healed", "Healthy"),0.0000)
        self.assertEqual(smart_match.similarity("Healed", "Heard"),0.0000)
        self.assertEqual(smart_match.similarity("Healed", "Herded"),0.0000)
        self.assertEqual(smart_match.similarity("Healed", "Help"),0.0000)
        self.assertEqual(smart_match.similarity("Healed", "Sold"),0.0000)
        self.assertEqual(smart_match.similarity("Healed", "Help"),0.0000)
        self.assertEqual(float('%.4f' %smart_match.similarity("Sam J Chapman", "Samuel John Chapman")),0.3333)
        self.assertEqual(smart_match.similarity("Sam Chapman", "S Chapman"),0.5000)
        self.assertEqual(smart_match.similarity("John Smith", "Samuel John Chapman"),0.5000)
        self.assertEqual(smart_match.similarity("John Smith", "Sam Chapman"),0.0000)
        self.assertEqual(smart_match.similarity("John Smith", "Sam J Chapman"),0.0000)
        self.assertEqual(smart_match.similarity("John Smith", "S Chapman"),0.0000)
        self.assertEqual(smart_match.similarity("Web Database Applications",
            "Web Database Applications with PHP & MySQL"),1.0000)
        self.assertEqual(smart_match.similarity("Web Database Applications",
            "Creating Database Web Applications with PHP and ASP"),1.0000)
        self.assertEqual(smart_match.similarity("Web Database Applications",
            "Building Database Applications on the Web Using PHP3"),1.0000)
        self.assertEqual(smart_match.similarity("Web Database Applications",
            "Building Web Database Applications with Visual Studio 6"),1.0000)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
            "Web Application Development With PHP")),0.3333)
        self.assertEqual(smart_match.similarity("Web Database Applications",
            "WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection"),
            1.0000)
        self.assertEqual(smart_match.similarity("Web Database Applications",
            "Structural Assessment: The Role of Large and Full-Scale Testing"),0.0000)
        self.assertEqual(smart_match.similarity("Web Database Applications",
            "How to Find a Scholarship Online"),0.0000)
        self.assertEqual(smart_match.similarity("Web Aplications",
            "Web Database Applications with PHP & MySQL"),0.5000)
        self.assertEqual(smart_match.similarity("Web Aplications",
            "Creating Database Web Applications with PHP and ASP"),0.5000)
        self.assertEqual(smart_match.similarity("Web Aplications",
            "Building Database Applications on the Web Using PHP3"),0.5000)
        self.assertEqual(smart_match.similarity("Web Aplications",
            "Building Web Database Applications with Visual Studio 6"),0.5000)
        self.assertEqual(smart_match.similarity("Web Aplications",
            "Web Application Development With PHP"),0.5000)
        self.assertEqual(smart_match.similarity("Web Aplications",
            "WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection"),
            0.5000)
        self.assertEqual(smart_match.similarity("Web Aplications",
            "Structural Assessment: The Role of Large and Full-Scale Testing"),0.0000)
        self.assertEqual(smart_match.similarity("Web Aplications",
            "How to Find a Scholarship Online"),0.0000)


    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'hero'), 0.25)
        self.assertEqual(smart_match.dissimilarity('hello', 'ehllo'), 0)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.5)
        self.assertEqual(smart_match.dissimilarity("Sam Chapman", "S Chapman"), 0.5000)
        self.assertEqual(smart_match.dissimilarity("John Smith", "Samuel John Chapman"), 0.5000)
        self.assertEqual(smart_match.dissimilarity("John Smith", "Sam Chapman"), 1.0000)
        self.assertEqual(smart_match.dissimilarity("John Smith", "Sam J Chapman"), 1.0000)
        self.assertEqual(smart_match.dissimilarity("John Smith", "S Chapman"), 1.0000)
        self.assertEqual(smart_match.dissimilarity("a b b c c", "a b c e f g"), 0.0000)
        self.assertEqual(smart_match.dissimilarity("Healed", "Sealed"), 1.0000)
        self.assertEqual(smart_match.dissimilarity("Healed", "Healthy"), 1.0000)
        self.assertEqual(smart_match.dissimilarity("Healed", "Heard"), 1.0000)
        self.assertEqual(smart_match.dissimilarity("Web Database Applications",
                                                "Web Database Applications with PHP & MySQL"), 0.0000)
        self.assertEqual(smart_match.dissimilarity("Web Database Applications",
                                                "Creating Database Web Applications with PHP and ASP"), 0.0000)
        self.assertEqual(smart_match.dissimilarity("Web Database Applications",
                                                "Building Database Applications on the Web Using PHP3"), 0.0000)
        self.assertEqual(smart_match.dissimilarity("Web Database Applications",
                                                "Building Web Database Applications with Visual Studio 6"), 0.0000)
if __name__ == '__main__':
    unittest.main()
