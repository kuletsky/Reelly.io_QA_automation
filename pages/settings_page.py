from selenium.webdriver.common.by import By

from pages.base_page import Page


class SettingsPage(Page):
    BTN_SUPPORT = (By.XPATH, '//div[@class="setting-text" and text()="Support"]')

    def btn_support(self):
        self.click(*self.BTN_SUPPORT)
