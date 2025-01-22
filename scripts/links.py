import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)
links=driver.find_elements("tag name",'a')
print(len(links))
for i in links:
    print(i.text)
for i in links:
    if i.text=='Home':
        i.click()
        break
time.sleep(3)

