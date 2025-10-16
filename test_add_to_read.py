import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


@allure.epic("Product Page")
@allure.feature("Add to read list")
def test_add_to_read(driver):
    driver.get('https://fidibo.com/book/4339-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%85%D9%84%D8%AA-%D8%B9%D8%B4%D9%82')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Click read button'):
        read = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label=read]')))
        read.click();
        read_marked = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label=read].fill')))
        assert read_marked.is_displayed(), "Marked as read must be filled"

    with allure.step('Remove from read list'):
        read.click();
        read = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label=read]')))
        assert read.is_displayed(), "Marked as read must not be filled"



    
    


