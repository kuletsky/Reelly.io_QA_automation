from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Current window', context.original_window)
    print('ALL windows', context.driver.window_handles)


@when('Click on "Support" option')
def click_on_support(context):
    context.app.settings_page.btn_support()


@then('Verify that URL of tab contains {partial_url}')
def verify_whatsapp_url(context, partial_url):
    # context.driver.wait.until(EC.url_contains(partial_url), message=f'URL does NOT contain {partial_url}')
    # context.app.settings_page.verify_url_of_new_tab(partial_url)
    context.app.settings_page.verify_partial_url(partial_url)
