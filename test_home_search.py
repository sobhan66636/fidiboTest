import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@allure.epic("Home Page")
@allure.feature("Search book")
def test_home_search(driver):
    driver.get('https://fidibo.com')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    search_selector = (By.NAME, 'search')
    search = wait.until(EC.visibility_of_element_located(search_selector))
    with allure.step('Type a book name'):
        search.send_keys('هری پاتر')
        search_suggestions_selector = (By.CLASS_NAME, 'header-search-suggestion')
        search_suggestions = wait.until(EC.visibility_of_element_located(search_suggestions_selector))
        suggestions_items = search_suggestions.find_elements(By.TAG_NAME, 'a')
        assert len(suggestions_items) > 0, "Search items must appear"
        