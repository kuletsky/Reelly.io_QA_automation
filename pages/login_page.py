from selenium.webdriver.common.by import By

from pages.base_page import Page


class LoginPage(Page):
    INPUT_EMAIL = (By.ID, 'email-2')
    INPUT_PSW = (By.ID, 'field')
    BTN_CONTINUE = (By.CSS_SELECTOR, 'a[wized="loginButton"]')

    def login_to(self, lgn, psw):
        self.input_text(lgn,*self.INPUT_EMAIL)
        self.input_text(psw,*self.INPUT_PSW)
        self.click(*self.BTN_CONTINUE)
