import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():
    chrome_options = Options()
    chrome_options.add_extension("/Users/suresh.aboutula/Downloads/GoFullPage-Full-Page-Screen-Capture-Chrome-Web-Store.crx")
    #chrome_options.add_argument("--proxy-server='your proxy server'")
    # chrome_options.add_argument("--page-load-strategy=none")
    # chrome_options.add_argument("--page-load-strategy=normal")
    # chrome_options.add_argument("--page-load-strategy=eager")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://youtube.com")
    driver.maximize_window()
    time.sleep(10)