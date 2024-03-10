from pages.register_page import RegisterPage
from utils.webdriver import WebDriver
from pages.home_page import HomePage
from pages.login_page import LoginPage


def before_all(context):

    pass


def after_all(context):

    pass


def before_scenario(context, scenario):
    context.driver = WebDriver().driver
    context.homepage = HomePage(context.driver)
    context.loginpage = LoginPage(context.driver)
    context.registerpage = RegisterPage(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
