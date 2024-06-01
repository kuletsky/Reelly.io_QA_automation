from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    BTN_OPEN_IN_BROWSER = (By.XPATH, '//div[text()="Open in browser"]')
    MENU_SECONDARY = (By.XPATH, '//div[@class="menu-button-text" and text()="Secondary"]')
    MENU_SETTINGS = (By.XPATH, '//div[@class="menu-button-text" and text()="Settings"]')

    def open_main_page(self):
        self.open('https://reelly.io/')

    def open_in_browser(self):
        self.click(*self.BTN_OPEN_IN_BROWSER)

    def menu_secondary(self):
        self.click(*self.MENU_SECONDARY)

    def menu_settings(self):
        self.click(*self.MENU_SETTINGS)