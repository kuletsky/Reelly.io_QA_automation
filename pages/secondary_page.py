from selenium.webdriver.common.by import By

from pages.base_page import Page


class SecondaryPage(Page):
    TXT_LISTINGS = (By.XPATH, '//div[text()="Listings"]')
    BTN_FILTER = (By.CSS_SELECTOR, '.filter-text')
    FILTER_SELL = (By.XPATH, '//div[text()="Want to sell"]')
    BTN_APPLY_FILTER = (By.XPATH, '//a[text()="Apply filter"]')

    def verify_right_page(self):
        self.find_element(*self.TXT_LISTINGS)

    def btn_filter(self):
        self.click(*self.BTN_FILTER)

    def btn_filter_want_to_sell(self):
        self.click(*self.FILTER_SELL)

    def btn_apply_filter(self):
        self.click(*self.BTN_APPLY_FILTER)
