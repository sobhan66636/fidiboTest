import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time;
@allure.epic("Books List")
@allure.feature("Filter text only books")
def test_filter_text_only(driver):
    driver.get('https://fidibo.com/contents/list')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Click text only filter'):
        filter = wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'category-filter-list-item')))[0]
        filter.click();
        assert wait.until(EC.url_to_be('https://fidibo.com/contents/list?types=[1]&sort=BESTSELLER')), "Type must be set to 1 and sort must be BESTSELLER when text only filter is checked."