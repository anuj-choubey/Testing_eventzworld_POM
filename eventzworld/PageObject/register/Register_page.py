from selenium.webdriver.common.by import By


class Register:
    def __init__(self, driver):
        self.driver = driver
        self.sign_up_btn_xpath = "//strong[contains(text(),'Sign Up')]"
        self.input_box_name_xpath = "//input[@placeholder='Name']"
        self.input_box_email_xpath = "//input[@placeholder='Email']"
        self.input_select_gender_xpath = "//select[@class='input-field']"
        self.select_mail_gender_xpath = "//option[contains(text(),'Male')]"
        self.select_femail_gender_xpath = "//option[contains(text(),'Male')]"
        self.input_password_field_xpath = "//input[@placeholder='Password']"
        self.input_confirm_password_xpath = "//input[@placeholder='Confirm Password']"
        self.input_location_xpath = "//input[@placeholder='Enter a location']"
        self.register_button_xpath = "//button[contains(text(),'Register')]"
        self.register_success_msg_xpath = "//h1[contains(text(),'Create Account')]"

    def sign_up_btn(self):
        self.driver.find_element(By.XPATH, self.sign_up_btn_xpath).click()

    def input_box_name(self, name):
        self.driver.find_element(By.XPATH, self.input_box_name_xpath).send_keys(name)

    def input_box_email(self, email):
        self.driver.find_element(By.XPATH, self.input_box_email_xpath).send_keys(email)

    def input_select_gender(self):
        self.driver.find_element(By.XPATH, self.input_select_gender_xpath).click()

    def select_mail(self):
        self.driver.find_element(By.XPATH, self.select_mail_gender_xpath).click()

    def select_femail_gender(self):
        self.driver.find_element(By.XPATH, self.select_femail_gender_xpath).click()

    def input_password_field(self, password):
        self.driver.find_element(By.XPATH, self.input_password_field_xpath).send_keys(password)

    def input_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, self.input_confirm_password_xpath).send_keys(confirm_password)

    def input_location(self, location):
        self.driver.find_element(By.XPATH, self.input_location_xpath).send_keys(location)

    def register_button(self):
        self.driver.find_element(By.XPATH, self.register_button_xpath).click()



