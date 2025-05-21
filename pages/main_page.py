from selenium.webdriver.common.by import By
from .main_page_registrarion_popup import MainPageRegistrationPopup
from .main_page_signin_popup import MainPageSigninPopup

class MainPage:
    login_and_register_button = "//button[text()='Вход и регистрация']"
    user_profile_pic = "//*[local-name()='svg' and @class='svgSmall']"
    user_profile_name = "//h3[@class='profileText name']"
    logout_user = "//button[@class='spanGlobal btnSmall']"
    submit_announcement = "//div[@class='header_flexRow__Xdqv1']/button[@class='buttonPrimary inButtonText undefined inButtonText']"

    @classmethod
    def register(cls, driver, email, password, password_submit=None):
        if password_submit is None:
            password_submit = password
        driver.find_element(By.XPATH, MainPage.login_and_register_button).click()
        driver.find_element(By.XPATH, MainPageSigninPopup.no_account_button).click()
        driver.find_element(By.XPATH, MainPageRegistrationPopup.email_input).send_keys(email)
        driver.find_element(By.XPATH, MainPageRegistrationPopup.password_input).send_keys(password)
        driver.find_element(By.XPATH, MainPageRegistrationPopup.submit_password_input).send_keys(password_submit)
        driver.find_element(By.XPATH, MainPageRegistrationPopup.registration_button).click()

    @classmethod
    def login(cls, driver, email, password):
        driver.find_element(By.XPATH, MainPage.login_and_register_button).click()
        driver.find_element(By.XPATH, MainPageSigninPopup.email_input).send_keys(email)
        driver.find_element(By.XPATH, MainPageSigninPopup.password_input).send_keys(password)
        driver.find_element(By.XPATH, MainPageSigninPopup.login_button).click()
