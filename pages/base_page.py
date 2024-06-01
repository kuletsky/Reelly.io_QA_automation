from selenium.webdriver.support import expected_conditions as EC
from log_files.logger import logger


class Page:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        logger.info(f'Page opened: {url}')

    def find_element(self, *locator):
        logger.info(f'Searching by: {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Searching by: {locator}')
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Clicking by: {locator}')
        self.find_element(*locator).click()

    def wait_until_clickable_click(self, *locator):
        logger.info(f'Waiting until clickable by: {locator}')
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            f'Element not clickable by: {locator}'
        ).click()

    def wait_until_visible(self, *locator):
        logger.info(f'Waiting until visible by: {locator}')
        self.driver.wait.until(
            EC.visibility_of_all_elements_located(*locator),
            f'Element not visible by: {locator}')

    def input_text(self, text, *locator):
        logger.info(f'Input text by: {text}')
        self.find_element(*locator).send_keys(text)

    def verify_right_page_opened(self, *locator):
        logger.info(f'Verifying right page by: {locator}')
        self.find_element(*locator)

    def verify_text_for_all_elements(self, expected_text, *locator):
        logger.info(f'Verifying text for all elements by: {locator}')
        all_elements = self.find_elements(*locator)
        print(f'How many elements on the page?: {len(all_elements)}')

        for element in all_elements:
            # print(element.text)
            assert element.text == expected_text, f'Error! {expected_text} IS NOT {element.text}'
