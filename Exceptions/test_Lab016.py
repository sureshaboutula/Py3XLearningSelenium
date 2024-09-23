import time
import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.positive
@allure.title("Mini Project - Exceptions Demo")
@allure.description("Exception with Try and Except")
def test_mini_project_exception_demo():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com/")
    driver.maximize_window()
    try:
        #driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys("The testing academy")
        driver.find_element(By.XPATH, "//textarea[@name='qqqq']").send_keys("The testing academy")
    except NoSuchElementException as nce:
        print(f"No Such an element found, check locator, {nce}")

    time.sleep(5)
    driver.quit()

