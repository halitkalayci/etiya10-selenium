from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
import requests

driver = Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/broken_images")


image_elements = driver.find_elements(By.TAG_NAME, "img")

broken_imglist=[]

for element in image_elements:
    src = element.get_attribute("src")
    response = requests.get(src)
    if response.status_code != 200:
        broken_imglist.append(src)

print("Bozuk image listesi:", broken_imglist)