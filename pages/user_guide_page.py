from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class UserGuidePage(Page):
    LESSON_TITLES = (By.CSS_SELECTOR, 'a[data-sessionlink="feature=player-title"]')

    def verify_all_contain_titles(self):
        all_lesson_titles = self.find_elements(*self.LESSON_TITLES)

        for title in all_lesson_titles:
            assert title.text, f'A lesson video does not have a title "{title.text}"'
