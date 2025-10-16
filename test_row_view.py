import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
@allure.epic("Books List")
@allure.feature("Change list view mode")
def test_row_view(driver):
    driver.get('https://fidibo.com/contents/list')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Click row view button'):
        container = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'page-options-header-main-buttons-section-grid')))
        button = container.find_elements(By.TAG_NAME, 'button')[0]
        button.click();
        row_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.content-card-container.row')))
        assert row_container.is_displayed(), "Row container must be visible when row view mode is clicked"