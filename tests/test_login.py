from selenium.webdriver.common.by import By

import config
from locators import *
from selenium.webdriver.remote.webdriver import WebDriver

def test_login_user(driver: WebDriver):
    MainPage.login(driver, config.email, config.password)
    assert driver.find_element(By.XPATH, MainPage.user_profile_pic).is_displayed() == True
    assert driver.find_element(By.XPATH, MainPage.user_profile_name).text == 'User.'
