from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

chrome = Chrome()
chrome.get("https://saucedemo.com")
chrome.maximize_window()

username_input = chrome.find_element(By.ID, "user-name")
username_input.send_keys("standard_user") # bir inputa yazı yazmak için.

password_input = chrome.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = chrome.find_element(By.CSS_SELECTOR, "[data-test='login-button']")
login_button.click()
time.sleep(5)

