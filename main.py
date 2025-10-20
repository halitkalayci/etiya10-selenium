from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome = Chrome()
wait = WebDriverWait(chrome, 10)
chrome.get("https://saucedemo.com")
chrome.maximize_window()

username_input = wait.until( EC.visibility_of_element_located((By.ID, "user-name")) ) # ✅ Max 10s elementi bekler ve öyle ilerler 
username_input.send_keys("standard_user") # bir inputa yazı yazmak için.

password_input = chrome.find_element(By.ID, "password") # ❌ Yanlış (Elementi beklemez direkt geldi varsayar)
password_input.send_keys("secret_sauce")

login_button = chrome.find_element(By.CSS_SELECTOR, "[data-test='login-button']")
login_button.click()

