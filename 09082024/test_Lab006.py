import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    driver.refresh()
    assert driver.current_url == "https://app.vwo.com/#/login"
    driver.get("https://google.com")
    assert driver.current_url == "https://www.google.com/"
    driver.back()
    assert driver.current_url == "https://app.vwo.com/#/login"
    driver.forward()
    assert driver.current_url == "https://www.google.com/"