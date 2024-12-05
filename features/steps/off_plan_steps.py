from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on top Menu {link_text}')
def click_on_top_menu(context, link_text):
    context.app.off_plan_page.click_link_on_off(link_text)


@when('Change Location {filter_location}')
def change_location(context, filter_location):
    # print(filter_location)
    context.app.off_plan_page.change_location(filter_location)


@then('Verify that all projects on Off-plan are shown')
def verify_all_projects(context):
    context.app.off_plan_page.verify_all_projects_on_off_plan()


@then('Verify that all projects on Secondary are shown')
def verify_all_projects(context):
    context.app.secondary_page.verify_all_projects_on_secondary()


@then('Verify "Total Projects" displays accurate project count')
def verify_total_projects(context):
    context.app.off_plan_page.verify_total_projects_on_off_plan()


@then('Verify "Total Projects" Count Updates with Location Filter Change')
def verify_total_projects(context):
    context.app.off_plan_page.verify_total_projects_count_updates()

@then('Verify the right page opens Off-plan')
def verify_right_page_off_plan(context):
    context.app.off_plan_page.verify_right_page()

@when('Go to the final page using the pegination button and back on Off-plan')
def go_to_final_page(context):
    context.app.off_plan_page.go_to_final_page_offplan()

@when('Click on Filters on Off-plan')
def click_on_filters(context):
    context.app.off_plan_page.btn_filter()

@then('Verify the price in all cards is inside the range off-plan')
def verify_range_of_price(context):
    context.app.off_plan_page.verify_range_of_price(context.min_price, context.max_price)
