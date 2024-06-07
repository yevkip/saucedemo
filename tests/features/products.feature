Feature: Products

  Scenario Outline: Add <final_qty> product(s) to cart
    Given Logged in User is on Products page
    When User adds <final_qty> product to cart
    When User navigates to cart
    Then Cart contains <final_qty> product(s)
    Examples:
      | final_qty |
      | 1         |
      | 6         |


  Scenario Outline: Remove <qty_to_remove> product(s) from cart from Products page
    Given Logged in User is on Products page
    Given Cart contains <initial_qty> product(s)
    When User clicks on Remove btn for <qty_to_remove> added product(s)
    When User navigates to cart
    Then Cart contains <final_qty> product(s)
    Examples:
      | initial_qty | qty_to_remove | final_qty |
      | 1           | 1             | 0         |
      | 6           | 2             | 4         |

  Scenario Outline: Remove <qty_to_remove> products from cart from Cart page
    Given Logged in User is on Products page
    Given Cart contains <initial_qty> product(s)
    Given User is on Cart page
    When In cart User clicks on Remove btn for <qty_to_remove> added product(s)
    Then Cart contains <final_qty> product(s)
    Examples:
      | initial_qty | qty_to_remove | final_qty |
      | 1           | 1             | 0         |
      | 6           | 2             | 4         |

  Scenario Outline: Verify btn state change from "<initial_state>" to "<final_state>"
    Given Logged in User is on Products page
    Given User picks a product
    Given Btn state is <initial_state>
    When User clicks on <initial_state> btn on Products page
    Then Btn state is <final_state>
    Examples:
      | initial_state | final_state |
      | Add to cart   | Remove      |

  Scenario Outline: Verify btn state change from "<initial_state>" to "<final_state>"
    Given Logged in User is on Products page
    Given User picks a product
    Given User clicks on <initial_state> btn on Products page
    Given Btn state is <initial_state>
    When User clicks on <initial_state> btn on Products page
    Then Btn state is <final_state>
    Examples:
      | initial_state | final_state |
      | Remove        | Add to cart |

  Scenario Outline: Cart counter increase. Total <final_qty> product(s)
    Given Logged in User is on Products page
    Given Cart contains <initial_qty> product(s)
    When User adds <qty_to_add> product to cart
    Then Cart badge shows <final_qty> product(s) in cart
    Examples:
      | initial_qty | qty_to_add | final_qty |
      | 0           | 1          | 1         |

  Scenario Outline: Cart counter decrease from Products page. <final_qty> products left.
    Given Logged in User is on Products page
    Given Cart contains <initial_qty> product(s)
    When User clicks on Remove btn for <qty_to_remove> added product(s)
    Then Cart badge shows <final_qty> product(s) in cart
    Examples:
      | initial_qty | qty_to_remove | final_qty |
      | 6           | 2             | 4         |

  Scenario Outline: Cart counter decrease from Cart page. <final_qty> products left.
    Given Logged in User is on Products page
    Given Cart contains <initial_qty> product(s)
    Given User is on Cart page
    When In cart User clicks on Remove btn for <qty_to_remove> added product(s)
    Then Cart badge shows <final_qty> product(s) in cart
    Examples:
      | initial_qty | qty_to_remove | final_qty |
      | 1           | 1             | 0         |

  Scenario: Verify btn state on Cart page is "Remove"
    Given Logged in User is on Products page
    Given Cart contains 3 product(s)
    Given User is on Cart page
    When User picks a product on Cart page
    Then Btn state is Remove

  Scenario: Verify product autonomy when "Add to cart" btn is clicked
    Given Logged in User is on Products page
    Given User picks a product
    When User clicks on "Add to cart" btn on Products page
    Then All products except affected one are displayed with "Add to cart" btn

