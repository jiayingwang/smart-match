import unittest
import smart_match


class TestNeedlemanWunch(unittest.TestCase):

    def setUp(self):
        smart_match.use('NW')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.9583333333333334)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.similarity('GATTACA', 'GCATGCU'), 0.5)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.similarity('a b c d', 'a b c e'), 0.8571428571428571)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sealed'), 0.8333333333333334)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Healthy'), 0.5714285714285714)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Help'), 0.5)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sold'), 0.3333333333333333)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Help'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('Sam J Chapman', 'Samuel John Chapman'), 0.6842105263157895)
        self.assertAlmostEqual(smart_match.similarity('Sam Chapman', 'S Chapman'), 0.8181818181818182)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Samuel John Chapman'), 0.2894736842105263)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam Chapman'), 0.09090909090909091)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam J Chapman'), 0.15384615384615385)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'S Chapman'), 0.15)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Web Database Applications with PHP & MySQL'), 0.5952380952380952)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Creating Database Web Applications with PHP and ASP'),
                               0.45098039215686275)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Building Database Applications on the Web Using PHP3'),
                               0.4230769230769231)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Building Web Database Applications with Visual Studio 6'),
                               0.45454545454545453)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Web Application Development With PHP'), 0.2916666666666667)

        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'WebRAD: Building Database Applications on the'
                                                      ' Web with Visual FoxPro and Web Connection'),
                               0.28735632183908044)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'Structural Assessment: The Role of Large and Full-Scale Testing')
                               , 0.16666666666666666)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications',
                                                      'How to Find a Scholarship Online'), 0.171875)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications',
                                                      'Web Database Applications with PHP & MySQL'),
                               0.35714285714285715)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.04166666666666663)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.dissimilarity('GATTACA', 'GCATGCU'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('a b c d', 'a b c e'), 0.1428571428571429)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Sealed'), 0.16666666666666663)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Healthy'), 0.4285714285714286)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Heard'), 0.33333333333333337)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Help'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Sold'), 0.6666666666666667)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed', 'Help'), 0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('Sam J Chapman', 'Samuel John Chapman'), 0.3157894736842105)
        self.assertAlmostEqual(smart_match.dissimilarity('Sam Chapman', 'S Chapman'), 0.18181818181818177)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'Samuel John Chapman'), 0.7105263157894737)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'Sam Chapman'), 0.9090909090909091)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'Sam J Chapman'), 0.8461538461538461)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith', 'S Chapman'), 0.85)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Web Database Applications with PHP & MySQL'),
                               0.40476190476190477)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Creating Database Web Applications with PHP and ASP'),
                               0.5490196078431373)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Building Database Applications on the Web Using PHP3'),
                               0.57692307692307693)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Building Web Database Applications with Visual Studio 6'),
                               0.5454545454545454)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Web Application Development With PHP'),
                               0.7083333333333333)

        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'WebRAD: Building Database Applications on the'
                                                         ' Web with Visual FoxPro and Web Connection'),
                               0.7126436781609196)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'Structural Assessment: The Role of Large and'
                                                         ' Full-Scale Testing'), 0.8333333333333334)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications',
                                                         'How to Find a Scholarship Online'), 0.828125)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications',
                                                         'Web Database Applications with PHP & MySQL'),
                               0.6428571428571428)

    def test_score(self):
        self.assertEqual(smart_match.score('test string1', 'test string2'), -1)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertEqual(smart_match.score('GATTACA', 'GCATGCU'), 0)
        self.assertAlmostEqual(smart_match.score('Healed', 'Help'), 0)
        smart_match.set_params(gap=-1, mismatch=-1, match=1)
        self.assertAlmostEqual(smart_match.score('Sam J Chapman', 'Samuel John Chapman'), 7)
        self.assertAlmostEqual(smart_match.score('Sam Chapman', 'S Chapman'), 7)
        self.assertAlmostEqual(smart_match.score('John Smith', 'Samuel John Chapman'), -8)
        self.assertAlmostEqual(smart_match.score('John Smith', 'Sam Chapman'), -9)
        self.assertAlmostEqual(smart_match.score('John Smith', 'Sam J Chapman'), -9)
        self.assertAlmostEqual(smart_match.score('John Smith', 'S Chapman'), -7)
        self.assertAlmostEqual(smart_match.score('Web Database Applications',
                                                 'Web Database Applications with PHP & MySQL'), 8)
        self.assertAlmostEqual(smart_match.score('Web Database Applications',
                                                 'Building Web Database Applications with Visual Studio 6'),-5)
        self.assertAlmostEqual(smart_match.score('Web Database Applications',
                                                 'Web Application Development With PHP'),-15)

        self.assertAlmostEqual(smart_match.score('Web Database Applications',
                                                 'WebRAD: Building Database Applications on the'
                                                 ' Web with Visual FoxPro and Web Connection'),-37)
        self.assertAlmostEqual(smart_match.score('Web Database Applications',
                                                 'Structural Assessment: The Role of Large and'
                                                 ' Full-Scale Testing'), -42)
        self.assertAlmostEqual(smart_match.score('Web Database Applications',
                                                 'How to Find a Scholarship Online'), -21)
        self.assertAlmostEqual(smart_match.score('Web Aplications',
                                                 'Web Database Applications with PHP & MySQL'),-12)


if __name__ == '__main__':
    unittest.main()
