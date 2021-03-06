import unittest
import smart_match

class TestLongestCommonSubsequence(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('Longest Common SubSequence')

    def test_similarity(self):
        self.assertEqual(smart_match.similarity('hello', 'hill'), 0.6)
        self.assertEqual(smart_match.similarity('test string1', 'test string2'), 0.9166666666666666)
        self.assertEqual(smart_match.similarity('test', 'test string2'), 0.3333333333333333)
        self.assertEqual(smart_match.similarity('', 'test string2'), 0.0)
        self.assertEqual(smart_match.similarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.8)
        self.assertEqual(smart_match.similarity('aaa bbb', 'aaa aaa'), 0.5714285714285714)
        self.assertEqual(smart_match.similarity('aaa', 'aaa aaa'), 0.42857142857142855)
        self.assertEqual(smart_match.similarity('a b c d', 'a b c e'), 0.8571428571428571)
        self.assertEqual(smart_match.similarity('uxaayw', 'uyxw'), 0.5)
        self.assertEqual(smart_match.similarity('uxyw', 'uyxw'), 0.75)
        self.assertEqual(smart_match.similarity('transpose', 'tranpsose'), 0.8888888888888888)
        self.assertEqual(smart_match.similarity('Healed', 'Sealed'), 0.8333333333333334)
        self.assertEqual(smart_match.similarity('Healed', 'Healthy'), 0.5714285714285714)

        self.assertEqual(smart_match.similarity('Web Database Applications', 'Web Database Applications with PHP & MySQL'), 0.5952380952380952)
        self.assertEqual(smart_match.similarity('Web Database Applications', 'Building Database Applications on the Web Using PHP3'),0.4230769230769231)
        self.assertEqual(smart_match.similarity('Web Database Applications','Building Web Database Applications with Visual Studio 6'), 0.45454545454545453)

        self.assertEqual(smart_match.similarity('Healed', 'Heard'), 0.6666666666666666)
        self.assertEqual(smart_match.similarity('Healed', 'Herded'), 0.6666666666666666)
        self.assertEqual(smart_match.similarity('Healed', 'Help'), 0.5)
        self.assertEqual(smart_match.similarity('Healed', 'sold'), 0.3333333333333333)
        self.assertEqual(smart_match.similarity('Sam J Chapman', 'Samuel John Chapman'), 0.6842105263157895)
        self.assertEqual(smart_match.similarity('Sam Chapman', 'S Chapman'), 0.8181818181818182)
        self.assertEqual(smart_match.similarity('John Smith', 'Samuel John Chapman'), 0.3157894736842105)
        self.assertEqual(smart_match.similarity('John Smith', 'Sam Chapman'), 0.2727272727272727)
        self.assertEqual(smart_match.similarity('John Smith', 'Sam J Chapman'), 0.23076923076923078)
        self.assertEqual(smart_match.similarity('John Smith', 'S Chapman'), 0.2)
        self.assertEqual(smart_match.similarity('Web Database Applications', 'Creating Database Web Applications with PHP and ASP'),0.45098039215686275)
        self.assertEqual(smart_match.similarity('Web Database Applications', 'Web Application Development With PHP'), 0.4166666666666667)
        self.assertEqual(smart_match.similarity('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.28735632183908044)
        self.assertEqual(smart_match.similarity('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'), 0.1746031746031746)
        self.assertEqual(smart_match.similarity('Web Database Applications', 'How to Find a Scholarship Online'), 0.28125)
        self.assertEqual(smart_match.similarity('Web Aplications', 'Web Database Applications with PHP & MySQL'), 0.35714285714285715)
        self.assertEqual(smart_match.similarity('Web Aplications', 'Creating Database Web Applications with PHP and ASP'),0.29411764705882354)
        self.assertEqual(smart_match.similarity('Web Aplications', 'Building Database Applications on the Web Using PHP3'), 0.25)
        self.assertEqual(smart_match.similarity('Web Aplications', 'Building Web Database Applications with Visual Studio 6'), 0.2727272727272727)
        self.assertEqual(smart_match.similarity('Web Aplications', 'Web Application Development With PHP'), 0.3888888888888889)
        self.assertEqual(smart_match.similarity('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.1724137931034483)
        self.assertEqual(smart_match.similarity('Web Aplications', 'Structural Assessment: The Role of Large and Full-Scale Testing'),0.12698412698412698)
        self.assertEqual(smart_match.similarity('Web Aplications', 'How to Find a Scholarship Online'), 0.1875)

    def test_dissimilarity(self):
        self.assertEqual(smart_match.dissimilarity('hello', 'hill'), 0.4)
        self.assertEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.08333333333333337)
        self.assertEqual(smart_match.dissimilarity('test', 'test string2'), 0.6666666666666667)
        self.assertEqual(smart_match.dissimilarity('', 'test string2'), 1.0)
        self.assertEqual(smart_match.dissimilarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.19999999999999996)
        self.assertEqual(smart_match.dissimilarity('aaa bbb', 'aaa aaa'), 0.4285714285714286)
        self.assertEqual(smart_match.dissimilarity('aaa', 'aaa aaa'), 0.5714285714285714)
        self.assertEqual(smart_match.dissimilarity('a b c d', 'a b c e'), 0.1428571428571429)
        self.assertEqual(smart_match.dissimilarity('transpose', 'tranpsose'), 0.11111111111111116)
        self.assertEqual(smart_match.dissimilarity('uxyw', 'uyxw'), 0.25)
        self.assertEqual(smart_match.dissimilarity('uxaayw', 'uyxw'), 0.5)
        self.assertEqual(smart_match.dissimilarity('Healed', 'Sealed'), 0.16666666666666663)
        self.assertEqual(smart_match.dissimilarity('Healed', 'Healthy'), 0.4285714285714286)
        self.assertEqual(smart_match.dissimilarity('Healed', 'Heard'), 0.33333333333333337)
        self.assertEqual(smart_match.dissimilarity('Healed', 'Herded'), 0.33333333333333337)
        self.assertEqual(smart_match.dissimilarity('Healed', 'Help'), 0.5)
        self.assertEqual(smart_match.dissimilarity('Healed', 'sold'), 0.6666666666666667)
        self.assertEqual(smart_match.dissimilarity('Sam J Chapman', 'Samuel John Chapman'), 0.3157894736842105)
        self.assertEqual(smart_match.dissimilarity('Sam Chapman', 'S Chapman'), 0.18181818181818177)
        self.assertEqual(smart_match.dissimilarity('John Smith', 'Samuel John Chapman'), 0.6842105263157895)
        self.assertEqual(smart_match.dissimilarity('John Smith', 'Sam Chapman'), 0.7272727272727273)
        self.assertEqual(smart_match.dissimilarity('John Smith', 'Sam J Chapman'), 0.7692307692307692)
        self.assertEqual(smart_match.dissimilarity('John Smith', 'S Chapman'), 0.8)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications', 'Web Database Applications with PHP & MySQL'),0.40476190476190477)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','Creating Database Web Applications with PHP and ASP'),0.5490196078431373)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications', 'Building Database Applications on the Web Using PHP3'),0.5769230769230769)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','Building Web Database Applications with Visual Studio 6'),0.5454545454545454)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications', 'Web Application Development With PHP'),0.5833333333333333)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.7126436781609196)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.8253968253968254)
        self.assertEqual(smart_match.dissimilarity('Web Database Applications', 'How to Find a Scholarship Online'),0.71875)
        self.assertEqual(smart_match.dissimilarity('Web Aplications', 'Web Database Applications with PHP & MySQL'),0.6428571428571428)
        self.assertEqual(smart_match.dissimilarity('Web Aplications', 'Creating Database Web Applications with PHP and ASP'),0.7058823529411764)
        self.assertEqual(smart_match.dissimilarity('Web Aplications', 'Building Database Applications on the Web Using PHP3'), 0.75)
        self.assertEqual(smart_match.dissimilarity('Web Aplications', 'Building Web Database Applications with Visual Studio 6'),0.7272727272727273)
        self.assertEqual(smart_match.dissimilarity('Web Aplications', 'Web Application Development With PHP'),0.6111111111111112)
        self.assertEqual(smart_match.dissimilarity('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.8275862068965517)
        self.assertEqual(smart_match.dissimilarity('Web Aplications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.873015873015873)
        self.assertEqual(smart_match.dissimilarity('Web Aplications', 'How to Find a Scholarship Online'), 0.8125)
    
    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'hill'), 3)
        self.assertEqual(smart_match.distance('test string1', 'test string2'), 2)
        self.assertEqual(smart_match.distance('test', 'test string2'), 8)
        self.assertEqual(smart_match.distance('', 'test string2'), 12)
        self.assertEqual(smart_match.distance('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 6)
        self.assertEqual(smart_match.distance('aaa bbb', 'aaa aaa'), 6)
        self.assertEqual(smart_match.distance('aaa', 'aaa aaa'), 4)
        self.assertEqual(smart_match.distance('a b c d', 'a b c e'), 2)
        self.assertEqual(smart_match.distance('uxyw', 'uyxw'), 2)
        self.assertEqual(smart_match.distance('uxaayw', 'uyxw'), 4)
        self.assertEqual(smart_match.distance('transpose', 'tranpsose'), 2)
        self.assertEqual(smart_match.distance('Healed', 'Sealed'), 2)
        self.assertEqual(smart_match.distance('Healed', 'Healthy'), 5)
        self.assertEqual(smart_match.distance('Healed', 'Heard'), 3)
        self.assertEqual(smart_match.distance('Healed', 'Herded'), 4)
        self.assertEqual(smart_match.distance('Healed', 'Help'), 4)
        self.assertEqual(smart_match.distance('Healed', 'sold'), 6)
        self.assertEqual(smart_match.distance('Sam J Chapman', 'Samuel John Chapman'), 6)
        self.assertEqual(smart_match.distance('Sam Chapman', 'S Chapman'), 2)
        self.assertEqual(smart_match.distance('John Smith', 'Samuel John Chapman'), 17)
        self.assertEqual(smart_match.distance('John Smith', 'Sam Chapman'), 15)
        self.assertEqual(smart_match.distance('John Smith', 'Sam J Chapman'), 17)
        self.assertEqual(smart_match.distance('John Smith', 'S Chapman'), 15)
        self.assertEqual(smart_match.distance('Web Database Applications', 'Web Database Applications with PHP & MySQL'), 17)
        self.assertEqual(smart_match.distance('Web Database Applications', 'Creating Database Web Applications with PHP and ASP'),30)
        self.assertEqual(smart_match.distance('Web Database Applications', 'Building Database Applications on the Web Using PHP3'), 33)
        self.assertEqual(smart_match.distance('Web Database Applications', 'Building Web Database Applications with Visual Studio 6'),30)
        self.assertEqual(smart_match.distance('Web Database Applications', 'Web Application Development With PHP'), 31)
        self.assertEqual(smart_match.distance('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),62)
        self.assertEqual(smart_match.distance('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'), 66)
        self.assertEqual(smart_match.distance('Web Database Applications','How to Find a Scholarship Online'), 39)
        self.assertEqual(smart_match.distance('Web Aplications', 'Web Database Applications with PHP & MySQL'), 27)
        self.assertEqual(smart_match.distance('Web Aplications', 'Creating Database Web Applications with PHP and ASP'), 36)
        self.assertEqual(smart_match.distance('Web Aplications', 'Building Database Applications on the Web Using PHP3'),41)
        self.assertEqual(smart_match.distance('Web Aplications','Building Web Database Applications with Visual Studio 6'), 40)
        self.assertEqual(smart_match.distance('Web Aplications', 'Web Application Development With PHP'), 23)
        self.assertEqual(smart_match.distance('Web Aplications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'), 72)
        self.assertEqual(smart_match.distance('Web Aplications','Structural Assessment: The Role of Large and Full-Scale Testing'), 62)
        self.assertEqual(smart_match.distance('Web Aplications', 'How to Find a Scholarship Online'), 35)

    def test_score(self):
        self.assertEqual(smart_match.score('hello', 'hill'), 3)
        self.assertEqual(smart_match.score('test string1', 'test string2'), 11)
        self.assertEqual(smart_match.score('test', 'test string2'), 4)
        self.assertEqual(smart_match.score('', 'test string2'), 0)
        self.assertEqual(smart_match.score('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 12)
        self.assertEqual(smart_match.score('aaa bbb', 'aaa aaa'), 4)
        self.assertEqual(smart_match.score('aaa', 'aaa aaa'), 3)
        self.assertEqual(smart_match.score('a b c d', 'a b c e'), 6)
        self.assertEqual(smart_match.score('transpose', 'tranpsose'), 8)
        self.assertEqual(smart_match.score('uxyw', 'uyxw'), 3)
        self.assertEqual(smart_match.score('uxaayw', 'uyxw'), 3)
        self.assertEqual(smart_match.score('Healed', 'Sealed'), 5)
        self.assertEqual(smart_match.score('Healed', 'Healthy'), 4)
        self.assertEqual(smart_match.score('Healed', 'Heard'), 4)
        self.assertEqual(smart_match.score('Healed', 'Herded'), 4)
        self.assertEqual(smart_match.score('Healed', 'Help'), 3)
        self.assertEqual(smart_match.score('Healed', 'sold'), 2)
        self.assertEqual(smart_match.score('Sam J Chapman', 'Samuel John Chapman'), 13)
        self.assertEqual(smart_match.score('Sam Chapman', 'S Chapman'), 9)
        self.assertEqual(smart_match.score('John Smith', 'Samuel John Chapman'), 6)
        self.assertEqual(smart_match.score('John Smith', 'Sam Chapman'), 3)
        self.assertEqual(smart_match.score('John Smith', 'Sam J Chapman'), 3)
        self.assertEqual(smart_match.score('John Smith', 'S Chapman'), 2)
        self.assertEqual(smart_match.score('Web Database Applications', 'Web Database Applications with PHP & MySQL'), 25)
        self.assertEqual(smart_match.score('Web Database Applications', 'Creating Database Web Applications with PHP and ASP'), 23)
        self.assertEqual(smart_match.score('Web Database Applications', 'Building Database Applications on the Web Using PHP3'),22)
        self.assertEqual(smart_match.score('Web Database Applications','Building Web Database Applications with Visual Studio 6'), 25)
        self.assertEqual(smart_match.score('Web Database Applications', 'Web Application Development With PHP'), 15)
        self.assertEqual(smart_match.score('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),25)
        self.assertEqual(smart_match.score('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'), 11)
        self.assertEqual(smart_match.score('Web Database Applications', 'How to Find a Scholarship Online'), 9)
        self.assertEqual(smart_match.score('Web Aplications', 'Web Database Applications with PHP & MySQL'), 15)
        self.assertEqual(smart_match.score('Web Aplications', 'Creating Database Web Applications with PHP and ASP'),15)
        self.assertEqual(smart_match.score('Web Aplications', 'Building Database Applications on the Web Using PHP3'), 13)
        self.assertEqual(smart_match.score('Web Aplications', 'Building Web Database Applications with Visual Studio 6'), 15)
        self.assertEqual(smart_match.score('Web Aplications', 'Web Application Development With PHP'), 14)
        self.assertEqual(smart_match.score('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),15)
        self.assertEqual(smart_match.score('Web Aplications', 'Structural Assessment: The Role of Large and Full-Scale Testing'),8)
        self.assertEqual(smart_match.score('Web Aplications', 'How to Find a Scholarship Online'), 6)

if __name__ == '__main__':
    unittest.main()
