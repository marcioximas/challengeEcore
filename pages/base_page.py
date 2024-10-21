from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver


    #* to separate the tuple
    def _find(self, locator: tuple) -> WebElement:
         return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 15):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple, time: int =10) -> bool:
        self._wait_until_element_is_visible(locator, time)
        try:
           return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def open_url(self,url:str):
        self._driver.get(url)


    def _get_text(self, locator: tuple, time: int =10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _is_text_present_in_element(self, locator: tuple, expected_text: str, time: int = 10) -> bool:
        self._wait_until_element_is_visible(locator, time)
        element_text = self._find(locator).text.strip()
        return expected_text in element_text
