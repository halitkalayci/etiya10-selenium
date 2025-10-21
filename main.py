from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

inv_items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[data-test='inventory-item']")))
print(f"Şu kadar ürün bulundu: {len(inv_items)}")

# Son ürüne tıkla.
# .find_element daima tüm chromeda değil elementin içinde de bulunur.
inv_items[len(inv_items) - 1].find_element(By.TAG_NAME, "button").click()

for i in len(inv_items):
    print(i)

time.sleep(60)

#dev->süreç
#test-> test.etiya.com (database) -> veriler dinamiktir ama veritabanı da bizde olduğu için hangi veriyle test edeceğimi bilirim.
#prod-> (database) testlerin bittiği canlı ortam
#......