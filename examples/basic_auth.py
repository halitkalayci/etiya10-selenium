from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.maximize_window()

# http basic authentication varsa
# https://username:password@adres.com
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

sleep(30)