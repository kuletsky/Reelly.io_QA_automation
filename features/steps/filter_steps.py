from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Filter the price of products range from {min_price} to {max_price} AED')
def filter_range_of_price(context, min_price, max_price):
    context.app.filter_page.set_filter_range(min_price, max_price)
    context.app.filter_page.btn_apply_filter()
    context.min_price = min_price
    context.max_price = max_price
