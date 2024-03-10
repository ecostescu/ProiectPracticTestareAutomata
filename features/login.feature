Feature: Login
  Background:
  Given I navigate to home page
    When I navigate to login

  Scenario: Successful Login
    And I enter my email
    And I enter my password
    And I click on Submit button
    Then I should be logged in with my user


  Scenario: Incorrect e-mail
    And I enter incorrect email
    And I enter my password
    And I click on Submit button
    Then I should receive an error message


  Scenario: Incorrect password
    And I enter my email
    And I enter incorrect password
    And I click on Submit button
    Then I should receive an error message


  Scenario: Empty email field
    And I enter no email
    And I enter my password
    And I click on Submit button
    Then I should see the validation error that the email is required


   Scenario: Empty password field
    And I enter my email
    And I enter no password
    And I click on Submit button
    Then I should see the validation error that the password is required


   Scenario: Email not formatted correctly
     And I enter invalid email
     Then I should see the validation error that only valid characters must be added


  Scenario Outline: Incorrect e-mail and password set
    And I enter an incorrect "<email>" and "<password>"
    And I click on Submit button
    Then I should receive an error message
    Examples:
      |email                |password           |
      |elena@2rd.ro         |123456             |
      |asca@koasdli.fe      |Superpassword      |
      |awdxas@yaasdhoo.com  |safepass           |
      |eawasmail@test.com   |verysecretpassword |
      |doiu@test.co.uk      |alabala            |
      |lumea@test.itf       |987654asda3210     |
      |ola@test.ro          |asedw212341        |