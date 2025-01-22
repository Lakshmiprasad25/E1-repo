import time
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

#single file
ele=driver.find_element("xpath",'//*[@id="singleFileInput"]')
ele.send_keys(r'C:\Users\QSPR\Pictures')

#multiple files
ele=driver.find_element("xpath",'//*[@id="multipleFilesInput"]')
files=[r'C:\Users\QSPR\Pictures',r'C:\Users\QSPR\Documents']
for i in files:
    ele.send_keys(i)

time.sleep(5)