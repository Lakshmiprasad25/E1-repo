import pytest

def test_1(setup):
    driver=setup
    driver.get(r'https://demoapps.qspiders.com/ui?scenario=1')
    print('test case 1')

def test_2(setup):
    driver = setup
    driver.get(r'https://testautomationpractice.blogspot.com/')
    print('test case 2')