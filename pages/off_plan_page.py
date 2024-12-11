from itertools import product
from select import select
from time import sleep

from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OffPlanPage(Page):
    GRID = (By.CSS_SELECTOR, 'a[wized="cardOfProperty"]')
    LINK_TEXT = (By.XPATH, '//a[text()={TEXT}]')
    FILTER_LOCATION = (By.ID, 'Location')
    FILTER_SALE = (By.ID, 'Location-2')
    FILTER_TEXT = (By.XPATH, '//option[text()="{TEXT}"]')
    COUNT_PROJECTS = (By.CSS_SELECTOR, '[wized = "totalPropertyCounter"]')
    TXT = ((By.XPATH, '//div[text()="Total projects"]'))
    TOTAL_PAGE = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')
    FORWARD = (By.CSS_SELECTOR, '[wized="nextPageProperties"]')
    BACK = (By.CSS_SELECTOR, '[wized="previousPageProperties"]')
    BTN_FILTER = (By.CSS_SELECTOR, 'a .filter-text')
    ALL_LIST_FOR_PRICE = (By.CSS_SELECTOR, '[wized="projectMinimumPrice"]')
    TITLE = (By.CSS_SELECTOR, '.project-name')
    PIC = (By.CSS_SELECTOR, '.project-image')
    TAG = (By.CSS_SELECTOR, '[wized="projectStatus"]')
    OPTION = (By.CSS_SELECTOR, '.tab div')

    def _get_locator(self, text):
        return [self.LINK_TEXT[0], self.LINK_TEXT[1].replace('{TEXT}', text)]

    def _get_filter_text(self, text):
        return [self.FILTER_TEXT[0], self.FILTER_TEXT[1].replace('{TEXT}', text)]

    def click_link_on_off(self, link_text):
        locator = self._get_locator(link_text)
        self.click(*locator)

    def change_location(self, filter_location):
        self.wait_until_any_text_appears(*self.COUNT_PROJECTS)
        self.total_projects_before = self.find_element(*self.COUNT_PROJECTS).text
        # print(self.total_projects_before)

        filter_dd = self.find_element(*self.FILTER_LOCATION)
        select = Select(filter_dd)
        select.select_by_visible_text(filter_location)

        self.wait_until_any_text_appears(*self.COUNT_PROJECTS)
        self.total_projects_after = self.find_element(*self.COUNT_PROJECTS).text
        # print(self.total_projects_after)

    def set_filtersale(self, filter_sale):
        self.wait_until_visible(*self.GRID)

        filter_dd = self.find_element(*self.FILTER_SALE)
        select = Select(filter_dd)
        select.select_by_value(filter_sale)

    def verify_filtersale(self, filter_sale):
        self.wait_until_visible(*self.GRID)

        products = self.find_elements(*self.GRID)
        for product in products:
            tag = product.find_element(*self.TAG).text
            assert filter_sale in tag, f'Error! Expected {filter_sale} BUT got {tag}'

    def verify_total_projects_count_updates(self):
        if self.total_projects_before == self.total_projects_after:
            self.find_element(*self.COUNT_PROJECTS).click()

    def verify_total_projects_on_off_plan(self):
        self.wait_until_any_text_appears(*self.COUNT_PROJECTS)

    def verify_all_projects_on_off_plan(self):
        self.verify_all_projects_are_shown(*self.GRID)

    def verify_right_page(self):
        self.verify_right_page_opened(*self.TXT)

    def go_to_final_page_offplan(self):
        self.wait_until_visible(*self.GRID)
        total_page = self.find_element(*self.TOTAL_PAGE).text
        print(total_page)
        i = 1
        while i <= int(total_page):
            print(i)
            self.wait_until_visible(*self.GRID)
            self.click(*self.FORWARD)
            i += 1
        self.i = i

    def go_to_first_page_offplan(self):
        self.wait_until_visible(*self.GRID)
        self.click(*self.BACK)
        while self.i != 1:
            print(self.i)
            self.wait_until_visible(*self.GRID)
            self.click(*self.BACK)
            self.i -= 1

    def btn_filter(self):
        self.wait_until_visible(*self.GRID)
        self.click(*self.BTN_FILTER)

    def verify_range_of_price(self, min_price, max_price):
        self.wait_until_visible(*self.GRID)
        all_elements = self.find_elements(*self.ALL_LIST_FOR_PRICE)
        print(f'How many elements on the page?: {len(all_elements)}')

        for element in all_elements:
            # print(element.text)
            price = element.text.replace('AED', '').replace(',', '')
            assert int(min_price) < int(price) < int(
                max_price), f'Error! Expected {price} between {min_price} and {max_price}'

    def verify_right_product(self):
        self.wait_until_visible(*self.GRID)
        products = self.find_elements(*self.GRID)
        print(f'How many products on the page?: {len(products)}')

        for product in products:
            # first approach
            assert product.find_element(*self.TITLE).is_displayed(), f'Error! Item does not have title'
            assert product.find_element(
                *self.PIC).is_displayed(), f'Error! Item {product.find_element(*self.TITLE).text} does not have Picture'

            # second approach
            assert product.find_element(*self.TITLE).text, f'Error! Item does not have title'
            assert product.find_element(
                *self.PIC), f'Error! Item {product.find_element(*self.TITLE).text} does not have Picture'

    def click_first_product(self):
        self.click(*self.TITLE)
