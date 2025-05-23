from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import config
from locators import *
from selenium.webdriver.remote.webdriver import WebDriver

def test_logout_user(driver: WebDriver):
    MainPage.login(driver, config.email, config.password)
    driver.find_element(By.XPATH, MainPage.logout_user).click()
    WebDriverWait(driver, 2).until(EC.invisibility_of_element_located((By.XPATH, MainPage.user_profile_pic)))
    assert driver.find_element(By.XPATH, MainPage.login_and_register_button).is_displayed() == True


