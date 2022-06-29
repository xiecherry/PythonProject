import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os



# 物料审核页面查询

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # 账号密码登陆系统================================================================================================
        self.driver.get("http://192.168.0.199:5008/Home/Index?menuid=Chery")

        elem = self.driver.find_element_by_name("uname")
        elem.send_keys("17601473711")
        time.sleep(1)
        elem = self.driver.find_element_by_name("upwd")
        elem.send_keys("123456")
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        # 切换工厂
        # self.driver.find_element_by_css_selector("a[longnows-event='changeSite']").click()
        # time.sleep(5)
        #
        # # 定位到弹框,用window_handles
        # windowhandle1 = self.driver.window_handles
        # print("切换工厂弹框" + windowhandle1[0])
        # self.driver.switch_to.window(windowhandle1[0])
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//*[@id='searchSite']/div[6]/i").click()
        # time.sleep(1)
        # # 点击确定按钮
        # self.driver.find_element_by_link_text("确认").click()
        # time.sleep(2)

        # =====点击基础资料模块================================================================
        # time.sleep(20)
        elem3 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/a/i')
        ActionChains(self.driver).click(elem3).perform()
        time.sleep(3)

        # 点击物料审核
        elem4 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/dl/dd[3]/a/cite')
        ActionChains(self.driver).click(elem4).perform()
        time.sleep(2)
        # 再点击子模块物料审核
        elem41 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/dl/dd[3]/dl/dd/a/cite')
        ActionChains(self.driver).click(elem41).perform()
        time.sleep(2)


        # 定位新的iframe
        elem6 = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(elem6)
        time.sleep(3)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        print('Test Over')


    # 具体的测试用例，一定要以test开头
    def test_11_audit_search(self):
        #设置审核状态下拉
        elem18 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem18).perform()
        time.sleep(2)

        #下拉选择我已审核
        elem19 = self.driver.find_element_by_xpath('/html/body/div[8]/div/div[2]')
        ActionChains(self.driver).click(elem19).perform()
        time.sleep(2)
        #点击查询按钮
        elem20 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/button[1]')
        ActionChains(self.driver).click(elem20).perform()
        time.sleep(2)

        #点击重置按钮
        elem21 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/button[2]')
        ActionChains(self.driver).click(elem21).perform()
        time.sleep(2)

        #点击查询按钮
        elem20 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/button[1]')
        ActionChains(self.driver).click(elem20).perform()
        time.sleep(2)


