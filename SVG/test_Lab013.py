import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.positive
@allure.title("SVG Demo for Flipkart Search")
@allure.description("Verify Flipkart search element using SVG")
def test_flipkart_search_project():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    allure.attach(driver.get_screenshot_as_png(), name="Flipkart-Homepage")
    assert driver.current_url == "https://www.flipkart.com/"

    WebDriverWait(driver=driver, timeout=3).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@title, 'Search')]"))
    )
    search_input_ele = driver.find_element(By.XPATH, "//input[contains(@title, 'Search')]")
    search_input_ele.send_keys("AC")

    # Find Search element
    # //*[local-name()='svg']/*[local-name()='path' and @stroke='#717478'] - Not unique
    #search_icon_ele = driver.find_element(By.XPATH, "//*[local-name()='svg']/*[contains(text(), 'Search Icon')]")
    # search_icon_ele.click() --> It does not work, use Action class Or use list of elements

    search_icon_list = driver.find_elements(By.XPATH, "//*[local-name()='svg']")
    search_icon_list[0].click()
    allure.attach(driver.get_screenshot_as_png(), name="Flipkart-Search_Result_Page")

    driver.find_element(By.XPATH, "//div[@data-id='ACNH3WMQGGKUMXWP']").click()

    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="Flipkart-AC-Product")

    driver.quit()