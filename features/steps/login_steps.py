from behave import *


@when("I enter my email")
def step_impl(context):
    context.loginpage.set_email(context.config.userdata['email'])


@when("I enter my password")
def step_impl(context):
    context.loginpage.set_password(context.config.userdata['password'])


@when("I click on Submit button")
def step_impl(context):
    context.loginpage.click_submit()


@when("I enter incorrect email")
def step_impl(context):
    context.loginpage.set_email(context.config.userdata['incorrect_email'])


@when("I enter incorrect password")
def step_impl(context):
    context.loginpage.set_password(context.config.userdata['incorrect_password'])

    
@when('I enter an incorrect "{email}" and {password}')
def step_impl(context, email, password):
    context.loginpage.set_email(email)
    context.loginpage.set_password(email)


@when("I enter no email")
def step_impl(context):
    context.loginpage.set_email('')


@when("I enter no password")
def step_impl(context):
    context.loginpage.set_password('')


@when("I enter invalid email")
def step_impl(context):
    context.loginpage.set_email('invalid_email')


@then("I should see the validation error that the email is required")
def step_impl(context):
    context.loginpage.is_empty_email_error_displayed()


@then("I should see the validation error that the password is required")
def step_impl(context):
    context.loginpage.is_no_password_error_displayed()


@then('I should receive an error message')
def step_impl(context):
    context.loginpage.is_login_error_displayed()


@then("I should see the validation error that only valid characters must be added")
def step_impl(context):
    assert str(context.loginpage.get_invalid_email_error()) \
           == 'Vă rugăm să introduceți numai caractere valide', \
        f"The login name is not as expected,\n{str(context.loginpage.get_invalid_email_error()).lower()} is " \
        f"expected"

