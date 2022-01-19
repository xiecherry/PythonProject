import unittest
import os
import HTMLTestRunner
import time


# os.getcwd() 方法用于返回当前工作目录。

# 用例路径
case_path = os.path.join(os.getcwd(),"Case1")
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    print(discover)
    return discover

if __name__ == '__main__':
    # 时间戳
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # 报告地址及报告名称
    # file_path = 'D:\\PythonProject\\Cherry_Discover\\HTMLReport\\report.html'
    file_path = 'D:\PythonProject\Cherry_Discover\HTMLReport\\'+now+'report.html'
    file_result = open(file_path, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=file_result,
        title='Test Report11',
        description='Test Result22'
    )
    # runner = unittest.TextTestRunner()
    runner.run(all_case())




