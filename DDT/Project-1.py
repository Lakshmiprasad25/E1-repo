import time
import Utilities
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://practicetestautomation.com/practice-test-login/')
driver.maximize_window()
time.sleep(2)

path=r'C:\Users\QSPR\Documents\DDT_data.xlsx'
rows=Utilities.row_count(path,"Sheet1")
for r in range(2,rows+1):
    UN=Utilities.read_data(path,"Sheet1",r,1)
    PWD=Utilities.read_data(path,"Sheet1",r,2)
    driver.find_element("xpath",'//*[@id="username"]').clear()
    driver.find_element("xpath", '//*[@id="username"]').send_keys(UN)
    time.sleep(1)
    driver.find_element("xpath",'//*[@id="password"]').clear()
    driver.find_element("xpath",'//*[@id="password"]').send_keys(PWD)
    time.sleep(1)
    driver.find_element("xpath",'//*[@id="submit"]').click()
    time.sleep(1)
    if driver.title=='Logged In Successfully | Practice Test Automation':
        print('test passed')
        Utilities.write_data(path,"Sheet1",r,4,'passed')
        driver.back()
    else:
        print('test failed')
        Utilities.write_data(path, "Sheet1", r, 4, 'failed')
    time.sleep(2)
time.sleep(3)