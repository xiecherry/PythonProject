import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


class test_04_import(unittest.TestCase):
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
        time.sleep(5)
        self.dr.find_element(By.XPATH,'//*[@id="searchSite"]/div[3]/i').click()
        self.dr.find_element(By.LINK_TEXT,'确认').click()

    def tearDown(self) -> None:
            self.dr.quit()

    def test_import(self):
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
        #点击导入按钮
        self.dr.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/button[1]').click()
        time.sleep(2)
        #点击选择文件
        # 绝对路径改为相对路径
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        print(self.current_dir)
        self.path_to_excel = os.path.join(self.current_dir, "导入模板_币制对照表.xls")
        time.sleep(3)
        # 选择文件
        self.dr.find_element(By.XPATH,'//*[@id="excelImportFormFile"]').send_keys(self.path_to_excel)
        time.sleep(2)
        #绝对路径选择文件
        #self.dr.find_element(By.XPATH,'//*[@id="excelImportFormFile"]').send_keys("E:\\Download\导入模板_币制对照表.xls")
        #time.sleep(10)
        #点击上传按钮
        #self.dr.find_element(By.XPATH,'//*[@id="excelImportFormDialog"]/div[2]/button[2]').click()
        # time.sleep(2)
