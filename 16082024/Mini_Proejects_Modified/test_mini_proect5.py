import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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
    allure.attach(driver.get_screenshot_as_png(), name="Homepage-screenshot")
    #time.sleep(5)
    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//a[contains(@id, 'btn-make-appointment')]"))
    )

    # <a id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">Make Appointment</a>

    driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    #time.sleep(3)
    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//a[contains(normalize-space(), 'Login')]"))
    )
    allure.attach(driver.get_screenshot_as_png(), name="Appointment-Login-Page-Screenshot")
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()
    allure.attach(driver.get_screenshot_as_png(), name="Make-appointment-Page-Screenshot")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    #assert driver.find_element(By.CLASS_NAME, "col-sm-12 text-center").is_displayed()
    assert driver.find_element(By.TAG_NAME, "h2").text == "Make Appointment"
    driver.quit()