import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.epic("Books List")
@allure.feature("Sort books")
def test_sort(driver):
    driver.get('https://fidibo.com/contents/list')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Click sort button'):
        sort = driver.find_elements(By.CLASS_NAME, 'page-options-header-main-buttons-section-item')[1]
        sort.click();
    with allure.step('Click highest price'):
        button = driver.find_elements(By.CLASS_NAME, 'sort-modal-container-item')[4]
        button.click();
        assert wait.until(EC.url_to_be('https://fidibo.com/contents/list?sort=HIGHEST_PRICE')), "Sort must be set to HIGHEST_PRICE when highest price is checked"

