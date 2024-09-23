import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.positive
@allure.title("Mini Project - Relative locators Demo")
@allure.description("Relative locators Demo")
def test_mini_project_relative_locators():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.aqi.in/real-time-most-polluted-city-ranking")
    driver.maximize_window()

    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//input[@id='search_city']"))
    )
    # Find Search box to Enter Text
    driver.find_element(By.XPATH, "//input[@id='search_city']").send_keys("India")
    time.sleep(3)

    list_of_states = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[2]")
    print("Name" + " | " + "AQI" + " | " + "Rank")
    for state in list_of_states:
        if "India" in state.text:
            s1 = driver.find_element(locate_with(By.TAG_NAME, 'p').to_right_of(state)).text
            s2 = driver.find_element(locate_with(By.TAG_NAME, 'p').to_left_of(state)).text
            s3 = driver.find_element(locate_with(By.TAG_NAME, 'p').below(state)).text
            s4 = driver.find_element(locate_with(By.TAG_NAME, 'p').above(state)).text
            print(state.text + " | " + s1 + " | " + s2)
            print(state.text + " | " + s3 + " | " + s4)
            print("*****************")
    time.sleep(5)

    driver.quit()