import unittest
import os
import HTMLTestRunner
import time


# os.getcwd() 方法用于返回当前工作目录。

# 用例路径
case_path = os.path.join(os.getcwd(),"报关行")
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
    report_dir = os.path.join(os.getcwd(),"进口台账报表")
    print(report_dir)
    # 创建报告输入的文件位置
    report_file = report_dir+'\\'+now+'report.html'
    # 判断文件目录是否存在，如果不存在则创建目录
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)
    # 打开报表文件并写入
    file_result = open(report_file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=file_result,
        title='Test 合作伙伴管理-报关行',
        description='报关行测试报告'
    )
    runner.run(all_case())
