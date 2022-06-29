import os

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

class Customs_broker_upload(unittest.TestCase):
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

    def test_upload(self):
        # 点击基础资料-合作伙伴管理-报关行
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/a/cite').click()
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[4]/a/cite').click()
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[4]/dl/dd[4]/a/cite').click()
        # 切换iframe(多重框架切换)
        a=self.dr.find_elements(By.TAG_NAME,'iframe')
        self.dr.switch_to.frame(a[1]) #第一层frame
        self.dr.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/button[1]').click()
        # 绝对路径改为相对路径
        current_dir = os.path.dirname(os.path.realpath(__file__))
        print(current_dir)
        path_to_excel = os.path.join(current_dir, "导入模板_报关行.xlsx")
        # 选择文件
        elem16 = self.dr.find_element_by_xpath('//*[@id="excelImportFormFile"]').send_keys(path_to_excel)
        time.sleep(2)
        # # 上传
        # self.dr.find_element(By.ID,'excelImportFormFile').send_keys(r'D:\PycharmProjects\pythonProject_1\CustomsBroker\导入模板_报关行.xlsx')
        # self.dr.find_element(By.XPATH,'//*[@id="excelImportFormDialog"]/div[2]/button[2]').click()
        # 校验
        page_soc=self.dr.page_source
        self.assertIn('通用报关行03',page_soc)

if __name__ == '__main__':
    unittest.main()