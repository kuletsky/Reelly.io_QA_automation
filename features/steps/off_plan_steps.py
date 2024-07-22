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