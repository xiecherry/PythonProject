import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# 进口管理新增、编辑、详情、导入表体、导出、导出表体、生成报关单、复制、查询、删除

class MyTestCase(unittest.TestCase):
    def setUp(self) :

        # self.chrome_options=Options()
        # self.chrome_options.add_argument("--headless")
        # self.chrome_options.add_argument("--start-maximized");
        # self.driver = webdriver.Chrome(options=self.chrome_options)
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
    def test_1_create(self):
        # ====================================================表头==============================================
        # 在进口台账页面点击新增按钮,这边用到iframe

        elem6 = self.driver.find_element_by_xpath('//*[@id="longnows_body"]/div[2]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(elem6)
        # 点击新增按钮
        elem7 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/button[1]')
        ActionChains(self.driver).click(elem7).perform()
        time.sleep(5)
        # 获取当前打开的所有窗口的句柄
        num1 = self.driver.window_handles
        print("创建页面句柄"+num1[0])
        self.driver.switch_to.window(num1[0])

        # 在进口台账的新增页面，定位到iframe
        elem8 = self.driver.find_element_by_xpath('//*[@id="longnows_tab_container"]/div[3]/iframe')
        print(elem8)
        # 跳转到frame里定位元素
        self.driver.switch_to.frame(elem8)

        # 点击进境关别下拉
        elem9 = self.driver.find_element_by_xpath('//*[@id="head"]/div[3]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem9).perform()
        time.sleep(1)
        # 选择进境关闭
        elem10 = self.driver.find_element_by_xpath('/html/body/div[16]/div/div[1]')
        ActionChains(self.driver).click(elem10).perform()
        time.sleep(1)
        # ============
        # 点击入境口岸下拉
        elem11 = self.driver.find_element_by_xpath('//*[@id="head"]/div[3]/div[4]/span/span/a')
        ActionChains(self.driver).click(elem11).perform()
        time.sleep(1)
        # 选择入境口岸
        elem12 = self.driver.find_element_by_xpath('/html/body/div[17]/div/div[1]')
        ActionChains(self.driver).click(elem12).perform()
        time.sleep(1)
        # ============
        # 点击申报地海关下拉
        elem13 = self.driver.find_element_by_xpath('//*[@id="head"]/div[2]/div[6]/span/span/a')
        ActionChains(self.driver).click(elem13).perform()
        time.sleep(1)
        # 选择入境口岸
        elem14 = self.driver.find_element_by_xpath('/html/body/div[15]/div/div[1]')
        ActionChains(self.driver).click(elem14).perform()
        time.sleep(1)

        # ============
        # 点击报关行单位
        elem15 = self.driver.find_element_by_xpath('//*[@id="head"]/div[7]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem15).perform()
        time.sleep(1)
        # 选择入境口岸
        elem16 = self.driver.find_element_by_xpath('/html/body/div[23]/div/div[1]')
        ActionChains(self.driver).click(elem16).perform()
        time.sleep(1)

        # ============
        # 点击监管方式
        elem17 = self.driver.find_element_by_xpath('//*[@id="head"]/div[9]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem17).perform()
        time.sleep(1)
        # 选择监管方式
        elem18 = self.driver.find_element_by_xpath('/html/body/div[25]/div/div[1]')
        ActionChains(self.driver).click(elem18).perform()
        time.sleep(1)

        # ============
        # 点击起运国
        elem19 = self.driver.find_element_by_xpath('//*[@id="head"]/div[10]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem19).perform()
        time.sleep(1)
        # 选择起运国
        elem20 = self.driver.find_element_by_xpath('/html/body/div[29]/div/div[1]')
        ActionChains(self.driver).click(elem20).perform()
        time.sleep(1)

        # ============
        # 点击境内目的地
        elem21 = self.driver.find_element_by_xpath('//*[@id="head"]/div[11]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem21).perform()
        time.sleep(1)
        # 选择境内目的地
        elem22 = self.driver.find_element_by_xpath('/html/body/div[35]/div/div[1]')
        ActionChains(self.driver).click(elem22).perform()
        time.sleep(1)

        # ============
        # 点击特殊关确认
        elem23 = self.driver.find_element_by_xpath('//*[@id="head"]/div[12]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem23).perform()
        time.sleep(1)
        # 选择特殊关系确认
        elem24 = self.driver.find_element_by_xpath('/html/body/div[39]/div/div[1]')
        ActionChains(self.driver).click(elem24).perform()
        time.sleep(1)

        # ============
        # 点击成交方式
        elem25 = self.driver.find_element_by_xpath('//*[@id="head"]/div[9]/div[4]/span/span/a')
        ActionChains(self.driver).click(elem25).perform()
        time.sleep(1)
        # 选择成交方式
        elem26 = self.driver.find_element_by_xpath('/html/body/div[27]/div/div[1]')
        ActionChains(self.driver).click(elem26).perform()
        time.sleep(1)

        # ============
        # 点击经停港
        elem27 = self.driver.find_element_by_xpath('//*[@id="head"]/div[10]/div[4]/span/span/a')
        ActionChains(self.driver).click(elem27).perform()
        time.sleep(1)
        # 选择经停港
        elem28 = self.driver.find_element_by_xpath('/html/body/div[30]/div/div[1]')
        ActionChains(self.driver).click(elem28).perform()
        time.sleep(1)

        # ============
        # 点击贸易国别（地区）
        elem29 = self.driver.find_element_by_xpath('//*[@id="head"]/div[11]/div[4]/span/span/a')
        ActionChains(self.driver).click(elem29).perform()
        time.sleep(1)
        # 选择贸易国别（地区）
        elem30 = self.driver.find_element_by_xpath('/html/body/div[33]/div/div[1]')
        ActionChains(self.driver).click(elem30).perform()
        time.sleep(1)

        # ============
        # 点击价格影响确认
        elem31 = self.driver.find_element_by_xpath('//*[@id="head"]/div[12]/div[4]/span/span/a')
        ActionChains(self.driver).click(elem31).perform()
        time.sleep(1)
        # 选择价格影响确认
        elem32 = self.driver.find_element_by_xpath('/html/body/div[40]/div/div[1]')
        ActionChains(self.driver).click(elem32).perform()
        time.sleep(1)

        # ============
        # 点击运输方式
        elem33 = self.driver.find_element_by_xpath('//*[@id="head"]/div[9]/div[6]/span/span/a')
        ActionChains(self.driver).click(elem33).perform()
        time.sleep(1)
        # 选择运输方式
        elem34 = self.driver.find_element_by_xpath('/html/body/div[28]/div/div[1]')
        ActionChains(self.driver).click(elem34).perform()
        time.sleep(1)

        # ============
        # 点击支付特殊权使确认
        elem35 = self.driver.find_element_by_xpath('//*[@id="head"]/div[12]/div[6]/span/span/a')
        ActionChains(self.driver).click(elem35).perform()
        time.sleep(1)
        # 选择支付特殊权使确认
        elem36 = self.driver.find_element_by_xpath('/html/body/div[41]/div/div[1]')
        ActionChains(self.driver).click(elem36).perform()
        time.sleep(1)

        # ============
        # 点击供应商
        elem37 = self.driver.find_element_by_xpath('//*[@id="head"]/div[8]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem37).perform()
        time.sleep(1)
        # 选择供应商
        elem38 = self.driver.find_element_by_xpath('/html/body/div[24]/div/div[1]')
        ActionChains(self.driver).click(elem38).perform()
        time.sleep(1)

        # ============
        # 点击货代
        elem39 = self.driver.find_element_by_xpath('//*[@id="head"]/div[7]/div[4]/span/span/a')
        ActionChains(self.driver).click(elem39).perform()
        time.sleep(1)
        # 选择货代
        elem40 = self.driver.find_element_by_xpath('/html/body/div[18]/div/div[1]')
        ActionChains(self.driver).click(elem40).perform()
        time.sleep(1)

        # ============
        # 点击表头保存按钮
        # elem41=self.driver.find_element_by_xpath('/html/body/div[1]/button[2]')
        elem41 = self.driver.find_element_by_xpath('/html/body/div[1]/button[contains(@lay-event,"headSave")]')
        ActionChains(self.driver).click(elem41).perform()
        time.sleep(2)

        # ===========================================表体======================================================

        # 点击表体新增按钮
        elem42 = self.driver.find_element_by_id('listInit')
        ActionChains(self.driver).click(elem42).perform()
        time.sleep(1)

        # =============
        # 点击商品料号下拉
        elem43 = self.driver.find_element_by_xpath('//*[@id="act_list_form"]/div[2]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem43).perform()
        time.sleep(1)
        # 选择商品料号
        elem44 = self.driver.find_element_by_xpath('/html/body/div[11]/div/div[1]')
        ActionChains(self.driver).click(elem44).perform()
        time.sleep(1)

        # 设置申报数量
        elem45 = self.driver.find_element_by_id('Qty')
        elem45.clear()
        elem45.send_keys(10)
        time.sleep(1)

        # 设置申报单价
        elem46 = self.driver.find_element_by_id('DecPrice')
        elem46.clear()
        elem46.send_keys(6)
        time.sleep(1)

        # 设置申报计量单位
        # 点击下拉按钮
        elem52 =  self.driver.find_element_by_xpath('//*[@id="act_list_form"]/div[6]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem52).perform()
        time.sleep(1)
        # 选择下拉
        elem53 = self.driver.find_element_by_xpath('/html/body/div[55]/div/div[1]')
        ActionChains(self.driver).click(elem53).perform()
        time.sleep(1)


        # 设置币制
        elem54 = self.driver.find_element_by_xpath('//*[@id="act_list_form"]/div[6]/div[4]/span/span/a')
        ActionChains(self.driver).click(elem54).perform()
        time.sleep(1)
        # 选择下拉
        elem55 = self.driver.find_element_by_xpath('/html/body/div[56]/div/div[1]')
        ActionChains(self.driver).click(elem55).perform()
        time.sleep(1)



        # 设置法定第一数量
        elem47 = self.driver.find_element_by_id('Qty1')
        elem47.clear()
        elem47.send_keys(10)
        time.sleep(1)

        # 设置净重
        elem48 = self.driver.find_element_by_id('NetWt').send_keys(10)
        time.sleep(1)

        # 设置毛重
        elem48 = self.driver.find_element_by_id('GrossWt').send_keys(60)
        time.sleep(1)

        # 设置原产国
        # 点击下拉按钮
        elem49 = self.driver.find_element_by_xpath('//*[@id="act_list_form"]/div[9]/div[2]/span/span/a')
        ActionChains(self.driver).click(elem49).perform()
        time.sleep(1)
        # 选择下拉
        elem50 = self.driver.find_element_by_xpath('/html/body/div[58]/div/div[2]')
        ActionChains(self.driver).click(elem50).perform()
        time.sleep(1)

        # 点击保存按钮
        elem51 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div[2]/button[contains(@lay-event,"listSave")]')
        ActionChains(self.driver).click(elem51).perform()
        time.sleep(2)
        # 截图
        self.driver.get_screenshot_as_file("D:\\PythonProject\\Cherry_Discover\\Image\\create.png")

        # 跳出iframe，点击取消按钮
        self.driver.switch_to.default_content()
        # 点击新增关闭按钮
        self.driver.find_element_by_css_selector("li[lay-id='CopActICreate'] > i").click()
        time.sleep(3)

