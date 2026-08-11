Feature: Shopping Cart

  Background:
    Given the user opens the BigBasket Bangladesh website

  Scenario: Add a product to cart
    When the user searches for "Milk"
    And the user opens the first product
    And the user adds the product to the cart
    Then the cart should contain the product

  Scenario: Remove a product from cart
    When the user searches for "Milk"
    And the user opens the first product
    And the user adds the product to the cart
    And the user opens the cart
    And the user removes the product
    Then the cart should be empty