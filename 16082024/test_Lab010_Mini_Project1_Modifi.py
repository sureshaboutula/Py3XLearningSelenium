import time


import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.positive
@allure.title("Mini Project 1 - Verify that URL changes after clicking on the Make appointment button")
@allure.description("Verify that URL changes after clicking on the Make appointment button")
def test_mini_project_1_modify():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    # Add screenshot
    allure.attach(driver.get_screenshot_as_png(), name="Katelon-Home-Page")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

    # Find the Make appointment element
    WebDriverWait(driver=driver, timeout=10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@id, 'btn-make-appointment')]"))
    )
    #<a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
    make_appointment_element = driver.find_element(By.XPATH, "//a[contains(@id, 'btn-make-appointment')]")

    # Click on Make appointment element
    make_appointment_element.click()
    allure.attach(driver.get_screenshot_as_png(), name="Katelon-Makeappointment-Page")
    # Verify the Url change
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    driver.quit()

