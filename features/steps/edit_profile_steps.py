from behave import given, when, then


@when('Click on "Edit profile" option')
def click_edit_profile(context):
    context.app.profile_page.btn_edit_profile()


# @when('Select Broker role')
# def select_broker_role(context):
#     context.app.profile_page.select_broker_role()


@then('Verify that Profile page opened')
def verify_profile_opened(context):
    context.app.profile_page.verify_profile_opened()


# @then('Verify that {role} role selected')
# def verify_broker_selected(context, role):
#     context.app.profile_page.verify_role(role)
