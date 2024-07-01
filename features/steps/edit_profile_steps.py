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


@then('Verify the right information is present into the input fields on the registration page')
def verify_new_user(context):
    context.app.profile_page.verify_new_user(context.name, context.phone, context.email, context.website)
    # context.app.profile_page.verify_user_presence(context.name)
    # context.app.profile_page.verify_user_phone(context.phone)
    # context.app.profile_page.verify_company_website(context.website)
    # context.app.profile_page.verify_email(context.email)


# @then('Verify the right User name')
# def verify_user_name(context):
#     context.app.profile_page.verify_user_presence(context.name)
#
#
# @then('Verify the right Phone number')
# def verify_user_phone(context):
#     context.app.profile_page.verify_user_phone(context.phone)
#
#
# @then('Verify the right Company website')
# def verify_company_website(context):
#     context.app.profile_page.verify_company_website(context.website)
#
#
# @then('Verify the Email')
# def verify_email(context):
#     context.app.profile_page.verify_email(context.email)
