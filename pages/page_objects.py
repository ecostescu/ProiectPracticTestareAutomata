class PageObjects:
    # URL:
    home_page_url = 'https://www.sinsay.com/ro/ro'
    register_page_url = 'https://www.sinsay.com/ro/ro/customer/account/login/#register/'

    #Fields
    login_email = '//input[@id="login[username]_id"]'
    login_password = '//input[@id="login[password]_id"]'

    #Buttons
    submit_button = '//button[@data-selen="login-submit"]'
    cookie_button_ok = '//button[text()="OK"]'
    login_button = '//button[@data-testid="account-info-logged-false"]'
    account_button = '//button[@data-testid="account-info-logged-true"]'
    login_error = '//div[@class="sc-TmdmN kRNdCB"]'
    no_email_error = '//div[@data-name="login[username]"]//div[@class="text-field__ErrorMessage-sc-1vll61a-4 WGIUj"]'
    no_password_error = '//div[@data-name="login[password]"]//div[@class="text-field__ErrorMessage-sc-1vll61a-4 WGIUj"]'
    logo_image = '//a[@data-testid="brand-logo-button"]'
    register_button = '//a[@data-testid="register-select"]'
    wishlist_button = '//div[@data-testid="header_heart"]/a'
    cart_button = '//button[@data-testid="cart-button"]'
    help_button = '//span[text()="Ajutor și contact"]'
    register_email = '//input[@data-selen="register-email"]'
    register_firstName = '//input[@data-selen="firstname"]'
    register_lastName = '//input[@data-selen="lastname"]'
    register_password = '//input[@data-selen="register-password"]'
    register_submit = '//button[@data-selen="create-account-submit"]'

