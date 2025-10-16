import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


@allure.epic("Library")
@allure.feature("Unbookmark item from library")
def test_library_unbookmark(driver):
    driver.get('https://fidibo.com/book/93755-%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B5%D9%88%D8%AA%DB%8C-%D9%BE%D8%AF%D8%B1-%D9%BE%D9%88%D9%84%D8%AF%D8%A7%D8%B1-%D9%BE%D8%AF%D8%B1-%D9%81%D9%82%DB%8C%D8%B1')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Create a new bookmark'):
        bookmark_selector = (By.CSS_SELECTOR, '[aria-label=bookmark]')
        bookmark = wait.until(EC.element_to_be_clickable(bookmark_selector))
        bookmark.click();
        bookmark_filled_selector = (By.CLASS_NAME, 'fidibo-bookmark-simple-fill')
        bookmark_filled = wait.until(EC.element_to_be_clickable(bookmark_filled_selector))
        assert bookmark_filled.is_displayed(), "Bookmark icon must be filled when bookmarked"
        

    with allure.step('Unbookmark from library'):
        driver.get('https://fidibo.com/library/book/bookmark')
        unbookmark = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fidibo-bookmark-simple-fill')))
        unbookmark.click();
        confirm = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'alert-modal-submit')))
        confirm.click();
        empty = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'library-page-empty')))
        assert empty.is_displayed(), "Bookmark icon must not be filled when unbookmarked"
    


    
    


