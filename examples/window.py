from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
import requests

driver = Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")

out_link = driver.find_element(By.XPATH, '//*[@id="content"]/div/a')

out_link.click()

sleep(1)
tabs = driver.window_handles
driver.switch_to.window(tabs[1])

# Görüntüsel olarak 2.sekme geçmek != seleniumun bu sekmede çalışması demek değildir.
h3 = driver.find_element(By.XPATH, '/html/body/div/h3')
print(h3.text)

sleep(30)