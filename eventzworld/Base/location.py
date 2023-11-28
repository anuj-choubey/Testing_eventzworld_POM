import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class LocationSelector:
    def __init__(self, driver):
        self.driver = driver
        self.search_input_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]"
        self.suggestions_dropdown_xpath = "//body/div[4]/div[1]/span[2]/span[1]"
        self.suggestion_elements_xpath = "//body/div[2]"
        self.clear_button_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]"

    def location_input(self, desired_location):
        time.sleep(2)
        clear_button_click = self.driver.find_element(By.XPATH, self.clear_button_xpath)
        clear_button_click.click()
        time.sleep(3)
        search_input = self.driver.find_element(By.XPATH, self.search_input_xpath)
        search_input.send_keys(desired_location)
        actions = ActionChains(self.driver)
        actions.click(on_element=search_input)
        actions.send_keys(desired_location)
        time.sleep(3)
        actions.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        actions.send_keys(Keys.ENTER)
        time.sleep(2)
        actions.perform()
        time.sleep(5)

    #