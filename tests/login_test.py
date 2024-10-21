import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Se quiser usar o WebDriver Manager para gerenciar o chromedriver

from pages.home_page import HomePage
from pages.invoice_details_page import InvoiceDetailsPage
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    # Usando o webdriver manager para simplificar o gerenciamento do driver
    service = Service(ChromeDriverManager().install())  # Isso baixa e usa o chromedriver correto
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/")
    login_page.field_login("demouser", "abc123")
    home_page = HomePage(driver)
    home_page.is_logout_button_displayed()
    home_page.click_invoice_details()
    window = driver.window_handles
    driver.switch_to.window(window[1])
    invoice_details_page = InvoiceDetailsPage(driver)
    invoice_details_page.is_invoice_details_displayed()
    invoice_details_page.get_invoice_details()



def test_fail_login(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/")
    login_page.field_login("Demouser", "abc123")
    assert login_page.get_error_message() == "Wrong username or password."
    driver.quit()