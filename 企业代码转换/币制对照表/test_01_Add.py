from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

class Bizhi_Zhuanhuan_add(unittest.TestCase):
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
        self.dr.find_element(By.XPATH,'//*[@id="searchSite"]/div[3]/i').click()
        self.dr.find_element(By.LINK_TEXT,'确认').click()


    def tearDown(self) -> None:
       self.dr.quit()

    def test_add(self):
        #点击企业代码转换
       self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/a').click()
       self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[5]/a/cite').click()
       self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[5]/dl/dd[1]/a/cite').click()

        # 点击新增按钮
       self.a=self.dr.find_elements(By.TAG_NAME,'iframe') #切换frame，进入币制对照表页面
       self.dr.switch_to.frame(self.a[1])  #第一层frame

       self.dr.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/button[2]').click()
       self.dr.switch_to.frame('layui-layer-iframe1')#第二层frame
       #填写新增页面的信息
       #企业币制代码
       self.dr.find_element(By.XPATH,'//*[@id="CreateForm"]/div/div[1]/div[2]/input').send_keys('USD005')
       time.sleep(2)
        #海关币制代码
       self.dr.find_element(By.XPATH,'//*[@id="CreateForm"]/div/div[2]/div[2]/span/span/a').click()
       time.sleep(2)
       self.dr.find_element(By.XPATH,'//*[@id="CusCode_easyui_combobox_i1_2"]').click()
       time.sleep(2)
       #备注
       self.dr.find_element(By.XPATH,'//*[@id="CreateForm"]/div/div[3]/div[2]/input').send_keys('mml自动化测试')
       time.sleep(2)
       self.dr.find_element(By.XPATH,'//*[@id="CreateForm"]/div/div[4]/div/button').click()
       time.sleep(1)
       #dr.switch_to.frame('CreateForm')#第三层frame
       #确认操作成功
       self.dr.find_element(By.XPATH,'//*[@id="layui-layer3"]/div[3]/a').click()
       time.sleep(2)
