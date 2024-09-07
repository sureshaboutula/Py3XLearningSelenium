import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Mini Project 1 - Verify that URL changes after clicking on the Make appointment button")
@allure.description("Verify that URL changes after clicking on the Make appointment button")
def test_mini_project_1():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

    # Find the Make appointment element
    #<a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")

    # Click on Make appointment element
    make_appointment_element.click()

    # Verify the Url change
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(4)

    driver.quit()

