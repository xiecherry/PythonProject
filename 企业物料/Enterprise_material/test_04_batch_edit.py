import time
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


# 物料批量编辑
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
        self.driver.implicitly_wait(5)

        # 切换工厂
        self.driver.find_element_by_css_selector("a[longnows-event='changeSite']").click()
        time.sleep(5)

        # 定位到弹框,用window_handles
        windowhandle1 = self.driver.window_handles
        print("切换工厂弹框" + windowhandle1[0])
        self.driver.switch_to.window(windowhandle1[0])
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@id='searchSite']/div[6]/i").click()
        time.sleep(1)
        # 点击确定按钮
        self.driver.find_element_by_link_text("确认").click()
        self.driver.implicitly_wait(5)

        # =====点击基础资料模块================================================================
        # time.sleep(20)
        elem3 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/a/i')
        ActionChains(self.driver).click(elem3).perform()
        self.driver.implicitly_wait(5)

        # 点击企业物料1//*[@id="nav-left"]/li[2]/dl/dd[2]/a
        elem4 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/dl/dd[2]/a')
        ActionChains(self.driver).click(elem4).perform()
        self.driver.implicitly_wait(5)
        # 再点击企业物料
        elem41 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/dl/dd[2]/dl/dd[1]/a')
        ActionChains(self.driver).click(elem41).perform()
        self.driver.implicitly_wait(5)


        # 定位新的iframe
        elem6 = self.driver.find_element_by_xpath('//*[@id="longnows_tab_container"]/div[2]/iframe')
        self.driver.switch_to.frame(elem6)
        self.driver.implicitly_wait(5)
        # 切换物料申请
        elem5 = self.driver.find_element_by_xpath('/html/body/div/ul/li[2]')
        ActionChains(self.driver).click(elem5).perform()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.quit()
        print('Test Over')

    def test_4_batch_edit(self):
        # ====================================================表头==============================================
        # 再定位新的iframe
        elem15 = self.driver.find_element_by_xpath('//*[@id="mainFrame"]')
        self.driver.switch_to.frame(elem15)
        self.driver.implicitly_wait(5)
        # 选中一条数据
        elem16 = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/div/i')
        ActionChains(self.driver).click(elem16).perform()
        self.driver.implicitly_wait(5)
        # 点击批量修改按钮
        elem7 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/button[3]')
        ActionChains(self.driver).click(elem7).perform()
        self.driver.implicitly_wait(5)

        # 在批量修改弹框，修改商品名称
        elem8 = self.driver.find_element_by_xpath('//*[@id="GName"]').send_keys('TestL001112')
        self.driver.implicitly_wait(5)

        # 点击确定按钮
        elem9 = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/a[1]')
        ActionChains(self.driver).click(elem9).perform()
        time.sleep(4)

   










