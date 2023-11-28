import time
import pytest
from PageObject.All_Login_page import Login
from PageObject.guest.Guest_login_page import GuestLogin
from PageObject.createpost.Create_post_page import CreatePost
from Base.Scroll import BaseDriver
from Base.location import LocationSelector


@pytest.mark.usefixtures("setup")
class TestEvent_GuestCreate_post:
    def test_guest_create_post(self):
        gl = GuestLogin(self.driver)
        lg = Login(self.driver)
        post = CreatePost(self.driver)
        scroll_page = BaseDriver(self.driver)
        location_selector = LocationSelector(self.driver)
        lg.login_btn()
        gl.guest_login_button()
        # time.sleep(2)
        post.btn_create_post()
        time.sleep(1)
        post.input_box_event_name("Anuj Choubey")
        # time.sleep(2)
        location_selector.location_input("sagar")
#         time.sleep(2)
        post.select_index_category()
#         time.sleep(3)
        post.input_box_event_venue("Dwarka dham colony")
#         time.sleep(1)
        post.input_box_date()
#         time.sleep(1)
        post.input_box_time()
        # time.sleep(1)
        scroll_page.scroll_to_bottom()
#         time.sleep(2)
        post.select_image("anuj img.jpg")
#         time.sleep(2)
        post.select_music("tu hai to.mp3")
#         time.sleep(2)
        post.select_video("short.mp4")
#         time.sleep(2)
        post.input_box_enter_your_text("Ram ji ki nikli sabari ")
#         time.sleep(2)
        post.post_button()
        time.sleep(2)

    def test_admin_create_page(self):
        lg = Login(self.driver)
        post = CreatePost(self.driver)
        scroll_page = BaseDriver(self.driver)
        location_selector = LocationSelector(self.driver)
        lg.login_btn()
        lg.input_username("aman@test.com")
        time.sleep(1)
        lg.input_password("1234")
        time.sleep(1)
        lg.submit_btn()
        post.btn_create_post()
        time.sleep(1)
        post.input_box_event_name("Anuj Choubey")
        time.sleep(2)
        location_selector.location_input("bhopal")
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
        post.select_image()
        time.sleep(2)
        post.select_music()
        time.sleep(2)
        post.select_video()
        time.sleep(2)
        post.input_box_enter_your_text("Ram ji ki nikli sabari ")
        time.sleep(2)
        post.post_button()
        time.sleep(2)

    def test_user_create_page(self):
        pass

