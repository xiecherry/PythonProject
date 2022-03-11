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

    def test_1_create(self):
        # ====================================================表头==============================================
        # 再定位新的iframe
        elem15 = self.driver.find_element_by_xpath('//*[@id="mainFrame"]')
        self.driver.switch_to.frame(elem15)
        time.sleep(3)
        # 点击新增按钮
        elem7 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/button[2]')
        ActionChains(self.driver).click(elem7).perform()
        time.sleep(2)
        # 获取当前打开的所有窗口的句柄
        # num1 = self.driver.window_handles
        # print("创建页面句柄"+num1[0])
        # self.driver.switch_to.window(num1[0])

        # # 在进口台账的新增页面，定位到iframe
        # elem8 = self.driver.find_element_by_xpath('//*[@id="longnows_tab_container"]/div[3]/iframe')
        # print(elem8)
        # # 跳转到frame里定位元素
        # self.driver.switch_to.frame(elem8)

        # 再定位新的iframe
        elem151 = self.driver.find_element_by_xpath('//*[@id="mainFrame"]')
        self.driver.switch_to.frame(elem151)
        time.sleep(3)


        # 设置商品料号
        self.driver.find_element_by_xpath('//*[@id="copGNo"]').send_keys('TestL001')
        time.sleep(1)
        # ============
        # 点击货品类型下拉
        elem10 = self.driver.find_element_by_xpath('//*[@id="colla1"]/div[1]/div[4]/span/span/a')
        ActionChains(self.driver).click(elem10).perform()
        time.sleep(1)
        # 选择货品类型
        elem11 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]')
        ActionChains(self.driver).click(elem11).perform()
        time.sleep(1)

        # 1.选择商品编码，先点击下拉按钮
        elem12 = self.driver.find_element_by_xpath('//*[@id="colla1"]/div[2]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem12).perform()
        time.sleep(1)
        # 2.选择对应的商品编码
        elem13 = self.driver.find_element_by_xpath('/html/body/div[10]/div/div[1]')
        ActionChains(self.driver).click(elem13).perform()
        time.sleep(1)

        #规则型号
        elem14 = self.driver.find_element_by_xpath('//*[@id="GModel"]')
        ActionChains(self.driver).click(elem14).perform()
        time.sleep(1)

        # 设置规则型号
        elem16 = self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]')
        ActionChains(self.driver).click(elem16).perform()
        time.sleep(1)

        # 设置申报计量单位
        elem17 = self.driver.find_element_by_xpath('//*[@id="colla1"]/div[5]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem17).perform()
        time.sleep(1)
        #下拉选择申报计量单位
        elem18 = self.driver.find_element_by_xpath('/html/body/div[6]/div/div[1]')
        ActionChains(self.driver).click(elem18).perform()
        time.sleep(1)

        # 设置企业物料类型
        elem20 = self.driver.find_element_by_xpath('//*[@id="colla1"]/div[9]/div[4]/span/span/a')
        ActionChains(self.driver).click(elem20).perform()
        time.sleep(1)
        # 选择企业物料类型下拉
        elem21 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]')
        ActionChains(self.driver).click(elem21).perform()
        time.sleep(1)

        # 点击保存按钮
        elem19 = self.driver.find_element_by_xpath('//*[@id="saveBtn"]')
        ActionChains(self.driver).click(elem19).perform()
        time.sleep(2)

        self.driver.switch_to.default_content()

        # 点击列表页面查询按钮，查询数据
        elem20 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/button[1]')
        ActionChains(self.driver).click(elem20).perform()
        time.sleep(3)






