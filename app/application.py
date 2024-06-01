from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.secondary_page import SecondaryPage
from pages.settings_page import SettingsPage


class Application:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.settings_page = SettingsPage(driver)
