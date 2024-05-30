from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    BTN_OPEN_IN_BROWSER = (By.XPATH, '//div[text()="Open in browser"]')
    MENU_SECONDARY = (By.XPATH, '//div[@class="menu-button-text" and text()="Secondary"]')

    def open(self):
        self.driver.get('https://reelly.io/')

    def open_in_browser(self):
        self.click(*self.BTN_OPEN_IN_BROWSER)

    def menu_secondary(self):
        self.click(*self.MENU_SECONDARY)