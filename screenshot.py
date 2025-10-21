from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os



driver = Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://saucedemo.com")


wait.until( EC.visibility_of_element_located((By.ID, "user-name")) ).send_keys("standard_user123") 

wait.until( EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce123")

login_button = wait.until( EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='login-button']")))
login_button.click()

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
os.makedirs("screenshots", exist_ok=True) # make directories, exist_ok=True klasör varsa onu kullan,yoksa oluştur.

login_button.screenshot("btn.png")
driver.save_screenshot("screenshots/"+timestamp+"_ss.png")