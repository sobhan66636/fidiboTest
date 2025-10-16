import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


@allure.epic("Product Page")
@allure.feature("Remove from cart")
def test_remove_from_cart(driver):
    driver.get('https://fidibo.com/basket')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Click remove button'):
        remove_selector = (By.CLASS_NAME, 'header-top-basket-menu-item-footer-remove')
        remove = wait.until(EC.element_to_be_clickable(remove_selector))
        remove.click();

    with allure.step('Confirm remove'):
        confirm_selector = (By.CLASS_NAME, 'alert-modal-submit')
        confirm = wait.until(EC.element_to_be_clickable(confirm_selector))
        confirm.click()
        assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'basket-page-content-empty'))), "Cart must be empty after removing item"

    


    
    


