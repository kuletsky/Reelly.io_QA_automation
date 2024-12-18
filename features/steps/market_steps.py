from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify the right page Market opens')
def market_page_opens(context):
    context.app.market_page.market_opens()


@then('Verify pagination to final page of Market')
def to_final_page(context):
    context.app.market_page.verify_final_pagination()


@then('Verify pagination to first page of Market')
def verify_first_pagination(context):
    context.app.market_page.verify_first_pagination()

@when('Click on Developers at the top of the page')
def click_on_dev(context):
    context.app.market_page.click_dev()

@then('Verify all cards has the license tag {option}')
def verify_tags(context, option):
    context.app.market_page.verify_tag(option)