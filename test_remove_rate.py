import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


@allure.epic("Product Page")
@allure.feature("Remove rating")
def test_remove_rate_book(driver):
    driver.get('https://fidibo.com/book/4339-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%85%D9%84%D8%AA-%D8%B9%D8%B4%D9%82')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Remove rating'):
        review_menu = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'review-login-button')))
        review_menu.click();
        remove = driver.find_elements(By.CLASS_NAME, 'review-menu-modal-menu-modal-btn')[1]
        remove.click()
        confirm = driver.find_element(By.CLASS_NAME, 'alert-modal-submit')
        confirm.click();
        assert wait.until(EC.staleness_of(confirm)), "Rating must be removed"
        
        


    
    


