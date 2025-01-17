from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MarketPage(Page):
    MARKET = (By.CSS_SELECTOR, '.page-title.agency')
    GRID = (By.CSS_SELECTOR, '[wized="marketPageCard"]')
    TOTAL_PAGE = (By.CSS_SELECTOR, '[wized="totalPageMarket"]')
    FORWARD = (By.CSS_SELECTOR, '[wized="nextPageMarket"]')
    BACK = (By.CSS_SELECTOR, '[wized="previousPageMarket"]')
    DEV = (By.CSS_SELECTOR, '[wized="marketTagDevelopers"]')
    # TAGS = (By.CSS_SELECTOR, '[wized="marketCompanyTagText"]')
    AGENC = (By.CSS_SELECTOR, '[wized="marketTagAgencies"]')
    TAGS = (By.XPATH, '//div[text()="License"]')
    BTN_ADD_COMP = (By.CSS_SELECTOR, '.add-company-button')
    TITLE_PAGE = (By.CSS_SELECTOR, '.h1-company')
    PUBLISH = (By.XPATH, '//*[text()="Publish my company"]')

    def market_opens(self):
        self.verify_right_page_opened(*self.MARKET)

    def verify_final_pagination(self):
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

    def verify_first_pagination(self):
        self.wait_until_visible(*self.GRID)
        self.click(*self.BACK)
        while self.i != 1:
            print(self.i)
            self.wait_until_visible(*self.GRID)
            self.click(*self.BACK)
            self.i -= 1

    def click_dev(self):
        self.click(*self.DEV)

    def click_agen(self):
        self.click(*self.AGENC)

    def verify_tag(self, option):
        self.wait_until_visible(*self.GRID)
        self.verify_text_for_all_elements(option, *self.TAGS)

    def click_add_company(self):
        self.find_element(*self.BTN_ADD_COMP).click()

    def verify_page(self):
        self.verify_right_page_opened(*self.TITLE_PAGE)

    def verify_btn(self):
        assert self.find_element(*self.PUBLISH).is_displayed(), "'Publish my company' button is not visible."
        assert self.find_element(*self.PUBLISH).is_enabled(), "'Publish my company' button is not enabled."

