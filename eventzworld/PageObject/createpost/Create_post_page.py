from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import pyautogui
from selenium.webdriver import ActionChains, Keys

class CreatePost:
    def __init__(self, driver):
        self.driver = driver
        self.btn_create_post_xpath = "//body/div[@id='root']/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]"
        self.input_box_event_name_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]"

        self.select_event_category_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/select[1]"
        self.category_dropdown_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/select[1]/option[1]"
        self.input_box_event_venue_xpath = "//input[@placeholder='Event Venue']"
        self.input_box_date_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/input[3]"
        self.input_box_time_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/input[4]"
        self.select_image_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/label[1]/*[1]"
        self.select_music_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]"
        self.select_video_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]"
        self.input_box_enter_your_text_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/textarea[1]"
        self.post_button_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]"
        self.input_date_element_xpath = "//input[@placeholder='Event Date']"

        self.search_input_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]"
        self.suggestions_dropdown_xpath = "//body/div[4]/div[1]/span[2]/span[1]"
        self.suggestion_elements_xpath = "//body/div[2]"
        self.clear_button_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]"

    def btn_create_post(self):
        self.driver.find_element(By.XPATH, self.btn_create_post_xpath).click()

    def input_box_event_name(self, name):
        self.driver.find_element(By.XPATH, self.input_box_event_name_xpath).send_keys(name)

    def location_input(self, desired_location):
        time.sleep(10)
        clear_button_click = self.driver.find_element(By.XPATH, self.clear_button_xpath)
        clear_button_click.click()
        # time.sleep(3)
        search_input = self.driver.find_element(By.XPATH, self.search_input_xpath)
        search_input.send_keys(desired_location)
        time.sleep(10)
        actions = ActionChains(self.driver)
        # time.sleep(5)
        actions.send_keys(desired_location)
        time.sleep(3)
        actions.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        actions.send_keys(Keys.ENTER)
        time.sleep(2)
        actions.perform()
        time.sleep(5)

    def select_index_category(self):
        dropdown_option = self.driver.find_element(By.XPATH, self.select_event_category_xpath)
        select = Select(dropdown_option)
        select.select_by_index(2)

    def input_box_event_venue(self, venue):
        self.driver.find_element(By.XPATH, self.input_box_event_venue_xpath).send_keys(venue)

    def input_box_date(self):
        current_date = datetime.now()
        next_day = current_date + timedelta(days=1)
        next_day_formatted = next_day.strftime("%mm/%dd/%YY")
        date_input = self.driver.find_element(By.XPATH, self.input_box_date_xpath)
        date_input.clear()
        date_input.send_keys(next_day_formatted)

    def input_box_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        enter_time = self.driver.find_element(By.XPATH, self.input_box_time_xpath)
        enter_time.send_keys(current_time)

    def select_image(self,image_filename):
        upload_image = self.driver.find_element(By.XPATH, self.select_image_xpath)
        upload_image.click()
        time.sleep(5)
        # image_filename = "anuj img.jpg"
        image_path = image_filename
        pyautogui.write(image_path)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)

    def select_music(self,music_filename):
        upload_music = self.driver.find_element(By.XPATH, self.select_music_xpath)
        upload_music.click()
        time.sleep(5)
        # music_filename = "tu hai to.mp3"
        music_path = music_filename
        pyautogui.write(music_path)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)

    def select_video(self,video_filename):
        upload_video = self.driver.find_element(By.XPATH, self.select_video_xpath)
        upload_video.click()
        time.sleep(1)
        # video_filename = "short.mp4"
        video_path = video_filename
        pyautogui.write(video_path)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)

    def input_box_enter_your_text(self, text):
        self.driver.find_element(By.XPATH, self.input_box_enter_your_text_xpath).send_keys(text)

    def post_button(self):
        self.driver.find_element(By.XPATH, self.post_button_xpath).click()
