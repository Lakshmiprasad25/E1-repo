import time
import requests
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)
links=driver.find_elements("xpath",'//a')
urls=[]
for i in links:
    urls+=[i.get_attribute('href')]
for i in urls:
    if i!=None:
        response=requests.get(i)
        if response.status_code>=400:
            print(f'{i} is broken link')
        else:
            print(f'{i} is valid link')
time.sleep(3)