import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Mini Project 5 - Open katalon URL and Click on Make Appointment")
@allure.description("Verify the make appointment screen after log in")
def test_mini_project_5():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(5)

    # <a id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">Make Appointment</a>

    driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="Login_Page_Screenshot")
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    allure.attach(driver.get_screenshot_as_png(), name="Loggedin_success_Screenshot")
    #assert driver.find_element(By.CLASS_NAME, "col-sm-12 text-center").is_displayed()
    assert driver.find_element(By.TAG_NAME, "h2").text == "Make Appointment"

    time.sleep(4)
    driver.quit()