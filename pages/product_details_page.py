from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductDetailsPage(Page):
    OPTION = (By.CSS_SELECTOR, '.tab div')

    def verify_option(self, option_1, option_2, option_3):
        elements = self.find_elements(*self.OPTION)
        options = [element.text.strip().lower() for element in elements]
        # print(options)

        expected_options = {option_1, option_2, option_3}
        assert expected_options.intersection(options), "None of the expected options are present!"

    def verify_clickable(self, option_1, option_2, option_3):
        elements = self.find_elements(*self.OPTION)
        expected_options = {option_1, option_2, option_3}

        for element in elements:
            text = element.text.strip().lower()
            if text in expected_options:
                element.click()
                # print(element.text)
