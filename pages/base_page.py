from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from log_files.logger import logger
from selenium.common.exceptions import TimeoutException


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(driver, 15)

    def open(self, url):
        logger.info(f'Page opened: {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        logger.info(f'Searching by: {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Searching by: {locator}')
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Waiting until clickable by: {locator}')
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            f'Element not clickable by: {locator}'
        ).click()

    def wait_until_visible(self, *locator):
        logger.info(f'Waiting until visible by: {locator}')
        self.driver.wait.until(
            EC.visibility_of_all_elements_located(locator),
            f'Element not visible by: {locator}')

    def wait_until_disappears(self, *locator):
        logger.info(f'Waiting until disappears by: {locator}')
        self.driver.wait.until(
            EC.invisibility_of_element_located(locator),
            f'Element still visible by: {locator}'
        )

    def wait_until_any_text_appears(self, *locator):
        def _wait_until_any_text_appears(driver):
            logger.info(f'Waiting until any text appears by: {locator}')
            element = driver.find_element(*locator)
            return bool(element.text.strip())

        try:
            WebDriverWait(self.driver, 15).until(_wait_until_any_text_appears)
        except TimeoutException:
            print(f'Timed out waiting until any text appears by: {locator}')

    def input_text(self, text, *locator):
        logger.info(f'Input text by: {text}')
        self.find_element(*locator).clear()
        self.find_element(*locator).send_keys(text)

    def get_current_window(self):
        current_window = self.driver.current_window_handle
        print('Current window', current_window)
        print('ALL windows', self.driver.window_handles)
        return current_window

    def switch_window_by_id(self, window_id):
        print('Switching to...', window_id)
        self.driver.switch_to.window(window_id)
        print('ALL windows', self.driver.window_handles)

    def switch_to_new_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('ALL windows', self.driver.window_handles)
        print('Switching to...', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def verify_right_page_opened(self, *locator):
        logger.info(f'Verifying right page opened by: {locator}')
        self.find_element(*locator)

    def verify_text_for_all_elements(self, expected_text, *locator):
        logger.info(f'Verifying text for all elements by: {locator}')
        all_elements = self.find_elements(*locator)
        print(f'How many elements on the page?: {len(all_elements)}')

        for element in all_elements:
            # print(element.text)
            assert element.text == expected_text, f'Error! Expected {expected_text}, but got {element.text}'

    def verify_all_projects_are_shown(self, *locator):
        logger.info(f'Verifying all elements are shown: {locator}')
        self.wait_until_visible(*locator)
        all_projects = self.find_elements(*locator)
        print(f'How many elements on the page?: {len(all_projects)}')

        for project in all_projects:
            assert project, f'Error! Projects are not shown'
        print(f'All {len(all_projects)} projects are shown')

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Error! Expected {expected_text}, but got {actual_text}'

    def verify_input(self, expected_text, *locator):
        actual_text = self.find_element(*locator).get_attribute('value')
        assert expected_text == actual_text, f'Error! Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Error! Expected {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_partial_url):
        self.driver.wait.until(EC.url_contains(expected_partial_url),
                               message=f'URL does not contain {expected_partial_url}')

    def verify_url(self, expected_url):
        self.driver.wait.until(EC.url_matches(expected_url),
                               message=f'URL does not contain {expected_url}')

    def close(self):
        self.driver.close()
