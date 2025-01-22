import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)
driver.find_element("xpath",'//*[@id="alertBtn"]').click()
time.sleep(2)
var=driver.switch_to.alert
var.accept()

time.sleep(2)
driver.find_element("xpath",'//*[@id="confirmBtn"]').click()
time.sleep(2)
var1=driver.switch_to.alert
# var1.accept()
var1.dismiss()

time.sleep(2)
driver.find_element("xpath",'//*[@id="promptBtn"]').click()
time.sleep(2)
var2=driver.switch_to.alert
var2.send_keys('silver')
var2.accept()
# var2.dismiss()


time.sleep(3)

