from selenium.webdriver.common.by import By

from pages.page_objects import PageObjects


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(PageObjects.home_page_url)

    def go_to_login(self):
        self.driver.find_element(By.XPATH, PageObjects.login_button).click()

    def go_to_register(self):
        self.driver.find_element(By.XPATH, PageObjects.register_button).click()

    def go_to_wishlist(self):
        self.driver.find_element(By.XPATH, PageObjects.wishlist_button).click()

    def go_to_cart(self):
        self.driver.find_element(By.XPATH, PageObjects.cart_button).click()

    def go_to_help(self):
        self.driver.find_element(By.XPATH, PageObjects.help_button).click()

    def accept_cookies(self):
        self.driver.find_element(By.XPATH, PageObjects.cookie_button_ok).click()

    def get_logged_in_name(self):
        return self.driver.find_element(By.XPATH, PageObjects.account_button).text

    def get_current_url(self):
        return self.driver.current_url


