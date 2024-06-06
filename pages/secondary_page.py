from selenium.webdriver.common.by import By

from pages.base_page import Page


class SecondaryPage(Page):
    TXT_LISTINGS = (By.XPATH, '//div[text()="Listings"]')
    BTN_FILTER = (By.CSS_SELECTOR, '.filter-text')
    FILTER_SELL = (By.XPATH, '//div[text()="Want to sell"]')
    FILTER_BUY = (By.XPATH, '//div[@class="tag-text-filters" and text()="Want to buy"]')
    BTN_APPLY_FILTER = (By.XPATH, '//a[text()="Apply filter"]')
    ALL_LIST_FOR_FILTER = (By.CSS_SELECTOR, 'div[wized="saleTagMLS"]')
    GRID = (By.XPATH, '//div[@wized="listingCardMLS"]')

    def btn_filter(self):
        self.click(*self.BTN_FILTER)

    def btn_filter_want_to_sell(self):
        self.click(*self.FILTER_SELL)

    def btn_filter_want_to_buy(self):
        self.click(*self.FILTER_BUY)

    def btn_apply_filter(self):
        self.click(*self.BTN_APPLY_FILTER)

    def verify_right_page(self):
        self.verify_right_page_opened(*self.TXT_LISTINGS)

    def verify_text_for_secondary_filter(self, expected_filter):
        self.verify_text_for_all_elements(expected_filter, *self.ALL_LIST_FOR_FILTER)