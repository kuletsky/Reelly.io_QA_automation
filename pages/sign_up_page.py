from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from time import sleep


class SignUpPage(Page):
    BTN_CREATE_ACCOUNT = (By.XPATH, '//div[text()="Create account"]')
    FULL_NAME = (By.CSS_SELECTOR, '[data-name="Full Name"]')
    PHONE_NUMBER = (By.CSS_SELECTOR, '[data-name="Phone"]')
    EMAIL = (By.CSS_SELECTOR, '[data-name="Email"]')
    PSW = (By.CSS_SELECTOR, '[data-name="Password"]')
    WEBSITE = (By.CSS_SELECTOR, '[data-name="Company website"]')
    TOPIC_ROLES = (By.ID, 'Role')
    POSITION = (By.ID, 'Position')
    COUNTRY = (By.ID, 'country-select')
    SIZE = (By.ID, 'Agents-amount-2')
    CREATE_ACCOUNT = (By.XPATH, '//a[text()="Create account"]')

    FULL_NAME_VERIFACATION = (By.CSS_SELECTOR, '[id="Fullname"]')

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

    def fill_in_website(self, website):
        self.input_text(website, *self.WEBSITE)

    def select_role_sign(self, topic):
        topic_dd = self.find_element(*self.TOPIC_ROLES)
        select = Select(topic_dd)
        select.select_by_value(topic)

    def select_country(self, country):
        country_dd = self.find_element(*self.COUNTRY)
        select = Select(country_dd)
        select.select_by_value(country)

    def select_size(self, size):
        size_dd = self.find_element(*self.SIZE)
        select = Select(size_dd)
        select.select_by_value(size)

    def sign_up_page_create_account(self):
        self.click(*self.CREATE_ACCOUNT)

    def verify_user_presence(self, name):
        sleep(4)
        # self.wait_until_visible(*self.FULL_NAME_VERIFACATION)
        print(*self.FULL_NAME_VERIFACATION)
        self.verify_text(name, *self.FULL_NAME_VERIFACATION)



    # def select_position_sign(self, position):
    #     position_dd = self.find_element(*self.POSITION)
    #     select = Select(position_dd)
    #     select.select_by_value(position)
