from selenium.webdriver.common.by import By
from behave import given, when, then


GRID = (By.XPATH, '//a[wized="cardOfProperty"]')


@then ('Verify that all projects are shown')
def verify_all_projects(context):
    context.app.off_plan_page.wait_until_visible(GRID)
