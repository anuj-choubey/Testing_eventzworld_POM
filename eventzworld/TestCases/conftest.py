from selenium import webdriver
import pytest
import configparser
config = configparser.ConfigParser()
config.read("D:\\Users\\eventzworld_page_object_model\\eventzworld\\Utilities\\.properties")
@pytest.fixture()
def setup(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get(config.get("Url","base_url"))
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(10)
    yield
    request.cls.driver.quit()