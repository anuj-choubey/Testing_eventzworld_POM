from selenium.webdriver.common.by import By


class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.success_msg_text_xpath = "//h2[contains(text(),'AdminTable')]"
        self.profile_name_xpath = "//div[contains(text(),'Aman')]"
        self.logout_btn_xpath = "//button[contains(text(),'Logout')]"

    def success_msg(self):
        return self.driver.find_element(By.XPATH, self.success_msg_text_xpath).text

    def profile_name(self):
        self.driver.find_element(By.XPATH, self.profile_name_xpath).click()

    def logout_btn(self):
        self.driver.find_element(By.XPATH, self.logout_btn_xpath).click()
