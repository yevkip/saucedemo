Feature: e2e scenarios

  Scenario: User Session is unique
    Given I load the website
    Given User1 is logged in
    Given User1 is on Products page
    Given User1 adds 1 product to cart
    Given User1 logged out
    When User2 is logged in
    Then Cart is empty









