import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.positive
@allure.title("Mini Project - Select Demo")
@allure.description("Select Demo to select static dropdown values")
def test_mini_project_3():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.maximize_window()

    select_element = driver.find_element(By.XPATH, "//*[@id='dropdown']")
    select = Select(select_element)
    select.select_by_visible_text("Option 2")
    select.select_by_value("1")
    time.sleep(2)
    driver.quit()