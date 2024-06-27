from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class SignUpPage(Page):
    BTN_CREATE_ACCOUNT = (By.XPATH, '//div[text()="Create account"]')
    FULL_NAME = (By.CSS_SELECTOR, '[data-name="Full Name"]')
    PHONE_NUMBER = (By.CSS_SELECTOR, '[data-name="Phone"]')
    EMAIL = (By.CSS_SELECTOR, '[data-name="Email"]')
    PSW = (By.CSS_SELECTOR, '[data-name="Password"]')
    TOPIC_ROLES = (By.ID, 'Role')
    POSITION = (By.ID, 'Position')

    def btn_create_account(self):
        self.click(*self.BTN_CREATE_ACCOUNT)

    def fill_in_full_name(self, name):
        self.input_text(name, *self.FULL_NAME)

    def fill_in_phone(self, phone):
        self.input_text(phone, *self.PHONE_NUMBER)

    def fill_in_email(self, email):
        self.input_text(email, *self.EMAIL)

    def fill_in_psw(self, password):
        self.input_text(password, *self.PSW)

    def select_role_sign(self, topic):
        topic_dd = self.find_element(*self.TOPIC_ROLES)
        select = Select(topic_dd)
        select.select_by_value(topic)

    # def select_position_sign(self, position):
    #     position_dd = self.find_element(*self.POSITION)
    #     select = Select(position_dd)
    #     select.select_by_value(position)