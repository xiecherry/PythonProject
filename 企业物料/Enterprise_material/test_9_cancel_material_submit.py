import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os

# 物料申请-取消提交

class MyTestCase(unittest.TestCase):
    def setUp(self):
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

        # =====点击基础资料模块================================================================
        # time.sleep(20)
        elem3 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/a/i')
        ActionChains(self.driver).click(elem3).perform()
        time.sleep(3)

        # 点击企业物料1//*[@id="nav-left"]/li[2]/dl/dd[2]/a
        elem4 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/dl/dd[2]/a')
        ActionChains(self.driver).click(elem4).perform()
        time.sleep(2)
        # 再点击企业物料
        elem41 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/dl/dd[2]/dl/dd[1]/a')
        ActionChains(self.driver).click(elem41).perform()
        time.sleep(2)


        # 定位新的iframe
        elem6 = self.driver.find_element_by_xpath('//*[@id="longnows_tab_container"]/div[2]/iframe')
        self.driver.switch_to.frame(elem6)
        time.sleep(3)
        # 切换物料申请
        elem5 = self.driver.find_element_by_xpath('/html/body/div/ul/li[2]')
        ActionChains(self.driver).click(elem5).perform()
        time.sleep(2)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        print('Test Over')


    # 具体的测试用例，一定要以test开头
    def test_9_cancel_material_submit(self):

        # 再定位新的iframe
        elem15 = self.driver.find_element_by_xpath('//*[@id="mainFrame"]')
        self.driver.switch_to.frame(elem15)
        self.driver.implicitly_wait(5)

        # 查询区域数据选择已提交
        # 定位审核状态已提交
        elem16 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[8]/span/span/a')
        ActionChains(self.driver).click(elem16).perform()
        time.sleep(2)
        # 选择已提交下拉
        elem17 = self.driver.find_element_by_xpath('/html/body/div[11]/div/div[3]')
        ActionChains(self.driver).click(elem17).perform()
        time.sleep(2)
        # 点击查询按钮
        elem18 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/button[1]')
        ActionChains(self.driver).click(elem18).perform()
        time.sleep(2)


        #选择一条数据
        elem19 = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/div/i')
        ActionChains(self.driver).click(elem19).perform()
        self.driver.implicitly_wait(5)

        #点击撤销申请按钮
        elem20 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/button[7]')
        ActionChains(self.driver).click(elem20).perform()
        time.sleep(2)

        # 点击确定按钮
        elem21 = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]')
        ActionChains(self.driver).click(elem21).perform()
        time.sleep(2)



