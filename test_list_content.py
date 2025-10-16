import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.epic("Product Page")
@allure.feature("Open content list")
def test_list_content(driver):
    driver.get('https://fidibo.com/book/66891-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%85%D8%A7%D8%AF%D8%B1%D9%85-%D8%AF%D9%88-%D8%A8%D8%A7%D8%B1-%D9%85%D8%B1%D8%AF')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    with allure.step('Click toc button'):
        toc = wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'book-toc-btn')))
        for btn in toc:
            if ('just-desktop' in btn.get_dom_attribute('class')): btn.click();
        items = wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'book-toc-item')))
        assert len(items) > 0, "Content list must have at least 1 item"

