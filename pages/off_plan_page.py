from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class OffPlanPage(Page):
    GRID = (By.CSS_SELECTOR, 'a[wized="cardOfProperty"]')
    LINK_TEXT = (By.XPATH, '//a[text()={TEXT}]')
     # = (By.CSS_SELECTOR, '[value="{TEXT}"]')
    FILTER_LOCATION = (By.ID, 'Location')
    FILTER_TEXT = (By.XPATH, '//option[text()="{TEXT}"]')

    # def verify_all_projects(self):
    #     self.wait_until_visible(*self.GRID)
    #     all_projects = self.find_elements(*self.GRID)
    #     print(f'How many elements on the page?: {len(all_projects)}')
    #
    #     for project in all_projects:
    #         assert project, f'Error! Projects are not shown'
    #     print(f'All {len(all_projects)} projects are shown')

    def _get_locator(self, text):
        return [self.LINK_TEXT[0], self.LINK_TEXT[1].replace('{TEXT}', text)]

    def _get_filter_text(self, text):
        return [self.FILTER_TEXT[0], self.FILTER_TEXT[1].replace('{TEXT}', text)]

    def click_link_on_off(self, link_text):
        locator = self._get_locator(link_text)
        self.click(*locator)

    def change_location(self, filter_location):
        # locator = self._get_filter_text(filter_location)
        # print(locator)
        filter_dd = self.find_element(*self.FILTER_LOCATION)
        # print(filter_dd)
        select = Select(filter_dd)
        select.select_by_visible_text(filter_location)

    def verify_all_projects_on_off_plan(self):
        self.verify_all_projects_are_shown(*self.GRID)
