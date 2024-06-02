Feature: Checkout

  Scenario Outline: User is able to checkout with <qty> products
    Given I load the website
    Given User is logged in
    Given User is on Products page
    When User adds <final_qty> product to cart
    When User navigates to cart
    When User clicks to "Checkout" btn
    Then User is on Checkout page
    Examples:
      | final_qty |
      | 1         |
      | 6         |

  Scenario Outline: User is able to checkout with <qty> products
    Given I load the website
    Given User is logged in
    Given User is on Products page
    When User adds <final_qty> product to cart
    When User navigates to cart
    When User clicks to "Checkout" btn
    When User enter first name, last name, Zip code on Checkout page
    When User clicks on "Continue" btn
    Then User is on Checkout Overview page
    Then <final_qty> added to cart products are displayed with expected prices
    Then Price Total has expected calculation
    Examples:
      | final_qty |
      | 1         |
      | 6         |

  Scenario Outline: User is able to checkout with <qty> products
    Given I load the website
    Given User is logged in
    Given User is on Products page
    When User adds <final_qty> product to cart
    When User navigates to cart
    When User clicks on "Checkout" btn
    When User enter first name, last name, Zip code on Checkout page
    When User clicks on "Continue" btn
    When User is on Checkout Overview page
    When User clicks on "Finish" btn
    Then User is on Checkout: Complete! page
    Then Checkout complete message is displayed
    Examples:
      | final_qty |
      | 1         |
      | 6         |

  Scenario: User is not able to checkout with empty cart
    Given I load the website
    Given User is logged in
    Given User is on Products page
    Given Cart is empty
    When User navigates to cart
    Then Checkout btn is disabled

  Scenario Outline: User is not able to checkout with missed checkout info <info>
    Given I load the website
    Given User is logged in
    Given User is on Products page
    Given User adds 1 product to cart
    When User navigates to cart
    When User clicks on "Checkout" btn
    When User complete checkout info without <info>
    When User clicks on "Continue" btn
    Then Error is displayed
    Then User is on Checkout page
    Examples:
      | info       |
      | First Name |
      | Last Name  |
      | Zip code   |
