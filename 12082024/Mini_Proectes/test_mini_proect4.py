import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Mini Project 3 - Open SignUp URL of VWO")
@allure.description("Verify that the URL changes, when user clicks on signup button")
def test_mini_project_4():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    assert driver.current_url == "https://www.idrive360.com/enterprise/login"
    time.sleep(5)

    # Find element for Email
    # <input _ngcontent-flo-c4="" autofocus=""
    # class="id-form-ctrl ng-valid ng-touched ng-dirty"
    # id="username" name="username" type="email">
    email_web_element = driver.find_element(By.ID, "username")
    email_web_element.send_keys("augtest_040823@idrive.com")

    # Find element for Password
    # <input _ngcontent-flo-c4=""
    # class="id-form-ctrl ng-pristine ng-valid ng-touched"
    # id="password" maxlength="20" name="password" tabindex="0" type="password">
    email_web_element = driver.find_element(By.ID, "password")
    email_web_element.send_keys("123456")

    # Find Signin element
    # <button _ngcontent-flo-c4=""
    # class="id-btn id-info-btn-frm"
    # id="frm-btn" type="submit">Sign in</button>
    signin_web_element = driver.find_element(By.ID, "frm-btn")
    signin_web_element.click()
    time.sleep(10)
    # <h5 _ngcontent-wjy-c10="" class="id-card-title">Your free trial has expired</h5>
    assert driver.find_element(By.CLASS_NAME, "id-card-title").text == "Your free trial has expired"
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    allure.attach(driver.get_screenshot_as_png(), name="error-message-screenshot")

    time.sleep(4)
    driver.quit()