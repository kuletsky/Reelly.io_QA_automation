from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class CommunityPage(Page):
    BTN_CONTACT_SUPPORT = (By.XPATH, '//a[text()="Contact support"]')

    def verify_contact_support_button(self):
        BTN_SUPPORT = self.find_elements(*self.BTN_CONTACT_SUPPORT)
        element = BTN_SUPPORT[1]
        self.driver.execute_script("arguments[0].click();", element)
