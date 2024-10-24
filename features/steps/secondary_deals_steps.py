from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.devtools.v85.debugger import pause


@when('Filter the products by {filter_sell_buy}')
def filter_want_sell_buy(context, filter_sell_buy):
    context.app.secondary_page.btn_filter()
    context.app.secondary_page.filter_want_to_sell_buy(filter_sell_buy)
    context.app.secondary_page.btn_apply_filter()


@then('Verify that all cards have {expected_filter} tag')
def verify_tag_for_buy(context, expected_filter):
    context.app.secondary_page.verify_text_for_secondary_filter(expected_filter)


@when('Click on Filters')
def click_on_filters(context):
    context.app.secondary_page.btn_filter()


@when('Filter the price of products range from {min_price} to {max_price} AED')
def filter_range_of_price(context, min_price, max_price):
    context.app.secondary_page.set_filter_range(min_price, max_price)
    context.app.secondary_page.btn_apply_filter()
    context.min_price = min_price
    context.max_price = max_price

@then('Verify the price in all cards is inside the range')
def verify_range_of_price(context):
    context.app.secondary_page.verify_range_of_price(context.min_price, context.max_price)


@then('Verify the right page opens')
def verify_right_page(context):
    context.app.secondary_page.verify_right_page()


@when('Go to the final page using the pegination button and back')
def go_to_final_page(context):
    context.app.secondary_page.go_to_final_page()
