import time
import unittest

import document as document
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# 企业物料-详情页面

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # 账号密码登陆系统================================================================================================
        self.driver.get("http://192.168.0.199:5008/Home/Index?menuid=Chery")

        elem = self.driver.find_element_by_name("uname")
        elem.send_keys("17601473754")
        self.driver.implicitly_wait(2)
        elem = self.driver.find_element_by_name("upwd")
        elem.send_keys("123456")
        self.driver.implicitly_wait(5)
        elem.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)

        # 切换工厂
        self.driver.find_element_by_css_selector("a[longnows-event='changeSite']").click()
        self.driver.implicitly_wait(5)

        # 定位到弹框,用window_handles
        windowhandle1 = self.driver.window_handles
        print("切换工厂弹框" + windowhandle1[0])
        self.driver.switch_to.window(windowhandle1[0])
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='searchSite']/div[6]/i").click()
        self.driver.implicitly_wait(2)
        # 点击确定按钮
        self.driver.find_element_by_link_text("确认").click()
        self.driver.implicitly_wait(2)

        # =====点击基础资料模块================================================================
        # time.sleep(20)
        elem3 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/a/i')
        ActionChains(self.driver).click(elem3).perform()
        self.driver.implicitly_wait(2)

        # 点击企业物料1//*[@id="nav-left"]/li[2]/dl/dd[2]/a
        elem4 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/dl/dd[2]/a')
        ActionChains(self.driver).click(elem4).perform()
        self.driver.implicitly_wait(2)
        # 再点击企业物料
        elem4 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/dl/dd[2]/dl/dd[1]/a')
        ActionChains(self.driver).click(elem4).perform()
        self.driver.implicitly_wait(2)


        # 定位新的iframe
        elem6 = self.driver.find_element_by_xpath('//*[@id="longnows_tab_container"]/div[2]/iframe')
        self.driver.switch_to.frame(elem6)
        self.driver.implicitly_wait(2)


    def tearDown(self):
        self.driver.implicitly_wait(2)
        self.driver.quit()
        print('Test Over')

    def test_16_enterprise_detail(self):
        # ====================================================表头==============================================
        # 再定位新的iframe
        elem15 = self.driver.find_element_by_xpath('//*[@id="mainFrame"]')
        self.driver.switch_to.frame(elem15)
        self.driver.implicitly_wait(2)
        # 查询审核状态是已通过的数据


        # 勾选一条数据
        elem16 = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/div/i')
        ActionChains(self.driver).click(elem16).perform()
        time.sleep(1)
        # 点击详情按钮
        elem17 = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[15]/div/button/i')
        ActionChains(self.driver).click(elem17).perform()
        time.sleep(2)

        # 关闭抽屉式弹框
        elem22 = self.driver.find_element_by_xpath('/html/body/div[4]')
        elem22_date = elem22.get_attribute('class')
        print(elem22_date)
        if elem22_date == "slider open":
            self.driver.execute_script('arguments[0].setAttribute(arguments[1],arguments[2])', elem22, 'class',
                                       'slider close')
            elem23_data = elem22.get_attribute('class')
            print(elem23_data)

            elem24 = self.driver.find_element_by_xpath('/html/body/div[5]')
            elem24_date = elem24.get_attribute('style')
            print(elem24_date)
            if elem24_date == "display: block;":
                self.driver.execute_script('arguments[0].setAttribute(arguments[1],arguments[2])', elem24, 'style',
                                           'display: none;')
                elem25_data = elem24.get_attribute('style')
                print(elem25_data)
        time.sleep(2)


