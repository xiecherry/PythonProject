from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import os, fnmatch
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

class Customs_broker_export(unittest.TestCase):
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

    def test_export(self):
        # 点击基础资料-合作伙伴管理-报关行
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/a/cite').click()
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[4]/a/cite').click()
        self.dr.find_element(By.XPATH,'//*[@id="nav-left"]/li[2]/dl/dd[4]/dl/dd[4]/a/cite').click()
        # 切换iframe(多重框架切换)
        a=self.dr.find_elements(By.TAG_NAME,'iframe')
        self.dr.switch_to.frame(a[1]) #第一层frame
        # 导出
        self.dr.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/div/lable').click()
        self.dr.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/div/dl/dd[1]').click()
        time.sleep(5)
        # 校验
        ls=[]
        # 查找指定文件夹
        names = os.listdir(r'C:\Users\Administrator\Downloads')
        for name in names:
            # 匹配指定文件名
            if fnmatch.fnmatch(name, '报关行*.xlsx'):
                ls.append(name)
                break
        # 校验是否导出成功
        count=len(ls)
        # print(count)
        self.assertNotEqual(count,0)

if __name__ == '__main__':
    unittest.main()

