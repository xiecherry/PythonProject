import sys
import unittest
from Cherry_Discover.Case1 import test_01_create, test_02_edit

if __name__ == '__main__':
    # 分三步走：第一步testloader根据传入的参数获得相应的测试用例，即对应具体的测试方法，
    # 然后makesuite在把所有的测试用例组装成testsuite，
    # 最后把testsiute传给testrunner进行执行。
    # loadTestsFromNames数组元素传入格式：'moudleName.testCaseClassName.testCaseName'
    # cases = ['Case1.test_01_create.MyTestCase','Case1.test_02_edit.MyTestCase']
    # 精确到对应的方法名称,写哪个就执行哪个
    cases = ['Case1.test_02_edit.MyTestCase.test_2_edit']

    suite1 = unittest.TestLoader().loadTestsFromNames(cases)
    suite = unittest.TestSuite()
    suite.addTest(suite1)
    # 测试结果展示内容
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)