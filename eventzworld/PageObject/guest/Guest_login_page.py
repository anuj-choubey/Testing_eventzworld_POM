from selenium.webdriver.common.by import By


class GuestLogin:
    def __init__(self, driver):
        self.driver = driver
        self.guest_login_button_xpath = "//button[normalize-space()='Guest Login']"
        self.guestH_btn_xpath = "//body/div[@id='root']/div[1]/nav[1]/div[1]/ul[1]/li[3]/div[1]/div[1]"
        self.verify_guest_login_page_msg_xpath = "//body/div[@id='root']/div[1]/nav[1]/div[1]/ul[1]/li[3]/div[1]/div[1]"
        self.logout_btn_xpath = "//body/div[@id='root']/div[1]/nav[1]/div[1]/ul[1]/li[3]/div[1]/div[2]/button[1]"

    def guest_login_button(self):
        self.driver.find_element(By.XPATH, self.guest_login_button_xpath).click()

    def hower_guest(self):
        return self.driver.find_element(By.XPATH, self.guestH_btn_xpath).text

    def verify_guest_msg(self):
        return self.driver.find_element(By.XPATH, self.verify_guest_login_page_msg_xpath).text

    def click_guest_name(self):
        return self.driver.find_element(By.XPATH, self.verify_guest_login_page_msg_xpath).click()

    def logout_btn(self):
        self.driver.find_element(By.XPATH,self.logout_btn_xpath).click()


