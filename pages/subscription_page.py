from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class SubscriptionPage(Page):
    TITLE = (By.CSS_SELECTOR, '.lotion-your-h3--price')
    BACK_1 = (By.CSS_SELECTOR, '.next-step--.black')
    BACK_2 = (By.CSS_SELECTOR, '.back-text')
    UPGRADE_PLAN = (By.XPATH, '//div[text()="Upgrade plan"]')

    def verify_title(self, title):
        self.verify_text(title, *self.TITLE)

    def verify_back_upgrade_plan_buttons(self):
        self.wait_until_visible(*self.UPGRADE_PLAN)
        self.wait_until_visible(*self.BACK_1)
        self.wait_until_visible(*self.BACK_2)
