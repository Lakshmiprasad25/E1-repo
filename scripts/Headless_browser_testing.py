import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
ob=Options()
ob.add_argument('--headless')
driver=webdriver.Chrome(options=ob)
driver.implicitly_wait(10)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

links=driver.find_elements("xpath",'//a')
print(len(links))

time.sleep(3)