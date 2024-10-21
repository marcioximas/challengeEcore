from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.invoice_details_page import InvoiceDetailsPage
from pages.home_page import HomePage

@when('I should be redirected to the dashboard')
@then('I should be redirected to the dashboard')
def step_verify_dashboard(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.current_url == "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/account"
    assert context.home_page.is_logout_button_displayed()
    assert context.home_page.get_header == "Invoice List"
    #context.driver.quit()

@when(u'I click on the invoice link on the Hotel name "Rendezvous Hotel"')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_invoice_details()


@then(u'I should be able to see the invoice details')
def step_impl(context):
    context.invoice_details_page = InvoiceDetailsPage(context.driver)
   # context.invoice_details_page.is_hotel_name_displayed()
    context.incvoice_details_page.get_invoice_details()