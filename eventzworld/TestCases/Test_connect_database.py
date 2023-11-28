# test_data_check.py

import pytest
from selenium import webdriver
import pymysql

from PageObject.All_Login_page import Login


@pytest.mark.usefixtures("setup")
class TestConnectDataBase:

    def test_user_data_match(self):
        login = Login(self.driver)
        # # Log in to the web application
        login.login_btn()
        login.input_username("aman@test.com")
        login.input_password("1234")
        login.submit_btn()

        # Navigate to the page displaying user data
        # user_data_page_link = self.driver.find_element("id", "userDataPageLink")
        # user_data_page_link.click()

        # Extract user data from the web page
        # user_data_web = self.driver.find_element("id", "userDataElement").text

        # Connect to the database and retrieve user data
        db_connection = pymysql.connect(
            host=' http://192.168.1.2:3000',
            user='your_database_user',
            password='your_database_password',
            database='your_database'
        )

        try:
            with db_connection.cursor() as cursor:
                # Execute a SELECT query to retrieve user data from the database
                query = "SELECT * FROM users WHERE condition"
                cursor.execute(query)
                user_data_db = cursor.fetchall()
        finally:
            db_connection.close()

        # Compare user data from the web page with the data from the database
        assert user_data_web == user_data_db
