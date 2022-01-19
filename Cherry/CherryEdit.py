import json
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
# 初次建立连接，随后方可修改cookie
driver.get("http://192.168.2.52/uni/home")

# 首先清除浏览器已有的cookies
driver.delete_all_cookies()

with open('../Test1/cookie.txt', 'r', encoding='utf-8') as cookief:
    cookieslist = json.load(cookief)
    # 方法1 将expiry类型变为int,这样就不会过期
    for cookie in cookieslist:
        if isinstance(cookie.get('expiry'),float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)
# 再次访问页面，便可实现免登陆访问
driver.get("http://192.168.2.104:5007/Home/Index?menuid=Chery")
driver.refresh()
time.sleep(5)
#切换工厂
driver.find_element_by_css_selector("a[longnows-event='changeSite']").click()
time.sleep(5)

#定位到弹框,用window_handles
windowhandle1 = driver.window_handles
print("切换工厂弹框"+windowhandle1[0])
driver.switch_to.window(windowhandle1[0])
time.sleep(2)
driver.find_element_by_xpath("//*[@id='searchSite']/div[4]/i").click()
time.sleep(1)
#点击确定按钮
driver.find_element_by_link_text("确认").click()
time.sleep(2)
# =================================点击进出口管理=================================================
# time.sleep(20)
elem3=driver.find_element_by_xpath('//*[@id="nav-left"]/li[3]/a/span')
ActionChains(driver).click(elem3).perform()
time.sleep(3)

# 点击进口管理
elem4=driver.find_element_by_xpath('//*[@id="nav-left"]/li[3]/dl/dd[2]/a/span')
ActionChains(driver).click(elem4).perform()
time.sleep(5)

# 点击进口台账
elem5=driver.find_element_by_xpath('//*[@id="nav-left"]/li[3]/dl/dd[2]/dl/dd[2]/a/cite')
ActionChains(driver).click(elem5).perform()
time.sleep(8)
# ========编辑=================

# 定位到iframe时
elem52 = driver.find_element_by_xpath('//*[@id="longnows_body"]/div[2]/div[2]/div[2]/iframe')
driver.switch_to.frame(elem52)
# 勾选列表页面第一条数据
driver.find_element_by_xpath('//*[@class="layui-table-box"]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/div/i').click()
time.sleep(2)
# 点击编辑按钮
driver.find_element_by_xpath('//*[@class="layui-table-box"]/div[4]/div[2]/table/tbody/tr/td/div/button/i').click()
time.sleep(5)
# 获取当前打开的所有窗口的句柄

num1=driver.window_handles
print("编辑页面句柄"+num1[0])
driver.switch_to.window(num1[0])
# 进入编辑页面======================


elem53 = driver.find_element_by_xpath('//*[@id="longnows_body"]/div[2]/div[2]/div[3]/iframe')
driver.switch_to.frame(elem53)
# 修改进境关别=====
# 点击进境关别下拉
elem54=driver.find_element_by_xpath('//*[@id="head"]/div[3]/div[2]/span/span/a')
ActionChains(driver).click(elem54).perform()
time.sleep(1)
# 选择进境关闭
elem10=driver.find_element_by_xpath('/html/body/div[16]/div/div[2]')
ActionChains(driver).click(elem10).perform()
time.sleep(1)
# 点击表头保存按钮
elem41=driver.find_element_by_xpath('/html/body/div[1]/button[contains(@lay-event,"headSave")]')
ActionChains(driver).click(elem41).perform()
time.sleep(2)

#跳出iframe，点击取消按钮
driver.switch_to.default_content()
#点击新增关闭按钮
driver.find_element_by_css_selector("#tab_title_container > li.layui-this > i").click()
time.sleep(5)
# 关闭浏览器
driver.quit()