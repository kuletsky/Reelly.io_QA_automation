from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class ProfilePage(Page):
    BTN_EDIT_PROFILE = (By.XPATH, '//div[text()="Edit profile"]')
    TXT_PROFILE = (By.XPATH, '//div[text()="Profile"]')
    TOPIC_ROLE = (By.ID, 'field')
    TOPIC_DEVELOPER = (By.CSS_SELECTOR, '[value="Developer"]')
    TOPIC_POSITION = (By.ID, 'Position')
    TOPIC_CEO = (By.CSS_SELECTOR, '[value="Manager / Director"]')

    def btn_edit_profile(self):
        self.click(*self.BTN_EDIT_PROFILE)

    def verify_profile_opened(self):
        self.verify_text('Profile', *self.TXT_PROFILE)

    def select_role(self, topic):
        topic_dd = self.find_element(*self.TOPIC_ROLE)
        select = Select(topic_dd)
        select.select_by_value(topic)

    def select_position(self, topic):
        topic_dd = self.find_element(*self.TOPIC_POSITION)
        select = Select(topic_dd)
        select.select_by_visible_text(topic)

    def verify_role(self, topic):
        self.verify_text(topic, *self.TOPIC_DEVELOPER)

    def verify_position(self, topic):
        self.verify_text(topic, *self.TOPIC_CEO)
