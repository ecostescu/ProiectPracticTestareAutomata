from behave import *


@when("I click on the 'Logo' image")
def step_impl(context):
    context.loginpage.click_logo()
