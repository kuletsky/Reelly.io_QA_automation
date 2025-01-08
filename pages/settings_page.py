from selenium.webdriver.common.by import By
import random
import string
from pages.base_page import Page


class SettingsPage(Page):
    BTN_CONTUCT_US = (By.XPATH, '//div[@class="setting-text" and text()="Contact us"]')
    BTN_SUPPORT = (By.XPATH, '//div[@class="setting-text" and text()="Support"]')
    BTN_COMMUNITY = (By.XPATH, '//div[@class="setting-text" and text()="Community"]')
    BTN_NEWS = (By.XPATH, '//div[@class="setting-text" and text()="News"]')
    BTN_ADD_PROJECT = (By.XPATH, '//div[@class="setting-text" and text()="Add a project"]')
    BTN_USER_GUIDE = (By.XPATH, '//div[@class="setting-text" and text()="User guide"]')
    BTN_CHANGE_PSW = (By.XPATH, '//div[@class="setting-text" and text()="Change password"]')
    BTN_SUBSCRIPTION = (By.XPATH, '//div[@class="setting-text" and text()="Subscription & payments"]')
    BTN_VERIFICATION = (By.XPATH, '//div[@class="setting-text" and text()="Verification"]')
    BTN_CONNECT = (By.CSS_SELECTOR, '.settings-block-menu .get-free-period.menu')
    INPUT_NAME = (By.CSS_SELECTOR, '[id="Your-name"]')
    INPUT_WEBSITE = (By.CSS_SELECTOR, '[id="Your-company-name"]')
    INPUT_ROLE = (By.CSS_SELECTOR, '[id="Role"]')
    INPUT_AGE = (By.CSS_SELECTOR, '[id="Age-of-the-company"]')
    INPUT_COUNTRY = (By.CSS_SELECTOR, '[id="Country"]')
    INPUT_PROJECT = (By.CSS_SELECTOR, '[id="Name-project"]')
    INPUT_PHONE = (By.CSS_SELECTOR, '[id="Phone"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, '[id="Email-add-project"]')
    SUBMIT = (By.CSS_SELECTOR, '[type = "submit"]')
    MSG = (By.XPATH, '//div[text()="Thank you! Your submission has been received!"]')
    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, '.text-social')
    OPTIONS_NUMBER = (By.CSS_SELECTOR, '.page-setting-block')


    def generate_random_email(self, prefix="testuser", domain="test.com"):
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{prefix}_{suffix}@{domain}"

    def generate_random_phone_number(self):
        country_code = "+1"
        area_code = ''.join(random.choices("0123456789", k=3))
        first_part = ''.join(random.choices("0123456789", k=3))
        second_part = ''.join(random.choices("0123456789", k=4))
        return f"{country_code} {area_code} {first_part} {second_part}"

    def generate_random_password(self, length=9):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        return password

    def generate_random_website(self, prefix="test", domain="com"):
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        return f"{prefix}{suffix}.{domain}"

    def btn_support(self):
        self.click(*self.BTN_SUPPORT)

    def btn_news(self):
        self.click(*self.BTN_NEWS)

    def btn_add_project(self):
        self.click(*self.BTN_ADD_PROJECT)

    def btn_community(self):
        self.click(*self.BTN_COMMUNITY)

    def btn_contact_us(self):
        self.click(*self.BTN_CONTUCT_US)

    def btn_user_guide(self):
        self.click(*self.BTN_USER_GUIDE)

    def btn_change_password(self):
        self.click(*self.BTN_CHANGE_PSW)

    def btn_subscription(self):
        self.click(*self.BTN_SUBSCRIPTION)

    def btn_verification(self):
        self.click(*self.BTN_VERIFICATION)

    def add_test_information(self):
        self.input_text('Tester', *self.INPUT_NAME)
        self.website = self.generate_random_website()
        self.input_text(self.website, *self.INPUT_WEBSITE)
        self.input_text('Manager', *self.INPUT_ROLE)
        self.input_text('11', *self.INPUT_AGE)
        self.input_text('Test', *self.INPUT_COUNTRY)
        self.input_text('Test Project', *self.INPUT_PROJECT)
        self.phone_number = self.generate_random_phone_number()
        self.input_text(self.phone_number, *self.INPUT_PHONE)
        self.email = self.generate_random_email()
        self.input_text(self.email, *self.INPUT_EMAIL)

    def verify_test_information(self):
        # self.wait_until_any_text_appears(*self.INPUT_EMAIL)
        self.verify_input('Tester', *self.INPUT_NAME)
        self.verify_input(self.website, *self.INPUT_WEBSITE)
        self.verify_input('Manager', *self.INPUT_ROLE)
        self.verify_input('11', *self.INPUT_AGE)
        self.verify_input('Test', *self.INPUT_COUNTRY)
        self.verify_input('Test Project', *self.INPUT_PROJECT)
        self.verify_input(self.phone_number, *self.INPUT_PHONE)
        self.verify_input(self.email, *self.INPUT_EMAIL)

    def send_application_button(self):
        self.click(*self.SUBMIT)
        self.wait_until_any_text_appears(*self.MSG)
        self.verify_text('Thank you! Your submission has been received!', *self.MSG)

    def connect_button(self):
        self.find_element(*self.BTN_CONNECT)

    def verify_number_of_social_media_icons(self, number):
        all_social = self.find_elements(*self.SOCIAL_MEDIA_ICONS)
        print(f'How many SOCIAL on the page?: {len(all_social)}')
        # all_elements = self.find_elements(*locator)
        # print(f'How many elements on the page?: {len(all_elements)}')

        assert len(all_social) >= int(number), f'Error! Expected {number}, but got {len(all_social)}'
        # for element in all_elements:
            # print(element.text)
            # assert element.text == expected_text, f'Error! Expected {expected_text}, but got {element.text}'

    def verify_number_of_settings(self, number):
        all_options = self.find_elements(*self.OPTIONS_NUMBER)
        print(f'How many options on the page?: {len(all_options)}')
        assert len(all_options) >= int(number), f'Error! Expected {number}, but got {len(all_options)}'

    def verify_verification_page():

