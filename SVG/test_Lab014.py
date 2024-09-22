import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.positive
@allure.title("SVG Demo for amcharts-maps")
@allure.description("Verify Click functionality for SVG maps")
def test_amcharts_maps_project():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    allure.attach(driver.get_screenshot_as_png(), name="amcharts-Homepage")
    assert driver.current_url == "https://www.amcharts.com/svg-maps/?map=india"

    # #Directly clicking the state element
    # WebDriverWait(driver=driver, timeout=3).until(
    #     EC.presence_of_element_located((By.XPATH, "//*[name()='path'][contains(@aria-label, 'Tripura')]"))
    # )
    # time.sleep(5)
    # Tripura_map__ele = driver.find_element(By.XPATH, "//*[name()='path'][contains(@aria-label, 'Tripura')]")
    # Tripura_map__ele.click()

    # Finding all states and clicking on requested state
    states_ele = driver.find_elements(By.XPATH, "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g'][1]/*[name()='path']")
    for state in states_ele:
        #print(state.get_attribute("aria-label"))
        if "Tripura" in state.get_attribute("aria-label"):
            time.sleep(5)
            state.click()
            break
    allure.attach(driver.get_screenshot_as_png(), name="State-Map-Clicked")

    driver.quit()