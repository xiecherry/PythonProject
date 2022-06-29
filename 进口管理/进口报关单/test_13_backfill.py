import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# 进口报关单-回填

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

        # 点击进口报关单审核
        elem5 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[3]/dl/dd[2]/dl/dd[6]/a/cite')
        ActionChains(self.driver).click(elem5).perform()
        time.sleep(8)



    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        print('Test Over')

    def test_13_backfill(self):
        # 定位到iframe时
        elem52 = self.driver.find_element_by_xpath('//*[@id="longnows_tab_container"]/div[2]/iframe')
        self.driver.switch_to.frame(elem52)
        # 要先查询，定位查询按钮
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/button[1]').click()
        time.sleep(2)
        # 勾选列表页面第一条数据
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div/i').click()
        time.sleep(1)
        #点击编辑按钮
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[2]/table/tbody/tr/td/div/button/i').click()
        time.sleep(1)

        # 跳转到编辑iframe位置
        elem53 = self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/iframe')

        self.driver.switch_to.frame(elem53)
        # 在弹框里，确定海关编号位置
        self.driver.find_element_by_xpath('//*[@id="EditForm"]/div/div[1]/div[4]/input').send_keys("000020221000000001")
        time.sleep(1)
        # 定位申报日期文本框
        self.driver.find_element_by_xpath('//*[@id="dDate"]').click()
        time.sleep(1)
        # 选择申报日期
        self.driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[2]/div/span[3]').click()
        time.sleep(1)
        # 点击确定按钮
        self.driver.find_element_by_xpath('//*[@id="EditForm"]/div/div[3]/div/button').click()
        time.sleep(2)
        # 截图
        self.driver.get_screenshot_as_file("D:\\PythonProject\\Cherry_Discover\\Image\\backfill.png")


        # 跳出iframe，点击取消按钮=======================
        self.driver.switch_to.default_content()
        # 点击新增关闭按钮
        self.driver.find_element_by_css_selector("#tab_title_container > li.layui-this > i").click()
        time.sleep(5)