import unittest
import smart_match

class TestGeneralizedOverlapCoefficient(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('Generalized Overlap Coefficient')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'hero'), 0.75)
        self.assertAlmostEqual(smart_match.similarity('abcd', 'abce'), 0.75)
        self.assertAlmostEqual(smart_match.similarity('abcd', 'abef'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('abc', 'abcefg'), 1)
        self.assertAlmostEqual(smart_match.similarity('abbcc', 'abcefg'), 0.6)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sealed'), 0.8333333333333334)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Healthy'), 0.6666666666666666)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Heard'), 0.8)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Herded'), 0.6666666666666666)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Help'), 0.75)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sold'), 0.5)
        
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('test', 'test string2'), 1)
        self.assertAlmostEqual(smart_match.similarity('', 'test string2'), 0)
        self.assertAlmostEqual(smart_match.similarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.75)
        self.assertAlmostEqual(smart_match.similarity('aaa bbb ccc ddd aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.75)
        self.assertAlmostEqual(smart_match.similarity('a b c d', 'a b c e'), 0.75)
        self.assertAlmostEqual(smart_match.similarity('a b c d', 'a b e f'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('a b c', 'a b c e f g'), 1)
        self.assertAlmostEqual(smart_match.similarity('a b b c c', 'a b c e f g'), 0.6)
        self.assertAlmostEqual(smart_match.similarity('Sam J Chapman', 'Samuel John Chapman'), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.similarity('Sam Chapman', 'S Chapman'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Samuel John Chapman'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam Chapman'), 0)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam J Chapman'), 0)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'S Chapman'), 0)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Web Database Applications with PHP & MySQL'), 1)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Creating Database Web Applications with PHP and ASP'), 1)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Building Database Applications on the Web Using PHP3'), 1)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Building Web Database Applications with Visual Studio 6'), 1)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Web Application Development With PHP'), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'), 1)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Structural Assessment: The Role of Large and Full-Scale Testing'), 0)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'How to Find a Scholarship Online'), 0)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Web Database Applications with PHP & MySQL'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Creating Database Web Applications with PHP and ASP'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Building Database Applications on the Web Using PHP3'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Building Web Database Applications with Visual Studio 6'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Web Application Development With PHP'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Structural Assessment: The Role of Large and Full-Scale Testing'), 0)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'How to Find a Scholarship Online'), 0)
                   
        smart_match.set_params(level='char')
        self.assertAlmostEqual(smart_match.similarity(("test", None), ("test","string2")), 0.5)

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'hero'), 0.25)
        self.assertEqual(smart_match.dissimilarity('hello', 'ehllo'), 0)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Sealed'), 0.16666666666666663)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Healthy'), 0.33333333333333337)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Heard'), 0.19999999999999996)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Herded'), 0.33333333333333337)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Help'), 0.25)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Sold'), 0.5)
        
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('test', 'test string2'), 0)
        self.assertAlmostEqual(smart_match.dissimilarity('', 'test string2'), 1)
        self.assertAlmostEqual(smart_match.dissimilarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.25)
        self.assertAlmostEqual(smart_match.dissimilarity('aaa bbb ccc ddd aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.25)

        smart_match.set_params(level='char')
        self.assertAlmostEqual(smart_match.similarity(("test", None), ("test","string2")), 0.5)

if __name__ == '__main__':
    unittest.main()
