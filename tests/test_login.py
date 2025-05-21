from selenium.webdriver.common.by import By
from pages import *
from selenium.webdriver.remote.webdriver import WebDriver

def test_login_user(driver: WebDriver):
    MainPage.login(driver, 'testusernewest@mail.ru', 'temporarypassword')
    assert driver.find_element(By.XPATH, MainPage.user_profile_pic).is_displayed() == True
    assert driver.find_element(By.XPATH, MainPage.user_profile_name).text == 'User.'
