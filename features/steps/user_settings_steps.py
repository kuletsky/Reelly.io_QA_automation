from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.settings_page.get_current_window()


@when('Click on "Support" option')
def click_on_support(context):
    context.app.settings_page.btn_support()


@when('Switch to the new window')
def switch_window(context):
    context.app.settings_page.switch_to_new_window()


@then('Verify that URL of window contains {partial_url}')
def verify_whatsapp_url(context, partial_url):
    context.app.settings_page.verify_partial_url(partial_url)


@when('Close current page')
def close(context):
    context.app.settings_page.close()


@when('Go back to original window')
def go_back_to_original_window(context):
    context.app.settings_page.switch_window_by_id(context.original_window)


@when('Click on "News" option')
def click_on_news(context):
    context.app.settings_page.btn_news()