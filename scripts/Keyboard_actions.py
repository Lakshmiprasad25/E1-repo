import time
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

ob=ActionChains(driver)

driver.find_element("xpath",'//*[@id="name"]').send_keys('selenium')
ob.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
ob.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
time.sleep(2)
ob.key_down(Keys.TAB).perform()
time.sleep(2)
ob.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

i=1
while i<=10:
    ob.key_down(Keys.PAGE_DOWN).perform()
    time.sleep(1)
    i+=1

time.sleep(3)
