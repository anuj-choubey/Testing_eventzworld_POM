import time

import pytest
from PageObject.All_Login_page import Login
from PageObject.guest.Guest_login_page import GuestLogin
from PageObject.createpost.Create_post_page import CreatePost
# from Base.location import DropdownHandler
# from Base.location import LocationSelector

@pytest.mark.usefixtures("setup")
class Test_NetherworldLocation:
    def test_create_post(self):
        gl = GuestLogin(self.driver)
        lg = Login(self.driver)
        post = CreatePost(self.driver)

        # location_selector = DropdownHandler(self.driver)
        lg.login_btn()
        gl.guest_login_button()
        time.sleep(2)
        post.btn_create_post()
        time.sleep(5)
        # location_selector
        post.input_box_enter_location("Sa")
        # location_selector.select_option_by_text("Sagar Ma")
        time.sleep(5)
