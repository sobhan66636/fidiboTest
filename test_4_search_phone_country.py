import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time;



@allure.epic("Login")
@allure.feature("Search a country in countries list")
def test_4_search_phone_country(driver):
    phone_country_selector = (By.CLASS_NAME, "phone-input-country")

    wait = WebDriverWait(driver, 10)
    driver.get('https://fidibo.com/login')

    country = wait.until(EC.visibility_of_element_located(phone_country_selector))
    wait.until(EC.element_to_be_clickable(country))
    country.click()

    with allure.step("Typing a part of USA"):
        search_selector = (By.NAME, "search")
        search = wait.until(EC.visibility_of_element_located(search_selector))
        search.send_keys('ایالات')
        element_text_selector = (By.CLASS_NAME, "country-menu-item-second")
        element_text = wait.until(EC.visibility_of_element_located(element_text_selector))
        assert element_text.text == 'ایالات متحده', "Search must find USA"    
