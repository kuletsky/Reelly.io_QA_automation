from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class ProfilePage(Page):
    BTN_EDIT_PROFILE = (By.XPATH, '//div[text()="Edit profile"]')
    TXT_PROFILE = (By.XPATH, '//div[text()="Profile"]')
    TOPIC_ROLE = (By.ID, 'field')
    TOPIC_POSITION = (By.ID, 'Position')
    TOPIC_OPTION = (By.XPATH, '//option[text()="{TOPIC_OPTION}"]')
    FULL_NAME_PROFILE = (By.CSS_SELECTOR, '[data-name="Fullname"]')
    NUMBER = (By.CSS_SELECTOR, '[data-name="number"]')
    EMAIL = (By.CSS_SELECTOR, '[data-name="Email 2"]')
    COMP_WEBSITE = (By.CSS_SELECTOR, '[data-name="Company name"]')
    LANGUAGE = (By.CSS_SELECTOR, '[data-name="Languages"]')
    BTN_SAVE_CHANGES = (By.XPATH, '//div[text()="Save changes"]')
    BTN_CLOSE = (By.XPATH, '//a[text()="Close"]')

    VERIFY_NAME = (By.CSS_SELECTOR, '[id="Fullname"]')
    VERIFY_PHONE = (By.CSS_SELECTOR, '[data-name="number"]')
    VERIFY_WEBSITE = (By.CSS_SELECTOR, '[data-name="Company name"]')
    VERIFY_EMAIL = (By.CSS_SELECTOR, '[data-name="Email 2"]')

    def _get_locator(self, text):
        return [self.TOPIC_OPTION[0], self.TOPIC_OPTION[1].replace('{TOPIC_OPTION}', text)]

    def btn_edit_profile(self):
        self.click(*self.BTN_EDIT_PROFILE)
        sleep(4)

    def select_role(self, topic):
        topic_dd = self.find_element(*self.TOPIC_ROLE)
        select = Select(topic_dd)
        select.select_by_value(topic)

    def select_position(self, topic):
        topic_dd = self.find_element(*self.TOPIC_POSITION)
        select = Select(topic_dd)
        select.select_by_visible_text(topic)

    def edit_full_name(self, name):
        self.input_text(name, *self.FULL_NAME_PROFILE)

    def edit_phone(self, phone):
        self.input_text(phone, *self.NUMBER)

    def edit_email(self, email):
        self.input_text(email, *self.EMAIL)

    def edit_website(self, company):
        self.input_text(company, *self.COMP_WEBSITE)

    def select_language(self, language):
        self.input_text(language, *self.LANGUAGE)

    def save_changes(self):
        self.click(*self.BTN_SAVE_CHANGES)

    def close_profile(self):
        self.click(*self.BTN_CLOSE)

    def verify_option(self, topic):
        locator = self._get_locator(topic)
        self.verify_text(topic, *locator)

    def verify_profile_opened(self):
        self.verify_text('Profile', *self.TXT_PROFILE)

    def verify_new_user(self, name, phone, email, website):
        self.verify_input(name, *self.VERIFY_NAME)
        self.verify_input(phone, *self.VERIFY_PHONE)
        self.verify_input(email, *self.VERIFY_EMAIL)
        self.verify_input(website, *self.VERIFY_WEBSITE)

    # def verify_user_presence(self, name):
    #     self.verify_input(name, *self.VERIFY_NAME)
    #
    # def verify_user_phone(self, phone):
    #     self.verify_input(phone, *self.VERIFY_PHONE)
    #
    # def verify_email(self, email):
    #     self.verify_input(email, *self.VERIFY_EMAIL)
    #
    # def verify_company_website(self, website):
    #     self.verify_input(website, *self.VERIFY_WEBSITE)
