from behave import given, when, then


@then('Verify title “{title}” is visible')
def verify_title(context, title):
    context.app.subscription_page.verify_title(title)


@then('Verify “back” and “upgrade plan” buttons are available')
def verify_back_upgrade_plan_buttons(context):
    context.app.subscription_page.verify_back_upgrade_plan_buttons()
