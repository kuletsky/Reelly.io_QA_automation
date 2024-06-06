from behave import given, when, then


@when('Click on "Edit profile" option')
def click_edit_profile(context):
    context.app.profile_page.btn_edit_profile()


@when('Select {topic} role')
def select_broker_role(context, topic):
    context.app.profile_page.select_topic(topic)


@then('Verify that Profile page opened')
def verify_profile_opened(context):
    context.app.profile_page.verify_profile_opened()


@then('Verify that {topic} role selected')
def verify_role(context, topic):
    context.app.profile_page.verify_topic(topic)
