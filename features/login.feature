@LoginTests
Feature: Login Page Tests
    As a user
    I want to login into the website
    So that I can access the dashboard

    Background:
        Given I am on the login page

    @TC001-Login(Positive)
    Scenario: Successful login with valid credentials
    When I log in with user "demouser" and password "abc123"
    Then I should be redirected to the dashboard

    @TC002-Login(Negative)
    Scenario Outline: Validating login with invalid credentials Interation n "<Iteration>"
    When I log in with user "<Username>" and password "<Password>"
    Then I should the error message "Wrong username or password."

    Examples:
      | Iteration | Username  | Password |
      | 1         | Demouser  | abc123   |
      | 2         | demouser_ | xyz      |
      | 3         | demouser  | nananana |
      | 4         | demouser  | abc123   |


    @TC003-ValidateInvoiceDetails
    Scenario: Successful login with valid credentials
    When I log in with user "demouser" and password "abc123"
    And I should be redirected to the dashboard
    And I click on the invoice link on the Hotel name "Rendezvous Hotel"
    Then the application should open the Invoice Details screen
    And I validate the information presented:
      | Key               | Value            |
      | Hotel Name        | Rendezvous Hotel |
      | Invoice Date      | 14/01/2018       |
      | Due Date          | 15/01/2018       |
      | Invoice Number    | 110              |
      | Booking Code      | 0875             |
      | Customer Details  | JOHNY SMITH R2  |
      | Room              | Superior Double  |
      | Check In          | 14/01/2018       |
      | Check Out         | 15/01/2018       |
      | Total Stay Count  | 1                |
      | Total Stay Amount | $150             |
      | Deposit Now       | USD $20.90       |
      | Tax & VAT         | USD $19          |
      | Total Amount      | USD $209         |





