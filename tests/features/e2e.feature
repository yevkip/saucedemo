Feature: e2e scenarios

  Scenario: User Session is unique
    Given Logged in User1 is on Products page
    Given Cart contains 1 product(s)
    When User1 logged out
    When User2 is logged in
    When User2 navigates to cart
    Then Cart is empty









