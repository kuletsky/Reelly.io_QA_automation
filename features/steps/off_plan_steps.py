from selenium.webdriver.common.by import By
from behave import given, when, then


@when ('Click on top Menu {link_text}')
def click_on_top_menu(context, link_text):
    context.app.off_plan_page.click_link_on_off(link_text)


@then ('Verify that all projects are shown')
def verify_all_projects(context):
    context.app.off_plan_page.verify_all_projects()
