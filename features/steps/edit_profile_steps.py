from behave import given, when, then
import random
import string
from features.environment import write_config, read_config


def generate_random_phone_number():
    country_code = "+1"
    area_code = ''.join(random.choices("0123456789", k=3))
    first_part = ''.join(random.choices("0123456789", k=3))
    second_part = ''.join(random.choices("0123456789", k=4))
    # phone_number = f"{country_code}{area_code}{first_part}{second_part}"
    # return phone_number
    return f"{country_code} {area_code} {first_part} {second_part}"


def generate_random_email(prefix="testuser", domain="test.com"):
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{prefix}_{suffix}@{domain}"


def generate_random_website(prefix="test", domain="com"):
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"{prefix}{suffix}.{domain}"


@when('Click on "Edit profile" option')
def click_edit_profile(context):
    context.app.profile_page.btn_edit_profile()


@when('Click on "Menu"')
def click_menu(context):
    context.app.main_page.mob_top_menu()


@when('Edit the Full name {name}')
def fill_in_full_name(context, name):
    context.name = name
    context.app.profile_page.edit_full_name(name)


@when('Edit random Phone')
def fill_in_phone(context):
    context.phone = generate_random_phone_number()
    context.app.profile_page.edit_phone(context.phone)


@when('Edit random Email')
def fill_in_email(context):
    context.email = generate_random_email()
    context.app.profile_page.edit_email(context.email)

    config = read_config()
    config['login'] = context.email
    write_config(config)


@when('Edit random Company website')
def fill_in_website(context):
    context.website = generate_random_website()
    context.app.profile_page.edit_website(context.website)


@when('Select {topic} role')
def select_topic_role(context, topic):
    context.app.profile_page.select_role(topic)


@when('Select {topic} position')
def select_topic_position(context, topic):
    context.app.profile_page.select_position(topic)


@when('Select language {language}')
def select_country(context, language):
    context.app.profile_page.select_language(language)


@when('Click on "Save changes"')
def save_changes(context):
    context.app.profile_page.save_changes()


@when('Click on "Close"')
def close_profile(context):
    context.app.profile_page.close_profile()


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
