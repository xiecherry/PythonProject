from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

class Bizhi_Zhuanhuan_delete(unittest.TestCase):
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

    def test_Delete(self):
         #点击企业代码转换
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/a').click()
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[5]/a/cite').click()
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[5]/dl/dd[1]/a/cite').click()

        #切换frame，进入币制对照表页面
        self.a=self.dr.find_elements(By.TAG_NAME,'iframe')
        self.dr.switch_to.frame(self.a[1]) #第一层frame

        #勾选，点击删除
        self.dr.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div/i').click()
        self.dr.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/button[3]').click()
        self.dr.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]').click()
        self.dr.find_element(By.XPATH,'//*[@id="layui-layer3"]/div[3]/a').click()
        time.sleep(2)


# #全选，删除
# dr.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[3]/div[1]/table/thead/tr/th[1]/div/div/i').click()
# dr.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/button[3]').click()
# dr.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]').click()
# dr.find_element(By.XPATH,'//*[@id="layui-layer3"]/div[3]/a').click()
# time.sleep(2)

#点击列表右边的删除图标进行删除
#dr.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[7]/div/button[2]/i').click()
#dr.find_element(By.XPATH,'//*[@id="layui-layer3"]/div[3]/a[1]').click()
# dr.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[7]/div/button[2]/i').click()
# dr.find_element(By.XPATH,'//*[@id="layui-layer3"]/div[3]/a[1]').click()