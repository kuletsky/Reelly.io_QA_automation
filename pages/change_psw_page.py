from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class ChangePswPage(Page):
    NEW_PSW = (By.CSS_SELECTOR, '[id="Enter-new-password"]')
    RPT_PSW = (By.CSS_SELECTOR, '[id="Repeat-password"]')
    BTN_CHANGE_PASSWORD = (By.XPATH, '//a[text()="Change password"]')

    def add_test_password(self, test_psw):
        self.input_text(test_psw, *self.NEW_PSW)
        self.input_text(test_psw, *self.RPT_PSW)

    def verify_btn_psw_available(self):
        self.wait_until_visible(*self.BTN_CHANGE_PASSWORD)
