import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


@allure.epic("Product Page")
@allure.feature("Rate book")
def test_rate_book(driver):
    driver.get('https://fidibo.com/book/4339-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%85%D9%84%D8%AA-%D8%B9%D8%B4%D9%82')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    time.sleep(3);
    with allure.step('Rate a book'):
        rate_item_selector = (By.CLASS_NAME, 'rate-item')
        rate_items = wait.until(EC.visibility_of_any_elements_located(rate_item_selector))
        rate_items[2].click()
        comment_box = wait.until(EC.visibility_of_element_located((By.NAME, 'comment')))
        comment_box.clear()
        comment_box.send_keys('کتاب خوبی است...')
        submit = driver.find_element(By.CLASS_NAME, 'add-rate-submit')
        submit.click();
        my_review_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'have-review')))
        assert my_review_title.is_displayed(), "My Review title must appear when rating a book"
        


    
    


