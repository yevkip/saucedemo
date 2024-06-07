Feature: Login

  Scenario Outline: Login as "<user>" user with valid creds
    Given Website is loaded
    When User enter <user> username to username field
    When User enter secret_sauce password to password field
    When User click on "Login" btn
    Then User is on Products page
    Examples:
      | user          |
      | standard_user |
      | problem_user  |
      | error_user    |
      | visual_user   |


  Scenario Outline: Login attempt <reason>
    Given Website is loaded
    When User enter <user> username to username field
    When User enter <password> password to password field
    When User click on "Login" btn
    Then User see an error <error>
    Examples:
      | user             | password     | reason                      | error                                                                     |
      | standard_user    | [blank]      | with missed password        | Epic sadface: Password is required                                        |
      | [blank]          | secret_sauce | with missed username        | Epic sadface: Username is required                                        |
      | [blank]          | [blank]      | with empty creds            | Epic sadface: Username is required                                        |
      | Standard_user    | secret_sauce | with username with uppecase | Epic sadface: Username and password do not match any user in this service |
      | nonexistent_user | secret_sauce | with nonexistent username   | Epic sadface: Username and password do not match any user in this service |
      | locked_out_user  | secret_sauce | as locked out user          | Epic sadface: Sorry, this user has been locked out.                       |


