import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



@allure.epic("Login")
@allure.feature("Clear phone number textbox")
def test_3_phone_clear_button(driver):
    phone_number_box_selector = (By.CLASS_NAME, "phone-input-field")
    phone_country_selector = (By.CLASS_NAME, "phone-input-country")
    phone_input_clear_selector = (By.CLASS_NAME, "phone-input-close")

    wait = WebDriverWait(driver, 10)
    driver.get('https://fidibo.com/login')

    country = wait.until(EC.visibility_of_element_located(phone_country_selector))
    phonebox = wait.until(EC.visibility_of_element_located(phone_number_box_selector))
    phonebox.send_keys('1')
    phone_input_clear = wait.until(EC.visibility_of_element_located(phone_input_clear_selector))

    wait.until(EC.element_to_be_clickable(country))

    with allure.step("Click clear phone number button"):
        phonebox.send_keys('123456')
        phone_input_clear.click();
        assert phonebox.text == '', "Phone input must be cleared"
