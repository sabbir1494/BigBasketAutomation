Feature: Footer Validation

  Background:
    Given the user opens the BigBasket Bangladesh website

  Scenario: Verify footer section
    When the user scrolls to the footer
    Then the footer should be displayed

  Scenario: Verify footer links
    When the user scrolls to the footer
    Then the footer links should be displayed

  Scenario: Open About Us page
    When the user scrolls to the footer
    And the user opens the About Us page
    Then the About Us page should open successfully

  Scenario: Open Contact Us page
    When the user scrolls to the footer
    And the user opens the Contact Us page
    Then the Contact Us page should open successfully