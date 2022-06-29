from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

class Customs_broker_delete(unittest.TestCase):
    def setUp(self) -> None:
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(15)
        self.dr.maximize_window()
        # 打开登陆
        self.dr.get('http://192.168.0.199:5008/Home/Index?menuid=Chery')
        self.dr.find_element('id', 'uname').send_keys('17714070410')
        self.dr.find_element(By.ID, 'upwd').send_keys('123456')
        self.dr.find_element(By.ID, 'login').click()
        # 切换公司(奇瑞)
        self.dr.find_element(By.XPATH, '//*[@id="companyName"]/span[2]').click()
        self.dr.find_element(By.XPATH, '//*[@id="searchSite"]/div[2]/div').click()
        self.dr.find_element(By.LINK_TEXT, '确认').click()

    def tearDown(self) -> None:
        self.dr.quit()

    def test_delete(self):
        # 点击基础资料-合作伙伴管理-报关行
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/a/cite').click()
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[4]/a/cite').click()
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[4]/dl/dd[4]/a/cite').click()
        # 切换iframe(多重框架切换)
        a=self.dr.find_elements(By.TAG_NAME,'iframe')
        self.dr.switch_to.frame(a[1]) #第一层frame
        self.dr.find_element('xpath','/html/body/div[2]/div[1]/div[1]/div/button[2]').click()
        # 输入必填项
        self.dr.switch_to.frame('mainFrame') #第二层frame
        self.dr.find_element('id','AgentCode').send_keys('A002')
        self.dr.find_element(By.NAME,'TradeCode').send_keys('1234554222')
        self.dr.find_element(By.NAME,'TradeCodeScc').send_keys('123456789987654222')
        self.dr.find_element(By.NAME,'AgentName').send_keys('通用报关行02')
        self.dr.find_element('id','headSave').click()
        # 关闭抽屉式弹窗
        self.dr.switch_to.parent_frame()
        a=self.dr.find_element(By.CSS_SELECTOR,'#titleSpan').click()
        # 删除相应数据
        b=self.dr.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[3]/div').text
        print(b)
        if b == '通用报关行02':
            self.dr.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div').click()
            self.dr.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/button[3]').click()
            self.dr.find_element(By.LINK_TEXT,'确认').click()
            self.dr.find_element(By.LINK_TEXT, '确定').click()
            # 断言
            soc=self.dr.page_source
            self.assertNotIn('通用报关行02',soc)

if __name__ == '__main__':
    unittest.main()