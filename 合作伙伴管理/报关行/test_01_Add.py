from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

class Customs_broker_add(unittest.TestCase):
    def setUp(self) -> None:
        self.dr=webdriver.Chrome()
        self.dr.implicitly_wait(15)
        self.dr.maximize_window()
        # 打开登陆
        self.dr.get('http://192.168.0.199:5008/Home/Index?menuid=Chery')
        self.dr.find_element('id','uname').send_keys('17714070410')
        self.dr.find_element(By.ID,'upwd').send_keys('123456')
        self.dr.find_element(By.ID,'login').click()
        # 切换公司(奇瑞)
        self.dr.find_element(By.XPATH,'//*[@id="companyName"]/span[2]').click()
        self.dr.find_element(By.XPATH,'//*[@id="searchSite"]/div[2]/div').click()
        self.dr.find_element(By.LINK_TEXT,'确认').click()

    def tearDown(self) -> None:
        self.dr.quit()

    def test_add(self):
        # 点击基础资料-合作伙伴管理-报关行
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/a/cite').click()
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[4]/a/cite').click()
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[4]/dl/dd[4]/a/cite').click()
        # 切换iframe(多重框架切换)
        self.a=self.dr.find_elements(By.TAG_NAME,'iframe')
        self.dr.switch_to.frame(self.a[1]) #第一层frame
        self.dr.find_element('xpath','/html/body/div[2]/div[1]/div[1]/div/button[2]').click()
        # 输入必填项
        self.dr.switch_to.frame('mainFrame') #第二层frame
        self.dr.find_element('id','AgentCode').send_keys('A001')
        self.dr.find_element(By.NAME,'TradeCode').send_keys('1234554321')
        self.dr.find_element(By.NAME,'TradeCodeScc').send_keys('123456789987654321')
        self.dr.find_element(By.NAME,'AgentName').send_keys('通用报关行')
        self.dr.find_element('id','headSave').click()
        # 关闭抽屉式弹窗
        # 方法一：
        self.dr.switch_to.parent_frame()
        self.a=self.dr.find_element(By.CSS_SELECTOR,'#titleSpan').click()
        # 方法二：
        # # 修改js属性，关闭抽屉式弹窗
        # # 此元素在上一层frame，续作切换
        # dr.switch_to.parent_frame()
        # element_1=dr.find_element(By.XPATH,'/html/body/div[3]')
        # # arguments[0]:类似python%s传参
        # # 第一步：关闭弹窗
        # dr.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",element_1,'class','close')
        # # 第二布：去掉置灰
        # element_2=dr.find_element(By.XPATH,'/html/body/div[4]')
        # dr.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",element_2,'style','display: none')
        # 断言
        source=self.dr.page_source
        self.assertIn('A001',source)
        # if source:
        #     print('测试通过')
        # else:
        #     print('测试失败')
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
