from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProfilePage(Page):
    BTN_EDIT_PROFILE = (By.XPATH, '//div[text()="Edit profile"]')
    TXT_PROFILE = (By.XPATH, '//div[text()="Profile"]')

    def btn_edit_profile(self):
        self.click(*self.BTN_EDIT_PROFILE)

    def verify_profile_opened(self):
        self.verify_text('Profile', *self.TXT_PROFILE)

    # def verify_role(self):
    #     actual_role =
