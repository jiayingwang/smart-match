import unittest
import smart_match

class TestEuclideanDistance(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('ED')

    def test_similarity(self):
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('hello', 'hero'), 0.0)
        self.assertAlmostEqual(smart_match.similarity('hello', 'ehllo'),0.0)
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)
        self.assertAlmostEqual(smart_match.similarity('test','test string2'),0.5527864045000421)
        self.assertAlmostEqual(smart_match.similarity('','test string2'),0.2928932188134524)
        self.assertAlmostEqual(smart_match.similarity('aaa bbb ccc ddd','aaa bbb ccc eee'),0.75)
        self.assertAlmostEqual(smart_match.similarity('a b c d','a b c e'),0.75)
        self.assertAlmostEqual(smart_match.similarity('a b c d','a b c e f'),0.7294991095997703)
        self.assertAlmostEqual(smart_match.similarity('a b c d','a b e f'),0.6464466094067263)
        self.assertAlmostEqual(smart_match.similarity('a b c','a b c e f g'),0.7418011102528389)
        self.assertAlmostEqual(smart_match.similarity('a b b c c','a b c e f g'),0.7137008328430658)
        self.assertAlmostEqual(smart_match.similarity('Healed','Sealed'),0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed','Healthy'),0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed','Heard'),0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed','Herded'),0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed','Help'),0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed','Sold'),0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed','Help'),0.0)
        self.assertAlmostEqual(smart_match.similarity('Healed','So'),0.0)
        self.assertAlmostEqual(smart_match.similarity('Sam J Chapman','Samuel John Chapman'),0.5285954792089682)
        self.assertAlmostEqual(smart_match.similarity('Sam Chapman','S Chapman'),0.5)
        self.assertAlmostEqual(smart_match.similarity('John Smith','Samuel John Chapman'),0.5196155385847385)
        self.assertAlmostEqual(smart_match.similarity('John Smith','Sam Chapman'),0.29289321881345254)
        self.assertAlmostEqual(smart_match.similarity('John Smith','Sam J Chapman'),0.3798263270539577)
        self.assertAlmostEqual(smart_match.similarity('John Smith','S Chapman'),0.29289321881345254)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','Web Database Applications with PHP & MySQL'),0.7373871342805549)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','Creating Database Web Applications with PHP and ASP'),0.7382880387048931)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','Building Database Applications on the Web Using PHP3'),0.7382880387048931)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','Building Web Database Applications with Visual Studio 6'),0.7382880387048931)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','Web Application Development With PHP'),0.5799159747915972)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.7629772684300113)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.6348516283298893)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications','How to Find a Scholarship Online'),0.5527864045000421)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications','Web Database Applications with PHP & MySQL'),0.6365781078441844)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications','Creating Database Web Applications with PHP and ASP'),0.6570028297149824)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications','Building Database Applications on the Web Using PHP3'),0.6570028297149824)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications','Web Application Development With PHP'),0.5847726007313001)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.7258750126848699)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.6402615329077492)
        self.assertAlmostEqual(smart_match.similarity('Web Aplications','How to Find a Scholarship Online'),0.5527864045000421)
        
    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hero'), 0.34921514788478913)
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'ehllo'),0.0)
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.08333333333333334)
        self.assertAlmostEqual(smart_match.dissimilarity('test','test string2'),0.22360679774997896)
        self.assertAlmostEqual(smart_match.dissimilarity('','test string2'),0.37267799624996495)
        self.assertAlmostEqual(smart_match.dissimilarity('aaa bbb ccc ddd','aaa bbb ccc eee'),0.19999999999999998)
        self.assertAlmostEqual(smart_match.dissimilarity('a b c d','a b c e'),0.14285714285714288)
        self.assertAlmostEqual(smart_match.dissimilarity('a b c d','a b c e f'),0.17541160386140586)
        self.assertAlmostEqual(smart_match.dissimilarity('a b c d','a b e f'),0.20203050891044214)
        self.assertAlmostEqual(smart_match.dissimilarity('a b c','a b c e f g'),0.28669108954049793)
        self.assertAlmostEqual(smart_match.dissimilarity('a b b c c','a b c e f g'),0.1723454968864278)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed','Sealed'),0.16666666666666669)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed','Healthy'),0.242535625036333)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed','Heard'),0.22176638128637186)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed','Herded'),0.23570226039551587)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed','Help'),0.2773500981126146)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed','Sold'),0.3922322702763681)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed','Help'),0.2773500981126146)
        self.assertAlmostEqual(smart_match.dissimilarity('Healed','So'),0.5)
        self.assertAlmostEqual(smart_match.dissimilarity('Sam J Chapman','Samuel John Chapman'),0.1063990353197863)
        self.assertAlmostEqual(smart_match.dissimilarity('Sam Chapman','S Chapman'),0.09950371902099893)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith','Samuel John Chapman'),0.2030141634031955)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith','Sam Chapman'),0.2773500981126146)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith','Sam J Chapman'),0.25139018680589903)
        self.assertAlmostEqual(smart_match.dissimilarity('John Smith','S Chapman'),0.2465227791969404)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','Web Database Applications with PHP & MySQL'),0.11391286426309005)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','Creating Database Web Applications with PHP and ASP'),0.13637772569945572)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','Building Database Applications on the Web Using PHP3'),0.13756671829544148)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','Building Web Database Applications with Visual Studio 6'),0.14988580127769788)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','Web Application Development With PHP'),0.13878329029749603)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.1760633165448035)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.17827109516018724)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Database Applications','How to Find a Scholarship Online'),0.16519463133513965)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications','Web Database Applications with PHP & MySQL'),0.16928560745943824)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications','Creating Database Web Applications with PHP and ASP'),0.19183621228155442)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications','Building Database Applications on the Web Using PHP3'),0.18009519124771117)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications','Web Application Development With PHP'),0.16418267275468842)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),0.20388829980917544)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications','Structural Assessment: The Role of Large and Full-Scale Testing'),0.20945691294067176)
        self.assertAlmostEqual(smart_match.dissimilarity('Web Aplications','How to Find a Scholarship Online'),0.18118018933869962)

    def test_distance(self):
        self.assertEqual(smart_match.distance('hello', 'hero'), 2.23606797749979)
        self.assertEqual(smart_match.distance('hello', 'ehllo'), 0.0)
        self.assertEqual(smart_match.distance('test string1', 'test string2'),1.4142135623730951)
        self.assertEqual(smart_match.distance('test','test string2'),2.8284271247461903)
        self.assertEqual(smart_match.distance('','test string2'),4.47213595499958)
        self.assertEqual(smart_match.distance('aaa bbb ccc ddd','aaa bbb ccc eee'),4.242640687119285)
        self.assertEqual(smart_match.distance('a b c d','a b c e'),1.4142135623730951)
        self.assertEqual(smart_match.distance('a b c d','a b c e f'),2.0)
        self.assertEqual(smart_match.distance('a b c d','a b e f'),2.0)
        self.assertEqual(smart_match.distance('a b c','a b c e f g'),3.4641016151377544)
        self.assertEqual(smart_match.distance('a b b c c','a b c e f g'),2.449489742783178)
        self.assertEqual(smart_match.distance('Healed','Sealed'),1.4142135623730951)
        self.assertEqual(smart_match.distance('Healed','Healthy'),2.23606797749979)
        self.assertEqual(smart_match.distance('Healed','Heard'),1.7320508075688772)
        self.assertEqual(smart_match.distance('Healed','Herded'),2.0)
        self.assertEqual(smart_match.distance('Healed','Help'),2.0)
        self.assertEqual(smart_match.distance('Healed','Sold'),2.8284271247461903)
        self.assertEqual(smart_match.distance('Healed','Help'),2.0)
        self.assertEqual(smart_match.distance('Healed','So'),3.1622776601683795)
        self.assertEqual(smart_match.distance('Sam J Chapman','Samuel John Chapman'),2.449489742783178)
        self.assertEqual(smart_match.distance('Sam Chapman','S Chapman'),1.4142135623730951)
        self.assertEqual(smart_match.distance('John Smith','Samuel John Chapman'),4.358898943540674)
        self.assertEqual(smart_match.distance('John Smith','Sam Chapman'),4.123105625617661)
        self.assertEqual(smart_match.distance('John Smith','Sam J Chapman'),4.123105625617661)
        self.assertEqual(smart_match.distance('John Smith','S Chapman'),3.3166247903554)
        self.assertEqual(smart_match.distance('Web Database Applications','Web Database Applications with PHP & MySQL'),5.5677643628300215)
        self.assertEqual(smart_match.distance('Web Database Applications','Creating Database Web Applications with PHP and ASP'),7.745966692414834)
        self.assertEqual(smart_match.distance('Web Database Applications','Building Database Applications on the Web Using PHP3'),7.937253933193772)
        self.assertEqual(smart_match.distance('Web Database Applications','Building Web Database Applications with Visual Studio 6'),9.055385138137417)
        self.assertEqual(smart_match.distance('Web Database Applications','Web Application Development With PHP'),6.082762530298219)
        self.assertEqual(smart_match.distance('Web Database Applications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),15.937377450509228)
        self.assertEqual(smart_match.distance('Web Database Applications','Structural Assessment: The Role of Large and Full-Scale Testing'),12.083045973594572)
        self.assertEqual(smart_match.distance('Web Database Applications','How to Find a Scholarship Online'),6.708203932499369)
        self.assertEqual(smart_match.distance('Web Aplications','Web Database Applications with PHP & MySQL'),7.54983443527075)
        self.assertEqual(smart_match.distance('Web Aplications','Creating Database Web Applications with PHP and ASP'),10.198039027185569)
        self.assertEqual(smart_match.distance('Web Aplications','Building Database Applications on the Web Using PHP3'),9.746794344808963)
        self.assertEqual(smart_match.distance('Web Aplications','Web Application Development With PHP'),6.4031242374328485)
        self.assertEqual(smart_match.distance('Web Aplications','WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'),18.0)
        self.assertEqual(smart_match.distance('Web Aplications','Structural Assessment: The Role of Large and Full-Scale Testing'),13.564659966250536)
        self.assertEqual(smart_match.distance('Web Aplications','How to Find a Scholarship Online'),6.4031242374328485)

if __name__ == '__main__':
    unittest.main()