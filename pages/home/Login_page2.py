from selenium.webdriver.common.by import By

class LoginPage2():

    def __init__(self, driver):
        self.driver = driver

    #   Log in page  Locators
    _login_link = "Login"
    _email_fieldID = "user_email"
    _password_fieldID = "user_password"
    _login_ButtonName = "commit"


    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT,self._login_link)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_fieldID)

    def getPasswordField(self):
        return self.driver.find_element(By.ID , self._password_fieldID)

    def getLoginButton(self):
        return self.driver.find_element(By.NAME,self._login_ButtonName)


    # ...................................................................
    # on this case .click and .send_keys is not Dynamic make sure to wright correct syntex

    def clickLoginLink(self):
        self.getLoginLink().click()

    def enterEmail(self,email):
        self.getEmailField().send_keys(email)

    def enterPassword(self,password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()




    def login(self, email, password):
       self.clickLoginLink()
       self.enterEmail(email)
       self.enterPassword(password)
       self.clickLoginButton()