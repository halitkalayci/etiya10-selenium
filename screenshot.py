from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://saucedemo.com")


wait.until( EC.visibility_of_element_located((By.ID, "user-name")) ).send_keys("standard_user123") 

wait.until( EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce123")

wait.until( EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='login-button']"))).click()

driver.save_screenshot("ss.png")