import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.epic("Product Page")
@allure.feature("Add book to cart")
def test_add_to_cart(driver):
    driver.get('https://fidibo.com/book/4339-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%85%D9%84%D8%AA-%D8%B9%D8%B4%D9%82')
    wait = WebDriverWait(driver, 10)
    with allure.step('Add item to cart'):
        buy = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='خرید']")))
        buy.click();
        wait.until(EC.staleness_of(buy))
        driver.get('https://fidibo.com/basket')
        items_container_selector = (By.CLASS_NAME, 'basket-page-content-first-section-list')
        items_container = wait.until(EC.visibility_of_element_located(items_container_selector))
        items = items_container.find_elements(By.TAG_NAME, 'div');
        assert len(items) > 0, "Cart items must be 1 or more"
    


    
    


