from behave import given, when, then


@when('Click on "Edit profile" option')
def click_edit_profile(context):
    context.app.profile_page.btn_edit_profile()


@when('Click on "Menu"')
def click_menu(context):
    context.app.main_page.mob_top_menu()


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


@then('Verify the right User name')
def verify_user_name(context):
    context.app.profile_page.verify_user_presence(context.name)


@then('Verify the right Phone number')
def verify_user_phone(context):
    context.app.profile_page.verify_user_phone(context.phone)
