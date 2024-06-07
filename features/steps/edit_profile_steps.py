from behave import given, when, then


@when('Click on "Edit profile" option')
def click_edit_profile(context):
    context.app.profile_page.btn_edit_profile()


@when('Select {topic} option')
def select_topic(context, topic):
    context.app.profile_page.select_option(topic)


@when('Select {topic} role')
def select_topic_role(context, topic):
    context.app.profile_page.select_role(topic)


@when('Select {topic} position')
def select_topic_position(context, topic):
    context.app.profile_page.select_position(topic)


@then('Verify that Profile page opened')
def verify_profile_opened(context):
    context.app.profile_page.verify_profile_opened()


@then('Verify that {topic} option selected')
def verify_role(context, topic):
    context.app.profile_page.verify_option(topic)
