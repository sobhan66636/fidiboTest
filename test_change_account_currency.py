import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time;


@allure.epic("Home Page")
@allure.feature("Change account currency")
def test_change_account_currency(driver):
    driver.get('https://fidibo.com/profile/account')
    wait = WebDriverWait(driver, 10)

    with allure.step('Set currency to dollar'):
        currency = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-currency-profile-side-button')))
        currency.click();
        container = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile-user-wallet-section-content')))
        dollar = container.find_elements(By.TAG_NAME, 'button')[1]
        dollar.click();
        assert wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "change-currency-profile-side-button"), "دلار")), "Currency must be set to dollar"
    
    with allure.step('Set currency back'):
        currency = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-currency-profile-side-button')))
        currency.click();
        container = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile-user-wallet-section-content')))
        dollar = container.find_elements(By.TAG_NAME, 'button')[0]
        dollar.click();
        assert wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "change-currency-profile-side-button"), "تومان")), "Currency must be set to toman"


