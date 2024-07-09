from pages.base_page import Page
from selenium.webdriver.common.by import By


class OffPlanPage(Page):
    GRID = (By.XPATH, '//a[@wized="cardOfProperty"]')

    def verify_all_projects(self):
        self.wait_until_visible(self.GRID)
        all_projects = self.find_elements(*self.GRID)
        print(f'How many elements on the page?: {len(all_projects)}')

        for project in all_projects:
            assert project, f'Error! Projects are not shown'
        print(f'All {len(all_projects)} projects are shown')
