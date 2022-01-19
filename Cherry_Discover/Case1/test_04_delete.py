import time
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
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

    def test_4_delete(self):
        # 定位到iframe时
        elem54 = self.driver.find_element_by_xpath('//*[@id="longnows_body"]/div[2]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(elem54)
        # 勾选列表页面第一条数据
        self.driver.find_element_by_xpath(
            '//*[@class="layui-table-box"]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/div/i').click()
        time.sleep(2)
        # 点击删除按钮
        self.driver.find_element_by_xpath(
            '//*[@class="layui-table-box"]/div[4]/div[2]/table/tbody/tr[1]/td/div/button[3]/i').click()
        time.sleep(2)
        # 获取当前打开的所有窗口的句柄

        num1 = self.driver.window_handles
        print("删除页面句柄" + num1[0])
        self.driver.switch_to.window(num1[0])

        elem55 = self.driver.find_element_by_xpath('//*[@id="longnows_tab_container"]/div[2]/iframe')
        self.driver.switch_to.frame(elem55)
        # 进入删除弹框======================
        self.driver.find_element_by_xpath('//*/body/div[16]/div[3]/a[1]').click()
        time.sleep(2)
        # 删除成功确定按钮
        self.driver.find_element_by_xpath('//*/body/div[16]/div[3]/a[1]').click()
        self.driver.get_screenshot_as_file("D:\\PythonProject\\Cherry_Discover\\Image\\delete.png")
        time.sleep(2)
        self.driver.refresh()


        #tearDown=============================================================================

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        print('Test Over')



