from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify the one of the three options of visualization are {option_1}, {option_2}, {option_3}')
def verify_one_option(context, option_1, option_2, option_3):
    context.app.product_details_page.verify_option(option_1, option_2, option_3)


@then('Verify the visualizatoin option are clickable')
def verify_clickable(context):
    context.app.product_details_page.verify_clickable()
