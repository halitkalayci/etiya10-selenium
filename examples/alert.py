from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By

driver = Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

alert_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
alert_btn.click()

sleep(2)

alert = driver.switch_to.alert
alert.accept() # tamama tıkla

confirm_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
confirm_btn.click()
sleep(2)
confirm = driver.switch_to.alert
confirm.dismiss() #iptal'e tıkla

prompt_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
prompt_btn.click()
sleep(2)
prompt = driver.switch_to.alert
prompt.send_keys("Örnek")
prompt.accept()

sleep(30)