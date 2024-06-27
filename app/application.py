from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.secondary_page import SecondaryPage
from pages.settings_page import SettingsPage
from pages.sign_up_page import SignUpPage


class Application:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.profile_page = ProfilePage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_up_page = SignUpPage(driver)
