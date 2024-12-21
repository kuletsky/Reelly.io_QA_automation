from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://automationexercise.com/')
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, 'a[href*="contact"]').click()
driver.find_element(By.CSS_SELECTOR, '[data-qa="name"]').send_keys('wegqw')
driver.find_element(By.CSS_SELECTOR, '[data-qa="email"]').send_keys('wegqw@dvg')
driver.find_element(By.CSS_SELECTOR, '[data-qa="subject"]').send_keys('wewqdgqw')
driver.find_element(By.CSS_SELECTOR, '[data-qa="message"]').send_keys('wewqdgqw')
# driver.find_element(By.CSS_SELECTOR, '[data-qa="submit-button"]').click()
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="submit-button"]'))
)
submit_button.click()
driver.switch_to.alert.accept()