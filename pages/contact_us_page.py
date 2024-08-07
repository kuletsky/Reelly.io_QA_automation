from selenium.webdriver.common.by import By

from pages.base_page import Page


class ContactUsPage(Page):
    CONNECT_COMPANY = (By.XPATH, '//div[text()="Connect the company"]')

    def verify_connect_button(self):
        self.find_element(*self.CONNECT_COMPANY).click()
