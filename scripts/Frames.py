import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://demoapps.qspiders.com/ui/frames/multiple?sublist=2')
driver.maximize_window()
time.sleep(2)

# F1=driver.find_element("xpath",'//*[@id="demoUI"]/main/section/article/aside/div/aside/div/iframe')
# driver.switch_to.frame(F1)
#
# F2=driver.find_element("xpath",'/html/body/div/div/section/div[2]/iframe')
# driver.switch_to.frame(F2)
#
# driver.find_element("xpath",'//*[@id="email"]').send_keys('selenium')
# driver.switch_to.default_content()
# driver.switch_to.parent_frame()

#Multiple frames
F1=driver.find_element("xpath",'//*[@id="demoUI"]/main/section/article/aside/div/aside/div/section[1]/div[1]/iframe')
driver.switch_to.frame(F1)
driver.find_element("xpath",'//*[@id="email"]').send_keys('selenium')
driver.switch_to.default_content()
time.sleep(2)
F2=driver.find_element("xpath",'//*[@id="demoUI"]/main/section/article/aside/div/aside/div/section[1]/div[2]/iframe')
driver.switch_to.frame(F2)
driver.find_element("xpath",'//*[@id="username"]').send_keys('selenium')

time.sleep(3)
