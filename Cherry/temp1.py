from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver= webdriver.Chrome()
driver.maximize_window()
driver.get("http://192.168.2.104:5007/Home/Index?menuid=Chery")