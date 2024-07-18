from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class MainPage(Page):
    BTN_OPEN_IN_BROWSER = (By.XPATH, '//div[text()="Open in browser"]')
    MENU_SECONDARY = (By.XPATH, '//div[@class="menu-button-text" and text()="Secondary"]')
    MENU_SETTINGS = (By.XPATH, '//div[@class="menu-button-text" and text()="Settings"]')
    MOB_TOP_MENU = (By.CSS_SELECTOR, '.mobile-top-menu')
    MOB_MENU_SECONDARY = (By.XPATH, '//div[@class="menu-text" and text()="Secondary"]')
    LANGUAGE = (By.CSS_SELECTOR, '[id="w-dropdown-toggle-0"]')
    TEXT = (By.CSS_SELECTOR, '.h1-menu')
    LINK_TEXT = (By.XPATH, '//div[text()={TEXT}]')

    def _get_locator(self, text):
        return [self.LINK_TEXT[0], self.LINK_TEXT[1].replace('{TEXT}', text)]

    def open_main_page(self):
        self.open('https://reelly.io/')

    def open_in_browser(self):
        self.click(*self.BTN_OPEN_IN_BROWSER)

    def menu_secondary(self):
        self.click(*self.MENU_SECONDARY)

    def mob_secondary_menu(self):
        self.click(*self.MOB_MENU_SECONDARY)

    def menu_settings(self):
        self.click(*self.MENU_SETTINGS)

    def mob_top_menu(self):
        self.click(*self.MOB_TOP_MENU)

    def click_link(self, link_text):
        locator = self._get_locator(link_text)
        self.click(*locator)

    def change_language(self):
        self.wait_until_visible(*self.LANGUAGE)
        ln = self.find_element(*self.LANGUAGE)

        actions = ActionChains(self.driver)
        actions.move_to_element(ln)
        # sleep(10)
        actions.move_by_offset(0, 25)
        actions.click()
        actions.perform()
        sleep(2)

    def verify_language(self):
        self.verify_text('Главное меню', *self.TEXT)
