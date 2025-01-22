import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://demoapps.qspiders.com/ui/frames/multiple?sublist=2')
driver.maximize_window()
time.sleep(2)

driver.find_element("xpath",'').click()
wids=driver.window_handles
driver.switch_to.window(wids[1])
driver.find_element("xpath",'').click()

time.sleep(3)