from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InvoiceDetailsPage(BasePage):
    # Invoice Details
    __invoice_details = (By.XPATH, "//h2[text()='Invoice Details']")
    __hotel_name = (By.XPATH, "//h4[@class='mt-5']")
    _invoice_date = (By.XPATH, "//span[text()='Invoice Date:']/parent::li")
    _due_date = (By.XPATH, "//section[@class='content']//ul/li[2]")
    _invoice_number = (By.XPATH, "//h6[@class='mt-2']")

    # Booking/Stay Details
    _booking_code = (By.XPATH, "//td[text()='Booking Code']/following-sibling::td")
    _room = (By.XPATH, "//td[text()='Room']/following-sibling::td")
    _total_stay_count = (By.XPATH, "//td[text()='Total Stay Count']/following-sibling::td")
    _total_stay_amount = (By.XPATH, "//td[text()='Total Stay Amount']/following-sibling::td")
    _check_in = (By.XPATH, "//td[text()='Check-In']/following-sibling::td")
    _check_out = (By.XPATH, "//td[text()='Check-Out']/following-sibling::td")

    # Customer Details
    _customer_details = (By.XPATH, "//h5[text()='Customer Details']/following-sibling::div[1]")

    # Billing Details
    _deposit_now = (By.CSS_SELECTOR, "table:nth-of-type(2) > tbody > tr > td:nth-of-type(1)")
    _tax_vat = (By.CSS_SELECTOR, "table:nth-of-type(2) > tbody > tr > td:nth-of-type(2)")
    _total_amount = (By.CSS_SELECTOR, "tbody > tr > td:nth-of-type(3)")

    def is_invoice_details_displayed(self) -> bool:
        return super()._is_displayed(self.__invoice_details)

    def get_invoice_details(self):
        """Retrieve all invoice details as a dictionary."""
        return {
            "Hotel Name": self._get_text(self.__hotel_name),
            "Invoice Date": self._get_text(self._invoice_date),
            "Due Date": self._get_text(self._due_date),
            "Invoice Number": self._get_text(self._invoice_number),
            "Booking Code": self._get_text(self._booking_code),
            "Customer Details": self._get_text(self._customer_details),
            "Room": self._get_text(self._room),
            "Check In": self._get_text(self._check_in),
            "Check Out": self._get_text(self._check_out),
            "Total Stay Count": self._get_text(self._total_stay_count),
            "Total Stay Amount": self._get_text(self._total_stay_amount),
            "Deposit Now": self._get_text(self._deposit_now),
            "Tax & VAT": self._get_text(self._tax_vat),
            "Total Amount": self._get_text(self._total_amount),
        }