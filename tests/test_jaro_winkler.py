import unittest
import smart_match

class TestJaroWinkler(unittest.TestCase):
    def setUp(self):
        smart_match.use('Jaro Winkler')
        
    def test_similarity(self):
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity('DwAyNE', 'DuANE')), 0.84)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity('TRATE', 'TRACE')), 0.9067)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("test string1", "test string2")),0.9667)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("", "test string2")),0.0000)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("aaa bbb ccc ddd", "aaa bbb ccc eee")),0.9200)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("a b c d", "a b c e")),0.9429)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("Healed", "Sealed")),0.8889)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("Healed", "Healthy")),0.8476)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("Healed", "Heard")),0.8756)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity( "Healed", "Help")),.8000)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("Healed", "Sold")),0.6111)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity( "Healed", "Help")),0.8000)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("Sam Chapman", "S Chapman")),0.8288)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("John Smith", "Samuel John Chapman")),0.5945)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("John Smith", "Sam Chapman")),0.4131)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("John Smith", "Sam J Chapman")),0.4949)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("John Smith", "S Chapman")),0.4333)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
            "Web Database Applications with PHP & MySQL")),0.9190)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
            "Creating Database Web Applications with PHP and ASP")),0.6901)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
            "Building Database Applications on the Web Using PHP3")),0.6353)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("Web Database Applications",
            "Building Web Database Applications with Visual Studio 6")),0.6582)

        smart_match.set_params(boost_threshold=0.6)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity('abcdefgh', 'abehc')), 0.7467)
        self.assertAlmostEqual(float('%.4f' %smart_match.similarity("Healed", "Herded")),0.7556)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity("Web Database Applications",
            "Web Application Development With PHP")),0.7786)  # 0.631
        
if __name__=='__main__':
    unittest.main()
