from behave import then

from pages.invoice_details_page import InvoiceDetailsPage
from behave import then

from pages.invoice_details_page import InvoiceDetailsPage


@then('the application should open the Invoice Details screen')
def step_verify_invoice_details_screen(context):
    context.invoice_details_page = InvoiceDetailsPage(context.driver)
    window_handles = context.driver.window_handles
    context.driver.switch_to.window(window_handles[1])
    assert context.invoice_details_page.is_invoice_details_displayed()
@then('I validate the information presented')
def step_validate_invoice_details(context):
    # Create an instance of the InvoiceDetailsPage to access its methods
    invoice_details_page = InvoiceDetailsPage(context.driver)

    # Retrieve actual invoice details from the page
    actual_invoice_details = invoice_details_page.get_invoice_details()

    # Loop through each row in the data table and check if expected value is present in the actual value
    for row in context.table:
        expected_label = row['Key']
        expected_value = row['Value']

        # Find the corresponding value in the actual data
        actual_value = actual_invoice_details.get(expected_label)

        normalized_expected_value = " ".join(expected_value.split())
        normalized_actual_value = " ".join(actual_value.split())

        # Assert that the expected value is present in the actual value (instead of exact match)
        assert normalized_expected_value in normalized_actual_value, f"Validation failed for {expected_label}: expected '{normalized_expected_value}' to be part of '{normalized_actual_value}'"

    # Quit the driver (optional if this step is meant to finish the test)
    context.driver.quit()