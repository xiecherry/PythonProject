import time
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


# 物料申请编辑
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
        elem4 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[2]/dl/dd[2]/dl/dd[1]/a')
        ActionChains(self.driver).click(elem4).perform()
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

    def test_2_edit(self):
        # ====================================================表头==============================================
        # 再定位新的iframe
        elem15 = self.driver.find_element_by_xpath('//*[@id="mainFrame"]')
        self.driver.switch_to.frame(elem15)
        time.sleep(3)
        # 选种一条数据
        elem16 = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/div/i')
        ActionChains(self.driver).click(elem16).perform()
        time.sleep(2)
        # 点击编辑按钮
        elem7 = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td/div/button[1]/i')
        ActionChains(self.driver).click(elem7).perform()
        time.sleep(2)


        # 再定位新的iframe
        elem151 = self.driver.find_element_by_xpath('//*[@id="mainFrame"]')
        self.driver.switch_to.frame(elem151)
        time.sleep(3)

        # 1.修改商品编码，先点击下拉按钮
        elem12 = self.driver.find_element_by_xpath('//*[@id="colla1"]/div[2]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem12).perform()
        time.sleep(1)
        # 2.选择对应的商品编码
        elem13 = self.driver.find_element_by_xpath('/html/body/div[10]/div/div[4]')
        ActionChains(self.driver).click(elem13).perform()
        time.sleep(1)

        # 点击保存按钮
        elem19 = self.driver.find_element_by_xpath('//*[@id="saveBtn"]')
        ActionChains(self.driver).click(elem19).perform()
        time.sleep(2)

        # 返回父文档iframe
        self.driver.switch_to.parent_frame()
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

        # 点击刷新按钮
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/button[1]').click()
        time.sleep(4)







