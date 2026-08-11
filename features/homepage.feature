Feature: BigBasket Bangladesh Homepage

  Background:
    Given the user opens the BigBasket Bangladesh website

  Scenario: Verify homepage loads successfully
    Then the homepage should load successfully

  Scenario: Verify homepage title
    Then the homepage title should be displayed

  Scenario: Verify homepage URL
    Then the homepage URL should be correct

  Scenario: Verify search box
    Then the search box should be visible

  Scenario: Verify website logo
    Then the website logo should be visible