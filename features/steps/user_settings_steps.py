from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on "Support" option')
def click_on_support(context):
    context.app.settings_page.btn_support()
