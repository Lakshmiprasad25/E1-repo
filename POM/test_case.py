import login_page,home_page

def test_script(setup):
    driver=setup
    L=login_page.LOGIN(driver)
    L.enter_username('student')
    L.enter_password('Password123')
    L.click_submit()

    H=home_page.HOME(driver)
    H.click_logout_button()




