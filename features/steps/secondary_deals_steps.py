from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


GRID = (By.XPATH, '//div[@wized="listingCardMLS"]')


@when('Filter the products by {filter_sell_buy}')
def filter_want_sell_buy(context, filter_sell_buy):
    context.app.secondary_page.wait_until_visible(GRID)

    context.app.secondary_page.btn_filter()
    context.app.secondary_page.filter_want_to_sell_buy(filter_sell_buy)
    context.app.secondary_page.btn_apply_filter()


@then('Verify that all cards have {expected_filter} tag')
def verify_tag_for_buy(context, expected_filter):
    context.app.secondary_page.wait_until_visible(GRID)
    context.app.secondary_page.verify_text_for_secondary_filter(expected_filter)


@then('Verify the right page opens')
def verify_right_page(context):
    context.app.secondary_page.verify_right_page()