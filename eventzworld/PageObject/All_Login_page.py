from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.login_button_xpath = "//a[normalize-space()='Login']"
        self.input_box_username_xpath = "//input[@placeholder='Username']"
        self.input_box_password_xpath = "//input[@placeholder='Password']"
        self.submit_login_button_xpath = "//button[normalize-space()='Login']"
        self.text_invalid_msg_xpath = "//div[contains(text(),'Invalid Credential')]"
        self.text_without_email_password_Error_msg_xpath = "//div[contains(text(),'Both email and password are required.')]"

    def login_btn(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def input_username(self, Username):
        self.driver.find_element(By.XPATH, self.input_box_username_xpath).send_keys(Username)

    def input_password(self, Password):
        self.driver.find_element(By.XPATH, self.input_box_password_xpath).send_keys(Password)

    def submit_btn(self):
        self.driver.find_element(By.XPATH, self.submit_login_button_xpath).click()

    def invalid_msg(self):
        return self.driver.find_element(By.XPATH, self.text_invalid_msg_xpath).text

    def without_email_password_error_msg(self):
        return self.driver.find_element(By.XPATH,self.text_without_email_password_Error_msg_xpath).text