try:
    import time
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(r'https://testautomationpractice.blogspot.com/')
    driver.maximize_window()
    time.sleep(2)

    driver.find_element("xpath",'*[@id="apple"]').click()
    time.sleep(3)
except:
    driver.save_screenshot(r'C:\Users\QSPR\PycharmProjects\PythonProject\scripts\demo.png')

