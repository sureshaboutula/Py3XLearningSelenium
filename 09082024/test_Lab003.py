import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():
    # Options class - What is this class?
    # customize the behaviour of the browser during automated testing
    # Chrome -> Headless or UI --> Headless mode is No UI
    # disable gps, add extension, maximize, set windows size, etc.....100 other options that you can set before starting the browser

    # Create an instance of ChromeOptions
    chrome_options = Options()
    # chrome_options.add_argument("--window-size=1920x1080")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--disable-infobars") --> It won't work, need to search for alternate command
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    time.sleep(2)
