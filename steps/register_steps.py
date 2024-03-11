from uuid import uuid4

from behave import *


@when("I enter valid register data")
def step_impl(context):
    context.registerpage.set_email(context.config.userdata['emailproto']+uuid4()+'@gmail.com')
    context.registerpage.set_first_name(context.config.userdata['firstname'])
    context.registerpage.set_last_name(context.config.userdata['lastname'])
    context.registerpage.set_password(context.config.userdata['password'])


@when("I click on register")
def step_impl(context):
    context.registerpage.click_register()
