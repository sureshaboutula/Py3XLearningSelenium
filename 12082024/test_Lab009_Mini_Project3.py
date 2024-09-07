import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Mini Project 3 - Open SignUp URL of VWO")
@allure.description("Verify that the URL changes, when user clicks on signup button")
def test_mini_project_3():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    assert driver.current_url == "https://app.vwo.com/#/login"

    # Find SignUp element
    # <a href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">Start a free trial</a>

    #signup_web_element = driver.find_element(By.LINK_TEXT, "Start a free trial")
    signup_web_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    signup_web_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(4)

    driver.quit()

