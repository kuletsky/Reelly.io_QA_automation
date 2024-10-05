from selenium.webdriver.common.by import By

from pages.base_page import Page


class SecondaryPage(Page):
    GRID = (By.XPATH, '//div[@wized="listingCardMLS"]')
    TXT_LISTINGS = (By.XPATH, '//div[text()="Listings"]')
    BTN_FILTER = (By.CSS_SELECTOR, '.filter-text')
    FILTER_SELL = (By.XPATH, '//div[text()="Want to sell"]')
    FILTER_BUY = (By.XPATH, '//div[@class="tag-text-filters" and text()="Want to buy"]')
    FILTER_BUY_SELL = (By.XPATH, '//div[@class="tag-text-filters" and text()="{FILTER}"]')
    BTN_APPLY_FILTER = (By.XPATH, '//a[text()="Apply filter"]')
    ALL_LIST_FOR_FILTER = (By.CSS_SELECTOR, 'div[wized="saleTagMLS"]')
    FORWARD = (By.CSS_SELECTOR, '[wized="nextPageMLS"]')
    BACK = (By.CSS_SELECTOR, '[wized="previousPageMLS"]')
    TOTAL_PAGE = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')


    def _get_locator(self, text):
        return [self.FILTER_BUY_SELL[0], self.FILTER_BUY_SELL[1].replace('{FILTER}', text)]

    def btn_filter(self):
        self.wait_until_visible(*self.GRID)
        self.click(*self.BTN_FILTER)

    def filter_want_to_sell_buy(self, filter_sell_buy):
        locator = self._get_locator(filter_sell_buy)
        self.click(*locator)

    def btn_apply_filter(self):
        self.click(*self.BTN_APPLY_FILTER)

    def verify_right_page(self):
        self.verify_right_page_opened(*self.TXT_LISTINGS)

    def verify_text_for_secondary_filter(self, expected_filter):
        self.wait_until_visible(*self.GRID)
        self.verify_text_for_all_elements(expected_filter, *self.ALL_LIST_FOR_FILTER)

    def verify_all_projects_on_secondary(self):
        self.verify_all_projects_are_shown(*self.GRID)

    def go_to_final_page(self):
        self.wait_until_visible(*self.GRID)
        total_page = self.find_element(*self.TOTAL_PAGE).text
        print(total_page)
        i = 1
        while i < int(total_page):
            print(i)
            self.wait_until_visible(*self.GRID)
            self.click(*self.FORWARD)
            i += 1

        self.click(*self.BACK)
        while i != 1:
            print(i)
            self.wait_until_visible(*self.GRID)
            self.click(*self.BACK)
            i -= 1

