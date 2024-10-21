from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.login_page import LoginPage



@given(u'I am on the login page')
def step_impl(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.login_page = LoginPage(context.driver)
    context.login_page.open_url("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/")

@when('I log in with user "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.field_login(username, password)



@then('I should the error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page = LoginPage(context.driver)
    assert context.login_page.get_error_message() == error_message
    context.driver.quit()
