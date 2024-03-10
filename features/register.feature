Feature: Register user
  Background:
  Given I navigate to home page
    And I navigate to register page

    Scenario: Successful Register
    And I enter my email
    And I enter my password
    And I click on Submit button
    Then I should be logged in with my user