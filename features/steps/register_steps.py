from behave import *


@when("I enter valid register data")
def step_impl(context):
    context.registerpage.set_email('')
    context.registerpage.set_first_name('')
    context.registerpage.set_last_name('')
    context.registerpage.set_password('')


@when("I enter no password")
def step_impl(context):
    context.loginpage.set_password('')
