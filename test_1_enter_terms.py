import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import shutil
import os;

@allure.epic("Login")
@allure.feature("Enter terms & conditions page")
def test_1_enter_terms(driver):
    if (os.path.isdir('fidibo_chromium')):
        shutil.rmtree('fidibo_chromium')
    link_selector = (By.CLASS_NAME, "login-box-rule-link")
    wait = WebDriverWait(driver, 10)
    driver.get("https://fidibo.com/login")
    link = wait.until(EC.visibility_of_element_located(link_selector))

    with allure.step("Click terms & conditions button"):
        link.click()
        assert wait.until(EC.url_to_be('https://fidibo.com/terms-of-use')), "Terms page must be loaded"
