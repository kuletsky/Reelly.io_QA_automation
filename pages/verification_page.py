from selenium.webdriver.common.by import By
from pages.base_page import Page


class VerificationPage(Page):
    TEXT = (By.CSS_SELECTOR, '.lotion-your-h3')
    UPLOAD_BTN = (By.CSS_SELECTOR, 'label[for="input_file"]')
    NEXT_BTN = (By.CSS_SELECTOR, '.next-step--')

    def verify_verification_page(self):
        self.verify_text('Upload your photo', *self.TEXT)

    def verify_btn(self):
        # Verify "Upload Image" button is visible and enabled
        uploadBtn = self.find_element(*self.UPLOAD_BTN)
        assert uploadBtn.is_displayed(), "'Upload Image' button is not visible."
        assert uploadBtn.is_enabled(), "'Upload Image' button is not enabled."

        # Verify "Next Step" button is visible and enabled
        nextBtn = self.find_element(*self.NEXT_BTN)
        assert nextBtn.is_displayed(), "'Upload Image' button is not visible."
        assert nextBtn.is_enabled(), "'Upload Image' button is not enabled."
