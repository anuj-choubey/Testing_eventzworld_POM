import time
import pytest
from PageObject.register.Register_page import Register
from PageObject.All_Login_page import Login
from PageObject.createpost.Create_post_page import CreatePost
from Base.Scroll import BaseDriver
from ErrorMessage.register_error_and_success_msg import Error_And_Success_Msg
from selenium.webdriver import ActionChains
from Base.mouse_hower import MouseOver


@pytest.mark.usefixtures("setup")
class TestEventz_world_register_page:
    def test_success(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)

        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        if "Create Account" in err.register_success_msg():
            assert True
        else:
            assert False

    def test_register(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)
        location = CreatePost(self.driver)
        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        reg.input_box_name("Anuj choubey")
        reg.input_box_email("ss@gmail.com")
        reg.input_select_gender()
        reg.select_mail()
        reg.input_password_field("12345678")
        reg.input_confirm_password("12345678")
        reg.input_location("sagar")
        reg.register_button()
        time.sleep(10)

    def test_name_error(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)
        location = CreatePost(self.driver)
        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        reg.input_box_name("")
        reg.input_box_email("auj@mistpl.com")
        reg.input_select_gender()
        reg.select_mail()
        reg.input_password_field("12345678")
        reg.input_confirm_password("12345678")
        reg.input_location("sagar")
        reg.register_button()
        if "Name is required." in err.name_error():
            assert True
        else:
            assert False

    def test_email_error(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)
        location = CreatePost(self.driver)
        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        reg.input_box_name("")
        reg.input_box_email("")
        reg.input_select_gender()
        reg.select_mail()
        reg.input_password_field("12345678")
        reg.input_confirm_password("12345678")
        reg.input_location("sagar")
        reg.register_button()
        if "Email is required" in err.email_error():
            assert True
        else:
            assert False

    def test_gender_error(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)
        location = CreatePost(self.driver)
        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        reg.input_box_name("")
        reg.input_box_email("auj@mistpl.com")
        # reg.input_select_gender()
        # reg.select_mail()
        reg.input_password_field("12345678")
        reg.input_confirm_password("12345678")
        reg.input_location("sagar")
        reg.register_button()
        if "Gender is required" in err.gender_error():
            assert True
        else:
            assert False

    def test_password_error(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)
        location = CreatePost(self.driver)
        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        reg.input_box_name("anuj")
        reg.input_box_email("auj@mistpl.com")
        reg.input_select_gender()
        reg.select_mail()
        reg.input_password_field("")
        reg.input_confirm_password("12345678")
        reg.input_location("sagar")
        reg.register_button()
        if "Password must be at least 8 characters long" in err.password_error():
            assert True
        else:
            assert False

    def test_confirm_password_error(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)
        location = CreatePost(self.driver)
        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        reg.input_box_name("anuj")
        reg.input_box_email("auj@mistpl.com")
        reg.input_select_gender()
        reg.select_mail()
        reg.input_password_field("12345678")
        reg.input_confirm_password("")
        reg.input_location("sagar")
        reg.register_button()
        if "Passwords do not match" in err.confirm_password_error():
            assert True
        else:
            assert False

    def test_without_data_input_error(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)
        location = CreatePost(self.driver)
        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        reg.input_box_name("")
        reg.input_box_email("")
        reg.input_select_gender()
        reg.input_password_field("")
        reg.input_confirm_password("")
        reg.input_location("")
        reg.register_button()
        if "Name is required." in err.name_error():
            assert True
        elif "Email is required" in err.email_error():
            assert True
        elif "Gender is required" in err.gender_error():
            assert True
        elif "Password must be at least 8 characters long" in err.password_error():
            assert True
        elif "Passwords do not match" in err.confirm_password_error():
            assert True
        else:
            assert False

    def test_already_registered_mail_msg(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)
        location = CreatePost(self.driver)
        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        reg.input_box_name("Anuj choubey")
        reg.input_box_email("auj@mistpl.com")
        reg.input_select_gender()
        reg.select_mail()
        reg.input_password_field("12345678")
        reg.input_confirm_password("12345678")
        time.sleep(3)
        reg.input_location("sagar")
        time.sleep(1)
        reg.register_button()
        if "User with this email already exists." in err.already_registered_mail_msg():
            assert True
        else:
            assert False
        time.sleep(5)

    def test_return_login_page_msg(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)
        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        lg.login_btn()
        if "Login Page" in err.login_page_return_success_msg():
            assert True
        else:
            assert False

    def test_navbar_hower_page(self):
        err = Error_And_Success_Msg(self.driver)
        reg = Register(self.driver)
        lg = Login(self.driver)
        scroll = BaseDriver(self.driver)
        hor = MouseOver(self.driver)
        lg.login_btn()
        time.sleep(2)
        scroll.scroll_to_bottom()
        reg.sign_up_btn()
        ActionChains(self.driver.move_to_element(hor.navbar_hower_all_page())).perform()
        time.sleep(5)
