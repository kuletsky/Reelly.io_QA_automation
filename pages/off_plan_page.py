from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OffPlanPage(Page):
    GRID = (By.CSS_SELECTOR, 'a[wized="cardOfProperty"]')
    LINK_TEXT = (By.XPATH, '//a[text()={TEXT}]')
    FILTER_LOCATION = (By.ID, 'Location')
    FILTER_TEXT = (By.XPATH, '//option[text()="{TEXT}"]')
    COUNT_PROJECTS = (By.CSS_SELECTOR, '[wized = "1totalPropertyCounter"]')

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

    def verify_total_projects_count_updates(self):
        if self.total_projects_before == self.total_projects_after:
            self.find_element(*self.COUNT_PROJECT).click()

    def verify_total_projects_on_off_plan(self):
        self.wait_until_any_text_appears(*self.COUNT_PROJECTS)

    def verify_all_projects_on_off_plan(self):
        self.verify_all_projects_are_shown(*self.GRID)
