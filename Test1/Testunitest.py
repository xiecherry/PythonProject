import json
import time
import unittest

from selenium.webdriver import ActionChains
from selenium import webdriver
import HTMLTestRunner



class Testunitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.168.2.104:5003/home/index?menuid=JINHAI")

        # 首先清除浏览器已有的cookies
        self.driver.delete_all_cookies()
        # 读取cookie
        with open('cookie.txt', 'r',encoding='utf-8') as cookief:
            cookieslist = json.load(cookief)
            # 方法1 将expiry类型变为int,这样就不会过期
            for cookie in cookieslist:
                if isinstance(cookie.get('expiry'), float):
                    cookie['expiry'] = int(cookie['expiry'])
                self.driver.add_cookie(cookie)
        time.sleep(10)
        self.driver.get("http://192.168.2.104:5003/home/index?menuid=JINHAI")
        self.driver.refresh()

        driver = self.driver
        driver.implicitly_wait(10)

        # 点击模块展开按钮
        elem2 = self.driver.find_element_by_id('longnows_app_flexible')
        ActionChains(self.driver).click(elem2).perform()



        # 点击进出口管理
        time.sleep(5)
        elem3 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[3]/a/span')
        ActionChains(self.driver).click(elem3).perform()
        time.sleep(3)

        # 点击进口管理
        elem4 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[3]/dl/dd[2]/a/span')
        ActionChains(self.driver).click(elem4).perform()
        time.sleep(5)

        # 点击进口台账模块，进入进口台账页面
        elem5 = self.driver.find_element_by_xpath('//*[@id="nav-left"]/li[3]/dl/dd[2]/dl/dd[3]/a/cite')
        ActionChains(self.driver).click(elem5).perform()
        time.sleep(8)

    def test_case1(self):
        driver = self.driver
        driver.implicitly_wait(10)

        # ====================================================表头==============================================
        # 在进口台账页面点击新增按钮,这边用到iframe
        elem6 = driver.find_element_by_xpath('//*[@id="longnows_body"]/div[2]/div[2]/div[2]/iframe')
        driver.switch_to.frame(elem6)
        # 点击新增按钮
        elem7 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/button[1]')
        ActionChains(driver).click(elem7).perform()
        time.sleep(5)
        # 获取当前打开的所有窗口的句柄
        num1 = driver.window_handles
        print(num1)
        driver.switch_to.window(num1[0])

        # 在进口台账的新增页面，选择进境关别下拉数据
        elem8 = driver.find_element_by_xpath('//*[@id="longnows_tab_container"]/div[3]/iframe')
        print(elem8)
        # elem8=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,".//iframe[contains(@src,'/Dec/CopAct/Modify?Type=3&IEFlag=I')]")))
        driver.switch_to.frame(elem8)
        # ============
        # 点击进境关口下拉
        elem9 = driver.find_element_by_xpath('//*[@id="head"]/div[3]/div[2]/span/span/a')
        ActionChains(driver).click(elem9).perform()
        time.sleep(1)
        # 选择进境关闭
        elem10 = driver.find_element_by_xpath('/html/body/div[16]/div/div[1]')
        ActionChains(driver).click(elem10).perform()
        time.sleep(1)

        # ============
        # 点击入境口岸下拉
        elem11 = driver.find_element_by_xpath('//*[@id="head"]/div[3]/div[4]/span/span/a')
        ActionChains(driver).click(elem11).perform()
        time.sleep(1)
        # 选择入境口岸
        elem12 = driver.find_element_by_xpath('/html/body/div[17]/div/div[1]')
        ActionChains(driver).click(elem12).perform()
        time.sleep(1)

        # ============
        # 点击申报地海关下拉
        elem13 = driver.find_element_by_xpath('//*[@id="head"]/div[2]/div[6]/span/span/a')
        ActionChains(driver).click(elem13).perform()
        time.sleep(1)
        # 选择入境口岸
        elem14 = driver.find_element_by_xpath('/html/body/div[15]/div/div[1]')
        ActionChains(driver).click(elem14).perform()
        time.sleep(1)

        # ============
        # 点击报关行单位
        elem15 = driver.find_element_by_xpath('//*[@id="head"]/div[7]/div[2]/span/span/a')
        ActionChains(driver).click(elem15).perform()
        time.sleep(1)
        # 选择入境口岸
        elem16 = driver.find_element_by_xpath('/html/body/div[23]/div/div[1]')
        ActionChains(driver).click(elem16).perform()
        time.sleep(1)

        # ============
        # 点击监管方式
        elem17 = driver.find_element_by_xpath('//*[@id="head"]/div[9]/div[2]/span/span/a')
        ActionChains(driver).click(elem17).perform()
        time.sleep(1)
        # 选择监管方式
        elem18 = driver.find_element_by_xpath('/html/body/div[25]/div/div[1]')
        ActionChains(driver).click(elem18).perform()
        time.sleep(1)

        # ============
        # 点击起运国
        elem19 = driver.find_element_by_xpath('//*[@id="head"]/div[10]/div[2]/span/span/a')
        ActionChains(driver).click(elem19).perform()
        time.sleep(1)
        # 选择起运国
        elem20 = driver.find_element_by_xpath('/html/body/div[29]/div/div[1]')
        ActionChains(driver).click(elem20).perform()
        time.sleep(1)

        # ============
        # 点击境内目的地
        elem21 = driver.find_element_by_xpath('//*[@id="head"]/div[11]/div[2]/span/span/a')
        ActionChains(driver).click(elem21).perform()
        time.sleep(1)
        # 选择境内目的地
        elem22 = driver.find_element_by_xpath('/html/body/div[35]/div/div[1]')
        ActionChains(driver).click(elem22).perform()
        time.sleep(1)

        # ============
        # 点击特殊关确认
        elem23 = driver.find_element_by_xpath('//*[@id="head"]/div[12]/div[2]/span/span/a')
        ActionChains(driver).click(elem23).perform()
        time.sleep(1)
        # 选择特殊关系确认
        elem24 = driver.find_element_by_xpath('/html/body/div[39]/div/div[1]')
        ActionChains(driver).click(elem24).perform()
        time.sleep(1)

        # ============
        # 点击成交方式
        elem25 = driver.find_element_by_xpath('//*[@id="head"]/div[9]/div[4]/span/span/a')
        ActionChains(driver).click(elem25).perform()
        time.sleep(1)
        # 选择成交方式
        elem26 = driver.find_element_by_xpath('/html/body/div[27]/div/div[1]')
        ActionChains(driver).click(elem26).perform()
        time.sleep(1)

        # ============
        # 点击经停港
        elem27 = driver.find_element_by_xpath('//*[@id="head"]/div[10]/div[4]/span/span/a')
        ActionChains(driver).click(elem27).perform()
        time.sleep(1)
        # 选择经停港
        elem28 = driver.find_element_by_xpath('/html/body/div[30]/div/div[1]')
        ActionChains(driver).click(elem28).perform()
        time.sleep(1)

        # ============
        # 点击贸易国别（地区）
        elem29 = driver.find_element_by_xpath('//*[@id="head"]/div[11]/div[4]/span/span/a')
        ActionChains(driver).click(elem29).perform()
        time.sleep(1)
        # 选择贸易国别（地区）
        elem30 = driver.find_element_by_xpath('/html/body/div[33]/div/div[1]')
        ActionChains(driver).click(elem30).perform()
        time.sleep(1)

        # ============
        # 点击价格影响确认
        elem31 = driver.find_element_by_xpath('//*[@id="head"]/div[12]/div[4]/span/span/a')
        ActionChains(driver).click(elem31).perform()
        time.sleep(1)
        # 选择价格影响确认
        elem32 = driver.find_element_by_xpath('/html/body/div[40]/div/div[1]')
        ActionChains(driver).click(elem32).perform()
        time.sleep(1)

        # ============
        # 点击运输方式
        elem33 = driver.find_element_by_xpath('//*[@id="head"]/div[9]/div[6]/span/span/a')
        ActionChains(driver).click(elem33).perform()
        time.sleep(1)
        # 选择运输方式
        elem34 = driver.find_element_by_xpath('/html/body/div[28]/div/div[1]')
        ActionChains(driver).click(elem34).perform()
        time.sleep(1)

        # ============
        # 点击支付特殊权使确认
        elem35 = driver.find_element_by_xpath('//*[@id="head"]/div[12]/div[6]/span/span/a')
        ActionChains(driver).click(elem35).perform()
        time.sleep(1)
        # 选择支付特殊权使确认
        elem36 = driver.find_element_by_xpath('/html/body/div[41]/div/div[1]')
        ActionChains(driver).click(elem36).perform()
        time.sleep(1)

        # ============
        # 点击供应商
        elem37 = driver.find_element_by_xpath('//*[@id="head"]/div[8]/div[2]/span/span/a')
        ActionChains(driver).click(elem37).perform()
        time.sleep(1)
        # 选择供应商
        elem38 = driver.find_element_by_xpath('/html/body/div[24]/div/div[1]')
        ActionChains(driver).click(elem38).perform()
        time.sleep(1)

        # ============
        # 点击货代
        elem39 = driver.find_element_by_xpath('//*[@id="head"]/div[7]/div[4]/span/span/a')
        ActionChains(driver).click(elem39).perform()
        time.sleep(1)
        # 选择货代
        elem40 = driver.find_element_by_xpath('/html/body/div[18]/div/div[1]')
        ActionChains(driver).click(elem40).perform()
        time.sleep(1)

        # ============
        # 点击表头保存按钮
        elem41=driver.find_element_by_xpath('/html/body/div[1]/button[2]')
        elem41 = driver.find_element_by_xpath('/html/body/div[1]/button[contains(@lay-event,"headSave")]')
        ActionChains(driver).click(elem41).perform()
        time.sleep(1)

        # ===========================================表体======================================================

        # 点击表头新增按钮
        elem42 = driver.find_element_by_id('listInit')
        ActionChains(driver).click(elem42).perform()
        time.sleep(1)

        # =============
        # 点击商品料号下拉
        elem43 = driver.find_element_by_xpath('//*[@id="act_list_form"]/div[2]/div[2]/span/span/a')
        ActionChains(driver).click(elem43).perform()
        time.sleep(1)
        # 选择商品料号
        elem44 = driver.find_element_by_xpath('/html/body/div[11]/div/div[1]')
        ActionChains(driver).click(elem44).perform()
        time.sleep(1)

        # 设置申报数量
        elem45 = driver.find_element_by_id('Qty')
        elem45.clear()
        elem45.send_keys(10)
        time.sleep(1)

        # 设置申报单价
        elem46 = driver.find_element_by_id('DecPrice')
        elem46.clear()
        elem46.send_keys(6)
        time.sleep(1)

        # 设置法定第一数量
        elem47 = driver.find_element_by_id('Qty1')
        elem47.clear()
        elem47.send_keys(10)
        time.sleep(1)

        # 设置净重
        elem48 = driver.find_element_by_id('NetWt').send_keys(10)
        time.sleep(1)

        # 设置原产国
        # 点击下拉按钮
        elem49 = driver.find_element_by_xpath('//*[@id="act_list_form"]/div[9]/div[2]/span/span/a')
        ActionChains(driver).click(elem49).perform()
        time.sleep(1)
        # 选择下拉
        elem50 = driver.find_element_by_xpath('/html/body/div[58]/div/div')
        ActionChains(driver).click(elem50).perform()
        time.sleep(1)

        # 点击保存按钮
        elem51 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/button[contains(@lay-event,"listSave")]')
        ActionChains(driver).click(elem51).perform()
        time.sleep(1)



    def test_edit(self):
        driver = self.driver
        driver.implicitly_wait(10)

        # ====================================================表头==============================================
        # 在进口台账页面点击编辑按钮,这边用到iframe
        e_elem1 = driver.find_element_by_xpath('//*[@id="longnows_body"]/div[2]/div[2]/div[2]/iframe')
        driver.switch_to.frame(e_elem1)
        # 点击编辑按钮
        e_elem2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[2]/table/tbody/tr/td/div/button[1]/i')
        ActionChains(driver).click(e_elem2).perform()
        driver.implicitly_wait(10)
        # 获取当前打开的所有窗口的句柄
        num11 = driver.window_handles
        print(num11)
        driver.switch_to.window(num11[0])
        # 进入编辑页面的iframe
        e_elem3= driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/iframe')
        print(e_elem3)
        driver.switch_to.frame(e_elem3)
        # 修改出口日期
        e_elem4 = driver.find_element_by_xpath('//*[@id="head"]/div[3]/div[4]/span/span/a')
        ActionChains(driver).click(e_elem4).perform()
        time.sleep(2)
        e_elem5=driver.find_element_by_xpath('/html/body/div[17]/div/div[3]')
        ActionChains(driver).click(e_elem5).perform()

        #点击保存按钮
        e_elem6 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/button[contains(@lay-event,"listSave")]')



    def tearDown(self):
        print('Test Over')

    # if __name__=='__main__':
    #     unittest.main()

if __name__=='__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Testunitest('test_case1'))
    # 获取当前时间
    testtime = time.strftime('%Y%m%d_%H%M%S_')
    # 报告地址及报告名称
    file_path = 'D:\\PythonProject\\Testunitreport\\report.html'
    file_result = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = file_result,
        title = 'Test Report',
        description = 'Test Result'
    )
    # 自动进行测试
    runner.run(testunit)
    file_result.close()

