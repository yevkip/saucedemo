Feature: Checkout

  Scenario Outline: Verify total price for <qty> products on checkout page
    Given Logged in User is on Products page
    Given User proceed to Checkout page with <qty> product(s) in cart
    When User complete checkout info and proceed to Checkout Overview page
    Then User is on Checkout Overview page
    Then Checkout Overview page contains <qty> product(s) with expected prices
    Then Price Total has expected calculation
    Examples:
      | qty |
      | 1   |
      | 6   |

  Scenario Outline: Verify successful checkout message
    Given Logged in User is on Products page
    Given User proceed to Checkout page with <qty> product(s) in cart
    Given User complete checkout info and proceed to Checkout Overview page
    When User clicks on "Finish" btn
    Then User is on Checkout: Complete! page
    Then Checkout complete message is displayed
    Examples:
      | qty |
      | 1 |
      | 6 |

  Scenario: User is not able to checkout with empty cart
    Given Logged in User is on Cart page. Cart Empty
    When User proceeds to checkout
    Then "Cart is empty" error is displayed
#
#  Scenario Outline: User is not able to checkout with missed checkout info <missed_info>
#    Given Logged in User is on Products page
#    When User adds 1 product to cart
#    When User navigates to cart
#    When User clicks on "Checkout" btn
#    When User complete checkout info without <missed_info>
#    When User clicks on "Continue" btn
#    Then Error is displayed
#    Then User is on Checkout page
#    Examples:
#      | missed_info | first_name | last_name | zip     |
#      | First Name  | [blank]    | Bond      | CB12GP  |
#      | Last Name   | James      | [blank]   | CB12GP  |
#      | Zip code    | James      | Bond      | [blank] |
