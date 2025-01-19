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
