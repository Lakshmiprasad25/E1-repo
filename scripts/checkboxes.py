import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)
checkboxes=driver.find_elements("xpath",'//input[@type="checkbox" and @class="form-check-input"]')
# print(len(checkboxes))
# for i in checkboxes:
#     i.click()
#     time.sleep(1)
# for i in checkboxes[::-1]:
#     i.click()
#     time.sleep(1)

for i in checkboxes:
    if i.get_attribute('id')=='sunday' or i.get_attribute('id')=='friday':
        i.click()

days=[]
for i in checkboxes:
    days+=[i.get_attribute('id')]
print(days)

time.sleep(3)