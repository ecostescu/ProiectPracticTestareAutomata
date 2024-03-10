import time

from behave import *


@Given("I navigate to home page")
def step_impl(context):    
    context.homepage.load()
    context.homepage.accept_cookies()


@when("I navigate to login")
def step_impl(context):
    time.sleep(2)
    context.homepage.go_to_login()


@when("I navigate to wishlist")
def step_impl(context):
    time.sleep(1)
    context.homepage.go_to_wishlist()

@when("I navigate to register page")
def step_impl(context):
    time.sleep(1)
    context.homepage.go_to_register()


@when("I navigate to cart")
def step_impl(context):
    context.homepage.go_to_cart()


@when("I navigate to help")
def step_impl(context):
    context.homepage.go_to_help()


@then("I should be logged in with my user")
def step_impl(context):
    assert str(context.homepage.get_logged_in_name()).lower() \
          == 'elena', f"The login name is not as expected,\n{str(context.homepage.get_logged_in_name()).lower()} is " \
                      f"expected"


@then("I should be redirected to the home page")
def step_impl(context):
    assert str(context.homepage.get_current_url()).lower() \
          == 'https://www.sinsay.com/ro/ro/', f"The url is not as expected," \
                                              f"\n{str(context.homepage.get_current_url()).lower()} is "\
                                              f"expected"


@then("I should be redirected to the wishlist page")
def step_impl(context):
    assert str(context.homepage.get_current_url()).lower() \
          == 'https://www.sinsay.com/ro/ro/wishlist/', f"The url is not as expected," \
                                              f"\n{str(context.homepage.get_current_url()).lower()} is "\
                                              f"expected"


@then("I should be redirected to the cart page")
def step_impl(context):
    assert str(context.homepage.get_current_url()).lower() \
          == 'https://www.sinsay.com/ro/ro/checkout/cart/', f"The url is not as expected," \
                                              f"\n{str(context.homepage.get_current_url()).lower()} is "\
                                              f"expected"


@then("I should be redirected to the help page")
def step_impl(context):
    assert str(context.homepage.get_current_url()).lower() \
           == 'https://www.sinsay.com/ro/ro/help', f"The url is not as expected," \
                                               f"\n{str(context.homepage.get_current_url()).lower()} is " \
                                               f"expected"