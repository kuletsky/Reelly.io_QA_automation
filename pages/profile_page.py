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
    VERIFY_NAME = (By.CSS_SELECTOR, '[id="Fullname"]')
    VERIFY_PHONE = (By.CSS_SELECTOR, '[data-name="number"]')

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

    def verify_option(self, topic):
        locator = self._get_locator(topic)
        self.verify_text(topic, *locator)

    def verify_profile_opened(self):
        self.verify_text('Profile', *self.TXT_PROFILE)

    def verify_user_presence(self, name):
        self.verify_input(name, *self.VERIFY_NAME)

    def verify_user_phone(self, phone):
        self.verify_input(phone, *self.VERIFY_PHONE)