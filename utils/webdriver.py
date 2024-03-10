from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()
