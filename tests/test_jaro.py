import unittest
import smart_match

class TestJaro(unittest.TestCase):
    def setUp(self):
        smart_match.use('jaro')
        
    def test_jaro_similarity1(self):
        self.assertAlmostEqual(smart_match.similarity('ABC','CBA'), 0.5555555555555555)
        self.assertAlmostEqual(smart_match.similarity('CRATE','TRACE'), 0.7333333333333334)
        self.assertAlmostEqual(smart_match.similarity('CRATE','TRACE'), 0.7333333333333334)
        self.assertAlmostEqual(smart_match.similarity('AABABCAAAC', 'ABAACBAAAC'), 0.9333333333333332)

        self.assertAlmostEqual(smart_match.similarity('\0\0\0\0', ''), 0.0000000000000000)
        self.assertAlmostEqual(smart_match.similarity('He0ll0o', 'Hel00lo'), 0.9047619047619048)
        self.assertAlmostEqual(smart_match.similarity('0000', '000000'), 0.8888888888888888)
        self.assertAlmostEqual(smart_match.similarity('H0000', '\0000000'), 0.8666666666666667)

        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity('MARTHA', 'MARHTA'))), 0.9444)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity('DWAYNE', 'DUANE'))), 0.8222)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity('DIXON', 'DICKSONX'))), 0.7667)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity('OZYMANDIAS', 'MARCUS'))), 0.6000)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity('OZYMANDIAS', ''))), 0.000)

        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity('test string1', 'test string2'))), 0.9444)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("test string1", "Sold"))), 0.0000)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("test", "test string2"))), 0.7778)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("", "test string2"))), 0.0000)

        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("aaa bbb ccc ddd", "aaa bbb ccc eee"))), 0.8667)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity('a b c d', 'a b c e'))), 0.9048)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Healed", "Sealed"))), 0.8889)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity('Healed', 'Healthy'))), 0.7460)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity('Healed', 'Heard'))), 0.8222)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity('Healed', 'Help'))), 0.7500)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("test", "test string2"))), 0.7778)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Healed", "Sold"))), 0.6111)

        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Sam J Chapman", "Samuel John Chapman"))), 0.7922)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Sam Chapman", "S Chapman"))), 0.8098)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("John Smith", "Samuel John Chapman"))), 0.5945)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("John Smith", "Sam Chapman"))), 0.4131)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("John Smith", "Sam J Chapman"))), 0.4949)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("John Smith", "S Chapman"))), 0.4333)

        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Database Applications", "Web Database Applications with PHP & MySQL"))), 0.8651)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Database Applications", "Creating Database Web Applications with PHP and ASP"))), 0.6901)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Database Applications", "Building Database Applications on the Web Using PHP3"))), 0.6353)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Database Applications", "Building Web Database Applications with Visual Studio 6"))), 0.6582)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Database Applications", "Web Application Development With PHP"))), 0.6310)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Database Applications", "WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection"))), 0.6291)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Database Applications", "Structural Assessment: The Role of Large and Full-Scale Testing"))), 0.4751)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Database Applications", "How to Find a Scholarship Online"))), 0.4882)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Aplications", "Web Database Applications with PHP & MySQL"))), 0.6635)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Aplications", "Creating Database Web Applications with PHP and ASP"))), 0.5980)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Aplications", "Building Database Applications on the Web Using PHP3"))), 0.5675)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Aplications", "Building Web Database Applications with Visual Studio 6"))), 0.5909)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Aplications", "Web Application Development With PHP"))), 0.7741)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Aplications", "WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection"))), 0.6352)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Aplications", "Structural Assessment: The Role of Large and Full-Scale Testing"))), 0.4751)
        self.assertAlmostEqual(float("%.4f" % (smart_match.similarity("Web Aplications", "How to Find a Scholarship Online"))), 0.4931)


if __name__=='__main__':
    unittest.main()
