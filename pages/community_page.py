from selenium.webdriver.common.by import By

from pages.base_page import Page


class CommunityPage(Page):
    BTN_CONTACT_SUPPORT = (By.XPATH, By.XPATH, '//div[@class="community-blog"]//div[@class="left-block"]//div[contains(@class, "chat-button") and contains(@class, "w-button")]')

    def verify_contact_support_button(self):
        self.click(*self.BTN_CONTACT_SUPPORT)
