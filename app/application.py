from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.secondary_page import SecondaryPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.secondary_page = SecondaryPage(driver)
