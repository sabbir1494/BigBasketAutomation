Feature: BigBasket Bangladesh Product Search

  Background:
    Given the user opens the BigBasket Bangladesh website

  Scenario: Search for Milk
    When the user searches for "Milk"
    Then search results should be displayed

  Scenario: Search for Rice
    When the user searches for "Rice"
    Then search results should be displayed

  Scenario: Search for Biscuit
    When the user searches for "Biscuit"
    Then search results should be displayed

  Scenario: Search for Egg
    When the user searches for "Egg"
    Then search results should be displayed

  Scenario: Search for Cooking Oil
    When the user searches for "Cooking Oil"
    Then search results should be displayed