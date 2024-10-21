from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage

class LoginPage(BasePage):
    __url = "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/"
    __username_locator = (By.NAME, "username")
    __password_locator = (By.NAME, "password")
    __submit_locator = (By.ID, "btnLogin")
    __error_message_locator = (By.XPATH, "//div[@role='alert']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def field_login(self, username: str, password: str):
        super()._type(self.__username_locator, username)
        super()._type(self.__password_locator, password)
        super()._click(self.__submit_locator)

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message_locator, time=5)