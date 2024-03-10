from selenium.webdriver.common.by import By

from pages.page_objects import PageObjects


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(PageObjects.home_page_url)

    def set_email(self, email):
        self.driver.find_element(By.XPATH, PageObjects.login_email).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, PageObjects.login_password).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH, PageObjects.submit_button).click()

    def get_title(self):
        return self.driver.title

    def is_login_error_displayed(self):
        assert self.driver.find_element(By.XPATH, PageObjects.login_error).is_displayed()

    def is_empty_email_error_displayed(self):
        assert self.driver.find_element(By.XPATH, PageObjects.no_email_error).is_displayed()

    def is_no_password_error_displayed(self):
        assert self.driver.find_element(By.XPATH, PageObjects.no_password_error).is_displayed()

    def get_invalid_email_error(self):
        return self.driver.find_element(By.XPATH, PageObjects.no_email_error).text

    def click_logo(self):
        self.driver.find_element(By.XPATH, PageObjects.logo_image).click()
