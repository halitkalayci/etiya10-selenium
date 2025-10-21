from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

class TestLogin():
    def test_login_valid(self):
        driver = Chrome()
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get("https://saucedemo.com")

        #Magic String
        wait.until( EC.visibility_of_element_located((By.ID, "user-name")) ).send_keys("standard_user123") 

        wait.until( EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce123")

        login_button = wait.until( EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='login-button']")))
        login_button.click()

        message_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        assert message_box.text == "Epic sadface: Username and password do not match any user in this service"
    
    def helper_function(self):
        print("Bu bir yardımcı fonksiyondur.")