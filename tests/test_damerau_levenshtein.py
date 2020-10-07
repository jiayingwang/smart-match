import unittest
import smart_match

class TestDamerauLevenshtein(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('DL')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'hero'), 0.6)
        self.assertEqual(float('%.4f' %smart_match.similarity("test string1", "test string2")), 0.9167)
        self.assertEqual(smart_match.similarity("", "test string2"),0.0000)
        self.assertEqual(smart_match.similarity( "aaa bbb ccc ddd", "aaa bbb ccc eee"),0.8000)
        self.assertEqual(float('%.4f' %smart_match.similarity("aaa bbb", "aaa aaa")),0.5714)
        self.assertEqual(float('%.4f' %smart_match.similarity("aaa", "aaa aaa")),0.4286)
        self.assertEqual(float('%.4f' %smart_match.similarity("a b c d", "a b c e")),0.8571)
        self.assertEqual(float('%.4f' %smart_match.similarity("uxyw", "uyxw")),0.7500)
        self.assertEqual(float('%.4f' %smart_match.similarity("uxaayw", "uyxw")),0.3333)
        self.assertEqual(float('%.4f' %smart_match.similarity("transpose", "tranpsose")),0.8889)
        self.assertEqual(float('%.4f' %smart_match.similarity("Healed", "Sealed")),0.8333)
        self.assertEqual(float('%.4f' %smart_match.similarity("Healed", "Healthy")),0.5714)
        self.assertEqual(float('%.4f' %smart_match.similarity("Healed", "Heard")),0.6667)
        self.assertEqual(float('%.4f' %smart_match.similarity("Healed", "Herded")),0.6667)
        self.assertEqual(float('%.4f' %smart_match.similarity("Healed", "Help")),0.5000)
        self.assertEqual(float('%.4f' %smart_match.similarity("Healed", "Sold")),0.3333)
        self.assertEqual(float('%.4f' %smart_match.similarity("Healed", "Help")),0.5000)
        self.assertEqual(float('%.4f' %smart_match.similarity("Sam J Chapman", "Samuel John Chapman")),0.6842)
        self.assertEqual(float('%.4f' %smart_match.similarity("Sam Chapman", "S Chapman")),0.8182)
        self.assertEqual(float('%.4f' %smart_match.similarity("John Smith", "Samuel John Chapman")),0.2632)
        self.assertEqual(float('%.4f' %smart_match.similarity("John Smith", "Sam Chapman")),0.0000)
        self.assertEqual(float('%.4f' %smart_match.similarity("John Smith", "Sam J Chapman")),0.0769)
        self.assertEqual(float('%.4f' %smart_match.similarity("John Smith", "S Chapman")),0.1000)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
        "Web Database Applications with PHP & MySQL")),0.5952)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
        "Creating Database Web Applications with PHP and ASP")),0.4510)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
        "Building Database Applications on the Web Using PHP3")),0.4231)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
        "Building Web Database Applications with Visual Studio 6")),0.4545)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
        "Web Application Development With PHP")),0.2500)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
        "WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection")),
            0.2874)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
            "Structural Assessment: The Role of Large and Full-Scale Testing")),0.1587)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
            "How to Find a Scholarship Online")),0.1562)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Aplications",
            "Web Database Applications with PHP & MySQL")),0.3571)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Aplications",
            "Creating Database Web Applications with PHP and ASP")),0.2941)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Aplications",
            "Building Database Applications on the Web Using PHP3")),0.2500)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Aplications",
            "Building Web Database Applications with Visual Studio 6")),0.2727)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Aplications",
            "Web Application Development With PHP")),0.3889)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Aplications",
            "WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection")),
            0.1724)
        self.assertEqual(float('%.4f' %smart_match.similarity("Web Aplications",
            "Structural Assessment: The Role of Large and Full-Scale Testing")),0.1111)

        self.assertEqual(float('%.4f' %smart_match.similarity("Web Aplications",
            "How to Find a Scholarship Online")),0.1875)
        self.assertEqual(float('%.4f' %smart_match.similarity( "uxyw", "")),0.0000)

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'hero'), 0.4)
        self.assertEqual(smart_match.dissimilarity('hello', 'hero'), 0.4)
        self.assertEqual(float('%.4f' % smart_match.dissimilarity("test string1", "test string2")), 0.0833)
        self.assertEqual(smart_match.dissimilarity("", "test string2"), 1)
        self.assertEqual(smart_match.dissimilarity("aaa bbb ccc ddd", "aaa bbb ccc eee"), 0.2000)
        self.assertEqual(float('%.4f' % smart_match.dissimilarity("aaa bbb", "aaa aaa")),  0.4286)

    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'hero'), 2)
        self.assertEqual(smart_match.distance('hello', 'ehllo'), 1)
        self.assertEqual(smart_match.distance("test string1",  "test string2"), 1.0000)
        self.assertEqual(smart_match.distance("test", "test string2"),8.0000)
        self.assertEqual(smart_match.distance("", "test string2"),12.0000)
        self.assertEqual(smart_match.distance("aaa bbb ccc ddd", "aaa bbb ccc eee"),3.0000)
        self.assertEqual(smart_match.distance( "aaa bbb", "aaa aaa"),3.0000)
        self.assertEqual(smart_match.distance("aaa", "aaa aaa"),4.0000)
        self.assertEqual(smart_match.distance( "a b c d", "a b c e"),1.0000)
        self.assertEqual(smart_match.distance("uxyw", "uyxw"),1.0000)
        self.assertEqual(smart_match.distance("uxaayw", "uyxw"),4.0000)
        self.assertEqual(smart_match.distance("transpose", "tranpsose"),1.0000)
        self.assertEqual(smart_match.distance("Healed", "Sealed"),1.0000)
        self.assertEqual(smart_match.distance("Healed", "Healthy"),3.0000)
        self.assertEqual(smart_match.distance("Healed", "Heard"),2.0000)
        self.assertEqual(smart_match.distance("Healed", "Herded"),2.0000)
        self.assertEqual(smart_match.distance("Healed", "Help"),3.0000)
        self.assertEqual(smart_match.distance("Healed", "Sold"),4.0000)
        self.assertEqual(smart_match.distance("Healed", "Help"),3.0000)
        self.assertEqual(smart_match.distance( "Sam J Chapman", "Samuel John Chapman"),6.0000)
        self.assertEqual(smart_match.distance("Sam Chapman", "S Chapman"),2.0000)
        self.assertEqual(smart_match.distance("John Smith", "Samuel John Chapman"),14.0000)
        self.assertEqual(smart_match.distance( "John Smith", "Sam Chapman"),11.0000)
        self.assertEqual(smart_match.distance("John Smith", "Sam J Chapman"),12.0000)
        self.assertEqual(smart_match.distance("John Smith", "S Chapman"),9.0000)
        self.assertEqual(smart_match.distance("Web Database Applications",
            "Web Database Applications with PHP & MySQL"),17.0000)
        self.assertEqual(smart_match.distance("Web Database Applications",
            "Creating Database Web Applications with PHP and ASP"),28.0000)
        self.assertEqual(smart_match.distance( "Web Database Applications",
            "Building Database Applications on the Web Using PHP3"),30.0000)
        self.assertEqual(smart_match.distance( "Web Database Applications",
            "Building Web Database Applications with Visual Studio 6"),30.0000)
        self.assertEqual(smart_match.distance("Web Database Applications",
            "Web Application Development With PHP"),27.0000)
        self.assertEqual(smart_match.distance("Web Database Applications",
            "WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection"),62.0000)
        self.assertEqual(smart_match.distance("Web Database Applications",
            "Structural Assessment: The Role of Large and Full-Scale Testing"),53.0000)
        self.assertEqual(smart_match.distance( "Web Database Applications",
            "How to Find a Scholarship Online"),27.0000)
        self.assertEqual(smart_match.distance("Web Aplications",
            "Web Database Applications with PHP & MySQL"),27.0000)
        self.assertEqual(smart_match.distance( "Web Aplications",
            "Creating Database Web Applications with PHP and ASP"),36.0000)
        self.assertEqual(smart_match.distance( "Web Aplications",
            "Building Database Applications on the Web Using PHP3"),39.0000)
        self.assertEqual(smart_match.distance("Web Aplications",
            "Building Web Database Applications with Visual Studio 6"),40.0000)
        self.assertEqual(smart_match.distance("Web Aplications",
            "Web Application Development With PHP"),22.0000)
        self.assertEqual(smart_match.distance("Web Aplications",
            "WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection"),72.0000)

        self.assertEqual(smart_match.distance("Web Aplications",
            "Structural Assessment: The Role of Large and Full-Scale Testing"),56.0000)
        self.assertEqual(smart_match.distance("Web Aplications",
            "How to Find a Scholarship Online"),26.0000)
if __name__ == '__main__':
    unittest.main()