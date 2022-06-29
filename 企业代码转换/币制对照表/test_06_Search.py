from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

class Bizhi_Zhuanhuan_Search(unittest.TestCase):
    def setUp(self) -> None:
        self.dr=webdriver.Chrome()
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()

        self.dr.get('http://192.168.0.199:5008/Home/Index?menuid=Chery')
        self.dr.find_element(By.ID,'uname').send_keys('18277329777')
        self.dr.find_element(By.ID,'upwd').send_keys('123456')
        self.dr.find_element(By.ID,'login').click()

        # 切换公司
        self.dr.find_element(By.XPATH,'//*[@id="companyName"]/span[2]').click()
        time.sleep(2)
        self.dr.find_element(By.XPATH,'//*[@id="searchSite"]/div[3]/i').click()
        self.dr.find_element(By.LINK_TEXT,'确认').click()

        #点击基础资料
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/a').click()
        #点击企业代码转换
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[5]/a/cite').click()
        #点击币制对照表
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[5]/dl/dd[1]/a/cite').click()

        #切换窗口，进入币制对照表页面
        self.a=self.dr.find_elements(By.TAG_NAME,'iframe')
        self.dr.switch_to.frame(self.a[1]) #第一层frame
        time.sleep(2)

    def tearDown(self) -> None:
            self.dr.quit()

    def test_Search(self):
         #查询
        self.dr.find_element(By.ID,'EntCode').send_keys('005')
        time.sleep(1)
        self.dr.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/button[1]').click()
        time.sleep(2)
        self.dr.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/button[2]').click()
        time.sleep(2)
        self.dr.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/button[1]').click()
        self.dr.find_element(By.ID,'CusCode').send_keys('USD')
        time.sleep(1)
        self.dr.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/button[1]').click()
        time.sleep(2)
        self.dr.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/button[2]').click()
        time.sleep(2)
        self.dr.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/button[1]').click()

