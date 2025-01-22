class LOGIN:
    username='//*[@id="username"]'
    password='//*[@id="password"]'
    submit='//*[@id="submit"]'

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,input):
        self.driver.find_element("xpath",self.username).send_keys(input)
    def enter_password(self,input):
        self.driver.find_element("xpath",self.password).send_keys(input)
    def click_submit(self):
        self.driver.find_element("xpath",self.submit).click()

