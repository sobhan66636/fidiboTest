import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.epic("Product Page")
@allure.feature("Text book sample")
def test_text_book_sample(driver):
    driver.get('https://fidibo.com/book/4339-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%85%D9%84%D8%AA-%D8%B9%D8%B4%D9%82')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Click sample'):
        sample = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'book-buy-box-footer-second')))
        sample.click()
        assert wait.until(EC.url_to_be('https://fidibo.com/reader-sample/4339-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%85%D9%84%D8%AA-%D8%B9%D8%B4%D9%82')), "Must be redirected to sample page"

    
    


