from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
search_input = driver.find_element(By.XPATH, "//body/div[@id = 'root']/div[1]/div[1]/div[1]/div[1]/form/input["
                                             "@placeholder='Enter a location']")
search_input.send_keys("sagar")  # Replace with your desired location
wait = WebDriverWait(driver, 10)
suggestions = wait.until(EC.visibility_of_element_located((By.XPATH, "")))  # Adjust the locator as needed
suggestions_list = suggestions.find_elements(By.CLASS_NAME, "sbsb_b")  # Locate the list of suggestions
first_suggestion = suggestions_list[0]  # Get the first suggestion
first_suggestion.click()  # Click on the first suggestion
driver.quit()
