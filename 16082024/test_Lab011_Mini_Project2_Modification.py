import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.positive
@allure.title("Mini Project 2 - VWO Login with invalid email and password")
@allure.description("Verify that with invalid email and password, error message will display")
def test_mini_project_2():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    assert driver.current_url == "https://app.vwo.com/#/login"

    # Email Input box element

    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@data-qa, 'hocewoqisi')]")
    ))
    #allure.attach(driver.get_screenshot_as_png(), name="VWO-Login-Page")
    # <input type="email" class="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi">
    #email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element = driver.find_element(By.XPATH, "//input[contains(@data-qa, 'hocewoqisi')]")
    email_web_element.send_keys("admin@admin.com")

    # Password Input box element
    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@data-qa, 'jobodapuxe')]"))
    )
    # <input type="password" class="text-input W(100%)" name="password" id="login-password" data-qa="jobodapuxe">
    password_web_element = driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']")
    password_web_element.send_keys("admin@123")

    # Click on Sign in Button
    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(normalize-space(), 'Sign in')][contains(@data-qa, 'sibequkica')]"))
    )
    # <button type="submit" id="js-login-btn" class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)" onclick="login.login(event)" data-qa="sibequkica">
    # <span class="icon loader hidden" data-qa="zuyezasugu"></span>
    # <span data-qa="ezazsuguuy">Sign in</span>
    # </button>

    #signin_btn_web_element = driver.find_element(By.CSS_SELECTOR, "[data-qa='sibequkica']")
    signin_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    signin_btn_web_element.click()
    time.sleep(3) # Using time.sleep is bad practice - Python interpreter will stop the execution for 3 sec. Ideally Webdriver should be stopped
    allure.attach(driver.get_screenshot_as_png(), name="VWO-Login-Page")
    # Error message element
    WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_element_located((By.XPATH,
                                       "//div[contains(normalize-space(), 'did not match')][contains(@data-qa, 'tozemoxine')]"))
    )
    allure.attach(driver.get_screenshot_as_png(), name="VWO-Login-Page-Error-Message")
    # <div class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">Your email, password, IP address or location did not match</div>
    assert driver.find_element(By.XPATH, "//div[contains(@data-qa, 'tozemoxine')]").text == "Your email, password, IP address or location did not match"
    driver.quit()

