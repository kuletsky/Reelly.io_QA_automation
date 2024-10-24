from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SecondaryPage(Page):
    GRID = (By.XPATH, '//div[@wized="listingCardMLS"]')
    TXT_LISTINGS = (By.XPATH, '//div[text()="Listings"]')
    BTN_FILTER = (By.CSS_SELECTOR, '.filter-text')
    FILTER_SELL = (By.XPATH, '//div[text()="Want to sell"]')
    FILTER_BUY = (By.XPATH, '//div[@class="tag-text-filters" and text()="Want to buy"]')
    FILTER_BUY_SELL = (By.XPATH, '//div[@class="tag-text-filters" and text()="{FILTER}"]')
    FILTER_PRICE_FROM = (By.CSS_SELECTOR, '[wized="unitPriceFromFilter"]')
    FILTER_PRICE_TO = (By.CSS_SELECTOR, '[wized="unitPriceToFilter"]')
    BTN_APPLY_FILTER = (By.XPATH, '//a[text()="Apply filter"]')
    ALL_LIST_FOR_FILTER = (By.CSS_SELECTOR, 'div[wized="saleTagMLS"]')
    ALL_LIST_FOR_PRICE = (By.CSS_SELECTOR, 'div[wized="unitPriceMLS"]')
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

    def set_filter_range(self, min_price, max_price):
        self.input_text(int(min_price), *self.FILTER_PRICE_FROM)
        self.input_text(int(max_price), *self.FILTER_PRICE_TO)
        # sleep(10)

    def verify_range_of_price(self, min_price, max_price):
        self.wait_until_visible(*self.GRID)
        all_elements = self.find_elements(*self.ALL_LIST_FOR_PRICE)
        print(f'How many elements on the page?: {len(all_elements)}')

        for element in all_elements:
            # print(element.text)
            price = element.text.replace('AED','').replace(',','')
            assert int(min_price) < int(price) < int(max_price), f'Error! Expected {price} between {min_price} and {max_price}'

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

