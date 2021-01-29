import unittest
import smart_match

class TestSmithWaterman(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('Smith Waterman')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Web Application Development With PHP'), 0.8666666666666667)
        self.assertAlmostEqual(smart_match.similarity('', 'eee'), 0)
        self.assertAlmostEqual(smart_match.similarity('aaa', 'eee'), 0)
        self.assertAlmostEqual(smart_match.similarity('eee', 'aaa'), 0)
        self.assertAlmostEqual(smart_match.similarity('ddd', 'aaa'), 0)
        self.assertAlmostEqual(smart_match.similarity('aaa', 'ddd'), 0)
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.9166666666666666)
        self.assertAlmostEqual(smart_match.similarity('test', 'test string2'), 1)
        self.assertAlmostEqual(smart_match.similarity('', 'test string2'), 0)
        self.assertAlmostEqual(smart_match.similarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.8)
        self.assertAlmostEqual(smart_match.similarity('a b c d', 'a b c e'), 0.8571428571428571)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sealed'), 0.8333333333333334)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Healthy'), 0.6666666666666666)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Heard'), 0.6)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Hearded'), 0.5666666666666667)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Help'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sold'), 0.25)
        self.assertAlmostEqual(smart_match.similarity('Sam J Chapman', 'Samuel John Chapman'),0.7846153846153846)
        self.assertAlmostEqual(smart_match.similarity('Sam Chapman', 'S Chapman'),0.8888888888888888)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Samuel John Chapman'),0.5)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam Chapman'),0.1)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam J Chapman'),0.1)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'S Chapman'),0.1111111111111111)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Web Database Applications with PHP & MySQL'),1)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Creating Database Web Applications with PHP and ASP'),0.8160)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Building Database Applications on the Web Using PHP3'),0.8800)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Building Web Database Applications with Visual Studio 6'),1)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Web Application Development With PHP'),0.496)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.88)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Structural Assessment: The Role of Large and Full-Scale Testing'),0.096)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'How to Find a Scholarship Online'),0.08)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Web Database Applications with PHP & MySQL'),0.76)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Creating Database Web Applications with PHP and ASP'),0.9333333333333333)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Building Database Applications on the Web Using PHP3'),0.7333333333333333)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Building Web Database Applications with Visual Studio 6'),0.76)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Web Application Development With PHP'),0.8666666666666666)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.7333333333333333)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Structural Assessment: The Role of Large and Full-Scale Testing'),0.1333333333333333)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'How to Find a Scholarship Online'),0.1333333333333333)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications', 'Web Application Development With PHP'), 0.1333333333333333)
        self.assertAlmostEqual(smart_match.dissimilarity('', 'eee'), 1)
        self.assertAlmostEqual(smart_match.dissimilarity('aaa', 'eee'), 1)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Help'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Sold'), 0.75)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications', 'Web Application Development With PHP'),0.504)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.12)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications', 'Structural Assessment: The Role of Large and Full-Scale Testing'),0.904)
        
    def test_score(self):
        self.assertEqual(smart_match.score('Web Aplications', 'Web Application Development With PHP'), 65)
        self.assertAlmostEqual(smart_match.score('', 'eee'), -3)
        self.assertAlmostEqual(smart_match.score('aaa', 'eee'), 0)
        self.assertAlmostEqual(smart_match.score('Healed', 'Help'), 10)
        self.assertAlmostEqual(smart_match.score('Healed', 'Sold'), 5)
        self.assertAlmostEqual(smart_match.score('Web Database Applications', 'Web Application Development With PHP'),62)
        self.assertAlmostEqual(smart_match.score('Web Database Applications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),110)
        self.assertAlmostEqual(smart_match.score('Web Database Applications', 'Structural Assessment: The Role of Large and Full-Scale Testing'),12)

if __name__ == '__main__':
    unittest.main()
