from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import config
from locators import *

def test_announcement_not_authorized(driver: WebDriver):
    driver.find_element(By.XPATH, MainPage.submit_announcement).click()
    assert driver.find_element(By.XPATH, MainPagePostAnnouncementPopup.authorization_form).is_displayed() == True

def test_announcement_authorized(driver: WebDriver):
    MainPage.login(driver, config.email, config.password)
    retry = 10
    while retry > 0:
        try:
            WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, MainPage.submit_announcement)))
            driver.find_element(By.XPATH, MainPage.submit_announcement).click()
            break
        except StaleElementReferenceException:
            retry -= 1
    driver.find_element(By.XPATH, AnnouncementPage.submit_name).send_keys('Название тест')
    driver.find_element(By.XPATH, AnnouncementPage.description).send_keys('Описание товара тест')
    driver.find_element(By.XPATH, AnnouncementPage.price).send_keys('1234')
    driver.find_element(By.XPATH, AnnouncementPage.dropdown_city).click()
    driver.find_element(By.XPATH, AnnouncementPage.dropdown_city_ekb).click()
    driver.find_element(By.XPATH, AnnouncementPage.dropdown_category).click()
    driver.find_element(By.XPATH, AnnouncementPage.dropdown_category_hobby).click()
    driver.find_element(By.XPATH, AnnouncementPage.radio_button_used).click()
    driver.find_element(By.XPATH, AnnouncementPage.publish_button).click()
    retry = 10
    while retry > 0:
        try:
            WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, MainPage.user_profile_pic)))
            driver.find_element(By.XPATH, MainPage.user_profile_pic).click()
            break
        except StaleElementReferenceException:
            retry -= 1
    assert driver.find_element(By.XPATH, ProfilePage.announcement_published).is_displayed() == True

