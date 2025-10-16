import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time;


@allure.epic("Home Page")
@allure.feature("Logout")
def test_zz_finally_logout(driver):
    driver.get('https://fidibo.com/profile/account')
    wait = WebDriverWait(driver, 10)
    with allure.step('Log out of account from profile page'):
        sidebar_buttons = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile-side-buttons')))
        logout = sidebar_buttons.find_elements(By.TAG_NAME, 'button')[4]
        logout.click();
        confirm = driver.find_element(By.CLASS_NAME, 'alert-modal-submit')
        confirm.click();
        assert wait.until(EC.url_to_be('https://fidibo.com/login')), "Must redirect to login page if logout was successful"



