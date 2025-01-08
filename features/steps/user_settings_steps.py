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


@when('Close current page')
def close(context):
    context.app.settings_page.close()


@when('Go back to original window')
def go_back_to_original_window(context):
    context.app.settings_page.switch_window_by_id(context.original_window)


@when('Click on "News" option')
def click_on_news(context):
    context.app.settings_page.btn_news()


@when('Click on "Add a project"')
def click_on_add_project(context):
    context.app.settings_page.btn_add_project()


@when('Add some test information to the input fields')
def add_test_information(context):
    context.app.settings_page.add_test_information()


@when('Click on "Community" option')
def click_on_community(context):
    context.app.settings_page.btn_community()


@when('Click on "Contact us" option')
def click_on_contact_us(context):
    context.app.settings_page.btn_contact_us()


@when('Click on "User Guide" option')
def click_on_user_guide(context):
    context.app.settings_page.btn_user_guide()


@when('Click on "Change password" option')
def click_on_change_password(context):
    context.app.settings_page.btn_change_password()


@when('Click on "Subscription & payments" option')
def click_on_subscription(context):
    context.app.settings_page.btn_subscription()


@when('Click on the verification option')
def click_verification_option(context):
    context.app.settings_page.btn_verification()


@then('Verify the right information is present in the input fields')
def verify_test_information(context):
    context.app.settings_page.verify_test_information()


@then('Verify “Send an application” button is available and clickable')
def verify_send_application_button(context):
    context.app.settings_page.send_application_button()


@then('Verify "connect the company" button is available')
def verify_connect_button(context):
    context.app.settings_page.connect_button()


@then('Verify the right page Verification opens')
def verify_verification(context):
    context.app.settings_page.verify_verification_page()


@then('Verify that URL of window contains {partial_url}')
def verify_whatsapp_url(context, partial_url):
    context.app.settings_page.verify_partial_url(partial_url)


@then('Verify there are at least {number} social media icons')
def verify_number_of_social_media_icons(context, number):
    context.app.settings_page.verify_number_of_social_media_icons(number)


@then('Verify “Contact support” button is available and clickable')
def verify_contact_support_button(context):
    context.app.community_page.verify_contact_support_button()


@then('Verify “Connect the company” button is available and clickable')
def verify_connect_button(context):
    context.app.contact_us_page.verify_connect_button()


@then('Verify there are {number} options for settings')
def verify_number_of_settings(context, number):
    context.app.settings_page.verify_number_of_settings(number)
