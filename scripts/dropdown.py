import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

ele=driver.find_element("xpath",'//*[@id="country"]')
obj=Select(ele)

drop_eles=obj.options
for i in drop_eles:
    print(i.text)

obj.select_by_index(9)
obj.select_by_value('india')
obj.select_by_visible_text('India')

ele=driver.find_element("xpath",'//*[@id="colors"]')
obj=Select(ele)
obj.select_by_visible_text("Red")
time.sleep(1)
obj.select_by_visible_text("Green")
time.sleep(1)
obj.select_by_visible_text("Yellow")
time.sleep(1)
obj.deselect_all()

obj.deselect_by_visible_text("Yellow")

eles=obj.all_selected_options
for i in eles:
    print(i.text)

print(obj.first_selected_option.text)

time.sleep(3)