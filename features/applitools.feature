Feature: Login and Expenses Table Validations
  As a tester
  I want to login and validate the expenses table
  So that each functionality is independently tested

  Scenario: Login redirects to dashboard
    Given I am on the login page
    When I login with username "testuser" and password "testpassword"
    Then I should be redirected to the expenses table page