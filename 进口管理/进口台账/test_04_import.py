import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os

class MyTestCase(unittest.TestCase):
    def setUp(self) :
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # 账号密码登陆系统================================================================================================
        self.driver.get("http://192.168.0.199:5008/Home/Index?menuid=Chery")

        elem = self.driver.find_element_by_name("uname")
        elem.send_keys("17601473754")
        time.sleep(1)
        elem = self.driver.find_element_by_name("upwd")
        elem.send_keys("123456")
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        # 切换工厂
        self.driver.find_element_by_css_selector("a[longnows-event='changeSite']").click()
        time.sleep(5)

        # 定位到弹框,用window_handles
        windowhandle1 = self.driver.window_handles
        print("切换工厂弹框" + windowhandle1[0])
        self.driver.switch_to.window(windowhandle1[0])
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='searchSite']/div[6]/i").click()
        time.sleep(1)
        # 点击确定按钮
        self.driver.find_element_by_link_text("确认").click()
        time.sleep(2)
        # =================================点击进出口管理================================================================
        # time.sleep(20)
        elem3 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[3]/a/span')
        ActionChains(self.driver).click(elem3).perform()
        time.sleep(3)

        # 点击进口管理
        elem4 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[3]/dl/dd[2]/a/span')
        ActionChains(self.driver).click(elem4).perform()
        time.sleep(5)

        # 点击进口台账
        elem5 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[3]/dl/dd[2]/dl/dd[2]/a/cite')
        ActionChains(self.driver).click(elem5).perform()
        time.sleep(8)



    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        print('Test Over')

    # 具体的测试用例，一定要以test开头
    def test_4_import(self):
        # ========编辑=================

        # 定位到iframe时
        elem52 = self.driver.find_element_by_xpath('//*[@id="longnows_body"]/div[2]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(elem52)
        # 勾选列表页面第一条数据
        self.driver.find_element_by_xpath(
            '//*[@class="layui-table-box"]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/div/i').click()
        time.sleep(2)
        # 点击编辑按钮
        self.driver.find_element_by_xpath(
            '//*[@class="layui-table-box"]/div[4]/div[2]/table/tbody/tr/td/div/button/i').click()
        time.sleep(5)
        # 获取当前打开的所有窗口的句柄

        num1 = self.driver.window_handles
        print("编辑页面句柄" + num1[0])
        self.driver.switch_to.window(num1[0])
        # 进入编辑页面======================

        elem53 = self.driver.find_element_by_xpath('//*[@id="longnows_body"]/div[2]/div[2]/div[3]/iframe')
        self.driver.switch_to.frame(elem53)
        time.sleep(2)

        # ===========================================表体=====

        # 点击导入按钮
        elem42 = self.driver.find_element_by_xpath('//*[@id="listImport"]')
        ActionChains(self.driver).click(elem42).perform()
        time.sleep(2)
        # 绝对路径改为相对路径
        current_dir = os.path.dirname(os.path.realpath(__file__))
        print(current_dir)
        path_to_excel = os.path.join(current_dir, "进口-导入模板_台账表体导入.xls")
        # 点击选择文件按钮
        elem43 = self.driver.find_element_by_xpath('//*[@id="excelImportFormFile"]').send_keys("D:\\PythonProject\Cherry_Discover\\Import_file\\进口-导入模板_台账表体导入.xls")
        time.sleep(2)
        # 点击上传按钮
        elem44 = self.driver.find_element_by_xpath('//*[@id="excelImportFormDialog"]/div[2]/button[2]')
        ActionChains(self.driver).click(elem44).perform()
        time.sleep(2)
        self.driver.get_screenshot_as_file("D:\\PythonProject\\Cherry_Discover\\Image\\import.png")
        # ==============================================退出======================================================

        # 跳出iframe，点击取消按钮
        self.driver.switch_to.default_content()
        # 点击新增关闭按钮
        self.driver.find_element_by_css_selector("#tab_title_container > li.layui-this > i").click()
        time.sleep(5)