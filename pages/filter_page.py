from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class FilterPage(Page):
    FILTER_PRICE_FROM = (By.CSS_SELECTOR, '[wized="unitPriceFromFilter"]')
    FILTER_PRICE_TO = (By.CSS_SELECTOR, '[wized="unitPriceToFilter"]')
    BTN_APPLY_FILTER = (By.XPATH, '//a[text()="Apply filter"]')


    def set_filter_range(self, min_price, max_price):
        self.input_text(int(min_price), *self.FILTER_PRICE_FROM)
        self.input_text(int(max_price), *self.FILTER_PRICE_TO)
        # sleep(10)

    def btn_apply_filter(self):
        self.click(*self.BTN_APPLY_FILTER)

    # def verify_range_of_price(self, min_price, max_price):
    #     self.wait_until_visible(*self.GRID)
    #     all_elements = self.find_elements(*self.ALL_LIST_FOR_PRICE)
    #     print(f'How many elements on the page?: {len(all_elements)}')
    #
    #     for element in all_elements:
    #         # print(element.text)
    #         price = element.text.replace('AED', '').replace(',', '')
    #         assert int(min_price) < int(price) < int(
    #             max_price), f'Error! Expected {price} between {min_price} and {max_price}'