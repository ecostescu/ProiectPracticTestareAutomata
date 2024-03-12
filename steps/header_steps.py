from behave import *
import time


@when("I click on the 'Logo' image")
def step_impl(context):
    time.sleep(2)
    context.loginpage.click_logo()
