import pytest

@pytest.fixture
def setup():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    time.sleep(1)
    yield driver
    time.sleep(1)
    driver.close()

