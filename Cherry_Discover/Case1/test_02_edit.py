import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class MyTestCase(unittest.TestCase):
    def setUp(self) :
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # 账号密码登陆系统================================================================================================
        self.driver.get("http://192.168.2.104:5007/Home/Index?menuid=Chery")

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

    def test_2_edit(self):
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
        # 修改进境关别=====
        # 点击进境关别下拉
        elem54 = self.driver.find_element_by_xpath('//*[@id="head"]/div[3]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem54).perform()
        time.sleep(1)
        # 选择进境关闭
        elem10 = self.driver.find_element_by_xpath('/html/body/div[16]/div/div[2]')
        ActionChains(self.driver).click(elem10).perform()
        time.sleep(1)
        # 点击表头保存按钮
        elem41 = self.driver.find_element_by_xpath('/html/body/div[1]/button[contains(@lay-event,"headSave")]')
        ActionChains(self.driver).click(elem41).perform()
        time.sleep(2)
        self.driver.get_screenshot_as_file("D:\\PythonProject\\Cherry_Discover\\Image\\edit.png")

        # 跳出iframe，点击取消按钮
        self.driver.switch_to.default_content()
        # 点击新增关闭按钮
        self.driver.find_element_by_css_selector("#tab_title_container > li.layui-this > i").click()
        time.sleep(5)

    def test_5_detail(self):
        # ========详情==================================================================================================

        # 定位到iframe时
        elem52 = self.driver.find_element_by_xpath('//*[@id="longnows_body"]/div[2]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(elem52)
        # 勾选列表页面第一条数据
        self.driver.find_element_by_xpath(
            '//*[@class="layui-table-box"]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/div/i').click()
        time.sleep(2)
        # 点击详情按钮
        self.driver.find_element_by_xpath(
            '//*[@class="layui-table-box"]/div[4]/div[2]/table/tbody/tr[1]/td/div/button[2]/i').click()
        time.sleep(2)
        # 获取当前打开的所有窗口的句柄

        num1 = self.driver.window_handles
        print("详情页面句柄" + num1[0])
        self.driver.switch_to.window(num1[0])
        # 进入详情页面======================

        elem53 = self.driver.find_element_by_xpath('//*[@id="longnows_body"]/div[2]/div[2]/div[3]/iframe')
        self.driver.switch_to.frame(elem53)
        time.sleep(5)
        self.driver.get_screenshot_as_file("D:\\PythonProject\\Cherry_Discover\\Image\\detail.png")
        # 跳出iframe，点击取消按钮
        self.driver.switch_to.default_content()
        # 点击详情关闭按钮
        self.driver.find_element_by_css_selector("#tab_title_container > li.layui-this > i").click()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()