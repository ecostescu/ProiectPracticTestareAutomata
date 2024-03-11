Feature: Register user
  Background:
  Given I navigate to home page

    @register_feature
    Scenario: Successful Register
    When I navigate to login
    And I navigate to register page
    And I enter valid register data
    And I click on register
    Then I should be logged in with my user
