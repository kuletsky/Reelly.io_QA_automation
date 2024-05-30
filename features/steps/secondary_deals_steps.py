from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


GRID = (By.XPATH, '//div[@wized="listingCardMLS"]')
ALL_LIST_FOR_SALE = (By.CSS_SELECTOR, 'div[wized="saleTagMLS"]')


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
    context.driver.wait.until(EC.visibility_of_all_elements_located(GRID))

    context.app.secondary_page.btn_filter()
    context.app.secondary_page.btn_filter_want_to_sell()
    context.app.secondary_page.btn_apply_filter()


@then('Verify that all cards have "for sale" tag')
def verify_tag_for_sale(context):
    context.driver.wait.until(EC.visibility_of_all_elements_located(GRID))
    all_property = context.driver.find_elements(*ALL_LIST_FOR_SALE)
    expected_result = 'For sale'
    # print(len(all_property))
    for property in all_property:
        # print(property.text)
        assert property.text == expected_result, f'Error! {property.text} IS NOT "For sale" '
