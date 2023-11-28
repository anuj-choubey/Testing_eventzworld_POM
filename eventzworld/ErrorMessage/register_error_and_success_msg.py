from selenium.webdriver.common.by import By


class Error_And_Success_Msg:
    def __init__(self, driver):
        self.driver = driver
        self.register_success_msg_xpath = "//h1[contains(text(),'Create Account')]"
        self.name_error_register_page_xpath = "//div[contains(text(),'Name is required.')]"
        self.email_error_register_page_xpath = "//div[contains(text(),'Email is required.')]"
        self.gender_error_xpath = "//div[contains(text(),'Gender is required.')]"
        self.password_error_xpath = "//div[contains(text(),'Password must be at least 8 characters long.')]"
        self.confirm_password_error_xpath = "//div[contains(text(),'Passwords do not match.')]"
        self.already_registered_mail_msg_xpath = "//div[contains(text(),'User with this email already exists.')]"
        self.login_page_return_success_msg_xpath = "//h1[normalize-space()='Login Page']"

    def register_success_msg(self):
        return self.driver.find_element(By.XPATH, self.register_success_msg_xpath).text

    def name_error(self):
        return self.driver.find_element(By.XPATH, self.name_error_register_page_xpath).text

    def email_error(self):
        return self.driver.find_element(By.XPATH, self.email_error_register_page_xpath).text

    def gender_error(self):
        return self.driver.find_element(By.XPATH, self.gender_error_xpath).text

    def password_error(self):
        return self.driver.find_element(By.XPATH, self.password_error_xpath).text

    def confirm_password_error(self):
        return self.driver.find_element(By.XPATH, self.confirm_password_error_xpath).text

    def already_registered_mail_msg(self):
        return self.driver.find_element(By.XPATH, self.already_registered_mail_msg_xpath).text

    def login_page_return_success_msg(self):
        return self.driver.find_element(By.XPATH,self.login_page_return_success_msg_xpath).text
