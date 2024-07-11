from selenium.webdriver.common.by import By
from behave import given, when, then
import random
import string
from time import sleep
from features.environment import write_config, read_config


def generate_random_email(prefix="testuser", domain="test.com"):
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{prefix}_{suffix}@{domain}"


def generate_random_phone_number():
    country_code = "+1"
    area_code = ''.join(random.choices("0123456789", k=3))
    first_part = ''.join(random.choices("0123456789", k=3))
    second_part = ''.join(random.choices("0123456789", k=4))
    return f"{country_code} {area_code} {first_part} {second_part}"


def generate_random_password(length=9):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password


def generate_random_website(prefix="test", domain="com"):
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"{prefix}{suffix}.{domain}"


@when('Click on the "Create account"')
def create_account(context):
    context.app.sign_up_page.btn_create_account()


@when('Fill in the Full name {name}')
def fill_in_full_name(context, name):
    context.name = name
    context.app.sign_up_page.fill_in_full_name(name)


@when('Fill in random Phone')
def fill_in_phone(context):
    context.phone = generate_random_phone_number()
    context.app.sign_up_page.fill_in_phone(context.phone)


@when('Fill in random Email')
def fill_in_email(context):
    context.email = generate_random_email()
    context.app.sign_up_page.fill_in_email(context.email)

    config = read_config()
    config['login'] = context.email
    write_config(config)


@when('Fill in random PSW')
def fill_in_psw(context):
    context.psw = generate_random_password()
    context.app.sign_up_page.fill_in_psw(context.psw)

    config = read_config()
    config['psw'] = context.psw
    write_config(config)


@when('Fill in random Company website')
def fill_in_website(context):
    context.website = generate_random_website()
    context.app.sign_up_page.fill_in_website(context.website)


@when('Select {topic} roles')
def select_role_sign(context, topic):
    context.app.sign_up_page.select_role_sign(topic)


@when('Select country {country}')
def select_country(context, country):
    context.app.sign_up_page.select_country(country)


@when('Select your company size {size}')
def select_size(context, size):
    context.app.sign_up_page.select_size(size)


@when('Click "Create account"')
def click_create_account(context):
    context.app.sign_up_page.sign_up_page_create_account()
