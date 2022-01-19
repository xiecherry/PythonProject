import sys
import unittest
from Cherry_Discover import Case1


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Case1.test_02_edit.MyTestCase)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Case1.test_03_detail.MyTestCase)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner().run(suite)