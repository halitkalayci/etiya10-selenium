from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():
    USERNAME_INPUT = (By.ID,"user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self):
        self.driver = Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def type_into(self, element, text):
       self.wait.until(EC.visibility_of_element_located(element)).send_keys(text)

    def click_into(self, element):
        self.wait.until(EC.visibility_of_element_located(element)).click()

    def login(self, username, password):
        self.type_into(self.USERNAME_INPUT, username)
        self.type_into(self.PASSWORD_INPUT, password)
        self.click_into(self.LOGIN_BUTTON)
    
    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_CONTAINER)).text