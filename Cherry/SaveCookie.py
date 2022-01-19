import json

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver= webdriver.Chrome()
driver.maximize_window()
driver.get("http://192.168.2.104:5007/Home/Index?menuid=Chery")

elem = driver.find_element_by_name("uname")
elem.send_keys("17601473754")
time.sleep(1)
elem = driver.find_element_by_name("upwd")
elem.send_keys("123456")
time.sleep(1)
elem.send_keys(Keys.RETURN)
time.sleep(3)

with open('../Cherry/cookie.txt', 'w') as cookief:
    # 将cookies保存为json格式
    cookief.write(json.dumps(driver.get_cookies()))

driver.quit()