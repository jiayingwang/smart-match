import unittest
import smart_match

class TestGeneralizedJaccard(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('gjac')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'helo'), 0.8)
        self.assertAlmostEqual(smart_match.similarity('abcd', 'abce'), 0.6)
        self.assertAlmostEqual(smart_match.similarity('abcd', 'abef'), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.similarity('abc', 'abcefg'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('abbcc', 'abcefg'), 0.375)
        
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.similarity('test', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('', 'test string2'), 0)
        self.assertAlmostEqual(smart_match.similarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.6)
        self.assertAlmostEqual(smart_match.similarity('aaa bbb ccc ddd aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.similarity('Sam J Chapman', 'Samuel John Chapman'), 0.2)
        self.assertAlmostEqual(smart_match.similarity('Sam Chapman', 'S Chapman'), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Samuel John Chapman'), 0.25)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam Chapman'), 0)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam J Chapman'), 0)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'S Chapman'), 0)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Web Database Applications with PHP & MySQL'), 0.42857142857142855)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Creating Database Web Applications with PHP and ASP'), 0.3750)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Building Database Applications on the Web Using PHP3'), 0.3750)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Building Web Database Applications with Visual Studio 6'), 0.3750)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Web Application Development With PHP'), 0.14285714285714285)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'), 0.23076923076923078)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Structural Assessment: The Role of Large and Full-Scale Testing'), 0)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'How to Find a Scholarship Online'), 0)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Web Database Applications with PHP & MySQL'), 0.1250)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Creating Database Web Applications with PHP and ASP'), 0.1111111111111111)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Building Database Applications on the Web Using PHP3'), 0.1111111111111111)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Building Web Database Applications with Visual Studio 6'), 0.1111111111111111)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Web Application Development With PHP'), 0.16666666666666666)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'), 0.07142857142857142)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Structural Assessment: The Role of Large and Full-Scale Testing'), 0)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'How to Find a Scholarship Online'), 0)
        self.assertAlmostEqual(smart_match.similarity('a b c d', 'a b c e'), 0.6)
        self.assertAlmostEqual(smart_match.similarity('a b c d', 'a b e f'), 0.3333333333333333)
        self.assertAlmostEqual(smart_match.similarity('a b c', 'a b c e f g'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('a b b c c', 'a b c e f g'), 0.375)
                
        smart_match.set_params(level='char')
        self.assertAlmostEqual(smart_match.similarity(('test', None), ('test', 'string2')), 0.3333333333333333)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'helo'), 0.2)
        self.assertAlmostEqual(smart_match.dissimilarity('abcd', 'abce'), 0.4)
        self.assertAlmostEqual(smart_match.dissimilarity('abcd', 'abef'), 0.6666666666666667)
        self.assertAlmostEqual(smart_match.dissimilarity('abc', 'abcefg'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('abbcc', 'abcefg'), 0.625)

        
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.6666666666666667)
        self.assertAlmostEqual(smart_match.dissimilarity('test', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('', 'test string2'), 1)
        self.assertAlmostEqual(smart_match.dissimilarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.4)
        self.assertAlmostEqual(smart_match.dissimilarity('aaa bbb ccc ddd aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.6666666666666667)

        
        smart_match.set_params(level='char')
        self.assertAlmostEqual(smart_match.dissimilarity(('test', None), ('test', 'string2')), 0.6666666666666667)

if __name__ == '__main__':
    unittest.main()
