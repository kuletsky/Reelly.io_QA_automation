from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


BTN_OPEN_IN_BROWSER = (By.XPATH, '//div[text()="Open in browser"]')
INPUT_EMAIL = (By.CSS_SELECTOR, '#email-2')
INPUT_PSWD = (By.CSS_SELECTOR, '#field')
BTN_CONTINUE = (By.CSS_SELECTOR, 'a[wized="loginButton"]')
MENU_SECONDARY = (By.XPATH, '//div[@class="menu-button-text" and text()="Secondary"]')
TXT_LISTINGS = (By.XPATH, '//div[text()="Listings"]')
GRID = (By.CSS_SELECTOR, 'div:nth-of-type > img')
BTN_FILTER = (By.CSS_SELECTOR, '.filter-text')
FILTER_SELL = (By.XPATH, '//div[text()="Want to sell"]')
BTN_APPLY_FILTER = (By.XPATH, '//a[text()="Apply filter"]')
ALL_LIST_FOR_SALE = (By.CSS_SELECTOR, 'div[wized="saleTagMLS"]')


@given('Open the main page')
def open_main_page(context):
    context.driver.get('https://reelly.io/')


@when('Click on the "Open in browser"')
def open_in_browser(context):
    context.driver.find_element(*BTN_OPEN_IN_BROWSER).click()


@when('Log in to the page {lgn}, {psw}')
def login(context, lgn, psw):
    context.driver.find_element(*INPUT_EMAIL).send_keys(lgn)
    context.driver.find_element(*INPUT_PSWD).send_keys(psw)
    context.driver.find_element(*BTN_CONTINUE).click()


@when('Click on "Secondary" option at the left side menu')
def secondary_side_menu(context):
    # context.driver.wait.until(EC.visibility_of_element_located(MENU_SECONDARY)).click()
    context.driver.find_element(*MENU_SECONDARY).click()


@then('Verify the right page opens')
def verify_right_page(context):
    context.driver.find_element(*TXT_LISTINGS)


@when('Filter the products by "want to sell"')
def filter_want_sell(context):
    sleep(6)
    context.driver.find_element(*BTN_FILTER).click()
    context.driver.find_element(*FILTER_SELL).click()
    context.driver.find_element(*BTN_APPLY_FILTER).click()
    sleep(6)


@then('Verify that all cards have "for sale" tag')
def verify_tag_for_sale(context):
    all_property = context.driver.find_elements(*ALL_LIST_FOR_SALE)
    # print(len(all_property))
    for property in all_property:
        # print(property.text)
        assert property.text == 'For sale', f'Error! {property.text} IS NOT "For sale" '
