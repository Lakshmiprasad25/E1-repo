import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r'https://demoapps.qspiders.com/ui/scroll/newHorizontal?scenario=1')
driver.maximize_window()
time.sleep(2)
ob=ActionChains(driver)
#right-click
# ele=driver.find_element("xpath",'//*[@id="name"]')
# ob.context_click(ele).perform()
#
# #double-click
# ele.send_keys('selenium')
# ob.double_click(ele).perform()
#
# #click & hold
# circle=driver.find_element("xpath",'//*[@id="circle"]')
# ob.click_and_hold(circle).perform()
#
# #mouse-hover
# point=driver.find_element("xpath",'//*[@id="HTML3"]/div[1]/div/button')
# laptop=driver.find_element("xpath",'//*[@id="HTML3"]/div[1]/div/div/a[2]')
# ob.move_to_element(point).move_to_element(laptop).perform()

# #drag & drop
# ele=driver.find_element("xpath",'//*[@id="draggable"]')
# tar=driver.find_element("xpath",'//*[@id="droppable"]')
# ob.drag_and_drop(ele,tar).perform()
#
# slider=driver.find_element("xpath",'//*[@id="slider-range"]/span[1]')
# ob.drag_and_drop_by_offset(slider,100,0).perform()
# time.sleep(2)
# ob.drag_and_drop_by_offset(slider,-100,0).perform()

#scroll from top to bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
#scroll from bottom to top
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
# #to get pixel value
# val=driver.execute_script("return window.pageYOffset;")
# print(val)
# #scroll based on value
# driver.execute_script("window.scrollBy(0,1500)")
# #scroll upto specified ele
# ele=driver.find_element("xpath",'//*[@id="blog-pager"]/a')
# driver.execute_script("arguments[0].scrollIntoView();",ele)

driver.find_element("xpath",'//*[@id="demoUI"]/main/section/article/aside/div/aside/div/section/a').click()
wids=driver.window_handles
driver.switch_to.window(wids[1])
time.sleep(2)
driver.execute_script("window.scrollBy(document.body.scrollWidth,0)")
time.sleep(2)
# driver.execute_script("window.scrollBy(-document.body.scrollWidth,0)")
val=driver.execute_script("return window.pageXOffset;")
print(val)
driver.execute_script("window.scrollBy(-document.body.scrollWidth,0)")
time.sleep(2)
driver.execute_script("window.scrollBy(3000,0)")
time.sleep(2)
driver.execute_script("window.scrollBy(-3000,0)")

time.sleep(5)

