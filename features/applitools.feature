Feature: Login and Expenses Table Validations
  As a tester
  I want to login and validate the dashboard table
  So that each functionality is independently tested

  Scenario: Login redirects to dashboard
    Given I am on the login page
    When I login with username "testuser" and password "testpassword"
    Then I should be redirected to the dashboard table page

  Scenario: Validate transactions count
    Given I am on the login page
    When I login with username "testuser" and password "testpassword"
    Then I should see exactly 6 transactions

  Scenario: Validate total balance
    Given I am on the login page
    When I login with username "testuser" and password "testpassword"
    Then the total balance should be "350"
  
  Scenario: Validate credit available
    Given I am on the login page
    When I login with username "testuser" and password "testpassword"
    Then the credit available should be "$17,800"

  Scenario: Validate positive amounts color
    Given I am on the login page
    When I login with username "testuser" and password "testpassword"
    Then positive amounts should be displayed in green

  Scenario: Validate negative amounts color
    Given I am on the login page
    When I login with username "testuser" and password "testpassword"
    Then negative amounts should be displayed in red

 Scenario: Compare Expenses
    Given I am on the login page
    When I login with username "testuser" and password "testpassword"
    Then the Compare Expenses