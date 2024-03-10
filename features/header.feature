Feature: Header and footer functionality on the website https://www.sinsay.com/ro/ro/.
    Background:
    Given I navigate to home page

Scenario: Check if the user is redirected to home page by clicking the 'logo'
    When I navigate to login
    And I click on the 'Logo' image
    Then I should be redirected to the home page

Scenario: When the user click on wishlist, should be redirected to wishlist page
    When I navigate to wishlist
    Then I should be redirected to the wishlist page

Scenario: When the user click on cart, should be redirected to cart page
    When I navigate to cart
    Then I should be redirected to the cart page

Scenario: When the user click on help, should be redirected to help page
    When I navigate to help
    Then I should be redirected to the help page