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


@when('Click on Agencies at the top of the page')
def click_agencies(context):
    context.app.market_page.click_agen()


@when('Click on "Add company" button')
def click_add_company(context):
    context.app.market_page.click_add_company()


@then('Verify all cards has the {option} tag')
def verify_tags(context, option):
    context.app.market_page.verify_tag(option)


@then('Verify the right page opened')
def verify_right_page(context):
    context.app.market_page.verify_page()


@then('Verify the button “Publish my company” is available.')
def verify_btn(context):
    context.app.market_page.verify_btn()
