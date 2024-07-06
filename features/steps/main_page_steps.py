from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


GRID = (By.XPATH, '//div[@wized="listingCardMLS"]')


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click on the "Open in browser"')
def open_in_browser(context):
    context.app.main_page.open_in_browser()


@when('Log in to the page {lgn}, {psw}')
def login_to(context, lgn, psw):
    context.app.login_page.login_to(lgn, psw)


@when('Click on "Secondary" option at the left side menu')
def secondary_side_menu(context):
    context.app.main_page.menu_secondary()


@when('Click on "Secondary" MOBILE menu')
def secondary_menu(context):
    context.app.main_page.mob_secondary_menu()


@when('Click on "Settings" option at the left side menu')
def settings_side_menu(context):
    context.app.main_page.menu_settings()


@when('Click on "Connect the company"')
def connect_company(context):
    context.app.main_page.connect_company()


@when('Click on "App Store"')
def app_store(context):
    context.app.main_page.app_store()
