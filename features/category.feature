Feature: Product Categories

  Background:
    Given the user opens the BigBasket Bangladesh website

  Scenario: Open first category
    When the user opens the category menu
    And the user opens the first category
    Then category products should be displayed

  Scenario: Verify category filters
    When the user opens the category menu
    And the user opens the first category
    Then the filter section should be displayed
    And the price filter should be displayed
    