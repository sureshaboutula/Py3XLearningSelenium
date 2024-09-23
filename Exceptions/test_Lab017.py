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
        textarea = driver.find_element(By.XPATH, "//textarea[@name='q']")
        driver.refresh()
        # textarea = driver.find_element(By.XPATH, "//textarea[@name='q']")
        textarea.send_keys("The testing academy")
        # DOM elements - refreshed
        # // Refresh, Navigate other Page, change in DOM elements (Ajax Calls) - VueJS, AngularJS
        # webdriver -> stale element exception
        ###driver.switch_to.alert
    ### except NoAlertPresentException as npe:
    #      print(f"No Such an element found, check locator, {npe}")
    except StaleElementReferenceException as sre:
          print(sre)

    time.sleep(5)
    driver.quit()

