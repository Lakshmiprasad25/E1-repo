import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

driver.find_element("xpath",'//*[@id="txtDate"]').click()

mon=driver.find_element("xpath",'//*[@id="ui-datepicker-div"]/div/div/select[1]')
obj=Select(mon)
obj.select_by_visible_text('May')

year=driver.find_element("xpath",'//*[@id="ui-datepicker-div"]/div/div/select[2]')
obj=Select(year)
obj.select_by_visible_text('2024')

dates=driver.find_elements("xpath",'//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')
for i in dates:
    if i.text=='20':
        i.click()
        break

time.sleep(3)