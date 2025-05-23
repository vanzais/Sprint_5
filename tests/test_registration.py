from selenium.webdriver.common.by import By
from locators import *
import config

def test_registration(driver, random_email):
    MainPage.register(driver, random_email,  config.password)
    assert driver.find_element(By.XPATH, MainPage.user_profile_pic).is_displayed() == True
    assert driver.find_element(By.XPATH, MainPage.user_profile_name).text == 'User.'

def test_registration_error(driver, random_email_error):
    MainPage.register(driver, random_email_error,  config.password)
    assert driver.find_element(By.XPATH, MainPageRegistrationPopup.error_text).is_displayed() == True
    assert 'rgb(255, 105, 114)' in driver.find_element(By.XPATH, MainPageRegistrationPopup.border_input_error).value_of_css_property('border')

def test_registration_existing_user(driver):
    MainPage.register(driver, config.email,  config.password)
    assert driver.find_element(By.XPATH, MainPageRegistrationPopup.error_text).is_displayed() == True
    assert 'rgb(255, 105, 114)' in driver.find_element(By.XPATH, MainPageRegistrationPopup.border_input_error).value_of_css_property('border')


