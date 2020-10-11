import unittest
import smart_match


class TestSimonWhite(unittest.TestCase):

    def setUp(self):
        smart_match.use('simon')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('abbcccdd', 'aaabccee'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('hello', 'hollow'), 0.7272727272727273)


        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)


        smart_match.set_params(level=2)
        self.assertAlmostEqual(smart_match.similarity('test', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.8888888888888888)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sealed'), 0.8)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Healthy'), 0.5454545454545454)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Heard'), 0.4444444444444444)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Herded'), 0.4)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Help'), 0.25)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'sold'), 0.0)

        self.assertAlmostEqual(smart_match.similarity('Sam J Chapman', 'Samuel John Chapman'),0.7272727272727273)
        self.assertAlmostEqual(smart_match.similarity('Sam Chapman', 'S Chapman'), 0.8571428571428571)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Samuel John Chapman'),0.2857142857142857)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam Chapman'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam J Chapman'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'S Chapman'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Web Database Applications with PHP & MySQL'),0.8163265306122449)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Creating Database Web Applications with PHP and ASP'),0.7142857142857143)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Building Database Applications on the Web Using PHP3'),0.7017543859649122)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','Building Web Database Applications with Visual Studio 6'),0.6666666666666666)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Web Application Development With PHP'),0.5106382978723404)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.4878048780487805)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.09090909090909091)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'How to Find a Scholarship Online'),0.04878048780487805)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Web Database Applications with PHP & MySQL'),0.5853658536585366)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Creating Database Web Applications with PHP and ASP'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Building Database Applications on the Web Using PHP3'),0.4897959183673469)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Building Web Database Applications with Visual Studio 6'),0.46153846153846156)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'Web Application Development With PHP'),0.5641025641025641)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.32432432432432434)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.06896551724137931)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications', 'How to Find a Scholarship Online'),0.06060606060606061)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('abbcccdd', 'aaabccee'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hollow'), 0.2727272727272727)

        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.5)

        smart_match.set_params(level=2)
        self.assertAlmostEqual(smart_match.dissimilarity('test', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.11111111111111116)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Sealed'), 0.19999999999999996)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Healthy'), 0.4545454545454546)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Heard'), 0.5555555555555556)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Herded'), 0.6)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Help'), 0.75)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'sold'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Sam J Chapman', 'Samuel John Chapman'),0.2727272727272727)
        self.assertAlmostEqual(smart_match.dissimilarity('Sam Chapman', 'S Chapman'), 0.1428571428571429)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'Samuel John Chapman'),0.7142857142857143)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'Sam Chapman'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'Sam J Chapman'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'S Chapman'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications', 'Web Database Applications with PHP & MySQL'),0.18367346938775508)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications', 'Creating Database Web Applications with PHP and ASP'),0.2857142857142857)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications', 'Building Database Applications on the Web Using PHP3'),0.29824561403508776)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','Building Web Database Applications with Visual Studio 6'),0.33333333333333337)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications', 'Web Application Development With PHP'),0.4893617021276596)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.5121951219512195)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.9090909090909091)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications', 'How to Find a Scholarship Online'),0.9512195121951219)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications', 'Web Database Applications with PHP & MySQL'),0.41463414634146345)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications', 'Creating Database Web Applications with PHP and ASP'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications', 'Building Database Applications on the Web Using PHP3'),0.5102040816326531)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications', 'Building Web Database Applications with Visual Studio 6'),0.5384615384615384)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications', 'Web Application Development With PHP'),0.4358974358974359)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.6756756756756757)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.9310344827586207)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications', 'How to Find a Scholarship Online'),0.9393939393939394)


if __name__ == '__main__':
    unittest.main()