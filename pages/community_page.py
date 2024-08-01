from selenium.webdriver.common.by import By

from pages.base_page import Page


class CommunityPage(Page):
    BTN_CONTACT_SUPPORT = (By.XPATH, '//a[text()="Contact support"]')

    def verify_contact_support_button(self):
        BTN_SUPPORT = self.find_elements(By.XPATH, self.BTN_CONTACT_SUPPORT)
        # BTN_SUPPORT[1].click()
        self.click(*BTN_SUPPORT[1])
