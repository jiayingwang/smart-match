import unittest
import smart_match


class TestSmithWatermanGotoh(unittest.TestCase):

    def setUp(self):
        smart_match.use('SWG')

    def test_similarity(self):
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("test string1", "test string2")), 0.9167)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("test", "test string2")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("", "test string2")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("aaa bbb ccc ddd", "aaa bbb ccc eee")), 0.8000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("a b c d", "a b c e")), 0.8571)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Sealed")), 0.8333)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Healthy")), 0.6667)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Heard")), 0.6000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Healed", "Herded")), 0.3333)

        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Sam J Chapman", "Samuel John Chapman")), 0.7692)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Sam Chapman", "S Chapman")), 0.8889)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("John Smith", "Samuel John Chapman")), 0.5000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("aaa bbb ccc ddd", "aaa bbb ccc eee")), 0.8000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("John Smith", "Sam Chapman")), 0.1500)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("John Smith", "S Chapman")), 0.1111)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications","Web Database Applications with PHP & MySQL")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications","Building Web Database Applications with Visual Studio 6")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications","Web Application Development With PHP")), 0.5000)

        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications","WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection")), 0.8800)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications","Structural Assessment: The Role of Large and Full-Scale Testing")), 0.1000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications","How to Find a Scholarship Online")), 0.0800)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Aplications","Web Database Applications with PHP & MySQL")), 0.8000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Aplications","Creating Database Web Applications with PHP and ASP")), 0.9667)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Aplications","Web Application Development With PHP")), 0.9000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Aplications","Structural Assessment: The Role of Large and Full-Scale Testing")), 0.1667)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Aplications","How to Find a Scholarship Online")), 0.1333)

    def test_dissimilarity(self):
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("test string1", "test string2")), 0.0833)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("test", "test string2")), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("", "test string2")), 1.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("aaa bbb ccc ddd", "aaa bbb ccc eee")), 0.2000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("a b c d", "a b c e")), 0.1429)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Sealed")), 0.1667)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Healthy")), 0.3333)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Heard")), 0.4000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Healed", "Herded")), 0.6667)

        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Sam J Chapman", "Samuel John Chapman")), 0.2308)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Sam Chapman", "S Chapman")), 0.1111)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("John Smith", "Samuel John Chapman")), 0.5000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("aaa bbb ccc ddd", "aaa bbb ccc eee")), 0.2000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("John Smith", "Sam Chapman")), 0.8500)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("John Smith", "S Chapman")), 0.8889)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Database Applications", "Web Database Applications with PHP & MySQL")),
                               0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Database Applications","Building Web Database Applications with Visual Studio 6")),
                               0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Database Applications", "Web Application Development With PHP")),
            0.5000)

        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Database Applications","WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection")),
                               0.1200)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Database Applications","Structural Assessment: The Role of Large and Full-Scale Testing")),
                               0.9000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Database Applications", "How to Find a Scholarship Online")),
            0.9200)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Aplications", "Web Database Applications with PHP & MySQL")),
            0.2000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Aplications", "Creating Database Web Applications with PHP and ASP")),
                               0.0333)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Aplications", "Web Application Development With PHP")), 0.1000)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Aplications","Structural Assessment: The Role of Large and Full-Scale Testing")),
                               0.8333)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity("Web Aplications", "How to Find a Scholarship Online")), 0.8667)
if __name__ == '__main__':
        unittest.main()