# config test .py

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    yield wait

# hata veren bütün testlerin ekran görüntüsü alınsın.

# Şu ana kadar yaptıklarımızı POM mimarisi ile tekrar refactor edelim.