from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage

class HomePage(BasePage):
    _url = 'https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/account'
    __title_locator = (By.TAG_NAME, "h2")
    __logOut_button_locator = (By.LINK_TEXT, "Logout")
    __rows_locator = (By.XPATH, "//div[@class='row']")
    __first_invoice_details_link = (By.XPATH, "//a[contains(text(), 'Invoice Details')][1]")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def get_header(self) -> str:
        return super()._get_text(self.__title_locator)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__logOut_button_locator)

    def click_invoice_details(self):
        self._click(self.__first_invoice_details_link)