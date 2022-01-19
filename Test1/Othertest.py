from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/")
a = driver.window_handles

driver.quit()

print("你好"+ a[0] )