Feature: Login Validation

  Background:
    Given the user opens the BigBasket Bangladesh website

  Scenario: Verify login popup
    When the user opens the login page
    Then the email field should be displayed
    And the password field should be displayed

  Scenario: Invalid login
    When the user opens the login page
    And the user enters email "test@gmail.com"
    And the user enters password "123456"
    And the user clicks the login button
    Then an error message should be displayed