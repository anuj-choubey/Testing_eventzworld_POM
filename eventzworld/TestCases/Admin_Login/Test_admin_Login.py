import time
import pytest
from PageObject.All_Login_page import Login
from PageObject.admin.Admin_dashbord_page import Dashboard
from Utilities.logger import Logclass
import configparser
config = configparser.ConfigParser()
config.read("D:\\Users\\eventzworld_page_object_model\\eventzworld\\Utilities\\.properties")


@pytest.mark.usefixtures("setup")
class TestEventz_world(Logclass):
    def test01(self):
        lg = Login(self.driver)
        db = Dashboard(self.driver)
        log = self.get_the_logs()
        log.info("Test Case 01 ")
        log.info("Test Case 01 starting")
        lg.login_btn()  # login_button_click_navbar
        log.info("Clicked Login Button")
        lg.input_username(config.get("Credentials","correct_admin_username"))
        log.info("Enter Username")
        # time.sleep(3)
        lg.input_password(config.get("Credentials","correct_admin_password"))
        log.info("Enter Password ")
        lg.submit_btn()
        log.info("Clicked Submit button")
        # time.sleep(3)
        if "AdminTable" in db.success_msg():
            assert True
            log.info("Test Case pass ")
        else:
            self.driver.save_screenshot("D:\\Users\\eventzworld_page_object_model\\eventzworld\\Screenshot\\admin\\test01.png")
            log.critical("Test Case failed ")
            assert False
        db.profile_name()
        log.info("Show profile")
        # time.sleep(3)
        db.logout_btn()
        log.info("Clicked logout button")

    def test02(self):
        lg = Login(self.driver)
        log = self.getthelogs()
        log.info("Test Case 02 ")
        lg.login_btn()
        log.info("clicked Login button ")
        lg.input_username(config.get("Credentials","incorrect_admin_username"))
        log.info("Enter Wrong username ")
        lg.input_password(config.get("Credentials","correct_admin_password"))
        log.info("Enter password")
        lg.submit_btn()
        log.info("Clicked submit button ")
        if 'Invalid Credential' in lg.invalid_msg():
            assert True
            log.info("Test Case pass")
        else:
            self.driver.save_screenshot("D:\\Users\\eventzworld_page_object_model\\eventzworld\\Screenshot\\admin\\test02.png")
            log.critical("Test Case failed ")
            assert False

    def test03(self):
        lg = Login(self.driver)
        log = self.getthelogs()
        log.info("Test Case 03")
        lg.login_btn()  # login_button
        log.info("clicked Login button ")
        lg.input_username(config.get("Credentials","correct_admin_username"))
        log.info("Enter Username")
        lg.input_password(config.get("Credentials","incorrect_password"))
        log.info("Enter Wrong password ")
        lg.submit_btn()
        log.info("Clicked submit button ")
        if 'Invalid Credential' in lg.invalid_msg():
            assert True
            log.info("Test Case pass")
        else:
            self.driver.save_screenshot("D:\\Users\\eventzworld_page_object_model\\eventzworld\\Screenshot\\admin\\test03.png")
            log.critical("Test Case failed ")
            assert False

    def test04(self):
        lg = Login(self.driver)
        log = self.getthelogs()
        log.info("Test Case 04")
        lg.login_btn()
        log.info("clicked Login button ")
        lg.submit_btn()
        log.info("Clicked submit button ")
        if "Both email and password are required." in lg.without_email_password_error_msg():
            assert True
            log.info("Test Case pass")
        else:
            self.driver.save_screenshot("D:\\Users\\eventzworld_page_object_model\\eventzworld\\Screenshot\\admin\\test04.png")
            log.critical("Test Case failed ")
            assert False
