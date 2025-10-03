from behave import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage



@given('I am on the login page')
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)
    context.dashboard_page = DashboardPage(context.driver)

@then('I should be redirected to the dashboard table page')
def assert_dashboard(context):
    assert context.dashboard_page.is_dashboard_page()
    assert context.dashboard_page.is_correct_url()

@then("I should see exactly 6 transactions")
def step_validate_transactions(context):
    assert context.dashboard_page.transactions_count() == 6

@then('the total balance should be "{expected_balance}"')
def step_validate_balance(context, expected_balance):
    print('actual balance', context.dashboard_page.total_balance())
    assert context.dashboard_page.total_balance() == expected_balance