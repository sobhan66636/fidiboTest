import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


@allure.epic("Product Page")
@allure.feature("Bookmark item")
def test_bookmark(driver):
    driver.get('https://fidibo.com/book/4339-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%85%D9%84%D8%AA-%D8%B9%D8%B4%D9%82')
    wait = WebDriverWait(driver, 10)
    with allure.step('Click bookmark button'):
        bookmark_selector = (By.CSS_SELECTOR, '[aria-label=bookmark]')
        bookmark = wait.until(EC.element_to_be_clickable(bookmark_selector))
        bookmark.click();
        bookmark_filled_selector = (By.CLASS_NAME, 'fidibo-bookmark-simple-fill')
        bookmark_filled = wait.until(EC.element_to_be_clickable(bookmark_filled_selector))
        assert bookmark_filled.is_displayed(), "Bookmark icon must be filled"
        

    with allure.step('Remove bookmark'):
        bookmark_filled.click();
        wait.until(EC.element_to_be_clickable(bookmark_selector))

    


    
    


