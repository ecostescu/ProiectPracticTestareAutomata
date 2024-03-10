from selenium.webdriver.common.by import By

from pages.page_objects import PageObjects


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.XPATH, PageObjects.register_email).send_keys(email)

    def set_first_name(self, firstname):
        self.driver.find_element(By.XPATH, PageObjects.register_firstName).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(By.XPATH, PageObjects.register_lastName).send_keys(lastname)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, PageObjects.register_password).send_keys(password)

    def click_register(self):
        self.driver.find_element(By.XPATH, PageObjects.register_submit).click()
