from selenium.webdriver.common.by import By
from behave import given, when, then


@then ('Verify that all projects are shown')
def verify_all_projects(context):
    context.app.off_plan_page.verify_all_projects()
