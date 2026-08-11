Feature: Product Details

  Background:
    Given the user opens the BigBasket Bangladesh website

  Scenario: Verify product details
    When the user searches for "Milk"
    And the user opens the first product
    Then the product name should be displayed
    And the product price should be displayed
    And the product image should be displayed
    And the product availability should be displayed

  Scenario: Add product to cart
    When the user searches for "Rice"
    And the user opens the first product
    And the user adds the product to the cart
    Then the product should be added successfully