import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://demoapps.qspiders.com/ui?scenario=1')
driver.maximize_window()
time.sleep(2)
driver.find_element("xpath",'//*[@id="demoUI"]/main/section/div/section/aside/div/ul/li[5]').click()
dis_ele=driver.find_element("xpath",'//*[@id="name"]')
driver.execute_script("arguments[0].removeAttribute('disabled')",dis_ele)
dis_ele.send_keys('selenium')

time.sleep(3)