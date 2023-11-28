import time
from ddt import ddt
import pytest
from Base.location import LocationSelector
from PageObject.All_Login_page import Login
from PageObject.guest.Guest_login_page import GuestLogin
from PageObject.createpost.Create_post_page import CreatePost
# from Base.mouse_hower import MouseOver
from Utilities.logger import Logclass
import configparser
config = configparser.ConfigParser()
config.read("D:\\Users\\eventzworld_page_object_model\\eventzworld\\Utilities\\.properties")
from Base.Scroll import BaseDriver


@pytest.mark.usefixtures("setup")
@ddt
class TestEvent_Guest_login(Logclass):
    def test_login_guest(self):
        log = self.get_the_logs()
        gl = GuestLogin(self.driver)
        lg = Login(self.driver)
        lg.login_btn()
        gl.guest_login_button()
        gl.verify_guest_msg()

    def test_button_highlight(self):
        gl = GuestLogin(self.driver)
        lg = Login(self.driver)
        lg.login_btn()
        gl.guest_login_button()
        time.sleep(2)
        gl.click_guest_name()
        time.sleep(5)

    def test_logout_button(self):
        gl = GuestLogin(self.driver)
        lg = Login(self.driver)
        lg.login_btn()
        gl.guest_login_button()
        time.sleep(2)
        gl.click_guest_name()
        time.sleep(5)
        gl.logout_btn()
        time.sleep(3)

    def test_guest_create_post(self):
        gl = GuestLogin(self.driver)
        lg = Login(self.driver)
        post = CreatePost(self.driver)
        scroll_page = BaseDriver(self.driver)
        location_selector = LocationSelector(self.driver)
        lg.login_btn()
        gl.guest_login_button()
        time.sleep(2)
        post.btn_create_post()
        time.sleep(1)
        post.input_box_event_name("Anuj Choubey")
        time.sleep(2)
        location_selector.location_input("sagar")
        time.sleep(2)
        post.select_index_category()
        time.sleep(3)
        post.input_box_event_venue("Dwarka dham colony")
        time.sleep(1)
        post.input_box_date()
        time.sleep(1)
        post.input_box_time()
        time.sleep(1)
        scroll_page.scroll_to_bottom()
        time.sleep(2)
        post.select_image("anuj img.jpg")
        time.sleep(2)
        post.select_music("tu hai to.mp3")
        time.sleep(2)
        post.select_video("short.mp4")
        time.sleep(2)
        post.input_box_enter_your_text("Ram ji ki nikli sabari ")
        time.sleep(2)
        post.post_button()
        time.sleep(10)

    def test_guest_without_data_create_post(self):
        gl = GuestLogin(self.driver)
        lg = Login(self.driver)
        post = CreatePost(self.driver)
        scroll_page = BaseDriver(self.driver)

        lg.login_btn()
        gl.guest_login_button()
        time.sleep(2)
        post.btn_create_post()
        time.sleep(5)
        post.input_box_event_name("")
        time.sleep(2)
        post.location_input("bhopal")
        time.sleep(5)
        post.select_index_category()
        time.sleep(3)
        post.input_box_event_venue("")
        time.sleep(1)
        post.input_box_date()
        time.sleep(1)
        post.input_box_time()
        time.sleep(1)
        scroll_page.scroll_to_bottom()
        time.sleep(2)
        post.select_image("")
        time.sleep(2)
        post.select_music("")
        time.sleep(2)
        post.select_video("")
        time.sleep(2)
        post.input_box_enter_your_text("")
        time.sleep(2)
        post.post_button()
        time.sleep(3)
