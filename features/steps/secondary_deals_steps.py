from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


GRID = (By.XPATH, '//div[@wized="listingCardMLS"]')


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open()


@when('Click on the "Open in browser"')
def open_in_browser(context):
    context.app.main_page.open_in_browser()


@when('Log in to the page {lgn}, {psw}')
def login_to(context, lgn, psw):
    context.app.login_page.login_to(lgn, psw)


@when('Click on "Secondary" option at the left side menu')
def secondary_side_menu(context):
    context.app.main_page.menu_secondary()


@then('Verify the right page opens')
def verify_right_page(context):
    context.app.secondary_page.verify_right_page()


@when('Filter the products by "want to sell"')
def filter_want_sell(context):
    context.app.secondary_page.wait_until_visible(GRID)

    context.app.secondary_page.btn_filter()
    context.app.secondary_page.btn_filter_want_to_sell()
    context.app.secondary_page.btn_apply_filter()


@then('Verify that all cards have "for sale" tag')
def verify_tag_for_sale(context):
    context.app.secondary_page.wait_until_visible(GRID)
    context.app.secondary_page.verify_tag_for_sale()
