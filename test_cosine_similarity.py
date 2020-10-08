import unittest
import smart_match


class TestCosineSimilarity(unittest.TestCase):

    def setUp(self):
        smart_match.use('cos')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'hero'), 0.5669467095138409)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('test', 'test string2'), 0.7071067811865475)
        self.assertAlmostEqual(smart_match.similarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.75)
        self.assertAlmostEqual(smart_match.similarity('a b c d', 'a b c e'), 0.75)
        self.assertAlmostEqual(smart_match.similarity('a b c d', 'a b e f'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('a b c', 'a b c e f g'), 0.7071067811865476)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sealed'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Healthy'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Heard'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Help'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sold'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Help'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('Sam J Chapman', 'Samuel John Chapman'), 0.33333333333333337)
        self.assertAlmostEqual(smart_match.similarity('Sam Chapman', 'S Chapman'), 0.4999999999999999)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Samuel John Chapman'), 0.40824829046386296)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam Chapman'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam J Chapman'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'S Chapman'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Web Database Applications with PHP & MySQL'), 0.6546536707079772)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Creating Database Web Applications with PHP and ASP'),
                               0.6123724356957945)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Building Database Applications on the Web Using PHP3'),
                               0.6123724356957945)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Building Web Database Applications with Visual Studio 6'),
                               0.6123724356957945)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Web Application Development With PHP'), 0.2581988897471611)

        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'WebRAD: Building Database Applications on the'
                                                      ' Web with Visual FoxPro and Web Connection'), 0.5962847939999439)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Structural Assessment: The Role of Large and Full-Scale Testing')
                               , 0.0)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'How to Find a Scholarship Online'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications',
                                                      'Web Database Applications with PHP & MySQL'), 0.26726124191242434)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hero'), 0.43305329048615915)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('test', 'test string2'), 0.29289321881345254)
        self.assertAlmostEqual(smart_match.dissimilarity('', 'test string2'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.25)
        self.assertAlmostEqual(smart_match.dissimilarity('a b c d', 'a b c e'), 0.25)
        self.assertAlmostEqual(smart_match.dissimilarity('a b c d', 'a b e f'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('a b c', 'a b c e f g'), 0.2928932188134524)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Sealed'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Healthy'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Heard'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Help'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Sold'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Help'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Sam J Chapman', 'Samuel John Chapman'),  0.6666666666666666)
        self.assertAlmostEqual(smart_match.dissimilarity('Sam Chapman', 'S Chapman'),  0.5000000000000001)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'Samuel John Chapman'), 0.5917517095361371)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'Sam Chapman'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'Sam J Chapman'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'S Chapman'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Web Database Applications with PHP & MySQL'),
                               0.3453463292920228)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Creating Database Web Applications with PHP and ASP'),
                               0.38762756430420553)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Building Database Applications on the Web Using PHP3'),
                               0.38762756430420553)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Building Web Database Applications with Visual Studio 6'),
                               0.38762756430420553)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Web Application Development With PHP'),
                               0.7418011102528389)

        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'WebRAD: Building Database Applications on the'
                                                         ' Web with Visual FoxPro and Web Connection'),
                               0.40371520600005606)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Structural Assessment: The Role of Large and'
                                                         ' Full-Scale Testing'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'How to Find a Scholarship Online'), 1.0)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications',
                                                         'Web Database Applications with PHP & MySQL'), 0.7327387580875757)


if __name__ == '__main__':
    unittest.main()
