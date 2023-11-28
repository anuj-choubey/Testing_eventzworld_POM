
from selenium.webdriver.common.by import By


class MouseOver:
    def __init__(self, driver):
        self.driver = driver
        self.navbar_all_page_xpath = "//a[normalize-space()='EventzWorld']"

    def navbar_hower_all_page(self):
        return self.driver.find_element(By.XPATH, self.navbar_all_page_xpath).text

