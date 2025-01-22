import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

driver.find_element("xpath",'//*[@id="datepicker"]').click()

while True:
    month=driver.find_element("xpath",'//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    year=driver.find_element("xpath",'//*[@id="ui-datepicker-div"]/div/div/span[2]').text
    if month=='May' and year=='2024':
        break
    else:
        driver.find_element("xpath",'//*[@id="ui-datepicker-div"]/div/a[1]').click()
    time.sleep(1)

dates=driver.find_elements("xpath",'//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')
for i in dates:
    if i.text=='20':
        i.click()
        break

time.sleep(3)