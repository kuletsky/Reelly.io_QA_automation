from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class ProfilePage(Page):
    BTN_EDIT_PROFILE = (By.XPATH, '//div[text()="Edit profile"]')
    TXT_PROFILE = (By.XPATH, '//div[text()="Profile"]')
    TOPIC_SELECTION = (By.ID, 'field')
    TOPIC_DEVELOPER = (By.CSS_SELECTOR, '[value="Developer"]')

    def btn_edit_profile(self):
        self.click(*self.BTN_EDIT_PROFILE)

    def verify_profile_opened(self):
        self.verify_text('Profile', *self.TXT_PROFILE)

    def select_topic(self, topic):
        topic_dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_dd)
        select.select_by_value(topic)

    def verify_topic(self, topic):
        self.verify_text(topic, *self.TOPIC_DEVELOPER)
