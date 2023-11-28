from selenium.webdriver.common.by import By


class Posts:
    def __init__(self, driver):
        self.driver = driver
        self.admin_table_xpath = "//a[contains(text(),'Admin Table')]"
        self.approve_button = "//body/div[@id='root']/div[1]/nav[1]/div[1]/ul[1]/li[3]/div[1]/div[2]/a[2]"
        self.reject_button = "//body/div[@id='root']/div[1]/nav[1]/div[1]/ul[1]/li[3]/div[1]/div[2]/a[3]"
