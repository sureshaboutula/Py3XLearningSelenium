from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_sample():
    driver = webdriver.Chrome()
    # driver =  webdriver.Chrome(ChromeDriverManager.install(self))
    driver.get("https://google.com")
    print(driver.session_id)
    assert driver.current_url == "https://www.google.com/"