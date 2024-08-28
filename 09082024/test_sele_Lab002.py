import time
from selenium import webdriver

def test_open_vwologin():
    driver = webdriver.Chrome()
    print(driver.session_id)
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(5)